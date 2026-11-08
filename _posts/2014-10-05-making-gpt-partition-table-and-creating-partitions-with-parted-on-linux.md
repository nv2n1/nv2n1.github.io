---
title: "Creating Linux Partitions with parted"
date: 2014-10-05 13:14:00 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /making-gpt-partition-table-and-creating-partitions-with-parted-on-linux/
---

GPT (GUID Partition Table) is required for disks larger than 2TB. The older MBR format maxes out at 2.2TB due to 32-bit sector addressing. Tools like `fdisk` will refuse to work properly with large drives and recommend switching to GPT. While `parted` has a steeper learning curve than some alternatives, it’s the standard for GPT manipulation on Linux.

## Why GPT Matters

Any disk over 2TB needs GPT. This includes modern SSDs, large RAID arrays, and cloud storage volumes. If you run `fdisk` on a 6TB disk, it will either warn you or silently limit usable space to 2TB—a frustrating gotcha in production.

## Basic Workflow: Creating a Single Partition

Here’s how to partition a new 6TB disk at `/dev/sdc`:

``` bash
sudo parted /dev/sdc
```

This launches the interactive `parted` shell. First, create a GPT label:

    (parted) mklabel gpt

You’ll see a warning that all data will be destroyed. Confirm with `Yes` if the disk is empty or you’ve backed up everything.

Now create a partition:

    (parted) mkpart primary ext4 2048s 100%

The `2048s` starting point aligns with 4K sector boundaries on modern SSDs, improving performance. The `100%` uses all remaining space.

    (parted) quit

Verify the partition was created:

``` bash
parted /dev/sdc print
```

Output:

    Model: Samsung SSD 870 (scsi)
    Disk /dev/sdc: 6001GB
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt

    Number  Start   End     Size    File system  Name     Flags
     1      1049kB  6001GB  6001GB               primary

## Using Partition Labels

Named partitions are more reliable than device paths, especially when adding or removing disks:

    (parted) mkpart storage ext4 2048s 100%
    (parted) name 1 storage
    (parted) quit

The partition is now accessible at `/dev/disk/by-partlabel/storage`. Use this in `/etc/fstab`:

    /dev/disk/by-partlabel/storage  /mnt/storage  ext4  defaults  0 2

## Non-Interactive Partitioning

For automation scripts, run `parted` commands directly without entering the shell:

``` bash
sudo parted -a opt /dev/sdc mklabel gpt
sudo parted -a opt /dev/sdc mkpart storage ext4 0% 100%
```

The `-a opt` flag enables partition alignment optimization. This is ideal for CI/CD pipelines or provisioning tools like Terraform or Ansible.

## Creating Multiple Partitions

To split a disk into boot, root, and data partitions:

    (parted) mkpart boot ext4 2048s 1GB
    (parted) mkpart root ext4 1GB 50%
    (parted) mkpart data ext4 50% 100%
    (parted) quit

Each partition gets a sequential number (`/dev/sdc1`, `/dev/sdc2`, `/dev/sdc3`).

## Verifying Alignment

Before finalizing, check that partitions are properly aligned:

``` bash
parted /dev/sdc align-check opt 1
```

Output should be:

    1 aligned

Misaligned partitions reduce I/O performance on SSDs and RAID arrays.

## Alternative Tools

**gdisk** provides a menu-driven interface similar to `cfdisk`:

``` bash
sudo gdisk /dev/sdc
```

Install it with `apt install gdisk` (Debian/Ubuntu) or `dnf install gdisk` (RHEL/Fedora). It’s easier to learn if you’re uncomfortable with `parted` syntax, though `parted` is more widely available.

## Formatting and Mounting

After partitioning, create a filesystem:

``` bash
sudo mkfs.ext4 /dev/sdc1
```

For newer systems using Btrfs or XFS:

``` bash
sudo mkfs.btrfs /dev/sdc1
# or
sudo mkfs.xfs /dev/sdc1
```

Mount and persist the mount:

``` bash
sudo mkdir -p /mnt/storage
sudo mount /dev/sdc1 /mnt/storage
```

Then add to `/etc/fstab` for automatic mounting at boot. Use the partition label:

    /dev/disk/by-partlabel/storage  /mnt/storage  ext4  defaults  0 2

## Common Gotchas

**Device busy errors**: If `parted` says the disk is in use, ensure nothing is mounted and no processes hold open file handles:

``` bash
sudo fuser -k /dev/sdc
```

**Partition table not recognized after creation**: If the kernel doesn’t see the new partitions, reload the partition table:

``` bash
sudo partprobe /dev/sdc
# or
sudo blockdev --rereadpt /dev/sdc
```

**Losing data during resizing**: Always back up before modifying partitions. `parted` can resize partitions, but it’s risky:

``` bash
sudo parted /dev/sdc resizepart 1 5TB
```

This should only be used when absolutely necessary and with verified backups.
