---
title: "Managing LVM Logical Volumes on Linux"
date: 2018-03-24 07:43:06 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /managing-lvm/
---

LVM (Logical Volume Management) abstracts physical storage into logical volumes, giving you flexibility to resize filesystems, snapshot data, and manage disk space without downtime. It sits between your physical disks and the filesystems you mount.

The three core LVM concepts are:

- **Physical Volumes (PVs)**: Physical disks or disk partitions
- **Volume Groups (VGs)**: Collections of PVs that act as a storage pool
- **Logical Volumes (LVs)**: Virtual partitions carved from a VG

## Creating and Initializing LVM

Start by preparing a disk or partition as a physical volume:

``` bash
# Initialize a physical volume
pvcreate /dev/sdb1

# Verify the PV was created
pvs
pvdisplay /dev/sdb1
```

Create a volume group from one or more physical volumes:

``` bash
# Create a VG named 'storage'
vgcreate storage /dev/sdb1

# Add another PV to the existing VG
vgextend storage /dev/sdc1

# View VG details
vgs
vgdisplay storage
```

Create logical volumes within the volume group:

``` bash
# Create a 50GB LV named 'data'
lvcreate -L 50G -n data storage

# Or use percentage of available space
lvcreate -l 80%VG -n backup storage

# List logical volumes
lvs
lvdisplay /dev/storage/data
```

Format and mount the logical volume:

``` bash
mkfs.ext4 /dev/storage/data
mkdir -p /mnt/data
mount /dev/storage/data /mnt/data
```

## Resizing Logical Volumes

One of LVM’s major advantages is resizing without unmounting (for most filesystems):

``` bash
# Extend an LV by 20GB
lvextend -L +20G /dev/storage/data

# Or extend to 150GB total
lvextend -L 150G /dev/storage/data

# Resize the filesystem to match the new LV size
resize2fs /dev/storage/data

# For XFS filesystems (which resize online)
xfs_growfs /mnt/data
```

To shrink a volume, unmount first and shrink the filesystem before the LV:

``` bash
umount /mnt/data
e2fsck -f /dev/storage/data
resize2fs /dev/storage/data 40G
lvreduce -L 40G /dev/storage/data
mount /dev/storage/data /mnt/data
```

## Removing and Recovering LVM Components

Remove a logical volume:

``` bash
umount /dev/storage/data
lvremove /dev/storage/data
```

Remove a volume group:

``` bash
vgremove storage
```

Remove a physical volume:

``` bash
pvremove /dev/sdb1
```

## Handling Missing Physical Volumes

If a disk fails or becomes unavailable, the volume group enters a degraded state. To recover:

``` bash
# First, identify what's missing
vgdisplay -v storage

# Remove missing PVs from the VG (use only if the disk is permanently gone)
vgreduce --removemissing storage

# For LVs mirrored across multiple PVs, you may need to force removal
vgreduce --removemissing --force storage
```

**Caution**: Before removing missing PVs, verify the disk is actually inaccessible and not just temporarily offline. Data loss can occur if you’re too aggressive with `--removemissing`.

## Snapshots

Create point-in-time snapshots of logical volumes for backups or testing:

``` bash
# Create a 10GB snapshot of the 'data' volume
lvcreate -L 10G -s -n data_snapshot /dev/storage/data

# The snapshot appears as /dev/storage/data_snapshot
mount /dev/storage/data_snapshot /mnt/snapshot

# Remove the snapshot
umount /mnt/snapshot
lvremove /dev/storage/data_snapshot
```

## Monitoring and Maintenance

Monitor LVM health regularly:

``` bash
# Check physical volume status
pvs -o pv_name,pv_size,pv_free

# Monitor for any warnings or errors
vgck storage

# Get detailed space usage
vgs -o vg_name,vg_size,vg_free,vg_extent_size

# Check specific LV utilization
df -h /mnt/data
```

Use `lvmdevices` (available in modern LVM versions) to manage which devices LVM scans:

``` bash
# List devices LVM will use
lvmdevices

# Update the device filter if needed
lvmdevices --adddev /dev/sdd1
```

## Practical Considerations

- Always take snapshots before major operations
- Monitor free space in volume groups—when a VG runs full, add more PVs with `vgextend`
- For production systems, consider mirrored or RAID-backed LVs for redundancy
- Use consistent naming conventions (e.g., `vg_prod`, `vg_test`)
- Keep LVM metadata backups: `vgcfgbackup` and `vgcfgrestore` can recover from metadata corruption

LVM is essential infrastructure for most Linux servers. Master these basics and you’ll handle storage management efficiently.
