---
title: "Using statvfs() to Check Disk Space on Linux"
date: 2015-04-14 01:48:02 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-available-filesystem-space-on-linux-a-c-function-and-a-cpp-example/
---

When writing to disk, you need to know if space is available — especially in systems software, daemons, and critical applications. The POSIX `statvfs()` call provides filesystem statistics across all POSIX systems, making it more reliable than Linux-specific alternatives like `statfs()`.

## The statvfs() API

Include the required header:

``` c
#include <sys/statvfs.h>
```

Function signature:

``` c
int statvfs(const char *path, struct statvfs *buf);
```

Returns 0 on success, -1 on error. The `struct statvfs` contains:

``` c
struct statvfs {
    unsigned long  f_bsize;    /* filesystem block size */
    unsigned long  f_frsize;   /* fragment size */
    fsblkcnt_t     f_blocks;   /* total blocks in filesystem */
    fsblkcnt_t     f_bfree;    /* total free blocks */
    fsblkcnt_t     f_bavail;   /* free blocks available to unprivileged users */
    fsfilcnt_t     f_files;    /* total inodes */
    fsfilcnt_t     f_ffree;    /* free inodes */
    fsfilcnt_t     f_favail;   /* free inodes for unprivileged users */
    unsigned long  f_fsid;     /* filesystem ID */
    unsigned long  f_flag;     /* mount flags (ST_RDONLY, etc.) */
    unsigned long  f_namemax;  /* maximum filename length */
};
```

The critical fields for space calculations:

- **f_bsize**: Block size in bytes
- **f_bavail**: Free blocks available to unprivileged users
- **f_bfree**: Total free blocks (includes root-reserved space)

For unprivileged users, available space = `f_bsize * f_bavail`. Root can additionally access `f_bsize * (f_bfree - f_bavail)`.

## Simple C Function

``` c
#include <sys/statvfs.h>
#include <stdio.h>

long GetAvailableSpace(const char* path)
{
    struct statvfs stat;

    if (statvfs(path, &stat) != 0) {
        perror("statvfs");
        return -1;
    }

    return stat.f_bsize * stat.f_bavail;
}
```

## C++ Implementation with Error Handling

``` cpp
#include <sys/statvfs.h>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstring>
#include <cerrno>

class FilesystemInfo {
public:
    static long GetAvailableSpace(const std::string& path) {
        struct statvfs stat;

        if (statvfs(path.c_str(), &stat) != 0) {
            std::cerr << "ERROR: failed to get available space for " << path 
                      << ": " << std::strerror(errno) << std::endl;
            return -1;
        }

        return stat.f_bsize * stat.f_bavail;
    }

    static void PrintFilesystemInfo(const std::string& path) {
        struct statvfs stat;

        if (statvfs(path.c_str(), &stat) != 0) {
            std::cerr << "ERROR: failed to get filesystem info for " << path 
                      << ": " << std::strerror(errno) << std::endl;
            return;
        }

        long total = stat.f_bsize * stat.f_blocks;
        long available = stat.f_bsize * stat.f_bavail;
        long used = total - (stat.f_bsize * stat.f_bfree);

        std::cout << "Filesystem info for: " << path << std::endl;
        std::cout << "  Total:     " << std::setw(15) << total << " bytes" << std::endl;
        std::cout << "  Used:      " << std::setw(15) << used << " bytes" << std::endl;
        std::cout << "  Available: " << std::setw(15) << available << " bytes" << std::endl;
        std::cout << "  Block size: " << stat.f_bsize << " bytes" << std::endl;
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <path>" << std::endl;
        return 1;
    }

    FilesystemInfo::PrintFilesystemInfo(argv[1]);
    return 0;
}
```

Compile with:

``` bash
g++ -std=c++17 -o fs_info fs_info.cpp
```

## Usage Examples

Check available space for any path (file, directory, or mount point):

``` bash
$ ./fs_info /tmp
Filesystem info for: /tmp
  Total:      8589934592 bytes
  Used:       2200000000 bytes
  Available:  4140032000 bytes
  Block size: 4096 bytes
```

The path doesn’t need to be a mount point — `statvfs()` returns info for the filesystem containing that path. If the path doesn’t exist:

``` bash
$ ./fs_info /nonexistent/path
ERROR: failed to get filesystem info for /nonexistent/path: No such file or directory
```

## Important Considerations

**Block size varies by filesystem**: ext4 typically uses 4096 bytes, but NTFS, btrfs, and others may differ. Always use the reported `f_bsize` rather than assuming a fixed value.

**Inode exhaustion is separate from space**: A filesystem can have free blocks but no available inodes. Check `f_favail` when creating many small files:

``` c
long available_inodes = stat.f_favail;
if (available_inodes < 1000) {
    // warn: running low on inodes
}
```

**Reserved space for root**: The `f_bavail` field accounts for filesystem reserved space (typically 5% on ext4). Use `f_bfree` if you need the actual total free blocks, but unprivileged processes will only reliably have `f_bavail` available.

**Detect read-only filesystems**: Check the mount flags before attempting writes:

``` c
#include <sys/statvfs.h>

if (stat.f_flag & ST_RDONLY) {
    // filesystem is mounted read-only
}
```

**Race conditions in production code**: Space can disappear between your check and your write. For critical applications, handle ENOSPC errors gracefully rather than relying solely on pre-write checks.

## Modern Alternatives

For C++17 and later, `std::filesystem::space()` provides a cleaner interface:

``` cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    auto info = fs::space("/tmp");
    std::cout << "Available: " << info.available << " bytes" << std::endl;
    return 0;
}
```

Compile with:

``` bash
g++ -std=c++17 -o fs_info fs_info.cpp
```

For lower-level control or maximum portability, `statvfs()` remains the standard choice across Unix-like systems.
