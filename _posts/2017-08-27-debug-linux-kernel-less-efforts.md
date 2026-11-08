---
title: "Debugging Kernel Modules with Runtime Parameters"
date: 2017-08-27 16:05:37 +0000
modified: 2026-04-11 16:21:11 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /debug-linux-kernel-less-efforts/
---

When you need to debug kernel behavior without full instrumentation frameworks, module parameters offer a pragmatic shortcut. Rather than immediately reaching for perf, kprobes, or eBPF, you can add simple toggles and state tracking directly in the code you’re investigating, then control them at runtime through sysfs.

Frameworks like perf, kprobes, and eBPF are powerful but carry overhead. If you’re debugging a specific subsystem and need quick answers—how long a process runs on CPU, what conditions trigger a bug, whether certain code paths execute—injecting minimal instrumentation with runtime control beats rebuilding the kernel repeatedly.

The technique is straightforward: add `module_param` declarations to export kernel variables, then read and write them via `/sys/module/*/parameters/` at runtime.

## Example: Tracing Scheduler Timeslices

Let’s trace how long a specific process executes before context switching. You’ll add module parameters to enable/disable tracing and specify a target PID, then log execution time when that process yields the CPU.

Here’s a minimal patch to `kernel/sched/core.c`:

``` c
#include <linux/moduleparam.h>

// Debug parameters
static int enable_debug = 0;
module_param(enable_debug, int, 0664);

static int target_pid = 0;
module_param(target_pid, int, 0664);

static unsigned long long prev_timestamp = 0;
module_param(prev_timestamp, ullong, 0444);
```

Then in the context switch path (around `__schedule()`), add timing logic:

``` c
static void __sched __schedule(bool preempt)
{
    // ... existing code ...

    if (rq->curr != next) {
        unsigned long long now = ktime_get_ns();
        struct task_struct *prev = rq->curr;

        if (enable_debug && prev->pid == target_pid) {
            unsigned long long delta = now - prev_timestamp;
            printk(KERN_INFO "sched: pid %d ran for %llu ns\n", 
                   prev->pid, delta);
        }

        prev_timestamp = now;
        rq->curr = next;
        // ... context switch logic ...
    }
}
```

## Runtime Control via sysfs

Once you’ve added module parameters, control them at runtime without recompiling:

Enable debugging for a specific process:

``` bash
echo 1 > /sys/module/core/parameters/enable_debug
echo 1234 > /sys/module/core/parameters/target_pid
```

Read current values:

``` bash
cat /sys/module/core/parameters/enable_debug
cat /sys/module/core/parameters/target_pid
```

Disable when finished:

``` bash
echo 0 > /sys/module/core/parameters/enable_debug
```

The permissions 0444, 0664, and 0755 control access. Use 0444 for read-only (like output-only variables such as `prev_timestamp`), and 0664 to let root write and others read.

## Modern Alternatives

While module parameters still work, several modern approaches often provide cleaner solutions:

**eBPF with bpftrace**: Attach lightweight probes without modifying source code:

``` bash
bpftrace -e 'tracepoint:sched:sched_stat_runtime { @us[args->pid] = sum(args->runtime); }'
```

This aggregates runtime by PID across all context switches without touching kernel code.

**Kernel tracepoints**: Use the built-in tracing infrastructure. List available tracepoints:

``` bash
cat /sys/kernel/debug/tracing/events/sched/sched_switch/format
```

Enable at runtime:

``` bash
echo 1 > /sys/kernel/debug/tracing/events/sched/sched_switch/enable
cat /sys/kernel/debug/tracing/trace_pipe
```

**ftrace**: The kernel’s built-in function tracer handles scheduler events and function calls without code changes:

``` bash
echo function > /sys/kernel/debug/tracing/current_tracer
echo __schedule >> /sys/kernel/debug/tracing/set_ftrace_filter
cat /sys/kernel/debug/tracing/trace
```

**trace-cmd**: Higher-level wrapper around ftrace for capture and analysis:

``` bash
trace-cmd record -e sched_switch sleep 5
trace-cmd report
```

## When to Use Each Approach

- **Module parameters**: Quick one-off investigations in code you’re already modifying, feature flags you control at runtime, collecting data in kernel logs. Best for prototyping and temporary debugging.
- **Tracepoints**: Standardized event logging, production-safe, works across kernel versions without code changes.
- **bpftrace**: Complex filtering, aggregation, and statistical analysis. Requires kernel 4.4+, ideal for performance analysis on live systems.
- **ftrace**: Function-level tracing and call graph analysis, minimal overhead, suitable for long-term investigation.

If you’re modifying scheduler code anyway, module parameters cost almost nothing and give you immediate runtime control. For unmodified kernels, reach for bpftrace or ftrace first.

## Best Practices

**Timing functions**: Use `ktime_get_ns()` for nanosecond precision instead of legacy `do_gettimeofday()`. For very frequent calls, consider `local_clock()` (already nanoseconds) or `sched_clock_cpu()`.

**Lock safety**: Avoid acquiring locks or doing heavy work in hot paths like schedulers. Keep instrumentation minimal—a few reads and conditional branches only.

**Validation**: Always validate target PIDs exist before enabling traces to avoid wasted output:

``` bash
kill -0 $TARGET_PID 2>/dev/null || echo "PID not found"
```

**Cleanup**: Remove debug code from production kernels. Even conditional checks in scheduler code accumulate measurable overhead. Use `#ifdef CONFIG_DEBUG_*` guards or compile-time configuration if traces must remain in the source.

**Atomicity**: When reading multi-word kernel variables via sysfs, use atomic types (`atomic_t`, `atomic64_t`) or memory barriers to avoid torn reads.
