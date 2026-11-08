---
title: "Handling Sparse Files on Linux"
date: 2018-04-05 11:33:04 +0000
modified: 2026-04-11 15:43:44 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /handling-sparse-files-on-linux/
---

Sparse files optimize storage by storing only metadata for contiguous zero-filled ranges instead of allocating actual disk blocks. They’re essential for VM images, virtual block devices, and large databases where much of the allocated space remains unused.

Most modern filesystems support sparse files: ext4, btrfs, and XFS on Linux; NTFS on Windows; and APFS on macOS. However, support varies — notably, some older filesystems and network storage backends may not preserve sparseness during transfers.

## Creating Sparse Files

### truncate

The simplest and fastest approach is `truncate`, which resizes a file to a specified size without writing actual data:

``` bash
truncate -s 20G ./vmdisk0
```

This creates a 20GB sparse file instantly, regardless of available RAM. If the file exists, `truncate` adjusts it to the exact size; if it doesn’t exist, it creates one. This is far more efficient than equivalent `dd` operations and should be your default choice for sparse file creation.

### dd with seek

While less common now, `dd` can create sparse files using the `seek` parameter:

``` bash
dd if=/dev/zero of=./vmdisk0 bs=1M seek=20480 count=0
```

The key is `count=0` (write zero blocks) combined with `seek` to jump to the desired size. This approach is slower and less reliable than `truncate` for simple sparse file creation. However, `dd` remains useful when you need to write actual data at the beginning while leaving the rest sparse:

``` bash
dd if=boot.bin of=./vmdisk0 bs=1M
dd if=/dev/zero of=./vmdisk0 bs=1M seek=100 count=0
```

### fallocate

Modern systems have `fallocate`, which pre-allocates space at the filesystem level:

``` bash
fallocate -l 20G ./vmdisk0
```

By default, `fallocate` creates a truly allocated file (not sparse). To create sparse regions, use the `-z` flag:

``` bash
fallocate -z -l 20G ./vmdisk0
```

However, `fallocate` has more limited filesystem support than `truncate` and may not work on all backends. Stick with `truncate` for maximum compatibility.

## Copying and Archiving Sparse Files

Modern tools automatically detect and preserve holes when the kernel supports `SEEK_HOLE` and `SEEK_DATA` (available since Linux 3.1). This means:

**cp**: Copy sparse files with the `--sparse=always` flag:

``` bash
cp --sparse=always source.img dest.img
```

Without `--sparse=always`, `cp` may materialize the file on some systems.

**rsync**: Automatically preserves sparseness:

``` bash
rsync -av --sparse source.img dest.img
```

**tar**: Preserve sparse files with the `--sparse` option:

``` bash
tar --sparse -czf archive.tar.gz vmdisk0
```

**dd**: For direct block-level copying with sparseness:

``` bash
dd if=source.img of=dest.img bs=4M conv=sparse
```

The `sparse` flag tells `dd` to detect and skip zero blocks.

## Checking Sparseness

Verify that a file is sparse by comparing logical size to actual disk usage:

``` bash
ls -lh vmdisk0          # Shows logical size
du -h vmdisk0           # Shows actual disk usage
stat vmdisk0            # Shows both allocated blocks and logical size
```

A sparse file will show different values in `ls` (logical size) and `du` (actual usage). For example:

    -rw-r--r-- 1 user user 20G  vmdisk0    # ls shows 20G
    4.0K                        vmdisk0    # du shows only 4K (metadata)

For detailed information about allocated vs. unallocated regions, use `filefrag`:

``` bash
filefrag -v vmdisk0
```

This shows the extent layout and identifies holes in the file.

## Library Functions for Sparse Files

### ftruncate()

For C code, `ftruncate()` is the preferred method for creating sparse files — it’s explicit and works identically across filesystems:

``` c
#include <unistd.h>
#include <fcntl.h>

int create_sparse_file(const char *path, off_t size)
{
    int fd = open(path, O_RDWR | O_CREAT | O_TRUNC, 0666);
    if (fd == -1)
        return -1;

    if (ftruncate(fd, size) == -1) {
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}
```

### lseek()

You can also create sparse files by seeking past the current position and writing, though this is less reliable than `ftruncate()`:

``` c
#include <fcntl.h>
#include <unistd.h>

int create_sparse_file(const char *path, off_t size)
{
    int fd = open(path, O_RDWR | O_CREAT | O_TRUNC, 0666);
    if (fd == -1)
        return -1;

    if (lseek(fd, size - 1, SEEK_SET) == -1) {
        close(fd);
        return -1;
    }

    if (write(fd, "\0", 1) != 1) {
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}
```

The write at `size - 1` is critical — seeking alone doesn’t guarantee the file ends; a write operation anchors the end. However, prefer `ftruncate()` when possible.

### fallocate()

For guaranteed filesystem allocation (avoiding `ENOSPC` errors later), use `fallocate()`, though it’s less portable:

``` c
#include <fcntl.h>

int alloc_file(const char *path, off_t size)
{
    int fd = open(path, O_RDWR | O_CREAT | O_TRUNC, 0666);
    if (fd == -1)
        return -1;

    // Allocate space; will not create sparse regions by default
    if (fallocate(fd, 0, 0, size) == -1) {
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}
```

## Detecting Holes with SEEK_HOLE

To efficiently iterate through a file and find sparse regions without reading the entire contents:

``` c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

void print_holes(int fd, off_t size)
{
    off_t pos = 0;

    while (pos < size) {
        off_t hole = lseek(fd, pos, SEEK_HOLE);
        if (hole == -1 || hole >= size)
            break;

        off_t data = lseek(fd, hole, SEEK_DATA);
        if (data == -1 || data >= size)
            data = size;

        printf("Hole from %ld to %ld (%ld bytes)\n", hole, data, data - hole);
        pos = data;
    }
}
```

This approach is much faster than reading the entire file for large sparse images. It works by alternating between `SEEK_HOLE` (jump to next hole) and `SEEK_DATA` (jump to next data region).

## Common Pitfalls

**NFS and network storage**: Network filesystems often don’t preserve sparseness. Always test before relying on it. `scp` and `sftp` will materialize sparse files — use `rsync` with `--sparse` or `dd` with `conv=sparse` for remote transfers instead.

**Filesystem support**: Some older or specialized filesystems may not handle sparse files well. Verify support with:

``` bash
touch test && fallocate -z -l 1G test && du test
```

If `du` shows more than a few kilobytes, your filesystem doesn’t support holes.

**Backup tools**: Not all backup software respects sparseness. Verify your backup strategy with:

``` bash
# Create test sparse file
truncate -s 1G sparse_test
du sparse_test  # Should show minimal usage

# Run backup
tar --sparse -czf backup.tar.gz sparse_test

# Check if backup preserves sparseness
tar -tzf backup.tar.gz sparse_test
```

**Container and VM layers**: When using sparse files with container or VM storage drivers (Docker, KVM, etc.), verify that your storage backend supports them. Some networked storage systems or older LVM configurations may not handle holes correctly.

**File system limits**: Be aware of file size limits on your filesystem. ext4 supports files up to 16TB, btrfs and XFS support much larger files, but older filesystems may have lower limits.
