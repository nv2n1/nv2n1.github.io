---
title: "How to Print the Function Call Stack in Linux Kernel"
date: 2018-03-24 11:51:30 +0000
modified: 2026-04-12 16:42:35 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-output-function-stack-in-linux-kernel/
---

Getting kernel function call stacks is essential for debugging driver issues, understanding kernel behavior, and performance profiling. The approach depends on what you’re trying to trace: live kernel execution, crash analysis, or post-mortem inspection.

## Using ftrace

The kernel’s built-in ftrace framework is the first tool to reach for. It’s zero-overhead when disabled and has minimal overhead when active.

Enable function tracing:

``` bash
echo function > /sys/kernel/debug/tracing/tracer
echo 1 > /sys/kernel/debug/tracing/tracing_on
```

View the trace output:

``` bash
cat /sys/kernel/debug/tracing/trace
```

Filter specific functions:

``` bash
echo 'do_sys_open' > /sys/kernel/debug/tracing/set_ftrace_filter
```

Disable tracing:

``` bash
echo 0 > /sys/kernel/debug/tracing/tracing_on
```

## Stack Traces with function_graph

For call graphs showing how functions call each other:

``` bash
echo function_graph > /sys/kernel/debug/tracing/tracer
echo 1 > /sys/kernel/debug/tracing/tracing_on
sleep 2
cat /sys/kernel/debug/tracing/trace
```

This shows entry and exit of functions with timing information and nesting depth.

## Using eBPF for Deep Kernel Inspection

For more sophisticated tracing without ftrace overhead, use eBPF tools. The `bcc` (BPF Compiler Collection) toolkit provides pre-built programs:

``` bash
# Stack sampling - shows which kernel functions are on CPU
sudo /usr/share/bcc/tools/profile -f 30

# Trace specific syscalls with stack
sudo /usr/share/bcc/tools/trace 'tracepoint:syscalls:sys_enter_open* "stack"'
```

Or use `bpftrace` for one-liners:

``` bash
# Show kernel stack for all malloc calls
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_open { print(kstack()); }'
```

## Kernel Panic and Crash Analysis

When the kernel crashes, the panic message includes a stack trace. For post-mortem analysis on crash dumps:

``` bash
# Install crash utility
sudo dnf install crash

# Analyze vmcore from crash
crash /boot/vmlinuz-$(uname -r) /var/crash/*/vmcore
```

In crash prompt:

    crash> bt
    crash> stack

## Using perf for Performance-Aware Stacks

Record stack traces during system execution:

``` bash
sudo perf record -g --call-graph dwarf -p <pid> sleep 10
sudo perf report
```

The `-g` flag records call graphs, and `dwarf` provides the most accurate stack information on modern systems.

## Kernel Module Debugging

For debugging issues in your own kernel module, add stack traces in your code:

``` c
#include <linux/stacktrace.h>

void dump_stack(void) {
    unsigned long entries[32];
    struct stack_trace trace = {
        .entries = entries,
        .max_entries = 32,
        .skip = 1,
    };
    save_stack_trace(&trace);
    print_stack_trace(&trace, 0);
}
```

Call `dump_stack()` at points where you need to understand the call chain.

## Practical Considerations

Always trace with debuginfo packages installed for readable symbol names:

``` bash
sudo dnf install kernel-debuginfo
```

Running extensive ftrace in production degrades performance. Use eBPF-based sampling for production diagnostics instead, which has sub-1% overhead compared to ftrace’s 5-10% potential impact.

For container environments, ensure `CONFIG_HAVE_SYSCALL_TRACEPOINTS=y` is enabled in your kernel build if you need syscall-level stacks.

When capturing stacks in loops, limit output to avoid overwhelming the trace buffer:

``` bash
echo 100000 > /sys/kernel/debug/tracing/buffer_size_kb
```

Disable tracing immediately after capturing data to prevent buffer wraparound and data loss.

## 2026 Best Practices and Advanced Techniques

For How to Print the Function Call Stack in Linux Kernel, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
