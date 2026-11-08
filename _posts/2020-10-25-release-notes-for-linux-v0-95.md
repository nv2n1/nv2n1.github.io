---
title: "Linux v0.95 Release Notes"
date: 2020-10-25 08:00:33 +0000
author: "Tony"
layout: post
categories: [testing-devops]
canonical: /release-notes-for-linux-v0-95/
---

This document preserves the historical release notes for Linux v0.95 (March 7, 1992), one of the earliest public kernel versions. These notes provide valuable insight into early Linux development decisions and technical challenges. The original notes are presented here with minor formatting improvements for readability.

## Copyright

Linux 0.95 is copyrighted under the GNU General Public License (GPL). You may freely copy and redistribute Linux in whole or in part, provided you make source code available at no more than copying cost. Any modifications you distribute fall automatically under the GPL.

The unistd library functions (system call interface) are exempt from this restriction—you may use them freely in binary applications without GPL obligations. Most other library components retain their original copyrights or remain in the public domain; see source files for specifics.

## Installation

Installation closely mirrors versions 0.11 and 0.12. You’ll need:

- A disk imaging tool (e.g., `rawrite.exe`)
- A partition editor (`fdisk` or equivalent)
- Boot and root filesystem images
- Backup of all existing data

**Critical:** Repartitioning destroys existing data. Proceed only if you understand the process completely.

### Minimum Required Files

- `RELNOTES-0.95` (this file)
- `INSTALL-0.11` and related documentation
- `bootimage-0.96.Z`
- `rootimage-0.95.Z`
- `rootimage-0.12.Z` (for tar and compress utilities)
- `rawrite.exe` or equivalent
- Disk partitioning tool

### Installation Steps

**1) Back up everything.** Linux 0.95 remains beta software. While it works reliably on the author’s hardware, behavior on other systems is untested.

**2) Test the boot disk.** Boot with the root filesystem image. Linux 0.95 now includes init/login, starting four login sessions on virtual consoles. Log in as root (no password). Switch consoles with `Alt+F1` through `Alt+F4`. Note: floppy boot is slow due to optimization for sequential access rather than demand-loading.

Test disk detection by running `fdisk` on the root disk. Any partition output indicates successful disk recognition.

**Device naming has changed.** The new scheme uses `/dev/hd` followed by:

- `a` for the first drive, `b` for the second
- Partition numbers 1-4 for primary partitions
- Numbers 5+ for extended partitions
- No number means the entire disk

Examples:

- `/dev/hda` = entire first disk (previously `/dev/hd0`)
- `/dev/hdb3` = partition 3 on second disk (previously `/dev/hd8`)

**3) Allocate a primary partition.** DOS fdisk often creates only two partitions (one primary, one extended). Use alternative partitioning tools if necessary. Linux fdisk currently displays partition info only; it doesn’t modify the disk.

**Warning:** Extended partition support in 0.95 is untested. Avoid using extended partitions unless you can verify correct setup—incorrect handling could overwrite other partitions.

**4) Create a filesystem.** After confirming the new partition appears in `fdisk`, create a filesystem:

``` bash
mkfs -c /dev/hdX nnn
```

Replace `X` with the device number from fdisk, and `nnn` with the size in blocks (kilobytes) as reported by fdisk.

**5) Mount and copy the root filesystem.** Mount the new partition and copy existing root files:

``` bash
mount /dev/hdX /mnt
for i in bin dev etc usr tmp; do
  cp -r /$i /mnt
done
```

Avoid `cp -r / /mnt` — this creates an infinite loop.

**6) Sync before rebooting.** Always sync the filesystem before shutdown:

``` bash
sync
sync
```

Wait for completion, then press `Ctrl+Alt+Delete`. **Never skip this step.** Failure to sync may corrupt the filesystem.

**7) Update the boot disk.** Modify the boot image to specify your root partition. See `INSTALL-0.11` for the procedure—the relevant offset is 508 bytes into the image.

**8) Migrate additional software.** Once running on your hard disk, mount the older rootimage-0.12 from a floppy to copy additional utilities:

``` bash
mkdir /floppy
mount /dev/PS0 /floppy    # for 3.5" drives
# or
mount /dev/at0 /floppy    # for 5.25" drives

cp /floppy/usr/bin/compress /usr/bin
cp /floppy/usr/bin/tar.Z /usr/bin
uncompress /usr/bin/tar.Z
```

## New Features in v0.95

### Init/Login

Linux now boots like a proper Unix system with a login prompt, courtesy of Peter Orbaeck. Log in as root (no password) and modify `/etc/passwd` or `/etc/inittab` to add additional users.

### Virtual Consoles

Select different consoles by pressing `Alt+F1` through `F8` (depending on your hardware and video mode). `/dev/tty0` represents the current screen; `/dev/tty1` is the main console; `/dev/tty2-8` are available depending on capabilities.

Virtual consoles now better conform to VT200 control codes, including support for special graphics characters and application-key mode (PF1-4 keys).

### Symbolic Links

Version 0.95 allows symlinks to point to other symlinks, with a maximum depth of 5 levels. Version 0.12 supported only one level of indirection.

### Virtual Memory Improvements

Memory management is more robust: no more lockups, and swapping works both to dedicated partitions and regular files. Two utilities manage swapping:

**mkswap** — Initialize a swap area

**swapon** — Enable swapping

To create a swap file:

``` bash
dd bs=1024 count=NN if=/dev/zero of=swapfile
mkswap swapfile NN
swapon swapfile
```

Replace `NN` with the desired size in blocks. Note: `dd` is not on the root disk; install it to the hard disk first.

When virtual memory is exhausted, the system degrades gracefully rather than locking up. Response times slow dramatically, but `Ctrl+C` remains functional.

### Floppy Performance

Floppy reads are significantly faster, especially for sequential operations like tape extraction. This becomes noticeable when untarring software packages. For practical purposes, floppies remain suitable only for backups; using them as filesystems is inadvisable.

### Filesystem Abstraction

The filesystem code has been partially refactored to reduce dependency on Minix filesystem specifics. Full VFS abstraction remains incomplete, but the foundation supports future improvements.
