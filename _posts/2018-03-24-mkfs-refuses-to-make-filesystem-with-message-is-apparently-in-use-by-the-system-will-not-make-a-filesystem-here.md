---
title: "mkfs Error: Device Apparently in Use by the System"
date: 2018-03-24 11:47:16 +0000
layout: post
canonical: https://www.systutorials.com/mkfs-refuses-to-make-filesystem-with-message-is-apparently-in-use-by-the-system-will-not-make-a-filesystem-here/
---

When you try to create a filesystem on a disk with `mkfs`, you may see this error:

    # mkfs -t ext4 /dev/sdd1
    mke2fs 1.42.8 (20-Jun-2013)
    /dev/sdd1 is apparently in use by the system; will not make a filesystem here!

Even though the device isn’t mounted, `mkfs` refuses to proceed. This safety mechanism prevents accidental data loss, but it can be frustrating when the device is legitimately unused. Here’s how to diagnose and fix it.

## Check what’s actually holding the device

Before forcing anything, verify what’s claiming the device:

``` bash
lsof /dev/sdd1
```

If that returns nothing, check if it’s used by the kernel:

``` bash
cat /proc/mdstat
```

Look for any mention of `sdd1` or check multipath status:

``` bash
sudo multipath -ll
```

## Common causes and solutions

**RAID metadata**

If the disk came from another server, it likely has RAID signatures that the kernel recognizes. The system won’t let you overwrite an active RAID member, even if you think it’s not in use.

Wipe RAID signatures with:

``` bash
sudo mdadm --zero-superblock /dev/sdd1
```

For older hardware RAID cards or if multiple RAID versions are present, you may need to wipe multiple superblock locations:

``` bash
sudo dd if=/dev/zero of=/dev/sdd1 bs=512 count=2048
sudo dd if=/dev/zero of=/dev/sdd1 bs=512 count=2048 seek=$(($(blockdev --getsz /dev/sdd1) - 2048))
```

This writes zeros to the first and last 1MB of the partition, clearing most RAID signatures.

**Multipath claiming the device**

If multipath is installed and active, it may claim the device as a multipath member. Check:

``` bash
sudo systemctl status multipathd
```

If it’s running, add the device to the blacklist in `/etc/multipath.conf`:

    blacklist {
        devnode "^sdd"
    }

Then reload multipath:

``` bash
sudo systemctl restart multipathd
sudo multipath -F
```

**Device mapper or LVM signatures**

Check if LVM or device-mapper metadata exists:

``` bash
sudo lvmdiskscan /dev/sdd1
```

If found, remove any remaining signatures:

``` bash
sudo pvremove /dev/sdd1
```

**Partition table issues**

If you recreated the partition with `cfdisk` but the error persists, the old filesystem signature might still be cached. Wipe the partition table and recreate it:

``` bash
sudo wipefs -a /dev/sdd1
sudo fdisk /dev/sdd
```

Then recreate the partition and try `mkfs` again.

## Force filesystem creation if safe

If you’ve verified the disk is not in use and contains no data you need, force `mkfs` to proceed:

``` bash
sudo mkfs -t ext4 -F /dev/sdd1
```

The `-F` flag forces creation without prompting. Use this only after confirming the device is truly safe to overwrite.

## Verify the filesystem was created

Once `mkfs` completes:

``` bash
sudo blkid /dev/sdd1
```

This confirms the new filesystem exists and shows its UUID and type.

## 2026 Best Practices and Advanced Techniques

For mkfs Error: Device Apparently in Use by the System, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
