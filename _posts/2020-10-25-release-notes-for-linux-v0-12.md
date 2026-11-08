---
title: "Linux v0.12 Release Notes"
date: 2020-10-25 06:59:35 +0000
modified: 2026-04-11 16:13:20 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /release-notes-for-linux-v0-12/
---

Linux v0.12 is a historical kernel release from the early days of Linux development. This document preserves the original release notes with minimal modifications to improve readability and accuracy. These notes are primarily of archaeological interest to those studying early Linux kernel history.

## Copyright

The Linux copyright was updated to conform with the GNU General Public License, removing the previous restriction against commercial distribution. This change took effect on February 1st, pending approval from contributors.

## Installation Overview

Installation for v0.12 closely parallels v0.11. You’ll need:

- A disk image writing utility (equivalent to modern `dd` or imaging tools)
- A partitioning tool (the DOS `fdisk`, `edpart.exe`, or similar)

**Critical warning:** Repartitioning will destroy existing data on the target drive. Verify your understanding of the installation process before proceeding.

### Pre-Installation Checklist

- Back up all data on the target hard disk. v0.12 is beta software with unpredictable behavior on untested hardware.
- Test the Linux boot disk with the provided root filesystem. If boot fails, verify hardware compatibility and report any issues.
- Test hard disk readability by running `fdisk` from the root disk. Successful partition detection indicates the kernel can read your drive.

### Installation Steps

**1. Verify partition availability**

Ensure at least one free primary partition exists. DOS `fdisk` typically creates only 2 partitions (one primary, one extended). Use alternative partitioning software if necessary. Note the partition size—this helps identify the correct device node.

**2. Create the Linux filesystem**

After booting Linux and confirming the new partition with `fdisk`, create the filesystem:

``` bash
mkfs -c /dev/hdX nnn
```

Where `X` is the device number from `fdisk` and `nnn` is the size in blocks (kilobytes).

**3. Mount and copy the root filesystem**

``` bash
mount /dev/hdX /user

for i in bin dev etc usr tmp
do
  cp -r /$i /user
done
```

Do not use `cp -r / /user` as this creates infinite loops.

**4. Synchronize and reboot**

``` bash
sync
# Wait for sync to complete
```

Press `Ctrl+Alt+Del` to reboot. The sync operation is critical—never power down without flushing buffers.

**5. Configure the boot disk**

Modify the boot disk to reference the correct root partition. The root device specification is a word at offset 508 in the boot image. Adjust this using the same tool used for initial boot disk creation, changing offset 508 to point to your Linux partition.

## New Features in v0.12

### Loading Progress Indication

The kernel now prints dots during boot, providing visual feedback on slower hardware and improving compatibility with machines that previously failed to initialize.

### Super-VGA Support

Extended alphanumeric modes are now detected and supported on compatible VGA cards. Tested hardware includes the ET400 SVGA card. Supported resolutions include 100×40 text mode as an alternative to the standard 80×25.

### Job Control

Background job suspension and management are now functional. The shell supports standard job control commands:

``` bash
bg          # Resume suspended job in background
fg          # Bring background job to foreground
jobs        # List active jobs
kill        # Terminate jobs
```

Job suspension with `Ctrl+Z` now works as expected.

### Virtual Consoles

Multiple virtual consoles are available on EGA/VGA systems. Switch between consoles using `Alt` + function key combinations. Device nodes `/dev/tty1` through `/dev/tty8` represent available consoles depending on video mode and hardware capabilities. `/dev/tty0` represents the current active console.

**Performance note:** Scrolling performance is noticeably slower with virtual consoles due to video memory constraints across multiple console buffers.

Virtual consoles support improved VT200 control codes and can function as terminals for compatible systems.

### Pseudo-terminals (PTYs)

PTY support is functional for basic operations, though hangup handling remains incomplete.

### Select System Call

The `select()` system call is implemented for multiplexing I/O operations, though it sees limited testing at this release stage.

### 387 Math Coprocessor Emulation

Partial 387 coprocessor instruction emulation allows execution of GCC 2.0-compiled programs. Heavy mathematical functions remain unimplemented.

### Symbolic Links

Symbolic link creation and dereferencing work correctly:

``` bash
ln -s target linkname
ls -l linkname
```

Note that utilities like `tar` may require recompilation to properly handle symbolic links. The v0.12 root disk includes updated file utilities with symbolic link support.

### Virtual Memory and Swap

A new `mkswap` utility creates swap partitions with identical syntax to `mkfs`:

``` bash
mkswap -c /dev/hdX nnn
```

Enable swapping by modifying the word at offset 506 in the boot image to specify the swap device. This allows the kernel to swap memory to disk, enabling execution of larger programs on systems with limited RAM.

**Testing status:** Swap functionality was tested on 2MB systems and enables running GCC without excessive memory constraints. However, limited testing was performed at release time.
