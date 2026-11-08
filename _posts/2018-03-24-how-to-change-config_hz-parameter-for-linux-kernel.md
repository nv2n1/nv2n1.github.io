---
title: "Configuring CONFIG_HZ in the Linux Kernel"
date: 2018-03-24 11:50:57 +0000
layout: post
canonical: https://www.systutorials.com/how-to-change-config_hz-parameter-for-linux-kernel/
---

CONFIG_HZ sets the kernel’s internal timer interrupt frequency (measured in Hz). This determines how often the kernel’s scheduler runs and how fine-grained process preemption can be. The default value is typically 250 Hz on most distributions, though some set it to 1000 Hz for lower latency workloads.

Higher CONFIG_HZ values (like 1000 Hz) reduce scheduling latency and improve responsiveness for interactive tasks, but increase CPU overhead and power consumption. Lower values (100 Hz) reduce overhead but increase latency. Real-time and embedded systems often tune this parameter based on workload requirements.

## Checking Current CONFIG_HZ

First, determine your kernel’s current CONFIG_HZ setting:

``` bash
cat /boot/config-$(uname -r) | grep CONFIG_HZ
```

On many systems, you can also infer it from the kernel’s timer interrupt frequency:

``` bash
grep "^CONFIG_HZ" /boot/config-$(uname -r)
```

If the config file isn’t available, check the running kernel’s jiffy rate:

``` bash
dmesg | grep -i "HZ"
```

## Rebuilding the Kernel

Changing CONFIG_HZ requires recompiling the kernel—there’s no runtime adjustment. Here’s the process:

### 1. Obtain Kernel Sources

``` bash
# On Debian/Ubuntu
sudo apt install linux-source build-essential libncurses-dev bison flex libssl-dev libelf-dev

# On RHEL/CentOS/Fedora
sudo dnf install kernel-devel gcc ncurses-devel bison flex openssl-devel elfutils-libelf-devel
```

### 2. Extract and Configure

``` bash
cd /usr/src/linux-source-*
cp /boot/config-$(uname -r) .config
```

Then run the configuration tool:

``` bash
make menuconfig
```

Navigate to **General setup** → **Kernel command line interface** (or similar, depending on kernel version) and locate the **Timer frequency (CONFIG_HZ)** option. Change the value to your desired setting (100, 250, 300, or 1000 Hz are common options).

Alternatively, edit `.config` directly:

``` bash
sed -i 's/CONFIG_HZ=250/CONFIG_HZ=1000/' .config
```

### 3. Build and Install

``` bash
make -j$(nproc)
sudo make modules_install install
```

### 4. Update Bootloader

For GRUB systems:

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

For UEFI systems, regenerate the EFI boot entry if necessary.

### 5. Reboot and Verify

``` bash
sudo reboot
cat /boot/config-$(uname -r) | grep CONFIG_HZ
```

## Considerations for Different Workloads

**Interactive/Desktop Systems**: Use CONFIG_HZ=1000 for lower input latency and smoother UI responsiveness.

**Server/Batch Processing**: Use CONFIG_HZ=250 (default) to reduce unnecessary scheduler overhead and power consumption.

**Real-Time Systems**: Use CONFIG_HZ=1000 or enable PREEMPT_RT patches for deterministic latency guarantees.

**Embedded/Low-Power Devices**: Use CONFIG_HZ=100 to minimize CPU wake-ups and extend battery life.

## Modern Alternatives

Rather than rebuilding kernels frequently, consider:

- **Using distribution kernels tuned for your use case**: Many distributions provide multiple kernel variants optimized for different workloads.
- **Dynamic frequency scaling**: Modern governors like `schedutil` adapt CPU frequency based on demand, reducing power consumption regardless of CONFIG_HZ.
- **eBPF-based monitoring**: Tools like BCC and libbpf allow kernel-level performance observation without modifying CONFIG_HZ.
- **Container-based testing**: Validate CONFIG_HZ changes in isolated environments before production deployment.

For most modern workloads, the default CONFIG_HZ value is sufficient. Only rebuild if profiling clearly identifies scheduling latency as a bottleneck.

## 2026 Best Practices and Advanced Techniques

For Configuring CONFIG_HZ in the Linux Kernel, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
