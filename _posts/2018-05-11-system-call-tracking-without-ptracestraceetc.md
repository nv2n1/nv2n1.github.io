---
title: "System Call Tracing with eBPF: Move Beyond ptrace"
date: 2018-05-11 15:22:48 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/system-call-tracking-without-ptracestraceetc/
---

Traditionally, tools like `strace` used `ptrace` to monitor system calls. While effective for development debugging, `ptrace` stops the entire process for every syscall, causing 2-10x slowdown. This makes it unsuitable for production workloads where you need real-time visibility without tanking performance.

Modern Linux offers significantly faster alternatives through eBPF (Extended Berkeley Packet Filter), which runs sandboxed programs directly in the kernel without recompilation or kernel source modifications.

## bpftrace: Kernel-Space Syscall Tracing

`bpftrace` is a high-level tracing language built on eBPF. It’s the fastest way to get syscall visibility on production systems, with overhead typically under 1-2% compared to `strace`‘s 2-10x slowdown.

Basic example — trace all `open()` and `openat()` calls with process name:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s (%d): %s\n", comm, pid, str(args->filename)); }'
```

Trace `openat()` failures only:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_exit_openat { if (retval < 0) { printf("%s: openat failed with %d\n", comm, retval); } }'
```

Monitor `write()` syscalls and their buffer sizes:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_write { printf("%s writes %d bytes\n", comm, args->count); }' | head -20
```

Count syscalls per process, updated every second:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[execname, name] = count(); } interval(s:1) { print(@); clear(@); }'
```

Filter by specific PID to reduce noise:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat /pid == 1234/ { printf("%s\n", str(args->filename)); }'
```

## perf: System-Wide Event Tracing

The `perf` tool can also trace syscalls via perf events, though `bpftrace` offers a more user-friendly interface:

``` bash
sudo perf trace -e open,openat,read,write -- /path/to/program
```

To trace a running process:

``` bash
sudo perf trace -p <PID> -e openat,read,write
```

`perf` is useful for broader system analysis and integrates with flame graphs, but requires more manual interpretation than `bpftrace`.

## auditd: Syscall Auditing and Compliance

For syscall auditing with permanent logging and filtering, `auditd` provides audit rules:

``` bash
sudo auditctl -a always,exit -F arch=b64 -S openat,open -F auid>=1000 -k file_access
sudo ausearch -k file_access
```

This is lightweight and logs to syslog or `/var/log/audit/audit.log`, making it suitable for compliance requirements. However, it’s less detailed than eBPF and has higher overhead for high-volume syscall tracking.

## Production Use Cases

**Security monitoring**: Cilium and Tetragon use eBPF to detect and block suspicious syscalls in Kubernetes and container environments without modifying application code. This is now standard in cloud-native deployments.

**Performance debugging**: Quickly identify which syscalls are slowing down your application:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[execname, name] = count(); } interval(s:1) { print(@); clear(@); }' | head -50
```

**Compliance and auditing**: Track file access, network syscalls, and privilege escalation attempts in real-time with persistent logs via `auditd`.

**Latency profiling**: Measure syscall latency per operation:

``` bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_read { @start[pid] = nsecs; } tracepoint:syscalls:sys_exit_read { @latency[comm] = hist(nsecs - @start[pid]); delete(@start[pid]); } interval(s:5) { print(@latency); }'
```

## Getting Started

**Check kernel support**: eBPF requires Linux 4.4+, but stable syscall tracepoints are available in 5.0+. Verify your kernel:

``` bash
uname -r
```

**List available syscall tracepoints**:

``` bash
sudo bpftrace -l | grep syscalls
```

**Run as non-root**: Grant capabilities instead of using full root:

``` bash
sudo setcap cap_bpf,cap_perfmon=ep /usr/bin/bpftrace
```

Or use a systemd service with `AmbientCapabilities=CAP_BPF CAP_PERFMON`.

**Save scripts for reuse**:

``` bash
cat > /etc/bpftrace/syscall_monitor.bt << 'EOF'
tracepoint:syscalls:sys_enter_openat {
  printf("%s (%d): %s\n", comm, pid, str(args->filename));
}
EOF

sudo bpftrace /etc/bpftrace/syscall_monitor.bt
```

**For persistent monitoring**, use container-native solutions like Tetragon (eBPF-based Kubernetes security) or embed `bpftrace` in systemd units.

## When to Use Each Tool

- **`bpftrace`**: Production monitoring, security, performance debugging — zero-overhead syscall tracing
- **`perf trace`**: System-wide profiling, integrating with performance tools
- **`auditd`**: Compliance logging, persistent audit trails
- **`strace`**: Development debugging only — too slow for production
