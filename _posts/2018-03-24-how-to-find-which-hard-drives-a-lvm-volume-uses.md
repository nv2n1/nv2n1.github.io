---
title: "Mapping LVM Logical Volumes to Physical Disks"
date: 2018-03-24 11:41:40 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-find-which-hard-drives-a-lvm-volume-uses/
---

When managing LVM storage, you need to know which physical disks support each logical volume — especially for risk assessment when hardware fails. This guide shows you how to trace those relationships.

## Using lvdisplay to map extents

The `lvdisplay` command with the `--maps` flag shows how logical extents map to physical volumes:

``` bash
lvdisplay --maps
```

This output displays each logical volume and which physical volumes (PVs) contain its data. Look for the physical extent ranges to understand the distribution across disks.

For a specific logical volume:

``` bash
lvdisplay --maps /dev/vg0/lv_data
```

## Using pvs for segment-level detail

For a more structured view of the physical-to-logical mapping, use `pvs` with segment information:

``` bash
pvs --segments -o+lv_name,seg_start_pe,segtype
```

This shows each physical volume’s segments, which logical volume owns each segment, and the segment type (linear, striped, etc.). This is useful when you need to understand RAID-like configurations or striped volumes.

## Finding affected volumes when a disk fails

If you know a specific physical volume might fail, check which logical volumes depend on it:

``` bash
lvs -o lv_name,seg_pe_ranges /dev/vg0 | grep /dev/sda
```

Or use `pvdisplay` to see all logical volumes on a physical volume:

``` bash
pvdisplay /dev/sda1
```

The output lists “Logical volumes” at the bottom, showing which LVs use that physical disk.

## Checking for single-disk dependencies

To find logical volumes that exist on only one physical disk (high-risk scenario):

``` bash
lvs -o lv_name,devices /dev/vg0
```

Then manually inspect the output for volumes without redundancy across multiple devices.

For a more automated check with multiple PVs in a VG:

``` bash
for lv in $(lvs -o lv_name --noheadings /dev/vg0); do
  pv_count=$(lvs -o devices --noheadings /dev/vg0/$lv | tr ',' '\n' | wc -l)
  echo "$lv uses $pv_count physical volume(s)"
done
```

## Stripe and mirror considerations

Check if volumes use striping or mirroring to understand failure impact:

``` bash
lvs -o lv_name,segtype,lv_layout /dev/vg0
```

Striped volumes lose data if any disk fails. Mirrored volumes (`segtype` showing “mirror”) survive single-disk loss. Linear volumes fail if their designated disk fails.

## Real-world example

Here’s a complete workflow to assess your VG’s fault tolerance:

``` bash
# Show physical volumes in the VG
pvs /dev/vg0

# List all logical volumes with their backing disks
lvs -o lv_name,devices /dev/vg0

# Check for striped or mirrored layouts
lvs -o lv_name,segtype,lv_layout /dev/vg0

# Detailed mapping of a critical volume
lvdisplay --maps /dev/vg0/critical_data
```

Use this data to plan redundancy upgrades or understand which services go down if a particular disk fails. This is essential input for your disaster recovery and capacity planning.

## 2026 Best Practices and Advanced Techniques

For Mapping LVM Logical Volumes to Physical Disks, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
