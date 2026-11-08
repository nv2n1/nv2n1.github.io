---
title: "Using ioprio_set to Control I/O Priority in Linux"
date: 2018-03-24 11:51:39 +0000
author: "Weiwei Jia"
layout: post
canonical: https://www.systutorials.com/how-to-use-ioprio_set-in-linux-c/
---

Linux doesn’t provide a glibc wrapper for `ioprio_set()`, so you need to call it directly via `syscall()`. Here’s the basic approach:

``` c
#include <unistd.h>
#include <sys/syscall.h>

syscall(SYS_ioprio_set, IOPRIO_WHO_PROCESS, pid, ioprio_value);
```

## Required definitions

You’ll need to define the I/O priority classes, target types, and helper macros. Add these to your source file or header:

``` c
/* I/O priority classes */
enum {
    IOPRIO_CLASS_NONE = 0,
    IOPRIO_CLASS_RT = 1,
    IOPRIO_CLASS_BE = 2,
    IOPRIO_CLASS_IDLE = 3,
};

/* Target types for ioprio_set */
enum {
    IOPRIO_WHO_PROCESS = 1,
    IOPRIO_WHO_PGRP = 2,
    IOPRIO_WHO_USER = 3,
};

/* Macros for priority encoding/decoding */
#define IOPRIO_CLASS_SHIFT 13
#define IOPRIO_PRIO_CLASS(mask) ((mask) >> IOPRIO_CLASS_SHIFT)
#define IOPRIO_PRIO_DATA(mask) ((mask) & ((1 << IOPRIO_CLASS_SHIFT) - 1))
#define IOPRIO_PRIO_VALUE(class, data) (((class) << IOPRIO_CLASS_SHIFT) | (data))
```

## Complete example

Here’s a working program that sets I/O priority for a process:

``` c
#include <unistd.h>
#include <sys/syscall.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum {
    IOPRIO_CLASS_NONE = 0,
    IOPRIO_CLASS_RT = 1,
    IOPRIO_CLASS_BE = 2,
    IOPRIO_CLASS_IDLE = 3,
};

enum {
    IOPRIO_WHO_PROCESS = 1,
    IOPRIO_WHO_PGRP = 2,
    IOPRIO_WHO_USER = 3,
};

#define IOPRIO_CLASS_SHIFT 13
#define IOPRIO_PRIO_VALUE(class, data) (((class) << IOPRIO_CLASS_SHIFT) | (data))

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <pid> <class> [priority]\n", argv[0]);
        fprintf(stderr, "Classes: 0=none, 1=realtime, 2=best-effort, 3=idle\n");
        return 1;
    }

    pid_t target_pid = atoi(argv[1]);
    int ioprio_class = atoi(argv[2]);
    int ioprio_data = (argc > 3) ? atoi(argv[3]) : 0;

    if (ioprio_class < 0 || ioprio_class > 3) {
        fprintf(stderr, "Invalid I/O priority class\n");
        return 1;
    }

    int ioprio = IOPRIO_PRIO_VALUE(ioprio_class, ioprio_data);

    if (syscall(SYS_ioprio_set, IOPRIO_WHO_PROCESS, target_pid, ioprio) < 0) {
        perror("ioprio_set");
        return 1;
    }

    printf("Set PID %d to I/O class %d with priority %d\n", 
           target_pid, ioprio_class, ioprio_data);
    return 0;
}
```

Compile with:

``` bash
gcc -o ioprio_set ioprio_set.c
```

Run to set a process to idle I/O priority:

``` bash
./ioprio_set 1234 3
```

## I/O priority classes explained

- **IOPRIO_CLASS_NONE**: No specific I/O scheduling hint
- **IOPRIO_CLASS_RT**: Real-time; gets highest I/O scheduling priority. Requires CAP_SYS_ADMIN
- **IOPRIO_CLASS_BE**: Best-effort (default for most processes). Priority ranges 0-7, where 0 is highest
- **IOPRIO_CLASS_IDLE**: Idle priority; only executes when no other I/O activity exists. Useful for background tasks

## Getting current I/O priority

You can read a process’s current I/O priority using `ioprio_get`:

``` c
int current_ioprio = syscall(SYS_ioprio_get, IOPRIO_WHO_PROCESS, target_pid);
if (current_ioprio < 0) {
    perror("ioprio_get");
} else {
    int class = IOPRIO_PRIO_CLASS(current_ioprio);
    int data = IOPRIO_PRIO_DATA(current_ioprio);
    printf("Class: %d, Priority: %d\n", class, data);
}
```

## Practical notes

- You typically need CAP_SYS_ADMIN capability to raise I/O priority or use realtime class
- Non-root users can generally lower their own process priority
- The `ionice` command-line tool uses these same syscalls under the hood
- I/O priority is per-process; threads inherit the parent’s priority but can be set individually
- Not all I/O schedulers support all classes (CFQ does; noop and deadline have limited support)

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Using ioprio_set to Control I/O Priority in Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Using ioprio_set to Control I/O Priority in Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
