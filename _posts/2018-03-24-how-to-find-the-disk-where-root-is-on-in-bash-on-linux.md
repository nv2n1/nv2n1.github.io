---
title: "Finding the Root Filesystem Disk in Linux Bash"
date: 2018-03-24 11:52:43 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-the-disk-where-root-is-on-in-bash-on-linux/
---

On Linux systems, the root filesystem (/) can be on various device types — a raw disk partition, an LVM logical volume, or other storage configurations. Finding the underlying physical disk requires checking the device hierarchy, which differs depending on the storage setup.

## Quick method with df and lsblk

The simplest approach uses `lsblk` with the PKNAME field, which returns the parent kernel device name:

``` bash
lsblk -oMOUNTPOINT,PKNAME -P | grep 'MOUNTPOINT="/"'
```

For a root filesystem on a raw partition, this returns:

    MOUNTPOINT="/" PKNAME="sda"

For a root filesystem on an LVM volume:

    MOUNTPOINT="/" PKNAME="sda5"

In both cases, PKNAME gives you the immediate parent device. For raw partitions, that’s the disk. For LVM, that’s the physical volume (PV) partition.

## Getting just the disk device

To extract the physical disk name from either case, strip the trailing partition numbers:

``` bash
disk=$(lsblk -oMOUNTPOINT,PKNAME -P | grep 'MOUNTPOINT="/"' | grep -o 'PKNAME="[^"]*"' | cut -d'"' -f2 | sed 's/[0-9]*$//')
echo $disk
```

This gives you `sda` in both scenarios.

## One-liner for shell scripts

If you need this in a function or script, wrap it cleanly:

``` bash
root_disk=$(eval $(lsblk -oMOUNTPOINT,PKNAME -P | grep 'MOUNTPOINT="/"'); echo $PKNAME | sed 's/[0-9]*$//')
echo $root_disk
```

The `eval` statement parses the key-value output from lsblk, setting PKNAME as a variable, then pipes it to `sed` to remove partition numbers.

## Understanding the hierarchy

When the root filesystem is on LVM:

``` bash
# Check the logical volume
lvs | grep root
  root  vgubuntu  -wi-ao----  18.5G

# Check the physical volume backing it
pvs
  PV         VG       Fmt  Attr PSize   PFree
  /dev/sda5  vgubuntu lvm2 a--  19.5G   976.0M
```

The LV is backed by `/dev/sda5`, a partition on `/dev/sda`. The `lsblk` command automatically follows this chain and returns `sda5` as PKNAME.

## Alternative approach with stat and df

If lsblk isn’t available, you can use `df` combined with `stat`:

``` bash
# Get the device backing root
root_device=$(df / | tail -1 | awk '{print $1}')

# For LVM, get the physical volume
if [[ $root_device == /dev/mapper/* ]]; then
  pv=$(dmsetup deps -o bluestack "$root_device" | grep -o '/dev/[a-z0-9]*')
  disk=$(echo $pv | sed 's/[0-9]*$//')
else
  # Raw partition
  disk=$(echo $root_device | sed 's/[0-9]*$//')
fi

echo $disk
```

However, this requires additional tools (dmsetup) for LVM and is less portable. The `lsblk` approach is cleaner.

## Verification

After finding the disk, verify it’s correct:

``` bash
disk="sda"
lsblk /dev/$disk
```

Or check using `fdisk`:

``` bash
fdisk -l /dev/$disk | head -5
```

For LVM-based systems, also confirm with `pvs`:

``` bash
pvs | grep $disk
```

## 2026 Best Practices and Advanced Techniques

For Finding the Root Filesystem Disk in Linux Bash, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
