---
title: "Xen DomU I/O Performance: LVM vs. Loopback Block Devices"
date: 2013-07-12 16:32:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /xen-domus-io-performance-of-lvm-and-loopback-backed-vbds/
---

This post covers Xen virtualization benchmarks from 2013. While Xen remains in production use (AWS EC2, Citrix Hypervisor), KVM has become the default hypervisor for most Linux distributions. For current production environments, evaluate KVM with libvirt, direct container solutions (Docker, Kubernetes), or cloud-native platforms. This post is preserved for historical reference and understanding legacy Xen deployments.

## Xen VBD Storage Backend Performance Comparison

This benchmark evaluates I/O performance between LVM-backed and file-backed virtual block devices (VBDs) in Xen DomU instances using bonnie++.

### Test Environment

**Dom0**

- vCPUs: 2 (Intel Xeon E5520 @ 2.27GHz)
- Memory: 2GB
- Hypervisor: Xen 3.4.3 with Xenified 2.6.32.13 kernel

**DomU**

- vCPUs: 2
- Memory: 2GB
- Kernel: Fedora (2.6.32.19-163.fc12.x86_64)

**DomU Configuration**

    name="10.0.1.200"
    vcpus=2
    memory=2048
    disk = ['phy:vg_xen/vm-10.0.1.150/vmdisk0,xvda,w']
    vif=['bridge=eth0']
    bootloader="/usr/bin/pygrub"
    on_reboot='restart'
    on_crash='restart'

The disk configuration was changed for each backend type tested:

- LVM: `phy:vg_xen/vm-10.0.1.150/vmdisk0,xvda,w`
- File-backed (aio): `tap:aio:/lhome/xen/vm0-f12/vmdisk0,xvda,w`
- File-backed (legacy): `file:/lhome/xen/vm0-f12/vmdisk0,xvda,w`

### Benchmark Methodology

Tests used bonnie++ to measure I/O performance:

``` bash
bonnie++ -u root
```

Test scenarios:

1.  Single VM with LVM-backed VBD
2.  Single VM with newly created LVM snapshot
3.  Single VM with file-backed VBD
4.  Two concurrent VMs on the same file-backed disk

Bonnie++ output format includes sequential and random I/O metrics, file creation/deletion performance, and CPU utilization percentages.

### Results

**LVM-backed VBD (single VM)**

    Sequential Output: 76–81 MB/s (98% CPU)
    Block Write: 107–120 MB/s (21–22% CPU)
    Block Rewrite: 46–47 MB/s (13% CPU)
    Sequential Input: 73–75 MB/s (91–94% CPU)
    Block Read: 150–159 MB/s (15–16% CPU)
    Random Seeks: 248–266 ops/sec

**LVM-backed VBD (fresh snapshot – early runs)**

Immediately after snapshot creation, write performance drops significantly:

    Sequential Output: 11–12 MB/s (15% CPU)
    Block Write: 12–18 MB/s (2–3% CPU)
    Sequential Input: 66–71 MB/s (89–92% CPU)
    Block Read: 141–146 MB/s (14% CPU)

Performance recovers as CoW (copy-on-write) pages are merged:

    Sequential Output: 58–66 MB/s (73–84% CPU)
    Block Write: 57–65 MB/s (10–12% CPU)
    Sequential Input: 66–72 MB/s (86–91% CPU)
    Block Read: 141–152 MB/s (14–15% CPU)

**File-backed VBD (single VM)**

    Sequential Output: 20–23 MB/s (27–32% CPU)
    Block Write: 18–23 MB/s (3–4% CPU)
    Sequential Input: 49–72 MB/s (63–92% CPU)
    Block Read: 122–154 MB/s (12–15% CPU)
    Random Seeks: 197–241 ops/sec

**Two concurrent file-backed VMs on same disk**

VM A performance:

    Sequential Output: 10–15 MB/s (13–19% CPU)
    Block Write: 9–11 MB/s (1–2% CPU)
    Sequential Input: 22–30 MB/s (30–41% CPU)
    Block Read: 57–86 MB/s (5–8% CPU)
    Random Seeks: 92–142 ops/sec (severe contention)

VM B performance:

    Sequential Output: 8–9 MB/s (11–13% CPU)
    Block Write: 8–11 MB/s (1% CPU)
    Sequential Input: 19–57 MB/s (26–73% CPU)
    Block Read: 55–119 MB/s (5–12% CPU)
    Random Seeks: 90–222 ops/sec

### Analysis

**LVM vs File-backed Performance**

LVM-backed VBDs deliver 3–4× higher sequential write throughput (107–120 MB/s vs 18–23 MB/s) and similar read performance with lower CPU overhead. Random seek performance favors LVM (248–266 ops/sec vs 197–241 ops/sec).

File-backed VBDs suffer from increased kernel I/O scheduling overhead and additional filesystem layer traversal. The aio backend (`tap:aio`) marginally improves over legacy file backend but doesn’t match LVM performance.

**LVM Snapshot Impact**

Fresh snapshots show severe write performance degradation (11–18 MB/s initial) as CoW metadata operations dominate. Performance stabilizes within several runs as the snapshot diverges from the parent volume. This penalty is temporary but significant for bulk data operations immediately after snapshot creation.

**Concurrency Effects**

Two file-backed VMs on identical storage compete for disk I/O, reducing both to 8–15 MB/s sequential write and causing random seek performance to degrade by 50%+. LVM with separate logical volumes avoids this contention if the underlying disk scheduler distributes I/O fairly.

### Recommendations

For production Xen deployments:

- Use LVM-backed VBDs for baseline performance and stability
- Avoid file-backed VBDs if write-heavy workloads are expected
- Plan for temporary performance dips when creating snapshots; defer bulk operations until CoW stabilization
- Monitor disk scheduler behavior when multiple VMs contend for the same storage device
- For legacy Xen systems, consider phased migration to KVM or containerized alternatives
