---
title: "Efficiently Copy Large Sparse Files with SEEK_HOLE and SEEK_DATA"
date: 2018-03-24 07:54:14 +0000
author: "Eric Ma"
layout: post
categories: [testing-devops]
canonical: /how-to-efficiently-archive-a-very-large-sparse-file/
---

Archiving or copying a 1TB sparse file containing only 32MB of actual data is impractical with naive approaches—you’ll waste time and I/O bandwidth copying zeros. The solution is using `SEEK_HOLE` and `SEEK_DATA` flags with `lseek()`, which allow tools to skip over hole regions entirely.

## How SEEK_HOLE and SEEK_DATA work

The Linux kernel provides two additional flags for `lseek()` that were introduced in kernel 3.1:

**SEEK_DATA**: Moves the file offset to the next location containing actual data. If the offset already points to data, it stays put.

**SEEK_HOLE**: Moves the file offset to the next hole (unallocated region). If the offset is already in a hole, it stays there. If no hole exists past the current offset, the offset moves to the end of the file.

By using these flags, applications can map only the allocated extents of a file and skip copying or archiving the zero-filled holes. On a 1TB file with 32MB of data, this reduces processing from hours to seconds.

## Tool support

Modern versions of `tar`, `cp`, and archive utilities rely on `libarchive` for sparse file handling. `libarchive` has supported `SEEK_HOLE/SEEK_DATA` detection since version 3.0.4 (March 2012).

**GNU coreutils `cp`** supports the `--sparse=auto` flag (enabled by default on many systems), which uses these semantics to preserve sparseness:

``` bash
cp --sparse=auto large-sparse-file backup-copy
```

**tar with bsdtar/libarchive** automatically detects sparse files:

``` bash
tar cSf archive.tar sparse-file
tar xSf archive.tar
```

The `-S` flag explicitly enables sparse file handling in tar. Modern versions (libarchive 3.0.4+) use `SEEK_HOLE/SEEK_DATA` automatically when available.

## Practical examples

Create a test sparse file:

``` bash
# Create a 1TB sparse file with 1MB of actual data
dd if=/dev/zero of=test-sparse.img bs=1M count=1 seek=1048576
ls -lh test-sparse.img
du -h test-sparse.img
```

Note the difference between apparent size (`ls -lh`) and actual disk usage (`du -h`). The file appears 1TB but only uses ~1MB on disk.

Copy preserving sparseness:

``` bash
# Using cp with sparse detection
time cp --sparse=auto test-sparse.img test-sparse-copy.img

# Verify sparseness was preserved
du -h test-sparse-copy.img
```

Archive with minimal overhead:

``` bash
# Create sparse archive (tiny tarball, ~kilobytes)
time tar cSf test-sparse.tar test-sparse.img
ls -lh test-sparse.tar

# Extract with sparseness preserved
mkdir extract-dir
cd extract-dir
time tar xSf ../test-sparse.tar
du -h test-sparse.img
```

Performance comparison on modern systems:

``` bash
# Direct copy (efficient with SEEK_HOLE/SEEK_DATA)
time cp --sparse=auto test-sparse.img copy1.img

# rsync with --sparse flag (also uses SEEK_HOLE/SEEK_DATA)
time rsync --sparse test-sparse.img copy2.img

# Both complete in milliseconds to seconds, not hours
```

## Important caveats

**Filesystem support**: Not all filesystems report holes correctly. Modern ext4, btrfs, and XFS handle this properly. NFS and some older filesystems may not, causing performance degradation.

**File must contain actual holes**: A file created with `dd if=/dev/zero of=file count=0 seek=10G` (zero bytes written) will be treated differently than `dd if=/dev/zero of=file count=1 seek=10G` (one byte written). The first creates a file with no extents and may not trigger sparse detection in some tools. Always write at least one byte to ensure the file contains proper extent metadata.

**Verify with `filefrag`**:

``` bash
filefrag -v test-sparse.img
```

This shows the actual extents allocated to the file. If output shows unmapped ranges, sparse detection is working.

**Tool version requirements**: Ensure you have at least `libarchive 3.0.4` (check with `bsdtar --version`) and modern GNU coreutils. Most distributions have shipped compatible versions for years.

## Manual sparse file handling in C

If you need custom sparse file logic:

``` c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int fd = open("sparse-file.img", O_RDONLY);
    off_t offset = 0;

    while (1) {
        // Find next data region
        off_t data_start = lseek(fd, offset, SEEK_DATA);
        if (data_start == (off_t)-1) break; // No more data

        // Find where data ends (next hole)
        off_t data_end = lseek(fd, data_start, SEEK_HOLE);
        if (data_end == (off_t)-1) {
            // Hole extends to EOF
            break;
        }

        printf("Data range: %ld to %ld (%ld bytes)\n", 
               data_start, data_end, data_end - data_start);

        offset = data_end;
    }
    close(fd);
    return 0;
}
```

Compile and run on a sparse file to see extent mapping in action.

## Modern best practice

In 2026, sparse file handling is standard—use `cp --sparse=auto` for general copying, `tar -S` for archiving, and verify with `du -h` versus `ls -lh` to confirm sparseness is preserved. For cloud storage and VM image management, this efficiency is essential.
