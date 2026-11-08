---
title: "Getting File Size in C on Linux"
date: 2018-03-24 11:40:56 +0000
modified: 2026-04-12 16:55:50 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-get-the-file-length-in-c-on-linux/
---

To determine file size in C, use `stat()` to populate a `struct stat` and read the `st_size` field. Here’s the correct approach:

``` c
#include <sys/stat.h>
#include <stdio.h>

off_t file_length(const char *path)
{
    struct stat st;
    if (stat(path, &st) == -1) {
        perror("stat");
        return -1;
    }
    return st.st_size;
}
```

## Why `off_t` and not `long`

Using `off_t` as the return type is essential:

- **Platform-independent**: `off_t` is defined by POSIX to handle file sizes on that platform
- **Large file support**: On 64-bit systems, it’s guaranteed to handle files larger than 2GB
- **Consistency**: Matches the actual type of `st_size` in `struct stat`

On 32-bit systems without LFS (Large File Support) enabled, `off_t` is still limited to 2GB. Compile with `-D_FILE_OFFSET_BITS=64` if you need to handle larger files on 32-bit platforms.

## Complete Working Example

``` c
#include <sys/stat.h>
#include <stdio.h>

off_t file_length(const char *path)
{
    struct stat st;
    if (stat(path, &st) == -1) {
        perror("stat");
        return -1;
    }
    return st.st_size;
}

int main(void)
{
    off_t size = file_length("/tmp/test.txt");
    if (size == -1) {
        fprintf(stderr, "Failed to get file length\n");
        return 1;
    }
    printf("File size: %lld bytes\n", (long long)size);
    return 0;
}
```

Compile and test:

``` bash
gcc -o filesize filesize.c
./filesize /tmp/test.txt
```

## stat() vs lstat()

- **`stat()`**: Follows symbolic links and returns the size of the target file
- **`lstat()`**: Returns the size of the symlink itself (usually 256 bytes or less)

Use `lstat()` when you need to detect and measure symlinks:

``` c
off_t file_length_nofollow(const char *path)
{
    struct stat st;
    if (lstat(path, &st) == -1) {
        perror("lstat");
        return -1;
    }
    return st.st_size;
}
```

## Handling Special Files and Edge Cases

**Sparse files**: `st_size` returns logical size, not physical disk usage. Check `st_blocks` (512-byte blocks) for actual space consumed:

``` c
printf("Logical size: %lld bytes, blocks used: %lld\n", 
       (long long)st.st_size, (long long)st.st_blocks * 512);
```

**Directories and special files**: These often return 0 or unreliable values. Always check the file type:

``` c
if (S_ISREG(st.st_mode)) {
    printf("Regular file: %lld bytes\n", (long long)st.st_size);
} else if (S_ISDIR(st.st_mode)) {
    printf("Directory\n");
} else if (S_ISLNK(st.st_mode)) {
    printf("Symlink: %lld bytes\n", (long long)st.st_size);
} else {
    printf("Special file (device, socket, pipe, etc.)\n");
}
```

**Race conditions**: If the file may be modified concurrently, use `fstat()` on an open file descriptor to avoid TOCTOU (time-of-check-time-of-use) issues:

``` c
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdio.h>

off_t file_length_fd(const char *path)
{
    int fd = open(path, O_RDONLY);
    if (fd == -1) {
        perror("open");
        return -1;
    }

    struct stat st;
    if (fstat(fd, &st) == -1) {
        perror("fstat");
        close(fd);
        return -1;
    }

    close(fd);
    return st.st_size;
}
```

This approach ensures the file stays open during the measurement and can’t be swapped, deleted, or truncated between the stat call and your use of the size.

## Printing off_t Portably

The format specifier for `off_t` varies across platforms. Always cast to `long long` and use `%lld` for portable output:

``` c
printf("Size: %lld\n", (long long)st.st_size);
```

Alternatively, use `PRIdMAX` from `<inttypes.h>`:

``` c
#include <inttypes.h>
printf("Size: %" PRIdMAX "\n", (intmax_t)st.st_size);
```

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Getting File Size in C on Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Getting File Size in C on Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
