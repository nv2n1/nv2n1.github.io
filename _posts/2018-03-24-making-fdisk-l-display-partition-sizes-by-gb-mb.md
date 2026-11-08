---
title: "Check Partition Sizes in Human-Readable Format with parted"
date: 2018-03-24 11:44:30 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /making-fdisk-l-display-partition-sizes-by-gb-mb/
---

`fdisk -l` displays partition information in sectors by default, which isn’t practical for most sysadmin tasks. While `fdisk` itself lacks options to change the unit display, `parted` shows partition sizes in GB/MB/KB automatically and is the better tool for this job.

## Using parted for readable partition output

Run `parted` with the `-l` flag to list all disks and partitions with human-readable sizes:

``` bash
parted -l
```

This gives you output like:

    Model: QEMU HARDDISK (scsi)
    Disk /dev/sda: 500GB
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt
    Disk Flags: 

    Number  Start   End     Size    File system Type     Flags
     1      1049kB  1075MB  1074MB  fat32      primary  boot, esp
     2      1075MB  500GB   499GB   ext4       primary

The output clearly shows sizes in GB, MB, or KB depending on what’s appropriate for each partition.

## Viewing a specific disk

To see details for a single disk instead of all attached disks:

``` bash
parted /dev/sda -l
```

## Setting unit preference

If you want to force output in a specific unit, use the `unit` command:

``` bash
parted /dev/sda unit GB print
parted /dev/sda unit MiB print
parted /dev/sda unit s print  # sectors
```

This is useful for scripting or when you need consistent units across different sized disks.

## Why parted over fdisk

`parted` is superior to `fdisk` for viewing partition information because:

- Human-readable output by default (GB/MB/KB instead of sectors)
- Works with both MBR and GPT partition tables seamlessly
- Shows filesystem types and partition flags clearly
- Better for modern large disks (handles 2TB+ without issues)
- Can be scripted with unit specification

`fdisk` still has its place for editing partition tables on MBR disks, but for viewing partition layout, `parted` is the standard approach.

## Alternative: lsblk for a different view

If you prefer a different format, `lsblk` also shows human-readable sizes:

``` bash
lsblk -h
lsblk -h /dev/sda
```

This displays a tree view of all block devices with their sizes, mountpoints, and types. It’s particularly useful for understanding the relationship between physical disks and mounted filesystems.

## Scripting partition size checks

If you need to extract partition sizes for automation, combine `parted` with `grep` or `awk`:

``` bash
parted /dev/sda unit GB print | grep "^[[:space:]]*[0-9]"
```

Or use `lsblk` with JSON output for parsing:

``` bash
lsblk -J /dev/sda
```

The JSON format works better with tools like `jq` for reliable parsing.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
