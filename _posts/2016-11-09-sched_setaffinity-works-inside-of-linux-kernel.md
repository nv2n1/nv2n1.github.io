---
title: "How sched_setaffinity Works in the Linux Kernel"
date: 2016-11-09 15:46:57 +0000
author: "Weiwei Jia"
layout: post
canonical: https://www.systutorials.com/sched_setaffinity-works-inside-of-linux-kernel/
---

CPU affinity binds a process or thread to specific CPU cores, reducing cache misses, improving performance isolation, and managing NUMA locality. The `sched_setaffinity()` system call is the primary mechanism in Linux. Understanding how it works at the kernel level clarifies scheduler internals and helps you use it effectively.

## System Call Entry Point

The `sched_setaffinity()` syscall entry point is defined via the `SYSCALL_DEFINE3` macro:

``` c
SYSCALL_DEFINE3(sched_setaffinity, pid_t, pid, unsigned int, len,
                 unsigned long __user *, user_mask_ptr)
```

Parameters:

- `pid`: The process ID to apply affinity to (0 means the calling process)
- `len`: The size of the cpumask structure
- `user_mask_ptr`: Pointer to the user-space cpumask buffer

The kernel validates these inputs before proceeding with the actual affinity operation. Permission checks ensure the calling process can only modify affinity for its own task or tasks it has permission to affect (typically the same user or root).

## Call Chain and Core Functions

When you invoke `sched_setaffinity()`, the kernel follows this execution path:

    sched_setaffinity()
    ├─ do_sched_setaffinity()
    └─ __set_cpus_allowed_ptr(struct task_struct *p, const struct cpumask *new_mask)
       ├─ Validate and update task struct affinity
       └─ stop_one_cpu() [if task is running]
          ├─ migration_cpu_stop()
          └─ __migrate_task()
             └─ move_queued_task()
                └─ enqueue_task()

## The \_\_set_cpus_allowed_ptr Function

After validation, `__set_cpus_allowed_ptr()` contains the core logic. It updates the task’s CPU affinity mask and determines the appropriate migration strategy based on task state:

**Task is running or about to run (TASK_WAKING)**: The kernel calls `stop_one_cpu()` to send an inter-processor interrupt (IPI) to the source CPU. This preempts the running task and triggers `migration_cpu_stop()` with the highest priority. This approach is necessary because you cannot safely dequeue a task from a runqueue while it’s executing on that CPU.

**Task is queued on a runqueue but not currently running**: The kernel performs a direct dequeue-and-enqueue operation without interrupting the source CPU. This avoids IPI overhead for non-running tasks.

**Task is blocked or waiting**: Only the affinity mask is updated. No queue migration occurs since the task isn’t executing anywhere yet. When the task wakes, the scheduler respects the new affinity constraints.

## The stop_one_cpu Mechanism

For actively running tasks, `stop_one_cpu()` is critical:

- Sends an IPI to the target CPU with the highest priority
- Preempts the running task and executes `migration_cpu_stop()` immediately
- Prevents context switches until migration completes, ensuring atomicity

This mechanism guarantees that a task cannot execute on a CPU after its affinity mask excludes that CPU.

## The migration_cpu_stop Function

Once the IPI is delivered, `migration_cpu_stop()` executes in stop-machine context:

``` c
static int migration_cpu_stop(void *data)
{
    struct migration_arg *arg = data;
    struct task_struct *p = arg->task;
    struct rq *rq = this_rq();

    /* Verify the task is still on the source CPU and affinity is current */
    if (task_cpu(p) != smp_processor_id())
        goto out;

    /* Perform actual migration */
    __migrate_task(p, rq, rq_dest_cpu(arg->rq_dest));

    /* Return to let scheduler reschedule on destination CPU */
out:
    return 0;
}
```

Running in stop-machine context guarantees that no other tasks will preempt `migration_cpu_stop()` on that CPU, preventing race conditions during the migration window.

## Moving Between Runqueues

The actual queue migration happens in `move_queued_task()` and `enqueue_task()`:

- `dequeue_task()` removes the task from the source CPU’s runqueue with load balancing adjustments
- The task structure’s CPU assignment is updated
- `enqueue_task()` adds the task to the destination CPU’s runqueue
- The scheduler determines whether to run the migrated task immediately (if the destination CPU is idle) or place it in the appropriate queue position based on scheduling class and priority

The operation maintains per-CPU runqueue integrity and load balancing data structures throughout.

## Practical Considerations

**Immediate Effect for Running Tasks**: For actively running tasks, migration happens almost immediately via IPI. The task will be preempted and moved. For queued tasks, migration happens at the next scheduling opportunity.

**Validation**: The kernel validates that the new mask is valid and contains at least one online CPU. If the current CPU isn’t in the new mask, immediate migration is forced.

**NUMA Considerations**: On NUMA systems, affinity changes don’t automatically adjust memory locality. You may also want to use `numactl` or `numa_migrate_pages()` to move memory pages after changing CPU affinity.

**Busy Loops and Polling**: If a task is in a tight polling loop with strict affinity constraints, the CPU has no opportunity to execute the migration interrupt until the task yields control. Consider adding explicit yield points if you’re debugging affinity-related issues.

**Runqueue Lock Contention**: For systems with many CPUs, frequent affinity changes can cause runqueue lock contention. Batch affinity changes when possible.

**Asymmetric CPU Architectures**: On systems with P-cores and E-cores (Intel 12th gen and later), you can use affinity to dedicate processes to specific core types. The `sched_util_clamp_min` and `sched_util_clamp_max` interfaces provide additional control over CPU selection for tasks even without strict affinity masking.

## Using sched_setaffinity from User Space

From C code, use `pthread_setaffinity_np()` for threads or call `sched_setaffinity()` directly:

``` c
#define _GNU_SOURCE
#include <sched.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    cpu_set_t mask;
    CPU_ZERO(&mask);
    CPU_SET(0, &mask);  /* Bind to CPU 0 */
    CPU_SET(2, &mask);  /* And CPU 2 */

    if (sched_setaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_setaffinity");
        return 1;
    }

    /* Verify with sched_getaffinity */
    if (sched_getaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_getaffinity");
        return 1;
    }

    /* Print which CPUs are now in the mask */
    for (int i = 0; i < CPU_SETSIZE; i++) {
        if (CPU_ISSET(i, &mask)) {
            printf("CPU %d is in affinity mask\n", i);
        }
    }

    return 0;
}
```

From the shell, use `taskset`:

``` bash
# Run a process with CPU affinity
taskset -c 0-3 ./my_program

# Change affinity of a running process (PID 1234)
taskset -p -c 0-2 1234

# Check current affinity for a process
taskset -p 1234

# Show affinity in verbose format
taskset -pc 1234
```

For threads within a process, use `taskset` with the thread ID (obtained from `ps -eLf`) or use `pthread_setaffinity_np()` from within the application.

## Performance Implications

Changing affinity on running tasks incurs measurable overhead: the IPI latency (typically 1-10 microseconds), context switch cost, and potential L3 cache invalidation on the destination CPU. For batch workloads, set affinity once at startup rather than dynamically. For real-time applications, set affinity at thread creation time to avoid migration latency during critical sections.

On modern kernels with frequency domains and thermal throttling, affinity changes can also interact with the CPU frequency scaling subsystem. A task migrated to a slower CPU might experience different performance characteristics. Use tools like `cpupower` to inspect frequency scaling states when tuning affinity for performance-critical workloads.

## Summary

When you call `sched_setaffinity()`, the kernel:

1.  Validates the input mask and caller permissions
2.  Checks task state to determine the migration strategy
3.  For running tasks: Sends IPI to source CPU to trigger atomic migration via `migration_cpu_stop()`
4.  For queued tasks: Directly dequeues from source and enqueues to destination CPU’s runqueue
5.  For blocked tasks: Updates only the affinity mask; migration happens when the task wakes
6.  Updates the task structure’s CPU assignment and affinity mask
7.  Returns immediately; actual runqueue movement completes on the destination CPU

This design ensures tasks never execute on CPUs outside their affinity mask while minimizing lock contention and IPI overhead for non-running tasks.
