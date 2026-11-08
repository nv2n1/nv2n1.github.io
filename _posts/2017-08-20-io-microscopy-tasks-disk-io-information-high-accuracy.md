---
title: "Measuring Task I/O with eBPF: Microsecond Precision"
date: 2017-08-20 06:26:19 +0000
modified: 2026-04-11 16:24:48 +0000
author: "Weiwei Jia"
layout: post
categories: [systems-architecture]
canonical: /io-microscopy-tasks-disk-io-information-high-accuracy/
---

Most popular task monitoring tools (top, iotop, procfs) sample disk I/O information at granularity limited by kernel timer frequency—typically once per second. This sampling rate misses short-lived I/O bursts and makes it difficult to accurately measure which tasks are truly I/O bound. eBPF and kernel tracepoints let you capture microsecond-level accuracy without heavy overhead.

## Why Sampling Isn’t Enough

Standard Linux task accounting collects I/O statistics via kernel timer interrupts. On most systems, this means updates happen every 10ms at best, but often only once per second. Tools reading `/proc/[pid]/io` or using the taskstats interface inherit this limitation.

Consider a workload where a task performs many small I/O operations in quick succession—perhaps a database table scan or a log aggregation pipeline. A 1Hz sample rate will miss most activity. You need to measure the actual time tasks spend blocked waiting for disk I/O completion.

## Defining I/O Utilization Accurately

Task I/O utilization is the accumulated time a task spends waiting for disk I/O operations to complete, divided by wall-clock time.

For example, if a task executes `dd if=/dev/zero of=./testfile bs=1M count=1000` and spends 5 seconds blocked waiting for disk writes to finish during a 10-second window, its I/O utilization is 50%.

The challenge is capturing this timing at sufficient granularity without heavy kernel overhead.

## Using eBPF for Microsecond-Level Tracing

Since kernel 4.1, eBPF provides efficient kernel instrumentation. Modern eBPF programs can hook into block device I/O tracepoints with microsecond timestamps, track individual I/O requests through their lifecycle, and accumulate timing per task without frequent context switches to userspace.

The approach:

- Trace the start time when a task submits an I/O request to the block layer
- Trace the completion time when the I/O completes
- Calculate the delta (time spent in flight)
- Accumulate deltas per PID
- Report I/O utilization as (total_accumulated_time / observation_window)

## Implementation with eBPF

Here’s a practical eBPF program that hooks block I/O tracepoints and tracks latency per task:

``` c
// biolatency.c - measure block I/O latency per task
#include <uapi/linux/ptrace.h>
#include <linux/blkdev.h>

typedef struct {
    u32 pid;
    char name[TASK_COMM_LEN];
} req_key_t;

typedef struct {
    u64 total_ns;     // total time spent in I/O
    u64 io_count;     // number of I/O operations
    u64 bytes;        // total bytes
} req_val_t;

BPF_HASH(inflight, struct request *, u64);
BPF_HASH(stats, req_key_t, req_val_t);

TRACEPOINT_PROBE(block, block_rq_issue) {
    u64 ts = bpf_ktime_get_ns();
    inflight.update(&args->req, &ts);
    return 0;
}

TRACEPOINT_PROBE(block, block_rq_complete) {
    u64 *tsp, delta_ns;
    struct task_struct *task = (struct task_struct *)bpf_get_current_task_btf();

    tsp = inflight.lookup(&args->req);
    if (!tsp)
        return 0;

    delta_ns = bpf_ktime_get_ns() - *tsp;
    inflight.delete(&args->req);

    req_key_t key = {};
    key.pid = bpf_get_current_pid_tgid() >> 32;
    bpf_get_current_comm(&key.name, sizeof(key.name));

    req_val_t *val = stats.lookup_or_try_init(&key, NULL);
    if (val) {
        __sync_fetch_and_add(&val->total_ns, delta_ns);
        __sync_fetch_and_add(&val->io_count, 1);
        __sync_fetch_and_add(&val->bytes, args->len);
    }

    return 0;
}
```

The Python userspace program:

``` python
#!/usr/bin/env python3
import sys
import time
from bcc import BPF

BPF_CODE = """
(kernel code above)
"""

b = BPF(text=BPF_CODE)
stats_table = b["stats"]

try:
    while True:
        time.sleep(1)
        print("\n%-6s %-16s %10s %8s %12s" % 
              ("PID", "COMM", "IO/sec", "MB/sec", "Avg Latency(us)"))

        for k, v in sorted(stats_table.items(), 
                          key=lambda item: item[1].total_ns, reverse=True):
            io_per_sec = v.io_count
            mb_per_sec = v.bytes / (1024 * 1024)
            avg_latency_us = v.total_ns / v.io_count / 1000 if v.io_count else 0

            print("%-6d %-16s %10d %8.2f %12.2f" % 
                  (k.pid, k.name.decode(), io_per_sec, mb_per_sec, avg_latency_us))

        stats_table.clear()

except KeyboardInterrupt:
    sys.exit(0)
```

Run it with:

``` bash
sudo python3 biolatency.py
```

This will output a real-time view of I/O operations per task, updated every second.

## Advantages Over Traditional Monitoring

- **Microsecond resolution**: Captures every I/O operation, not kernel timer samples
- **Per-task accuracy**: Distinguishes between truly I/O-bound tasks and false positives
- **Low overhead**: eBPF executes in kernel with minimal context switching
- **No kernel rebuilds**: Works with standard kernels supporting eBPF (4.1+)

## Kernel Requirements and Compatibility

Modern kernels (5.10+) have stable `bpf_get_current_task_btf()` and improved tracepoint support. If running on older kernels (4.1–5.9), you may need to adjust task_struct field accesses. The nanosecond timing accuracy issues present in earlier kernels were fixed in stable kernels 5.1+, so modern deployments won’t encounter them.

## Production Considerations

For production deployments, consider these enhancements:

**Device filtering**: Hook `block_rq_issue` to filter by major/minor device numbers if tracking specific storage only. This reduces noise from unrelated I/O.

**Percentile latency**: Track p50, p95, p99 instead of just averages using BPF histograms:

``` c
BPF_HISTOGRAM(io_latency, u64);
// In block_rq_complete:
io_latency.increment(bpf_log2l(delta_ns));
```

**Per-cgroup tracking**: Group I/O by cgroup v2 for container and Kubernetes environments:

``` c
typedef struct {
    u64 cgroup_id;
    char name[TASK_COMM_LEN];
} cgroup_key_t;

BPF_HASH(cgroup_stats, cgroup_key_t, req_val_t);
// Use bpf_get_current_cgroup_id() to key by cgroup
```

**Long-running aggregation**: Keep statistics across multiple observation windows for trend analysis rather than clearing each interval. Track peak I/O rates and identify slow periods.

**Storage integration**: Filter by device type (NVMe, HDD, network block device) to separate local and remote I/O characteristics.

These enhancements help surface performance problems that would be invisible with traditional sampling approaches.
