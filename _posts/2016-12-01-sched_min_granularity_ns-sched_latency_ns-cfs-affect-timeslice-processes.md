---
title: "How the CFS Scheduler Controls Process Timeslices and Preemption"
date: 2016-12-01 06:31:04 +0000
modified: 2026-04-11 16:21:22 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /sched_min_granularity_ns-sched_latency_ns-cfs-affect-timeslice-processes/
---

The Completely Fair Scheduler (CFS) is the default process scheduler in Linux kernels since 2.6.23. It allocates CPU time proportionally based on process priority, but the actual timeslices and preemption behavior depend on three key tunable parameters: `sched_latency_ns`, `sched_min_granularity_ns`, and `sched_wakeup_granularity_ns`. Understanding how these work together is essential for tuning scheduler behavior on production systems.

## How CFS Calculates the Scheduling Period

CFS groups runnable tasks into scheduling periods. All ready-to-run processes get one turn during each period. The kernel computes the period dynamically based on task count:

``` c
static u64 __sched_period(unsigned long nr_running)
{
    u64 period = sysctl_sched_latency;
    unsigned long nr_latency = sysctl_sched_latency / sysctl_sched_min_granularity;

    if (nr_running > nr_latency) {
        period = sysctl_sched_min_granularity * nr_running;
    }

    return period;
}
```

The logic:

- Start with the base period: `sched_latency_ns`
- Calculate how many tasks fit in one period: `sched_latency_ns / sched_min_granularity_ns`
- If runnable tasks exceed this count, scale the period linearly with task count

**Default values** (as of kernel 6.x):

- `sched_latency_ns`: 24ms
- `sched_min_granularity_ns`: 3ms
- `sched_wakeup_granularity_ns`: 1ms

With these defaults, the period can accommodate 8 tasks (24ms ÷ 3ms) before scaling kicks in.

**Example calculations:**

- 4 runnable tasks → period = 24ms (below threshold)
- 8 runnable tasks → period = 24ms (at threshold)
- 16 runnable tasks → period = 48ms (16 × 3ms, scaled linearly)

This prevents individual timeslices from shrinking indefinitely under high load.

## Computing Individual Task Timeslices

Once the period is determined, each task receives a proportional slice based on its weight (derived from its nice value). Lower nice values = higher weight = longer timeslice.

``` c
timeslice = period × (task_weight / total_runqueue_weight)
```

Weight mapping for nice values:

- nice=-20: weight ≈ 88761
- nice=0: weight = 1024
- nice=+19: weight ≈ 15

**Practical example with two equal-priority tasks:**

- Both nice=0, weight=1024 each
- Total weight = 2048
- Period = 24ms
- Each task gets: 24ms × (1024 / 2048) = **12ms**

**Example with different priorities:**

- Task A (nice=0): weight = 1024
- Task B (nice=1): weight ≈ 819
- Total weight = 1843
- Period = 24ms
- Task A gets: 24ms × (1024 / 1843) ≈ **13.4ms**
- Task B gets: 24ms × (819 / 1843) ≈ **10.7ms**

## When Preemption Happens During Timer Ticks

The kernel evaluates preemption decisions at each timer tick via `check_preempt_tick()`. A task is preempted if either condition holds:

1.  It has run longer than its ideal timeslice
2.  It has run longer than `sched_min_granularity_ns` AND another task is significantly behind in virtual runtime (vruntime)

``` c
static void check_preempt_tick(struct cfs_rq *cfs_rq, struct sched_entity *curr)
{
    unsigned long ideal_runtime = sched_slice(cfs_rq, curr);
    u64 delta_exec = curr->sum_exec_runtime - curr->prev_sum_exec_runtime;

    if (delta_exec > ideal_runtime) {
        resched_curr(rq_of(cfs_rq));
        return;
    }

    if (delta_exec > sysctl_sched_min_granularity) {
        struct sched_entity *se = __pick_first_entity(cfs_rq);
        s64 delta = curr->vruntime - se->vruntime;

        if (delta > ideal_runtime)
            resched_curr(rq_of(cfs_rq));
    }
}
```

The key insight: `sched_min_granularity_ns` is a lower bound. Even if a task’s ideal slice is 1ms, it won’t be preempted until at least `sched_min_granularity_ns` has elapsed. This reduces context-switch overhead.

## Wakeup Preemption and sched_wakeup_granularity_ns

When a sleeping task wakes (after I/O completion, lock release, etc.), the scheduler decides whether to immediately preempt the currently running task. The decision uses:

``` c
static int wakeup_preempt_entity(struct sched_entity *curr, struct sched_entity *se)
{
    s64 gran = wakeup_gran(se);
    s64 vdiff = curr->vruntime - se->vruntime;

    return (vdiff > gran);
}
```

Where `wakeup_gran` is calculated as:

    wakeup_granularity = sched_wakeup_granularity_ns × (waking_task_weight / total_weight)

Preemption occurs only if the waking task’s vruntime lag exceeds its scaled wakeup granularity. This prevents thrashing from frequent short-lived wakeups (e.g., periodic timer callbacks) while still responsively scheduling I/O-bound tasks that have fallen behind.

## Viewing and Modifying Parameters

Check current values:

``` bash
cat /proc/sys/kernel/sched_latency_ns
cat /proc/sys/kernel/sched_min_granularity_ns
cat /proc/sys/kernel/sched_wakeup_granularity_ns
```

Make temporary changes:

``` bash
echo 48000000 > /proc/sys/kernel/sched_latency_ns
```

For persistence across reboots, add to `/etc/sysctl.d/99-sched.conf`:

    kernel.sched_latency_ns = 48000000
    kernel.sched_min_granularity_ns = 3000000
    kernel.sched_wakeup_granularity_ns = 500000

Then apply:

``` bash
sysctl -p /etc/sysctl.d/99-sched.conf
```

## Tuning Guidelines

**For CPU-bound workloads (batch processing, compute jobs):**

- Increase `sched_latency_ns` to 36–48ms to reduce context-switch overhead
- Keep `sched_min_granularity_ns` at 3–4ms
- Rationale: Longer scheduling periods mean fewer context switches, better CPU cache utilization

**For I/O-heavy workloads (web servers, databases):**

- Decrease `sched_wakeup_granularity_ns` to 500µs–1ms for faster responsiveness
- Keep `sched_latency_ns` at 24ms or lower
- Rationale: I/O tasks wake frequently; aggressive preemption keeps them responsive

**For interactive workloads (desktop, SSH sessions):**

- Keep defaults or reduce `sched_min_granularity_ns` to 2ms (not below 1ms)
- Reduce `sched_wakeup_granularity_ns` to 500µs
- Rationale: Lower granularity improves perceived latency for user input

**Testing methodology:**

- Use `taskset -c 0` to pin test processes to a single CPU for reproducibility
- Monitor preemption patterns: `perf sched record && perf sched latency`
- Measure application latency and throughput under realistic load
- Test for at least 10–15 minutes to capture sustained behavior
- Always revert changes if tail latency increases

## Important Caveats

- These parameters interact; changing one affects the behavior of others
- Very small `sched_min_granularity_ns` (\< 1ms) increases context-switch overhead and context-switch jitter
- Very large `sched_latency_ns` (\> 100ms) can harm interactive responsiveness
- On systems with many CPUs, per-CPU runqueues mean less contention, making these parameters less critical
- For real-time workloads, consider using SCHED_FIFO or SCHED_RR instead of SCHED_NORMAL
