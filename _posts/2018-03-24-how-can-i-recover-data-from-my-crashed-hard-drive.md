---
title: "Recovering Data from a Failed Hard Drive"
date: 2018-03-24 11:45:47 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-can-i-recover-data-from-my-crashed-hard-drive/
---

When a hard drive fails physically, data recovery becomes challenging but sometimes possible. If the drive isn’t recognized by the system or showing signs of mechanical failure, professional recovery services may be necessary—but they’re expensive. Before going that route, you can attempt recovery yourself using open-source tools.

## When to attempt DIY recovery

You can safely attempt recovery if:

- The drive is recognized by BIOS/UEFI but the filesystem is corrupted
- The drive shows up in `lsblk` or `fdisk -l` but isn’t mounting
- You can access the drive through a USB adapter on another system
- There are no clicking, beeping, or grinding sounds (signs of mechanical failure)

If the drive makes unusual noises or isn’t detected at all, the platters or read/write heads are likely damaged—professional recovery is your only option.

## Using PhotoRec for file recovery

PhotoRec is a free, open-source tool designed to recover lost files. Despite its name, it recovers far more than photos—it can reconstruct hundreds of file types including documents, archives, databases, and media files.

Install PhotoRec on your recovery system:

``` bash
# Ubuntu/Debian
sudo apt install testdisk

# RHEL/CentOS/Fedora
sudo dnf install testdisk

# macOS
brew install testdisk
```

PhotoRec is bundled with TestDisk, a companion tool for partition recovery.

## Recovery procedure

Connect the failed drive via USB adapter or dock to another working system. Identify the device:

``` bash
lsblk
sudo fdisk -l | grep -E "^/dev"
```

Run PhotoRec (use `sudo` for full access):

``` bash
sudo photorec /dev/sdX
```

Replace `sdX` with your actual device (e.g., `sdb`). PhotoRec opens an interactive menu:

1.  Select the device partition or entire disk
2.  Choose the filesystem type (or let it auto-detect)
3.  Select the recovery destination (must be a different drive with sufficient space)
4.  Start the scan

PhotoRec performs a deep scan of the drive, reading raw data blocks and identifying file signatures. The process can take hours for large drives. Recovered files are written to the destination drive in numbered directories.

## What files can be recovered

PhotoRec supports recovery of over 400 file types, including:

- Documents: PDF, Office formats, text files
- Images: JPEG, PNG, GIF, RAW camera formats
- Video: MP4, AVI, MOV, MKV
- Audio: MP3, WAV, FLAC, AAC
- Archives: ZIP, TAR, 7Z
- Databases: SQLite, MySQL InnoDB tables

See the complete list at the <a href="https://www.cgsecurity.org/wiki/PhotoRec" rel="nofollow noopener" target="_blank">PhotoRec documentation</a>.

## Limitations and alternatives

PhotoRec has drawbacks:

- Recovered files lose their original names and directory structure
- Fragmented files may not recover completely
- The process is slow on large drives
- Some file types with complex structures (like Office documents) may be partially corrupted

For more aggressive recovery targeting specific partitions, try **TestDisk** (included in the same package) to rebuild partition tables before running PhotoRec.

If the drive contains RAID arrays or complex storage setups, **ddrescue** can create an image of the drive for safer recovery attempts:

``` bash
sudo ddrescue -n /dev/sdX /path/to/image.img /path/to/mapfile.map
```

This copies readable sectors and logs bad blocks, allowing multiple recovery attempts without stressing the failing drive further.

## When professional recovery is necessary

Professional data recovery services cost \$300–\$3,000+ but are worth it if:

- The drive has mechanical or electronic failure
- The data is critical business information
- DIY recovery attempts fail completely
- You need guaranteed chain-of-custody for legal/compliance reasons

Budget several days for recovery regardless of method—don’t expect instant results.
