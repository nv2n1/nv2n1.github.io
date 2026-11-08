---
title: "Understanding Work-Conserving vs. Non-Work-Conserving I/O Schedulers"
date: 2018-03-24 11:54:34 +0000
layout: post
canonical: https://www.systutorials.com/what-is-the-difference-between-work-conserving-i-o-scheduler-and-non-work-conserving-i-o-scheduler/
---

I/O schedulers in Linux sit between application requests and physical disk hardware, deciding the order in which I/O operations execute. The fundamental difference between work-conserving and non-work-conserving schedulers comes down to how they handle idle periods.

### Work-Conserving Schedulers

A work-conserving scheduler must dispatch a pending I/O request whenever one exists, regardless of physical disk positioning. If requests are queued, something gets sent to the disk immediately — there’s no idle waiting.

Examples of work-conserving schedulers:

- **Deadline** — prioritizes requests by deadline, processes pending work aggressively
- **NOOP** — simple FIFO queue with minimal overhead

The advantage is straightforward: the disk is never idle if work exists. This maximizes raw throughput and prevents unnecessary latency buildup.

### Non-Work-Conserving Schedulers

Non-work-conserving schedulers deliberately introduce idle periods, betting that incoming requests will be more favorably positioned than currently pending ones. Instead of dispatching what exists now, they wait slightly for potentially better requests.

Examples include:

- **Anticipatory Scheduler (AS)** — waits briefly after read completion, hoping the same process will issue a nearby follow-up request
- **CFQ (Completely Fair Queuing)** — attempts to maintain per-process I/O locality and fairness, which sometimes means delaying dispatches

The rationale is workload-dependent. For workloads with strong spatial locality — where sequential or nearby requests arrive predictably — waiting for them can reduce disk head movement and improve overall throughput.

### Real-World Performance Impact

The tradeoff becomes obvious under different conditions:

**Single-process intensive I/O workload:**\
In controlled tests, Deadline can nearly double throughput compared to CFQ on a single heavy process. This happens because:

- CFQ waits for requests closer to the current disk head position
- With only one process, those “better” requests may never arrive
- Deadline dispatches pending work immediately, keeping the disk saturated
- The waiting in CFQ becomes pure overhead

**Multi-process or highly concurrent workload:**\
Non-work-conserving schedulers shine here. They maintain per-process fairness and exploit locality from multiple sources. CFQ ensures one process doesn’t starve others while still grouping related requests together.

**Highly fragmented filesystem data:**\
When files are scattered across the disk (common on ext4 with many small files or long-running systems), anticipatory scheduling provides diminishing returns. AS assumes nearby blocks will be requested soon — but if they’re actually distant, waiting wastes time.

### Practical Considerations

Several factors determine which scheduler works best for your specific case:

**1. Block layout and filesystem fragmentation**\
Files stored non-consecutively on disk reduce anticipatory scheduler effectiveness. A 100K+ file directory with 1–5MB files written via Windows/Samba through ext4 will likely have scattered blocks. RAID controllers can mitigate this by handling parallel I/O across multiple spindles.

**2. Application-level blocking behavior**\
Programs typically block on I/O completion. If a process reads a file and immediately waits for its read to complete before issuing the next request, the scheduler can’t anticipate future requests. Non-work-conserving schedulers fail here because they’re waiting for requests that won’t arrive for another application-level cycle.

**3. Thread behavior**\
Linux treats user-space threads as separate kernel tasks. A multi-threaded process reading files in parallel presents requests from different kernel tasks (same TGID, different PIDs). Schedulers treat these as separate streams, reducing their ability to recognize locality patterns.

**4. Virtual environments**\
In KVM or Xen, you add another layer of scheduling. The hypervisor schedules vCPUs, the guest kernel schedules I/O, and the storage backend may reorder further. Non-work-conserving heuristics often fail entirely because the scheduler can’t see actual physical block positions.

**5. Storage hardware**\
Modern RAID controllers with battery-backed cache, deep command queues, and parallel channel handling reduce I/O scheduler importance. The controller’s firmware often reorders requests more effectively than the kernel scheduler. NVMe devices with native command queuing also diminish scheduler impact.

### Choosing a Scheduler

Check your current scheduler:

``` bash
cat /sys/block/sda/queue/scheduler
```

List available options:

``` bash
cat /sys/block/sda/queue/scheduler
```

Change at runtime:

``` bash
echo deadline > /sys/block/sda/queue/scheduler
```

**Use Deadline if:**

- Single-process or single-application workloads dominate
- You need predictable latency
- Filesystem fragmentation is high

**Use CFQ (mq-deadline in newer kernels) if:**

- Multi-tenant systems with competing I/O loads
- Fairness matters more than peak throughput
- Working with SSD or high-performance storage

**Use NOOP/none if:**

- Running on modern NVMe or high-end storage arrays
- The storage controller handles scheduling better than the kernel

Modern Linux kernels increasingly favor `mq-deadline` (the multi-queue variant) as it handles both traditional HDD and NVMe workloads reasonably well without the overhead of CFQ’s fairness mechanisms. For most production systems, the kernel’s default choice is adequate, and profiling your specific workload beats theoretical optimization.
