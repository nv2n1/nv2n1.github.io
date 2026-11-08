---
title: "Latency Numbers Every Systems Engineer Should Know"
date: 2013-07-19 05:47:44 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /software-engineering-advice-from-building-large-scale-distributed-systems-by-jeff-dean/
---

Jeff Dean’s foundational work on large-scale distributed systems at Google established performance metrics that remain essential for making sound architectural decisions. While absolute numbers shift with hardware advances, the relative orders of magnitude have proven remarkably stable.

These latency figures represent the raw cost of fundamental operations. Understanding them prevents decisions that seem reasonable in isolation but create cascading problems at scale.

## Current Latency Hierarchy

| Operation                           | Latency        |
|-------------------------------------|----------------|
| L1 cache reference                  | 0.5 ns         |
| Branch mispredict                   | 5 ns           |
| L2 cache reference                  | 7 ns           |
| Mutex lock/unlock                   | 100 ns         |
| Main memory reference               | 100 ns         |
| Compress 1K bytes with Zstd         | 1,000 ns       |
| Send 2K bytes over 1 Gbps network   | 20,000 ns      |
| Read 1 MB sequentially from memory  | 250,000 ns     |
| Round trip within same datacenter   | 500,000 ns     |
| Read 1 MB sequentially from SSD     | 1,000,000 ns   |
| Disk seek (rotational)              | 10,000,000 ns  |
| Read 1 MB sequentially from disk    | 30,000,000 ns  |
| Read 1 MB sequentially over network | 10,000,000 ns  |
| Intercontinental round trip         | 150,000,000 ns |

Modern hardware has shifted absolute numbers—compression algorithms like Zstd outpace older options, and SSDs have become the standard storage tier. But the relative relationships between layers remain your actual guide for design decisions.

## Why These Relationships Matter

**Cache locality is non-negotiable.** The 200x difference between L1 and main memory access means algorithmic efficiency measured in CPU cycles translates directly to wall-clock performance. A cache miss in a tight loop will outweigh algorithmic cleverness in most real workloads. This is why memory-efficient data structures and access patterns matter more than theoretical algorithm complexity at the CPU level.

**Network I/O dominates system design.** Once you cross the datacenter boundary, a single request costs as much as millions of CPU operations. This fundamental asymmetry drives distributed systems architecture entirely—batching, caching, connection pooling, and replication exist primarily to minimize network round trips. Even within a datacenter, that 500 microsecond round trip multiplies quickly. At 10,000 requests per second, you’re consuming 5 seconds of latency per second just on network overhead.

**Disk seeks remain catastrophic.** A rotational disk handles roughly 100 random I/O operations per second. This hasn’t changed materially in decades, which explains:

- Sequential disk I/O is 3000x faster than random I/O
- SSDs (1-2 ms latency) are now standard for any serious workload
- Write-ahead logs are sequential by design
- Database indices exist to eliminate seeks

**Memory bandwidth is a real constraint.** Reading 1 MB from memory takes 250 microseconds. This limits streaming throughput and explains why compression trades CPU cycles for reduced bandwidth—almost always a winning trade. You can compress data faster than you can move uncompressed data across the network or from slower storage.

## Practical Application

When designing a system, work through this decision tree:

1.  **Can you avoid the operation?** Caching, memoization, and prefetching turn expensive operations into cache hits. A value already in memory beats every alternative.

2.  **Can you batch the operation?** Amortizing fixed overhead across multiple requests reduces per-request cost. Network requests, disk operations, and lock acquisitions all benefit from batching.

3.  **What’s the cheapest alternative?** A local disk read (30ms) beats a network request to disk (40ms), but both beat doing it poorly in CPU with repeated work.

## Compound Effects at Scale

These numbers compound dramatically. A service handling 100,000 requests per second that adds 100 microseconds of unnecessary latency through poor I/O is consuming 10 seconds of system resources per second. Across a fleet of 50 machines, that’s equivalent to idling 8+ additional servers doing nothing but burning through that one mistake.

A single extra database round trip per request in a 1 million request-per-second system becomes 1,000 seconds of round-trip time happening simultaneously—enough latency overhead to require significant additional infrastructure.

## Modern Context (2026)

The hierarchy remains stable, but implementation details have shifted:

- **NVMe SSDs** are the baseline storage tier; rotational disks survive mainly in archive workloads and cold storage.
- **Compressed data formats** (Zstd, LZ4) are standard in transit. Uncompressed network payloads are wasteful unless you have specific reasons to avoid CPU overhead.
- **Kernel bypass networking** (DPDK, io_uring) has reduced some network latency for specialized workloads, but most systems remain bound by the hierarchy above.
- **Memory is cheaper**, so trading memory for reduced I/O remains a sound default.

Build systems around this hierarchy. The absolute values will shift as hardware evolves, but the relative relationships are your north star for sound architectural choices.
