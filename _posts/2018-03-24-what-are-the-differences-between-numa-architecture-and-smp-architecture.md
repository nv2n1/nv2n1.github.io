---
title: "NUMA vs SMP: Key Architectural Differences"
date: 2018-03-24 11:54:41 +0000
author: "Weiwei Jia"
layout: post
canonical: https://www.systutorials.com/what-are-the-differences-between-numa-architecture-and-smp-architecture/
---

**SMP (Symmetric Multiprocessing)** and **NUMA (Non-Uniform Memory Access)** represent two fundamentally different approaches to multi-processor system architecture. Understanding the distinction matters because it affects how you tune applications, configure kernel parameters, and optimize workloads.

### Memory Access Latency

In **SMP**, all processors have equal latency when accessing any memory location. Every CPU communicates with RAM through a shared bus or interconnect, so the distance to memory is uniform—hence “symmetric.” This simplicity made SMP the standard for smaller systems, but it doesn’t scale well. As you add more processors, contention on the shared memory bus becomes a bottleneck.

In **NUMA**, each processor (or group of processors) has local memory attached directly to it. A processor can access its own local memory quickly, but accessing memory attached to another processor incurs higher latency. Memory is physically distributed and partitioned asymmetrically across the system.

### When NUMA Became Necessary

SMP architectures hit scalability limits around 4-8 sockets. Modern high-core-count systems (16+ sockets) switched to NUMA because:

- Local memory access is 2-4x faster than remote access
- Scaling beyond shared-bus limitations becomes possible
- Each NUMA node independently manages its memory controllers and interconnects

Most modern x86-64 systems with multiple sockets are NUMA. AMD EPYC, Intel Xeon, and ARM systems with many cores all use NUMA topology.

### Cache Hierarchy Complications

Your intuition about cache being part of the memory hierarchy is correct, but it requires clarification. **Cache is technically coherent but logically separate** from the NUMA/SMP distinction:

- In SMP, cache coherency is simpler because all processors see the same memory bus
- In NUMA, you still have cache coherency (using protocols like MESIF or MOESI), but cache coherency traffic travels across NUMA interconnects, adding latency

So modern systems are best described as **“NUMA with coherent caches”** rather than “SMP+NUMA hybrid.” The cache hierarchy doesn’t change whether you’re SMP or NUMA—it’s orthogonal.

### Practical Implications for System Administration

**Checking your system’s topology:**

``` bash
# View NUMA nodes and CPU mapping
numactl --hardware

# Check which node a process is bound to
numactl --show

# List CPUs per node
lscpu --extended
```

**Memory locality matters for performance:**

``` bash
# Run a process with memory locality awareness
numactl --cpunodebind=0 --membind=0 ./myapp

# Interleave memory across nodes (useful for some workloads)
numactl --interleave=all ./myapp
```

**Pin threads to specific NUMA nodes** to maximize cache hits and minimize remote memory access. For workloads like databases (PostgreSQL, MySQL), search engines, or data analytics, NUMA-aware tuning can improve throughput by 20-50%.

**Kernel configuration:** On NUMA systems, ensure zone reclaim is configured appropriately:

``` bash
# Check current setting (higher = more aggressive reclaim of local memory)
sysctl vm.zone_reclaim_mode

# Set to prevent excessive remote memory access
sysctl -w vm.zone_reclaim_mode=1
```

### Legacy SMP and Modern Reality

Pure SMP is now found only in small embedded systems or older hardware. Every modern multi-socket server is NUMA. Single-socket systems with multiple cores (whether x86, ARM, or otherwise) are technically SMP but benefit from treating them like NUMA for consistent performance tuning practices.

The distinction still matters in kernel development and scheduler design, but from an operational standpoint, assume NUMA on anything with more than one socket, and configure accordingly.
