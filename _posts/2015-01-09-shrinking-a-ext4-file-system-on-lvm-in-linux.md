---
title: "Safely Shrinking Ext4 Filesystems on LVM"
date: 2015-01-09 08:04:32 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/shrinking-a-ext4-file-system-on-lvm-in-linux/
---

Shrinking an ext4 filesystem on LVM is riskier than expanding—it requires the filesystem offline and careful size planning. The operation can take hours on large volumes, and mistakes can destroy data. This guide walks through the safe path with verification at each step.

## Prerequisites

Before starting:

- **Backup everything**. A full backup of the data being resized is mandatory. Test the backup restoration.
- **Calculate actual usage**: Run `df -h` and `du -sh` to see what’s actually consuming space. Identify files to delete if the filesystem is too full.
- **Leave breathing room**: Never shrink to exactly the size of your data. Plan for 10–20% free space after the operation completes.
- **Schedule downtime**: Block out time—this can take hours on filesystems larger than 500GB.
- **Check for errors first**: Run `fsck.ext4 -n /dev/vg/lv_data` while mounted (read-only check) to catch corruption before shrinking.

## The Safe Shrink Procedure

Assume you have:

- Physical volume: `/dev/sdb1` in volume group `vg`
- Logical volume: `lv_data` with ext4 filesystem
- Current mount point: `/mnt/data`
- Target size: 200GB

### Step 1: Unmount the filesystem

``` bash
umount /mnt/data
```

This is non-negotiable. Shrinking touches allocation metadata that the kernel actively manages on a mounted filesystem. Unmounting prevents corruption and ensures safe metadata writes.

Verify it’s unmounted:

``` bash
lsblk | grep lv_data
```

### Step 2: Run fsck before shrinking

Always check the filesystem before resize operations:

``` bash
fsck.ext4 -f /dev/vg/lv_data
```

The `-f` flag forces a check even if the filesystem appears clean. Address any errors reported before proceeding.

### Step 3: Shrink the filesystem and LV together

Use `lvresize` with `--resizefs` to handle both operations atomically:

``` bash
lvresize --resizefs --size 200G /dev/vg/lv_data
```

The `--resizefs` flag is critical—it automatically runs `resize2fs` before shrinking the LV, preventing size mismatches that can corrupt the filesystem. Avoid running `resize2fs` and `lvresize` separately unless you have a specific reason.

Expected output:

    fsck from util-linux 2.39.1
    /dev/mapper/vg-lv_data: 1523/6553600 files (0.2% non-contiguous), 892145/26214400 blocks
    resize2fs 1.47.0 (5-Feb-2023)
    Resizing the filesystem on /dev/mapper/vg-lv_data to 52428800 (4k) blocks.
    Reducing logical volume lv_data to 200.00 GiB
    Logical volume lv_data successfully resized

**Don’t interrupt this.** On a 500GB filesystem with heavy fragmentation, this can take 2–4 hours. Monitor progress in another terminal:

``` bash
lvs -o lv_name,lv_size vg
```

### Step 4: Remount and verify

``` bash
mount /mnt/data
df -hT /mnt/data
```

Confirm the size and that the filesystem is readable. Check for any kernel errors in `dmesg`:

``` bash
dmesg | tail -20
```

Run a second `fsck` to validate:

``` bash
umount /mnt/data
fsck.ext4 -n /dev/vg/lv_data
mount /mnt/data
```

## Freeing Space in the Volume Group

The space freed from shrinking the LV now belongs to the volume group:

``` bash
vgs vg
```

You can allocate this to other LVs or leave it available for future growth.

## Removing a Physical Volume (Optional)

If you’re decommissioning the disk entirely:

### Move data off the PV

``` bash
pvmove /dev/sdb1
```

This migrates all data from `/dev/sdb1` to other PVs in `vg`. Check free space first:

``` bash
vgs vg
lvs -o +devices vg
```

The move can take hours on large LVs. Don’t interrupt it.

### Remove the PV from the VG

``` bash
vgreduce vg /dev/sdb1
pvremove /dev/sdb1
```

The disk can now be physically removed or repurposed.

## Shrinking the Partition (Optional)

If you want to reclaim raw disk space, shrink both the PV metadata and partition boundary.

### Shrink the physical volume

``` bash
pvresize --setphysicalvolumesize 650G /dev/sdb1
```

Verify:

``` bash
pvs -o pv_name,pv_size
```

### Shrink the partition boundary

With `parted`:

``` bash
parted /dev/sdb
(parted) print
(parted) resizepart 1 650GB
(parted) quit
```

Confirm the kernel sees the change:

``` bash
partprobe /dev/sdb
fdisk -l /dev/sdb | head -20
```

If `partprobe` fails silently, reboot to force partition table re-read.

For automated/scriptable shrinking, use `parted` in non-interactive mode:

``` bash
parted -s /dev/sdb resizepart 1 650GB
```

For GPT partitions with strict alignment requirements, `gdisk` offers finer control:

``` bash
gdisk /dev/sdb
# Command: p (print)
# Command: d (delete partition 1)
# Command: n (new partition, set end sector manually)
# Command: w (write and exit)
```

## Final Verification

After all operations, validate the system state:

``` bash
lvs -o lv_name,lv_size,lv_attr vg
pvs -o pv_name,pv_size
vgs vg
df -h /mnt/data
```

Run your workloads on the shrunken filesystem for at least 24 hours before removing the backup. Watch `dmesg` and system logs for any ext4-related warnings.

## Common Failure Points

- **Partition not aligned**: Shrinking to an unaligned sector boundary can cause partition table corruption on GPT disks. Use `parted` defaults or calculate alignment explicitly (typically 1MB boundaries).
- **Not enough free space on other PVs**: `pvmove` fails if the target PVs can’t hold the migrated data. Check `vgs` output before running it.
- **Filesystem too fragmented**: Highly fragmented ext4 filesystems resize slowly. Use `e4defrag` before shrinking if the operation stalls.
- **Kernel doesn’t reread partition table**: `partprobe` doesn’t always work. Reboot if partition changes don’t take effect.
