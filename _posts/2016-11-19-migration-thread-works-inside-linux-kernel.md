---
title: "How Linux Kernel Migration Threads Work"
date: 2016-11-19 01:58:42 +0000
layout: post
canonical: https://www.systutorials.com/migration-thread-works-inside-linux-kernel/
---

In computer systems, resources must be balanced across available hardware to maximize performance. The Linux kernel runs migration threads as per-CPU daemons to handle this work. These threads manage task migration between CPUs, CPU hotplug operations, and stop-machine synchronization.

You can observe migration threads on any modern system:

``` bash
$ ps aux | grep migration
root         9  0.0  0.0      0     0 ?        S    Nov17   0:00 [migration/0]
root        15  0.0  0.0      0     0 ?        S    Nov17   0:00 [migration/1]
root        21  0.0  0.0      0     0 ?        S    Nov17   0:00 [migration/2]
root        27  0.0  0.0      0     0 ?        S    Nov17   0:00 [migration/3]
root        33  0.0  0.0      0     0 ?        S    Nov17   0:00 [migration/4]
```

Each CPU gets one migration thread. There’s one `[migration/N]` thread per logical CPU on your system. These are kernel threads (notice the brackets in the COMM field and zero RSS).

## How Migration Works

The Linux kernel uses a layered approach to perform CPU migrations. When you call `sched_setaffinity()` to restrict a task to specific CPUs, or when the scheduler needs to move a running task, the kernel queues migration work to the appropriate CPU’s migration thread.

### The Call Chain

When a task needs to migrate (particularly if it’s currently running or in `TASK_WAKING` state), the kernel executes this call stack:

    stop_one_cpu()
      → cpu_stop_queue_work()
        → __cpu_stop_queue_work()
          → list_add_tail()         // Add work to queue
          → wake_up_process()       // Wake the migration thread

The migration work gets packaged as a work item, added to the target CPU’s work queue, and the migration thread is awakened to process it.

### Practical Example

You can trigger migrations manually to observe this in action:

``` bash
# Restrict a process to CPU 0 only
$ taskset -p -c 0 <pid>

# Move an already-running process to CPUs 1-3
$ taskset -p -c 1-3 <pid>

# Verify the change took effect
$ taskset -cp <pid>
```

When taskset executes, it calls `sched_setaffinity()`, which triggers the kernel’s migration path we just described.

## Kernel Implementation

Migration threads are created as per-CPU kernel threads using the `smp_hotplug_thread` mechanism. Here’s how the kernel structures them:

``` c
static struct smp_hotplug_thread cpu_stop_threads = {
    .store                  = &cpu_stopper.thread,
    .thread_should_run      = cpu_stop_should_run,
    .thread_fn              = cpu_stopper_thread,
    .thread_comm            = "migration/%u",
    .create                 = cpu_stop_create,
    .park                   = cpu_stop_park,
    .selfparking            = true,
};

static int __init cpu_stop_init(void)
{
    unsigned int cpu;

    for_each_possible_cpu(cpu) {
        struct cpu_stopper *stopper = &per_cpu(cpu_stopper, cpu);

        spin_lock_init(&stopper->lock);
        INIT_LIST_HEAD(&stopper->works);
    }

    BUG_ON(smpboot_register_percpu_thread(&cpu_stop_threads));
    stop_machine_unpark(raw_smp_processor_id());
    stop_machine_initialized = true;
    return 0;
}
early_initcall(cpu_stop_init);
```

Each CPU gets its own `cpu_stopper` structure containing a spinlock and a work queue (`works` list). The thread function `cpu_stopper_thread()` continuously processes items from this queue in a loop, checking `thread_should_run()` to determine if work is pending.

The spinlock protecting each CPU’s work queue prevents concurrent modifications. When a CPU’s stopper thread runs, it acquires the lock, executes pending work items serially, then releases the lock and potentially sleeps until awakened again.

## Initialization Sequence

Migration threads are initialized early during kernel boot as part of the `early_initcall` stage:

    start_kernel()
      → rest_init()
        → kernel_init()
          → kernel_init_freeable()
            → do_pre_smp_initcalls()
              → do_one_initcall()       // cpu_stop_init() runs here

The initialization order follows this sequence:

- early (cpu_stop_init runs here)
- core
- postcore
- arch
- subsys
- fs
- device
- late

Migration thread initialization happens during the “early” phase, ensuring per-CPU threads are available before the scheduler becomes fully active. This ordering is critical because the scheduler and task migration depend on these threads being ready.

## Why This Design

Using dedicated per-CPU migration threads provides several advantages:

**Serialization**: Each CPU’s migration thread is single-threaded, preventing race conditions when modifying a CPU’s task queue. Without this, concurrent migration requests could corrupt scheduler data structures.

**Stop-machine safety**: The migration mechanism integrates with stop-machine, allowing the kernel to halt all CPUs when needed. This is essential for CPU hotplug operations (disabling CPU cores), live patching, and other operations requiring atomic consistency across cores.

**Deterministic execution**: Migration work executes in a controlled context (the migration thread) rather than from arbitrary interrupt handlers or random scheduler paths. This makes timing more predictable and easier to debug.

**Separation of concerns**: Migration concerns are isolated from the general work queue system (kworker threads), giving them dedicated resources and priority handling.

## Monitoring Migration Activity

### Direct Process Inspection

``` bash
# Check migration/0 thread details
$ cat /proc/9/status

# View scheduling class and priority
$ ps -o pid,comm,cls,pri -p 9

# Monitor CPU time spent in migration
$ cat /proc/stat | grep cpu0
```

### Using Tracepoints

``` bash
# Record all task migration events
$ trace-cmd record -e sched_migrate_task sleep 5
$ trace-cmd report

# Look for patterns of migrations
$ trace-cmd report | grep sched_migrate_task
```

### Performance Tools

``` bash
# Monitor scheduling events with perf
$ perf record -e sched:sched_migrate_task -a sleep 10
$ perf report

# Generate flame graph of scheduler activity
$ perf record -e sched:sched_migrate_task -F 99 -a sleep 30
$ perf script > out.perf
```

### Checking Stopper Thread Load

``` bash
# See recent CPU usage of migration threads
$ ps aux | grep migration | grep -v grep

# Get per-thread CPU time
$ cat /proc/<pid>/stat | awk '{print $14, $15}' # utime, stime in jiffies
```

High migration thread CPU usage often indicates the scheduler is frequently moving tasks between CPUs, which can signal:

- Uneven workload distribution
- CPU affinity settings that conflict with scheduler load balancing
- Too-frequent CPU hotplug operations
- Inefficient task placement in NUMA systems

## Related Mechanisms

Other kernel daemon threads follow similar patterns. `softirqd`, `kworker`, and `ksoftirqd` all use `smp_hotplug_thread` registration to create per-CPU kernel threads that handle domain-specific work. Understanding migration threads gives you a template for how the kernel manages per-CPU coordination.

The stopper thread also handles stop-machine work beyond just migration. When the kernel needs to synchronize all CPUs (for example, during live patching with kpatch or kgraft), work items are queued to each CPU’s stopper thread to ensure atomic execution across the system.

## Implementation Across Kernel Versions

The migration thread mechanism has remained largely stable from kernel 5.x through the current 6.x releases. Core concepts haven’t changed, though implementation details vary:

- **5.x kernels**: Used the classic stop-machine implementation with direct work queueing
- **6.x kernels**: Integrated better with the scheduler’s load-balancing framework
- **6.10+**: Added further refinements to migration latency and CPU hotplug response times

The fundamental architecture — per-CPU serialized work queues woken by the scheduler — remains consistent across all recent versions.
