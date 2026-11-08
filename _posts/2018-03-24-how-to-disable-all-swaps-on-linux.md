---
title: "Disabling All Swap on Linux"
date: 2018-03-24 08:13:49 +0000
modified: 2026-04-12 16:04:56 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-disable-all-swaps-on-linux/
---

To disable all active swap spaces on Linux, run:

``` bash
swapoff -a
```

The `-a` flag targets all currently enabled swap devices and files. This forces the kernel and applications to rely entirely on physical RAM.

### When You’d Do This

Disabling swap is useful for:

- **Performance testing**: Eliminating swap I/O variance to get consistent benchmarks
- **Latency-sensitive workloads**: High-frequency trading, real-time systems, or audio processing where swap latency is unacceptable
- **Memory-constrained environments**: When you want to fail fast rather than degrade gracefully under memory pressure
- **Troubleshooting OOM behavior**: To observe how your application handles actual out-of-memory conditions

### Important Caveats

Before you disable swap, understand the risks:

- **No fallback for memory pressure**: If your workload exceeds available RAM, the kernel will invoke the OOM killer and terminate processes. There’s no graceful degradation.
- **System instability**: Even desktop or server workloads can trigger OOM killing of critical services (sshd, systemd, etc.), making your system unreachable.
- **Not reversible without restart**: While you can re-enable swap with `swapon -a`, applications already killed by OOM won’t recover.

### Checking Current Swap Status

Before making changes, see what swap devices are active:

``` bash
swapon --show
```

Or use the traditional method:

``` bash
free -h
cat /proc/swaps
```

### Disabling Specific Swap Devices

To disable a single swap device or file instead of all:

``` bash
swapoff /dev/sda2
swapoff /swapfile
```

### Re-enabling Swap

To turn swap back on after disabling it:

``` bash
swapon -a
```

This re-enables all swap devices and files listed in `/etc/fstab`.

To enable a specific device:

``` bash
swapon /dev/sda2
swapon /swapfile
```

### Making Changes Persistent

These commands only affect the running system. To permanently disable swap across reboots, either:

1.  **Comment out swap entries in `/etc/fstab`**:

    ``` bash
    # /swapfile                                 none            swap    sw              0       0
    # /dev/sda2                                 none            swap    sw              0       0
    ```

2.  **Disable swap in systemd**:

    ``` bash
    systemctl mask dev-sda2.swap
    ```

### Recommended Approach for Production

Instead of completely disabling swap, consider lowering `vm.swappiness`:

``` bash
sysctl vm.swappiness=10
```

This reduces swap usage while keeping it available as a safety net. Values range from 0 (minimal swap, but not disabled) to 100 (aggressive swapping). Most production systems use values between 10–30.

To make this permanent, add to `/etc/sysctl.conf`:

``` bash
vm.swappiness=10
```

Then reload:

``` bash
sysctl -p
```

This approach prevents OOM kills while still using physical memory primarily, offering a practical middle ground between performance and stability.

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
