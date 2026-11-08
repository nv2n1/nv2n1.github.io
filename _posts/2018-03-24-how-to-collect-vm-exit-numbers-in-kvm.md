---
title: "Tracking VM Exit Events in KVM"
date: 2018-03-24 11:51:07 +0000
modified: 2026-04-12 16:42:09 +0000
author: "Weiwei Jia"
layout: post
categories: [programming-languages]
canonical: /how-to-collect-vm-exit-numbers-in-kvm/
---

VM exits occur when a guest VM transitions to hypervisor mode to handle privileged operations, I/O requests, or other events. Tracking exit counts and types helps identify performance bottlenecks, inefficient guest behavior, and hypervisor overhead.

## Quick Exit Statistics

The debugfs interface provides a simple view of exit counts:

``` bash
kvm_stat
```

`kvm_stat` ships with KVM (sometimes as `/usr/share/kvm/kvm_stat`) and reads KVM tracepoints to show a live breakdown of exit reasons and their frequencies across all VMs. Run it as root. It needs tracing support enabled in the kernel and debugfs mounted at `/sys/kernel/debug`.

If you’re running with SELinux or AppArmor, ensure your user has appropriate access to debugfs. On hardened systems, you may need to disable enforcing mode temporarily:

``` bash
semanage fcontext -a -t debugfs_t "/sys/kernel/debug(/.*)?"
restorecon -Rv /sys/kernel/debug
```

## Per-VM Exit Tracking

For per-VM statistics, check the VM-specific stats:

``` bash
kvm_stat -p <qemu-pid>
```

This focuses the live view on one VM, showing which workloads generate the most exits. High exit rates from specific guests indicate either workload characteristics (expected) or tuning opportunities.

## Detailed Tracing with perf

For performance analysis beyond raw counts, use perf to trace exit reasons with full context:

``` bash
perf record -e kvm:kvm_exit -a sleep 30
perf script | grep kvm_exit | head -20
```

This captures exit events including the specific exit reason (e.g., `EXIT_REASON_HLT`, `EXIT_REASON_IO_INSTRUCTION`, `EXIT_REASON_CPUID`, `EXIT_REASON_EPT_VIOLATION`). Exit reasons vary by CPU architecture—x86_64 and ARM64 have different sets.

For more granular analysis, combine multiple KVM tracepoints:

``` bash
perf record -e kvm:kvm_exit,kvm:kvm_entry,kvm:kvm_page_fault -a -p <pid>
perf report --stdio
```

This traces entries, exits, and page faults for a specific QEMU process, useful when debugging single VM performance issues.

## ftrace Alternative

If perf isn’t available or you prefer kernel tracing directly:

``` bash
echo 1 > /sys/kernel/debug/tracing/events/kvm/kvm_exit/enable
cat /sys/kernel/debug/tracing/trace_pipe
```

Capture to a file for later analysis:

``` bash
echo 1 > /sys/kernel/debug/tracing/events/kvm/kvm_exit/enable
timeout 10 cat /sys/kernel/debug/tracing/trace_pipe > /tmp/kvm_exits.txt
```

## Interpreting Exit Reasons

Common high-volume exits typically include:

- **HLT**: Guest CPU idle loop—usually normal and low-cost
- **IO_INSTRUCTION**: I/O port access requiring emulation—investigate if excessive
- **EPT_VIOLATION**: Memory mapping faults—high rates suggest memory pressure or suboptimal guest memory configuration
- **CPUID**: CPUID instruction execution—usually infrequent unless workload heavily queries CPU features
- **PAUSE**: Guest pause instruction—normal in spinlock scenarios, but can indicate contention

Use `perf stat -e kvm:*` to get a quick breakdown across your running VMs, then drill into specific reasons with `perf record` and `perf script` filtering.

## Kernel Requirements

Exit statistics require:

- KVM tracepoint support (part of standard KVM builds)
- debugfs mounted (usually automatic on modern systems)
- Sufficient permissions (typically requires `root` or `kvm` group membership)

Check your kernel config:

``` bash
grep -E 'CONFIG_KVM=|CONFIG_DEBUG_FS' /boot/config-$(uname -r)
```

For production workloads, reserve detailed tracing for specific troubleshooting windows—continuous high-frequency KVM event tracing adds measurable overhead.

## 2026 Best Practices and Advanced Techniques

For Tracking VM Exit Events in KVM, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
