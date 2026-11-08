---
title: "Extend an Ext4 Filesystem on LVM Without Downtime"
date: 2014-08-15 02:26:38 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/extending-a-mounted-ext4-file-system-on-lvm-in-linux/
---

LVM abstracts physical storage into logical volumes, letting you resize filesystems online, add drives transparently, and manage capacity without downtime. This guide covers the most common task: extending a mounted ext4 filesystem when you need more space.

## Prerequisites

Online extension requires the `resize_inode` option enabled on your ext4 filesystem. Check this first:

``` bash
tune2fs -l /dev/vg/lv_home | grep resize_inode
```

If the output shows `Filesystem features: ... resize_inode`, you’re good. If not, you’ll need to unmount the filesystem and enable it:

``` bash
tune2fs -O resize_inode /dev/vg/lv_home
```

Replace `/dev/vg/lv_home` with your actual logical volume path. Always back up critical data before disk operations.

## Example Scenario

We’ll extend a volume group named `vg` with logical volume `lv_home` (mounted at `/home`) using a new 1TB drive `/dev/sdb`.

## Step 1: Partition the New Drive

Use `cfdisk` for an interactive approach:

``` bash
cfdisk /dev/sdb
```

Create a new partition using all available space and set its type to `Linux` (code 83). Exit and save. The partition will be `/dev/sdb1`.

Verify the partition exists:

``` bash
fdisk -l /dev/sdb
```

## Step 2: Add the Drive to LVM

Create a physical volume:

``` bash
pvcreate /dev/sdb1
```

Extend your volume group:

``` bash
vgextend vg /dev/sdb1
```

Confirm the volume group now shows available space:

``` bash
vgdisplay vg
```

Check the `Free PE / Size` line—this is what you can allocate.

## Step 3: Extend the Logical Volume and Filesystem

The `--resizefs` flag handles both steps atomically, which is safer for online resizing:

``` bash
lvresize --resizefs --size +931G /dev/vg/lv_home
```

Or extend to consume all available space:

``` bash
lvresize --resizefs -l +100%FREE /dev/vg/lv_home
```

The filesystem stays mounted and accessible throughout. This is the recommended approach.

### Manual Extension (Alternative)

If you need explicit control, extend the logical volume first:

``` bash
lvextend -L +931G /dev/vg/lv_home
```

Then resize the filesystem:

``` bash
resize2fs /dev/vg/lv_home
```

Both approaches achieve the same result; `--resizefs` is just more convenient.

## Verification

Check the filesystem size:

``` bash
df -hT /home
```

Verify the logical volume metadata:

``` bash
lvdisplay /dev/vg/lv_home
```

Both should show the new capacity.

## Shrinking a Filesystem

Shrinking is riskier than extending and requires unmounting. If necessary:

``` bash
umount /home
e2fsck -f /dev/vg/lv_home
resize2fs /dev/vg/lv_home 500G
lvreduce -L 500G /dev/vg/lv_home
mount /home
```

Always run `e2fsck` before shrinking. Data loss is possible if the filesystem contains data beyond the target size.

## Common Issues

**“Physical volume /dev/sdb1 not found”**

Verify the partition exists with `fdisk -l /dev/sdb` and ensure you ran `pvcreate /dev/sdb1`.

**“Resize failed: Filesystem has unsupported features”**

Check features with `tune2fs -l /dev/vg/lv_home`. Some older kernels don’t support online resizing of certain ext4 features. Update your kernel or unmount and resize offline with `resize2fs`.

**“No space left on device” during resize2fs**

The volume group lacks free space. Verify with `vgdisplay` that the physical volume was added and the free space is available.

**Logical volume won’t extend**

Confirm the physical volume is initialized with `pvdisplay /dev/sdb1`. If missing, run `pvcreate /dev/sdb1` again.

## When to Consider Alternatives

For new systems, `btrfs` or `XFS` with LVM offer more flexible online management and better tooling. `ext4` remains battle-tested and widely deployed, making this workflow reliable for production systems. If you’re managing many volumes, `thin provisioning` with LVM can reduce manual resizing overhead.
