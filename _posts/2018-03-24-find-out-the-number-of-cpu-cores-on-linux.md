---
title: "How to Check CPU Core Count on Linux"
date: 2018-03-24 08:17:38 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /find-out-the-number-of-cpu-cores-on-linux/
---

Determining the number of CPU cores available on a Linux system is essential for performance tuning, application configuration, and capacity planning. Several approaches exist depending on what information you need.

### Quick check: nproc

The simplest way to get the number of CPU cores is `nproc`:

``` bash
$ nproc
8
```

This reports the number of logical processors available to the current process. It’s typically what you want for application threading or container resource limits.

### Detailed CPU information: /proc/cpuinfo

For more granular information, read `/proc/cpuinfo`:

``` bash
$ cat /proc/cpuinfo
```

This file contains detailed information about each logical processor. To count just the cores:

``` bash
$ grep -c "^processor" /proc/cpuinfo
8
```

Or to see physical vs. logical cores:

``` bash
$ grep "^physical id" /proc/cpuinfo | sort -u | wc -l
2
$ grep "^processor" /proc/cpuinfo | wc -l
8
```

In this example, there are 2 physical CPUs with 4 logical cores each (likely due to hyperthreading).

### Using lscpu

The `lscpu` command provides structured output and is more reliable than parsing `/proc/cpuinfo`:

``` bash
$ lscpu | grep -E "^CPU\(s\)|^Core\(s\)|^Thread\(s\)"
CPU(s):               8
Core(s) per socket:   4
Thread(s) per core:   2
```

This makes it clear that you have 2 sockets × 4 cores × 2 threads = 8 logical processors.

### In containerized environments

When running in containers (Docker, Kubernetes), `nproc` respects CPU limits set via cgroups:

``` bash
# Container with --cpus="2"
$ nproc
2
```

However, `/proc/cpuinfo` may still show the host’s full CPU count. For containers, `nproc` is the correct value to use since it reflects what the application can actually access.

### Checking hyperthreading status

To determine if hyperthreading is enabled:

``` bash
$ lscpu | grep "Thread(s) per core"
Thread(s) per core:   2
```

If this value is 1, hyperthreading is disabled. A value greater than 1 means multiple threads per physical core.

### In scripts and applications

For programmatic use, `nproc` is portable and reliable:

``` bash
#!/bin/bash
cores=$(nproc)
threads=$((cores * 2))
echo "Processing with $threads threads"
```

In Python, use the `multiprocessing` module:

``` python
import multiprocessing
cores = multiprocessing.cpu_count()
print(f"Available cores: {cores}")
```

### Performance considerations

When configuring applications like database servers, web servers, or thread pools, be aware of the difference between logical and physical cores. A system with 4 physical cores and hyperthreading enabled will report 8 logical cores. For CPU-bound workloads, using more threads than physical cores may degrade performance due to context switching overhead. For I/O-bound workloads, logical cores are often appropriate.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
