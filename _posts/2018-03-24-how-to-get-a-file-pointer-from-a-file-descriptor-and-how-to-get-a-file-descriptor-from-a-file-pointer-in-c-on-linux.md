---
title: "Converting Between File Descriptors and FILE Pointers in C"
date: 2018-03-24 11:48:07 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-get-a-file-pointer-from-a-file-descriptor-and-how-to-get-a-file-descriptor-from-a-file-pointer-in-c-on-linux/
---

When working with file I/O in C on Linux, you’ll often need to convert between low-level file descriptors (returned by `open()`, `socket()`, etc.) and higher-level `FILE` pointers (returned by `fopen()`). This is common when integrating different libraries or mixing POSIX I/O with standard C I/O.

## Getting a FILE Pointer from a File Descriptor

Use `fdopen()` to wrap an existing file descriptor in a `FILE` stream:

``` c
#include <stdio.h>

int fd = open("file.txt", O_RDONLY);
if (fd < 0) {
    perror("open");
    return 1;
}

FILE *file = fdopen(fd, "r");
if (file == NULL) {
    perror("fdopen");
    close(fd);
    return 1;
}

// Use file normally
fgets(buffer, sizeof(buffer), file);
fclose(file);  // This also closes fd
```

**Important points:**

- The mode string (`"r"`, `"w"`, `"a"`, etc.) must be compatible with how the descriptor was originally opened
- Don’t close the file descriptor separately after calling `fdopen()` — `fclose()` on the `FILE` pointer will close both
- If mode compatibility is wrong (e.g., `fdopen(fd, "w")` on a read-only descriptor), `fdopen()` succeeds but subsequent I/O will fail
- The `FILE` stream doesn’t own the descriptor — if `fdopen()` fails, you must close the descriptor yourself

## Getting a File Descriptor from a FILE Pointer

Use `fileno()` to extract the underlying file descriptor:

``` c
#include <stdio.h>

FILE *file = fopen("file.txt", "r");
if (file == NULL) {
    perror("fopen");
    return 1;
}

int fd = fileno(file);
if (fd < 0) {
    perror("fileno");
    fclose(file);
    return 1;
}

// Use fd directly with POSIX functions
struct stat st;
fstat(fd, &st);
printf("File size: %ld bytes\n", st.st_size);

fclose(file);
```

**Important points:**

- `fileno()` returns -1 on error (though failure is rare with valid `FILE` pointers)
- The descriptor remains owned by the `FILE` stream — don’t close it directly
- Closing the `FILE` pointer will close the descriptor
- Changes made via the descriptor (seek position, flags) affect the `FILE` stream and vice versa

## Practical Example: Mixing POSIX and stdio I/O

``` c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(void) {
    // Open with POSIX, use with stdio
    int fd = open("data.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        return 1;
    }

    FILE *file = fdopen(fd, "w");
    if (file == NULL) {
        perror("fdopen");
        close(fd);
        return 1;
    }

    fprintf(file, "Hello from stdio\n");
    fflush(file);  // Ensure data is written

    // Get descriptor back for POSIX operations
    fd = fileno(file);
    if (fsync(fd) < 0) {
        perror("fsync");
    }

    fclose(file);
    return 0;
}
```

## Caveats with Buffering

When mixing the descriptor and `FILE` pointer, be aware of buffering:

- `FILE` streams are buffered by default (fully buffered for files, line-buffered for terminals)
- Data written via `fprintf()` may not reach the OS immediately
- Use `fflush()` before performing POSIX operations on the descriptor to ensure consistency
- Use `setvbuf()` to control buffering if needed

``` c
FILE *file = fdopen(fd, "r");
setvbuf(file, NULL, _IONBF, 0);  // Disable buffering
```

Both `fdopen()` and `fileno()` are standard POSIX functions available on all modern Linux systems and other Unix-like operating systems.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Converting Between File Descriptors and FILE Pointers in C with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Converting Between File Descriptors and FILE Pointers in C. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
