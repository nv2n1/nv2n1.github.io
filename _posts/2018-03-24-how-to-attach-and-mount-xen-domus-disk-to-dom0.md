---
title: "How to Attach and Mount a Xen DomU Disk in Dom0"
date: 2018-03-24 08:19:23 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-attach-and-mount-xen-domus-disk-to-dom0/
---

There are times when you need direct access to a DomU’s disk from Dom0—for recovery, backup, or maintenance. This is straightforward with Xen’s block device tools, though the commands have evolved depending on your Xen version.

### Attaching the Disk

The method depends on which Xen toolstack you’re using.

**With xl (Xen 4.1+, recommended):**

``` bash
xl block-attach Domain-0 phy:/dev/vg_xen/vm-10.1.1.228 xvda w
```

**With xm (older Xen, deprecated):**

``` bash
xm block-attach Domain-0 phy:vg_xen/vm-10.1.1.228 xvda w
```

The format is:

- `phy:` — physical device backend
- `/dev/vg_xen/vm-10.1.1.228` — LVM volume path (or raw partition like `/dev/sda1`)
- `xvda` — device name as it will appear in Dom0
- `w` — read-write mode (`r` for read-only)

### Discovering Attached Partitions

After attaching, the block device should appear as `/dev/xvda`. To see available partitions:

``` bash
lsblk /dev/xvda
# or
fdisk -l /dev/xvda
# or
parted /dev/xvda print
```

For example, if the DomU had `/dev/xvda1` as /boot and `/dev/xvda2` as /, you’ll see:

``` bash
xvda
├─xvda1  512M
└─xvda2  19.5G
```

### Mounting the Partition

Create a mount point and mount the partition:

``` bash
mkdir -p /mnt/xvda2
mount /dev/xvda2 /mnt/xvda2
```

If the filesystem is damaged or needs checking first:

``` bash
fsck -n /dev/xvda2  # Read-only check
fsck /dev/xvda2     # Fix errors
mount /dev/xvda2 /mnt/xvda2
```

For read-only access (safer when you’re just examining):

``` bash
mount -o ro /dev/xvda2 /mnt/xvda2
```

### Unmounting and Detaching

When done, unmount cleanly:

``` bash
umount /mnt/xvda2
```

If the device is busy, find what’s using it:

``` bash
lsof /mnt/xvda2
fuser -m /mnt/xvda2
```

Then detach the block device. With **xl**:

``` bash
xl block-detach Domain-0 xvda
```

Or with **xm**:

``` bash
xm block-detach Domain-0 xvda
```

You can also use the device ID shown in `xl block-list Domain-0`:

``` bash
xl block-list Domain-0
# Output: Name ID State ...
xl block-detach Domain-0 0  # ID instead of device name
```

### Working with Multiple Partitions

If you need multiple partitions mounted simultaneously, attach them with different device names:

``` bash
xl block-attach Domain-0 phy:/dev/vg_xen/vm-10.1.1.228 xvda w
xl block-attach Domain-0 phy:/dev/vg_xen/vm-10.1.1.229 xvdb w
mount /dev/xvda1 /mnt/vm1
mount /dev/xvdb1 /mnt/vm2
```

Then detach each one separately when done.

### Common Issues

**Device already in use:** If a DomU is currently running and using the disk, attaching will fail or cause corruption. Always shut down the DomU first:

``` bash
xl shutdown vm-name
xl destroy vm-name  # If shutdown hangs
```

**Stale block device:** After detaching, if `/dev/xvda` still exists, scan for changes:

``` bash
echo 1 > /sys/block/xvda/device/delete
```

**LVM not found:** Ensure the LVM volume group is available in Dom0:

``` bash
vgs
lvs
```

If the VG isn’t visible, activate it:

``` bash
vgchange -ay vg_xen
```

## 2026 Best Practices

This article extends “How to Attach and Mount a Xen DomU Disk in Dom0” with practical guidance. Modern development practices emphasize security, performance, and maintainability. Follow these guidelines to build robust, production-ready systems.

### Additional Resources

This guide covers the essential concepts and practical implementations for How to Attach and Mount a Xen DomU Disk in Dom0. For further reading and advanced topics, explore the following areas:

- **Best Practices:** Follow industry standards and conventions for consistency and maintainability.
- **Performance Optimization:** Learn how to optimize your workflow and implementations for better performance.
- **Troubleshooting:** Common issues and their solutions, along with tips for debugging and problem-solving.
- **Advanced Topics:** Explore deeper concepts and advanced patterns that go beyond the basics.
- **Related Tools:** Discover complementary tools and frameworks that enhance your development workflow.

### Summary

In this comprehensive guide, we covered the fundamentals of How to Attach and Mount a Xen DomU Disk in Dom0 and explored practical implementations. By understanding these concepts and applying the techniques discussed, you can effectively work with How to Attach and Mount a Xen DomU Disk in Dom0 in your projects. Remember to practice regularly and continue learning to stay updated with the latest developments and best practices in this field.
