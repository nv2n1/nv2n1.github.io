---
title: "Removing a Disk from an LVM Volume Group"
date: 2018-03-24 08:19:28 +0000
modified: 2026-04-12 16:47:45 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-delete-a-disk-from-a-lvm-group-while-keeping-the-data/
---

You have an LVM physical volume (PV) you need to remove from a volume group (VG), but the data needs to be preserved and moved to other available PVs. This is a straightforward but important operation that requires careful execution.

### Prerequisites

Before starting, verify:

- The VG has sufficient free space on remaining PVs to accommodate all data from the disk being removed
- Check free space: `vgs -o vg_name,vg_free`
- Ensure no logical volumes are using extents exclusively on the target PV
- The system isn’t heavily I/O constrained during the move (plan for downtime or off-peak hours if possible)

### Step 1: Move the Data

Use `pvmove` to relocate all extents from the physical volume to other PVs in the group:

``` bash
pvmove /dev/sdb
```

This command scans the target PV and migrates all allocated extents to other PVs in the same VG. The operation can take significant time depending on the volume of data—hours for large disks. Progress is displayed on the console.

For verbose output to monitor the operation:

``` bash
pvmove -v /dev/sdb
```

To run the operation in the background (useful for remote sessions):

``` bash
pvmove -b /dev/sdb
```

To check the status of an in-progress `pvmove`:

``` bash
pvmove -c /dev/sdb
```

Or monitor with:

``` bash
watch -n 5 'pvs /dev/sdb'
```

### Step 2: Remove the PV from the VG

Once `pvmove` completes, remove the empty physical volume from the volume group:

``` bash
vgreduce vg /dev/sdb
```

Verify the PV is no longer part of the VG:

``` bash
vgs -o +pv_name
pvs /dev/sdb
```

The PV should no longer appear in VG membership.

### Step 3: Clean Up the Disk

Wipe LVM metadata from the disk to prevent it from being accidentally detected as an LVM PV:

``` bash
pvremove /dev/sdb
```

This removes all LVM labels and headers from the device. Confirm removal:

``` bash
pvs /dev/sdb
```

You should see “PV not found” or similar error.

### After Removal

The disk can now be:

- Physically removed from the system
- Wiped and repurposed for non-LVM use
- Repurposed as a new PV in another VG

To add a new disk and extend your VG:

``` bash
pvcreate /dev/sdc
vgextend vg /dev/sdc
```

### Important Considerations

**Interrupted pvmove**: If `pvmove` is interrupted, you can safely resume it by running the same command again. LVM tracks migration state.

**Low disk space**: If the move fails due to insufficient free space, you may need to free up space elsewhere or add a temporary disk. Add a temporary PV, retry `pvmove`, then remove the temporary disk.

**I/O performance**: `pvmove` operations are I/O intensive. Monitor system load and consider throttling I/O using `nice`, `ionice`, or by running during maintenance windows.

**Mirrored LVs**: If your VG contains mirrored logical volumes, `pvmove` respects the mirror leg placement and will not move extents to invalid locations.

## 2026 Best Practices and Advanced Techniques

For Removing a Disk from an LVM Volume Group, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
