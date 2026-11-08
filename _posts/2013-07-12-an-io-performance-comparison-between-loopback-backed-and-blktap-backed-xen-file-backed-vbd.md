---
title: "I/O Performance: Loopback vs. Blktap for Xen File-backed VBDs"
date: 2013-07-12 16:31:54 +0000
modified: 2026-04-12 05:27:23 +0000
author: "Eric Ma"
layout: post
categories: [design-patterns-architecture]
canonical: /an-io-performance-comparison-between-loopback-backed-and-blktap-backed-xen-file-backed-vbd/
---

This post analyzes I/O performance between loopback and blktap backends for Xen file-backed virtual block devices (VBDs), based on testing from 2013. While Xen remains in production use (AWS EC2, Citrix Hypervisor), most Linux deployments now default to KVM. For modern virtualization needs, consider KVM/libvirt or container solutions like Docker and Kubernetes. This post is preserved as historical reference for legacy Xen environments.

## Test Setup

**DomU Configuration:**

- CPU: 2x Intel Xeon E5520 @ 2.27GHz
- Memory: 1GB
- Storage: ext3/ext4 filesystems on xvda1

**Dom0 Configuration:**

- Raw image files stored on ext4 partition

**Benchmark Tool:** Bonnie++ 1.03c with default parameters

## Results

### Loopback Driver Backed VBD

    Sequential Output:        25,511 K/sec (35% CPU)
    Block Sequential Output:  18,075 K/sec (3% CPU)
    Rewrite:                  199,488 K/sec (47% CPU)
    Sequential Input:         71,094 K/sec (98% CPU)
    Block Sequential Input:   937,880 K/sec (86% CPU)
    Random Seeks:             ++++ (maxed out)
    File Creation (16 files): +++++ ops/sec

### blktap Driver Backed VBD

    Sequential Output:        69,438 K/sec (96% CPU)
    Block Sequential Output:  93,549 K/sec (20% CPU)
    Rewrite:                  38,118 K/sec (10% CPU)
    Sequential Input:         54,955 K/sec (76% CPU)
    Block Sequential Input:   131,645 K/sec (8% CPU)
    Random Seeks:             249.1 ops/sec
    File Creation (16 files): 29,488 ops/sec (79% CPU)

## Analysis

The loopback backend shows exceptionally high read performance (937,880 K/sec) but consumes maximum CPU and dominates I/O handling in dom0. This creates a bottleneck under sustained read workloads. The loopback backend also shows poor write performance (18,075 K/sec sequential).

blktap provides more balanced performance across read and write operations with significantly better write throughput (93,549 K/sec). While sequential read performance is lower, the overall I/O profile is more predictable and doesn’t saturate dom0 CPU.

## Why Choose blktap Over Loopback

**Scalability Limits:**
Linux loopback device driver defaults to supporting only 8 file-backed VBDs system-wide. To increase this, you must either:

- Pass `max_loop=N` kernel boot parameter
- Recompile dom0 kernel with `CONFIG_BLK_DEV_LOOP` as a loadable module and adjust max_loop via modprobe

blktap has no such architectural limitation and scales to many more concurrent block devices.

**I/O-Intensive Workloads:**
Loopback backend suffers substantial performance degradation under heavy sustained I/O because all block operations are serialized through a single Linux block device in dom0. This causes:

- CPU starvation in dom0
- Increased context switching overhead
- Dirty page flushing delays

blktap bypasses the loopback layer entirely, handling I/O more efficiently.

**Advanced Disk Features:**
blktap natively supports:

- Copy-on-Write (CoW) disk images
- Encryption layers
- Sparse disk formats
- Compression
- Snapshot capabilities

Loopback treats files as raw block devices, making these features difficult to implement without external tooling.

**Memory Efficiency:**
Loopback relies on Linux page cache and dirty page writeback mechanisms, which can cause unexpected I/O stalls and memory pressure. blktap manages its own buffering more efficiently.

## Migration Considerations

If moving an existing VM from loopback to blktap:

1.  Create a new blktap-backed disk image
2.  Copy data using `dd` or `rsync` during a maintenance window
3.  Update `/etc/xen/` domain config to reference new disk backend
4.  Test thoroughly before committing

For I/O-intensive workloads, consider LVM-backed VBDs instead. LVM provides better performance than both loopback and blktap for high-concurrency scenarios, though at the cost of less flexibility for snapshot and copy-on-write features.
