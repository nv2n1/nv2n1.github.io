---
title: "Linux Kernel: Implement SEEK_HOLE/SEEK_DATA in Custom llseek Handlers"
date: 2020-09-20 14:38:33 +0000
modified: 2026-04-11 16:14:00 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /fs-handle-seek_hole-seek_data-properly-in-all-fss-that-define-their-own-llseek/
---

The kernel commit “fs: handle SEEK_HOLE/SEEK_DATA properly in all fs’s that define their own llseek” (06222e4) by Josef Bacik ensures that all filesystems with custom `llseek` implementations properly handle the `SEEK_HOLE` and `SEEK_DATA` whence values introduced in Linux 3.1.

### Why This Matters

When a filesystem implements a custom `llseek` handler, it bypasses the generic implementation. Without explicit `SEEK_HOLE` and `SEEK_DATA` support, applications using these flags would receive incorrect results or errors. This commit standardizes behavior across NFS, CIFS, Ceph, FUSE, block devices, and other filesystems.

### What SEEK_HOLE and SEEK_DATA Do

`SEEK_DATA` and `SEEK_HOLE` allow applications to efficiently skip sparse regions in files:

- `SEEK_DATA`: Find the next byte with data at or after the given offset
- `SEEK_HOLE`: Find the next hole (unallocated space) at or after the given offset

These are critical for tools like `cp --sparse`, backup utilities, and database engines that need to handle sparse files efficiently.

### Implementation Patterns

The commit introduces three patterns across different filesystems:

**Pattern 1: Return -EINVAL**

Filesystems that don’t support sparse file semantics return `EINVAL`:

``` c
if (whence == SEEK_DATA || whence == SEEK_HOLE)
    return -EINVAL;
```

HPFS used this approach since it doesn’t track holes.

**Pattern 2: Revalidate File Size First**

Network filesystems (NFS, CIFS) must refresh file metadata before handling `SEEK_HOLE` and `SEEK_DATA`, since the file could have changed on the server:

``` c
if (origin != SEEK_SET && origin != SEEK_CUR) {
    int rc = nfs_revalidate_file_size(inode, filp);
    if (rc < 0)
        return rc;
}

switch (origin) {
case SEEK_END:
case SEEK_DATA:
case SEEK_HOLE:
    /* handle accordingly */
}
```

**Pattern 3: Full Implementation**

Filesystems like Ceph and FUSE that support sparse files implement the full logic:

``` c
case SEEK_DATA:
    if (offset >= inode->i_size) {
        return -ENXIO;
    }
    break;

case SEEK_HOLE:
    if (offset >= inode->i_size) {
        return -ENXIO;
    }
    offset = inode->i_size;
    break;
```

They return `ENXIO` when seeking beyond file bounds, and for `SEEK_HOLE`, they return the file size (the first hole after valid data).

### Key Code Changes

The commit standardized several improvements:

1.  **Consistent whence handling**: Replaced numeric constants (0, 1, 2) with symbolic `SEEK_SET`, `SEEK_CUR`, `SEEK_END` values
2.  **Explicit default cases**: Added `default:` clauses returning `-EINVAL` for unsupported whence values
3.  **Proper bounds checking**: Added validation to catch out-of-range offsets early

Block device handling was particularly important:

``` c
/* Before: incomplete switch handling */
switch (origin) {
    case 2:  /* SEEK_END */
        offset += size;
    case 1:  /* SEEK_CUR */
        offset += file->f_pos;
}

/* After: explicit cases and default */
switch (origin) {
    case SEEK_END:
        offset += size;
        break;
    case SEEK_CUR:
        offset += file->f_pos;
        break;
    case SEEK_SET:
        break;
    default:
        return -EINVAL;
}
```

### Practical Implications

For system administrators and developers, this meant:

- Sparse file tools now work correctly on network mounts
- Block device seeking is more predictable
- Custom filesystems (FUSE) can properly support sparse semantics
- Applications using `lseek(fd, offset, SEEK_HOLE)` get consistent behavior

### Testing SEEK_HOLE/SEEK_DATA

You can verify support with simple commands:

``` bash
# Create a sparse file
dd if=/dev/zero of=sparse.img bs=1M count=0 seek=100

# Test with lseek (requires testing tool)
# Most modern file utilities handle this transparently
cp --sparse=always sparse.img sparse_copy.img

# Verify sparseness
du -s sparse.img sparse_copy.img
ls -lh sparse.img sparse_copy.img
```

The kernel continues to support these semantics, with modern filesystems expected to implement proper `SEEK_HOLE`/`SEEK_DATA` handlers rather than returning `EINVAL`.
