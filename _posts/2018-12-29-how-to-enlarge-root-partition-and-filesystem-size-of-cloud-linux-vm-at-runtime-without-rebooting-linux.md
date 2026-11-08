---
title: "Expanding Root Partition on Cloud Linux VMs Without Rebooting"
date: 2018-12-29 06:23:57 +0000
modified: 2026-04-11 15:42:56 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-enlarge-root-partition-and-filesystem-size-of-cloud-linux-vm-at-runtime-without-rebooting-linux/
---

Before expanding your root partition and filesystem:

- Back up your data using cloud snapshots or external backup tools. Partition and filesystem resizing can cause data loss if misconfigured.
- Have root access to the VM.
- Ensure your cloud provider has already expanded the underlying block device (EBS volume for AWS, persistent disk for GCP, managed disk for Azure). This post covers making Linux recognize and use that expanded space.

This procedure works on modern Linux distributions with ext4, XFS, or Btrfs filesystems. Examples use Ubuntu 24.04 LTS on AWS EC2 with NVMe storage, but the steps apply across providers.

## Verify Current Disk Usage

Check your current disk utilization:

``` bash
df -hT
```

Example output from a full root partition:

    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/nvme0n1p1 ext4       20G   20G  1.5M 100% /

Confirm the block device has actually been enlarged by your cloud provider:

``` bash
lsblk
```

Get exact size in bytes:

``` bash
blockdev --getsize64 /dev/nvme0n1
```

If the block device size hasn’t increased yet, the resize operation may still be pending on the cloud platform’s side. Wait a few moments and retry. Some providers require explicit resize confirmation in their management console.

You can also check the partition size directly:

``` bash
cat /sys/block/nvme0n1/nvme0n1p1/size
```

## Expand the Partition Table

Use `growpart` to expand the partition to fill the block device:

``` bash
growpart /dev/nvme0n1 1
```

The `1` is the partition number. For `/dev/sda`, use `growpart /dev/sda 1`. For NVMe devices, partition 1 is typically `p1` (e.g., `/dev/nvme0n1p1`).

Expected output:

    CHANGED: partition=1 start=2048 old: size=41940959 end=41943007 new: size=209713119 end=209715167

If `growpart` is not installed, install it:

**Debian/Ubuntu:**

``` bash
apt-get update && apt-get install -y cloud-guest-utils
```

**RHEL/CentOS/Fedora:**

``` bash
dnf install -y cloud-utils-growpart
```

Verify the partition grew:

``` bash
lsblk
```

The partition size should now match the underlying block device. If `growpart` reports `NOCHANGE`, the partition is already using the full block device size — proceed to the filesystem resize.

## Resize the Filesystem

The resize command depends on your filesystem type. All of these work on mounted filesystems without requiring a reboot.

### For ext4 (most common on cloud Linux)

``` bash
resize2fs /dev/nvme0n1p1
```

Expected output:

    resize2fs 1.47.0 (5-Feb-2023)
    Filesystem at /dev/nvme0n1p1 is mounted on /; on-line resizing required
    old_desc_blocks = 3, new_desc_blocks = 13
    The filesystem on /dev/nvme0n1p1 is now 26214139 (4k) blocks long.

Verify the filesystem metadata was updated:

``` bash
tune2fs -l /dev/nvme0n1p1 | grep "Block count"
```

### For XFS (common on RHEL/CentOS/Fedora)

``` bash
xfs_growfs /
```

Note: Pass the mount point, not the device path. Expected output:

    meta-data=/dev/nvme0n1p1 isize=512    agcount=4, agsize=1310720 blks
             =                       sectsz=4096  attr=2, projid32bit=1
    data     =                       bsize=4096   blocks=5242880, imaxpct=25
    realtime =none                   extsz=4096   blocks=0, rtextents=0
    data blocks changed from 5242880 to 20971520

Verify with:

``` bash
xfs_info /
```

### For Btrfs

``` bash
btrfs filesystem resize max /
```

Verify with:

``` bash
btrfs filesystem show /
```

## Verify the Expansion

Check that your filesystem now uses the full space:

``` bash
df -hT
```

Expected output:

    Filesystem     Type      Size  Used Avail Use% Mounted on
    /dev/nvme0n1p1 ext4       97G   20G   78G  20% /

## Working with LVM

If your root filesystem uses LVM, expanding the partition is only the first step. After growing the partition, expand the physical volume:

``` bash
pvresize /dev/nvme0n1p1
```

Then expand the logical volume to use all available space. If your root filesystem is on `/dev/mapper/vg0-root`:

``` bash
lvresize -l +100%FREE /dev/vg0/root
```

Then resize the filesystem. For ext4:

``` bash
resize2fs /dev/vg0/root
```

For XFS:

``` bash
xfs_growfs /
```

For Btrfs:

``` bash
btrfs filesystem resize max /
```

## Troubleshooting

**`growpart` command not found**

Install the required package:

- Debian/Ubuntu: `apt-get install -y cloud-guest-utils`
- RHEL/CentOS/Fedora: `dnf install -y cloud-utils-growpart`

**Partition didn’t grow**

Confirm the underlying block device was resized by your cloud provider. Run `lsblk` and verify the block device size exceeds the partition size. Some providers require additional steps or may take a few minutes before the resize is visible to the OS.

**`growpart` reports `NOCHANGE`**

The partition already uses the full block device. Proceed to resizing the filesystem.

**`resize2fs` fails with “Device or resource busy”**

This is rare on a mounted filesystem. Avoid heavy I/O operations during the resize. Check for filesystem locks:

``` bash
cat /proc/locks | grep nvme0n1p1
```

If the error persists, check system logs:

``` bash
journalctl -xe
```

If the first `resize2fs` run was interrupted, run it again without arguments:

``` bash
resize2fs /dev/nvme0n1p1
```

**Filesystem still shows old size after `resize2fs`**

Run `resize2fs` again. If the first run was interrupted, a second invocation will complete the operation.

**`xfs_growfs` shows “input/output error”**

Ensure you’re using the mount point, not the device path:

``` bash
xfs_growfs /
```

Not `xfs_growfs /dev/nvme0n1p1`.

**Partition table changes are not recognized**

Modern kernels support partition table rereading without reboot. Trigger a rescan manually:

``` bash
echo 1 > /sys/block/nvme0n1/device/rescan
```

Or use `partprobe`:

``` bash
partprobe /dev/nvme0n1
```

## Important Notes

- This procedure requires root privileges.
- Test on non-production systems first whenever possible.
- The filesystem resize happens online while mounted — no reboot needed.
- Partition table changes are safe on modern systems; the kernel rereads the updated table without reboot.
- For LVM setups, expand the physical volume and logical volume after growing the partition.
- This works on AWS EC2, Google Cloud, Azure, DigitalOcean, and most major cloud providers, as long as they’ve expanded the underlying block device.
- Monitor disk space growth after expansion. Set up monitoring alerts if the filesystem approaches capacity again.
