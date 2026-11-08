---
title: "Linux Kernel\u2019s taskstats: Per-Task Performance Metrics"
date: 2017-02-14 01:56:21 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-collect-task-stats-data/
---

The Linux kernel provides the taskstats API to monitor detailed per-task statistics, including I/O wait time, CPU scheduling delays, and memory reclamation waits. Understanding how these metrics are collected at the kernel level is essential for diagnosing performance issues and understanding process behavior.

## How the Kernel Records I/O Delays

The kernel records I/O wait delays through a two-step process: marking when I/O begins and calculating elapsed time when it completes.

When a task needs to wait for synchronous I/O, the kernel calls `io_schedule_timeout()` in `kernel/sched/core.c`. This function:

1.  Sets the task’s `in_iowait` flag to 1
2.  Calls `delayacct_blkio_start()` to record the current time via `ktime_get_ns()`
3.  Increments the runqueue’s `nr_iowait` counter
4.  Yields to the scheduler
5.  Upon I/O completion, calls `delayacct_blkio_end()` to calculate the elapsed time
6.  Decrements `nr_iowait` and restores the task state

The kernel code looks like this:

``` c
long __sched io_schedule_timeout(long timeout)
{
    int old_iowait = current->in_iowait;
    struct rq *rq;
    long ret;

    current->in_iowait = 1;
    blk_schedule_flush_plug(current);

    delayacct_blkio_start();
    rq = raw_rq();
    atomic_inc(&rq->nr_iowait);
    ret = schedule_timeout(timeout);
    current->in_iowait = old_iowait;
    atomic_dec(&rq->nr_iowait);
    delayacct_blkio_end();

    return ret;
}
```

The delay calculation — the time from `delayacct_blkio_start()` to `delayacct_blkio_end()` — is stored in the task’s `delays->blkio_delay` field. The kernel maintains this in nanosecond precision internally.

## Accumulating Delays into blkio_delay_total

When userspace requests task statistics via the taskstats API (typically at process exit or via explicit query), the kernel accumulates all I/O delays for that task. This happens in `__delayacct_add_tsk()` in `kernel/delayacct.c`:

``` c
int __delayacct_add_tsk(struct taskstats *d, struct task_struct *tsk)
{
    ...
    tmp = d->blkio_delay_total + tsk->delays->blkio_delay;
    d->blkio_delay_total = (tmp < d->blkio_delay_total) ? 0 : tmp;
    ...
    return 0;
}
```

This code adds the current `blkio_delay` to the running total. The ternary operator handles overflow: if the sum wraps around, it resets to 0. In practice, 64-bit unsigned counters rarely overflow, but the check provides defensive behavior.

## Other Tracked Delay Metrics

The kernel tracks several types of delays using the same instrumentation pattern:

- **cpu_delay_total** — time waiting for CPU scheduling (measured during context switch path)
- **blkio_delay_total** — time waiting for block I/O (measured in `io_schedule` paths)
- **swapin_delay_total** — time waiting for swapped-in pages (measured in page fault handler)
- **freepages_delay_total** — time waiting for memory reclamation during page allocation

Each follows the same pattern: mark start time when entering the wait path, calculate delta when resuming, and accumulate into the task’s delay counters.

## Querying Task Stats from Userspace

First, enable delay accounting:

``` bash
echo 1 > /proc/sys/kernel/task_delayacct
```

This adds minimal overhead (a few bytes per `task_struct`). Then query stats using the `getdelays` tool:

``` bash
# Query a running process
getdelays -p <pid>

# Query a command and its children
getdelays -c sleep 5

# Query a process group
getdelays -g <pgrp>
```

The output includes `blkio_delay_total` in nanoseconds, along with other delay metrics:

    PID     COMMAND        DELAYS
                           CPU       IO     SWAPIN   RECLAIM
    10234   sleep          5ms       12ms   0ms      0ms

You can also access this programmatically via the netlink taskstats interface. For additional granularity, read `/proc/<pid>/stat` and related files, though these provide less detailed delay information than taskstats.

## Precision and Limitations

The kernel measures delays using `ktime_get_ns()`, providing nanosecond precision at the API level. However, several factors affect measurement accuracy and usefulness:

**Timer Source Granularity** — Resolution depends on the system’s timer source. Modern systems use TSC (Time Stamp Counter) with NTP correction or HPET (High Precision Event Timer). Virtualized systems may have coarser granularity, potentially missing sub-millisecond delays. Check your system with:

``` bash
cat /sys/devices/system/clocksource/clocksource0/current_clocksource
```

**Overhead Not Included** — The kernel only measures the actual I/O wait duration, not the time spent in the scheduler before yielding or the latency to reach the I/O path. Context switch overhead is separate from I/O delay.

**Per-I/O Granularity** — Each `delayacct_blkio_end()` call adds to the total, so you see cumulative delays, not per-request breakdowns. For individual I/O tracing, use `blktrace` or `iotrace`.

**Sampling Blind Spots** — The kernel only tracks explicit I/O waits via `io_schedule()` paths. Asynchronous I/O, buffered reads that hit cache, and memory-mapped file accesses may not register as I/O delays.

## When to Use taskstats

Taskstats is most useful when you need to:

- Profile long-running processes at exit to identify cumulative I/O bottlenecks
- Compare delay metrics across different tasks or runs for baseline performance
- Integrate delay accounting into process accounting systems (systemd uses this for resource tracking)
- Identify whether a slow process is CPU-bound, I/O-bound, or memory-bound

For workload analysis, combine taskstats with complementary tools:

- **iotop** — real-time I/O usage per process (uses `/proc/<pid>/io`)
- **iostat** — per-device I/O statistics
- **bpftrace / eBPF** — trace individual I/O requests and latencies
- **perf** — CPU sampling and event tracing

## Example: Monitoring a Batch Job

To measure I/O impact on a batch workload:

``` bash
# Enable delay accounting
echo 1 > /proc/sys/kernel/task_delayacct

# Run your workload
getdelays -c ./my_batch_job --arg1 --arg2
```

Sample output:

    CPU: 2500ms  IO: 800ms  SWAPIN: 0ms  RECLAIM: 50ms
    Total elapsed: 3500ms (I/O accounts for ~23% of total time)

This tells you whether optimizing I/O access patterns or increasing I/O concurrency would help. If I/O delay is high but CPU delay is low, you’re I/O-bound. If both are high, you likely have contention on a shared resource. High freepages_delay indicates memory pressure; high swapin_delay suggests insufficient physical memory or misaligned NUMA topology.
