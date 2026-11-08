---
title: "Measuring CFS Scheduler Timeslices in Linux"
date: 2016-12-05 02:47:34 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /length-timeslice-processes-cfs-process-scheduling-algorithm-linux-kernel/
---

CFS (Completely Fair Scheduling) is the default process scheduler in modern Linux kernels. Understanding actual timeslice allocation—how long a process runs before being context-switched out—is essential for performance debugging, verifying fairness assumptions, and identifying scheduling anomalies. The challenge is that /proc interfaces and ps commands show scheduling policy but not the actual on-CPU duration per scheduling event.

## Why Timeslice Measurement Matters

Understanding actual timeslice allocation helps with:

- Performance debugging of scheduling behavior and latency issues
- Verifying fairness assumptions in your workload
- Detecting processes starved of CPU time
- Identifying priority inversion and scheduling anomalies
- Custom scheduler research and kernel development

## Using perf (Fastest Start)

The perf tool captures context switch events with minimal overhead:

``` bash
# Record context switches for a specific PID for 10 seconds
perf record -e sched:sched_switch -p <PID> -- sleep 10

# View the raw data
perf script | head -20

# Real-time context switch tracing
perf trace -e sched:sched_switch -p <PID> sleep 30
```

This records kernel events without instrumentation. The timestamps in the output allow you to calculate actual timeslice durations by measuring the time between consecutive sched_switch events for a given PID.

For analyzing the results with higher-level statistics:

``` bash
# Get summary of context switches per process
perf script | grep sched_switch | awk -F'[()]' '{print $2}' | sort | uniq -c

# Export to CSV for analysis
perf script > /tmp/sched_trace.txt
```

## Using ftrace Directly

ftrace provides kernel event tracing without kernel recompilation and works on all modern kernels:

``` bash
# Enable sched_switch tracing for a specific PID
echo "sched_switch" > /sys/kernel/debug/tracing/set_event
echo <PID> > /sys/kernel/debug/tracing/set_ftrace_pid
cat /sys/kernel/debug/tracing/trace_pipe

# Output shows: <PID>-<TID> [CPU] TIMESTAMP: sched_switch: prev_comm=...
```

For continuous monitoring with output to file:

``` bash
# Start background tracing
echo <PID> > /sys/kernel/debug/tracing/set_ftrace_pid
cat /sys/kernel/debug/tracing/trace_pipe > /tmp/sched.log &
TRACE_PID=$!

# Let it run, then stop
sleep 30
kill $TRACE_PID

# Parse timestamps to calculate timeslices
awk '/sched_switch/{print $3}' /tmp/sched.log | sed 's/://' | awk '{if(prev) print $1-prev; prev=$1}'
```

Clear the trace buffer when done:

``` bash
echo 0 > /sys/kernel/debug/tracing/set_ftrace_pid
echo "" > /sys/kernel/debug/tracing/set_event
```

## Using eBPF and BCC Tools (Production Recommended)

eBPF is the modern approach for production systems—efficient, no kernel recompilation, lower overhead:

``` bash
# Install bcc tools
apt install bpfcc-tools  # Debian/Ubuntu
dnf install bcc         # RHEL/Fedora
```

Use built-in tools to monitor scheduling:

``` bash
# Monitor scheduler queue depth
/usr/share/bcc/tools/runqlen 10

# Measure time between sched_switch events (context switch latency)
/usr/share/bcc/tools/offcputime -p <PID> 10
```

For custom eBPF programs, write a simple timeslice measurement tool:

``` c
// sched_measure.c - eBPF program
#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

BPF_HASH(start_times, u32);
BPF_HASH(timeslice_stats, u32);

struct timeslice_info {
    u64 total_ns;
    u64 count;
    u64 min_ns;
    u64 max_ns;
};

TRACEPOINT_PROBE(sched, sched_switch) {
    u32 prev_pid = args->prev_pid;
    u32 next_pid = args->next_pid;
    u64 now = bpf_ktime_get_ns();

    // Record when prev_pid stops running
    if (prev_pid != 0) {
        u64 *start = start_times.lookup(&prev_pid);
        if (start) {
            u64 timeslice_ns = now - *start;

            struct timeslice_info *stats = timeslice_stats.lookup(&prev_pid);
            if (stats) {
                stats->total_ns += timeslice_ns;
                stats->count++;
                if (timeslice_ns < stats->min_ns) stats->min_ns = timeslice_ns;
                if (timeslice_ns > stats->max_ns) stats->max_ns = timeslice_ns;
            } else {
                struct timeslice_info new_stats = {
                    .total_ns = timeslice_ns,
                    .count = 1,
                    .min_ns = timeslice_ns,
                    .max_ns = timeslice_ns
                };
                timeslice_stats.update(&prev_pid, &new_stats);
            }
        }
    }

    // Record when next_pid starts running
    start_times.update(&next_pid, &now);
    return 0;
}
```

Compile with `llvm-clang` and libbpf, or use bcc’s Python bindings for rapid development.

## Understanding CFS Scheduler Parameters

CFS uses virtual runtime (vruntime) to allocate fair timeslices. The actual timeslice depends on:

- **Min granularity**: Minimum timeslice for any process (default 0.75ms on most systems)
- **Target latency**: Desired scheduling period across all runnable tasks (default 6ms)
- **Timeslice calculation**: `timeslice = target_latency / nr_running` (capped at min/max bounds)

Check current parameters:

``` bash
cat /proc/sys/kernel/sched_min_granularity_ns
cat /proc/sys/kernel/sched_latency_ns
cat /proc/sys/kernel/sched_wakeup_granularity_ns
```

On a system with 4 runnable processes and default settings, each expects roughly 1.5ms of CPU per scheduling cycle. On a 2GHz CPU, that’s 3 million instruction cycles per timeslice—significant for latency-critical workloads.

Adjust for latency-sensitive workloads (requires testing):

``` bash
# Reduce min granularity for lower-latency switching (higher overhead)
echo 500000 > /proc/sys/kernel/sched_min_granularity_ns

# Reduce target latency (more frequent switches, higher overhead)
echo 3000000 > /proc/sys/kernel/sched_latency_ns
```

For real-time workloads, use `SCHED_FIFO` or `SCHED_RR` instead of tuning CFS:

``` bash
chrt -f 50 ./my_realtime_app  # SCHED_FIFO with priority 50
```

## Custom Kernel Instrumentation (For Research Only)

Custom kernel modifications are rarely needed for timeslice measurement. The above methods cover most use cases. Only consider kernel instrumentation for scheduler research or custom scheduler variants.

If you must instrument the kernel, modify `kernel/sched/core.c` to track timestamps:

``` c
static void __schedule(void)
{
    struct task_struct *prev = current;
    struct task_struct *next = pick_next_task(rq, prev, rf);

    u64 switch_time = ktime_get_ns();

    if (prev->pid && target_monitoring_enabled) {
        u64 timeslice_ns = switch_time - prev->se.exec_start;
        trace_sched_timeslice(prev->pid, timeslice_ns);
    }

    prev->se.exec_start = switch_time;
    context_switch(rq, prev, next);
}
```

Use ktime_get_ns() for nanosecond precision (available since kernel 3.17).

## Practical Measurement Examples

Measure a CPU-bound workload:

``` bash
# Create a simple CPU-bound loop
bash -c 'while true; do :; done' &
PID=$!

# Trace its scheduling for 5 seconds
perf record -e sched:sched_switch -p $PID -- sleep 5

# Analyze context switches
perf script | grep sched_switch | wc -l

kill $PID
```

Measure under system load:

``` bash
# Start a test workload
stress-ng --cpu 2 --timeout 10s &

# In another terminal, monitor system scheduling
perf record -e sched:sched_switch -a -- sleep 10
perf script | grep sched_switch | awk '{print $(NF-1)}' | sort -n | uniq -c | tail -20
```

Compare scheduling fairness across multiple processes:

``` bash
# Run three processes
for i in 1 2 3; do
  bash -c 'while true; do :; done' &
  echo $!
done

# Record all context switches
perf record -e sched:sched_switch -a -- sleep 5
perf script | awk '/sched_switch/{print $3}' | sort | uniq -c | sort -rn
```

## Interpreting Results

When analyzing timeslice data:

- **Expected range**: On a system running N processes, expect timeslices near `target_latency / N` in nanoseconds (e.g., 1.5ms on a 4-CPU loaded system with defaults)
- **Variance**: Some variance is normal; consistent under-allocation indicates scheduler congestion or high load
- **Outliers**: Timeslices much longer than expected may indicate priority inheritance, real-time constraints, or I/O wait
- **Fairness**: All non-RT processes of equal priority should have similar average timeslices over time; large deviations suggest load imbalance across CPUs

Check load distribution:

``` bash
# See per-CPU runqueue lengths
cat /proc/sched_debug | grep "cpu#" -A 10 | grep "cfs_rq\|nr_running"

# Monitor in real-time
watch -n 0.1 'cat /proc/sched_debug | grep -A 2 "cpu#"'
```

## Common Issues and Solutions

**High variance in timeslice measurements**: This is often normal. Real systems have timer interrupts, NUMA effects, and wake-up jitter. Collect longer traces (30+ seconds) to see overall trends.

**Process getting less CPU than expected**: Check task priority with `ps -o pri,ni <PID>` and verify it’s not blocked on I/O with `cat /proc/<PID>/stat | awk '{print $3}'` (look for ‘S’ = interruptible sleep).

**Tracing overhead is too high**: Switch from perf to eBPF, or use ftrace with filters (`set_ftrace_filter`) to limit traced events. In extreme cases, measure on an isolated test system rather than production.
