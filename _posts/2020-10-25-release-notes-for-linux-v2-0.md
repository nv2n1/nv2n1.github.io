---
title: "Linux 2.0 Release Notes"
date: 2020-10-25 15:07:39 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /release-notes-for-linux-v2-0/
---

This document provides the essential software versions and upgrade instructions for running Linux 2.0.x kernels successfully. It covers package compatibility, known issues, and practical solutions for system administrators upgrading from earlier kernel releases.

## Networking Configuration

The loopback route configuration in many older network scripts is incorrect and will cause kernel errors in 2.0.x. Look for lines like:

``` bash
route add -net 127.0.0.1
```

Change them to:

``` bash
route add -net 127.0.0.0
```

This affects all Red Hat distributions and derivatives. Edit `/etc/sysconfig/network-scripts/ifup-lo` and update the route command accordingly.

## Bootloader and Kernel Build Changes

The 2.0.x boot subsystem supports larger kernels via `bzImage` format and can load initial ramdisks (initrd). Update your bootloader if you need these features. Use `make bzImage`, `make bzlilo`, or `make bzdisk` instead of the older `zImage` targets.

If your system uses LILO and you have `ramdisk=0` in your configuration, comment it out and rerun `lilo`. This is common in older Slackware installations.

## C Library Compatibility

The stable libc-5.2.18 release introduces changes that can break some utilities—notably GNU make. Read the release notes before upgrading from libc-5.0.9 or earlier.

The beta libc-5.3.12 release fixes a dirent structure bug and resolves an rlogin security vulnerability. However, it breaks programs that incorrectly call `free()` on pointers not returned by `malloc()`. Some GNU packages (including older make versions) depend on the buggy behavior and require patching.

If you see this error:

    fcntl_setlk() called by process 123 with broken flock() emulation

Upgrade to at least libc-5.2.18. The 2.0.x kernel adds proper BSD-style `flock()` support, which older libc versions don’t recognize. You can suppress the warning by commenting out the `printk` call in `linux/fs/locks.c` if upgrading isn’t feasible.

## Process Utilities (Procps)

The `/proc` filesystem structure changed in 2.0.x. Upgrade procps to 1.01 or later to avoid floating-point errors in `ps` and related commands.

## Kernel Modules

Almost all 2.0.x drivers can be built as modules. Kerneld is now integrated into the kernel itself, so you need the latest module utilities (modules-2.0.0 or later).

Important limitations:

- You cannot compile both a.out and ELF support as modules. Choose one to compile into the kernel.
- All filesystems and device drivers needed at boot time must be compiled into the kernel, not as modules. Don’t forget ext2 and IDE/SCSI support.

If modules fail to load with symbol mismatch errors, upgrade your module utilities.

## PPP Networking

Use pppd from ppp-2.2.0f or later. Earlier versions are incompatible with 2.0.x.

## Named Pipes and Init System

Linux’s named pipe implementation changed to follow proper Unix semantics rather than SunOS behavior. This breaks SysVinit 2.59 and earlier, causing repeated “INIT: error reading initrequest” messages during shutdown.

Upgrade to sysvinit-2.64 or later to fix this. The same issue affects other daemons that use named pipes opened in read-only mode. If you encounter problems with applications like Hylafax, change their configuration to open named pipes in read-write mode:

``` bash
# Before
CONFIG_OPENFIFO="O_RDONLY"

# After
CONFIG_OPENFIFO="O_RDWR"
```

## File Locking (Sendmail)

Mixed file locking styles are no longer allowed in 2.0.x. A file cannot be simultaneously locked with both `flock()` and `fcntl()`. Sendmail versions prior to 8.7.x fail with lock errors on `aliases.dir` and similar files.

Upgrade to sendmail 8.7.5 or later.

## Serial Line Configuration (Uugetty)

Older uugetty versions don’t support bidirectional serial lines. Upgrade to getty_ps-2.0.7i or later.

## Keyboard Support

For non-ASCII character and font support, upgrade to kbd-0.91 or later.

## Mount Utilities

The mount utility is part of util-linux. Upgrade to version 2.5 or later if you use loop devices, NFS, or automounting. Modern loop device support requires updated mount utilities.

## Console and Terminal Configuration

The Linux console type changed in 2.0.x. Update terminfo if console output displays incorrectly:

``` bash
ln -s /usr/lib/terminfo/l/linux /usr/lib/terminfo/c/console
```

Alternatively, update termcap to version 2.0.8 or the fixed 2.0.8.fix version. If terminal entries are too long, use the fixed version.

The console driver now manages character-to-glyph mapping. If display problems occur, run:

``` bash
loadunimap def
```

## Disk Performance (Hdparm)

Hdparm 3.1 and later versions take advantage of new 2.0.x kernel driver features for disk optimization.

## IP Firewall and Masquerading

The firewall architecture changed significantly. Three rule categories now exist: incoming, outgoing, and forwarded packets. You can match rules by device name and address to prevent spoofing.

Use ipfwadm-2.3.0 or later to configure firewall rules. The older ipfw tool has no 2.0.x support.

IP masquerading is now built-in, but you must load separate modules for FTP (`ip_masq_ftp.o`) and IRC (`ip_masq_irc.o`) support.

## IP Accounting

All IP packets now pass through the accounting chain. Forwarded packets pass through twice. Use ipfwadm-2.3.0 to define directional accounting rules.

## Network Tools

Update net-tools to 1.32-alpha or later due to `/proc/net` format changes. Note that ipfw has no 2.0.x support; use ipfwadm instead.

## Additional Features

**ISDN Support**: Kernel 2.0.x includes ISDN drivers. Install isdn4k-utils-2.0 or later for configuration.

**Frame Relay**: Frame relay support is available for Sangoma cards. Refer to frad and routing packages for implementation.

**NTP Daemon**: Upgrade xntpd to xntp3.5f or later.

**Sound Drivers**: The sound driver was upgraded, breaking vplay. Install snd-util-3.5 or later and recompile other sound utilities as needed.

## Floppy and IDE I/O Control

The floppy ioctl numbering scheme changed in 2.0.x. Recompile mtools, fdutils, and similar utilities to use the new scheme. The old scheme generates warnings in 2.0 and disappears entirely in 2.1.x.

## SCSI Drivers

NCR 53c810 drivers are included in the kernel source but require Perl to compile. Ensure Perl is installed before building.

## Perl Compatibility

Perl’s `connect()` call times out with 2.0.x kernels due to changes in optional `bind()` behavior. Remove the `bind()` call from your scripts.

Older Perl versions also have issues with `readdir()` due to libc changes. Upgrade to a current Perl version.

## Compiler and Build Tools

If you encounter “Internal compiler error: program cc1 got fatal signal 11” errors, check the Sig11 FAQ (<a href="http://www.bitwizard.nl/sig11/" rel="nofollow noopener" target="_blank">http://www.bitwizard.nl/sig11/</a>). These are usually hardware problems, not kernel bugs. If using Pentium-optimized GCC patches, downgrade to standard GCC.

Random OOPses without clear causes may relate to APM support on some motherboards. Try disabling APM or recompiling the kernel with APM enabled.

## Cyclades Serial Drivers

Minor device numbers changed from starting at 32 to starting at 0. Use `mknod` or an updated `MAKEDEV` script to recreate device files.

## Documentation and Terminal Issues

**Groff/Man Pages**: Slackware users may see display issues with man pages. Set `LESSCHARSET=latin1` or edit `/usr/lib/man.config` to change `-Tlatin1` to `-Tascii`.

**E2fsprogs**: e2fsprogs 1.02 works with 2.0.x but cannot compile on it. Use version 1.04 or later if you need to rebuild.

**Tcsh**: If tcsh behaves incorrectly, add `#define SYSMALLOC` to `config_f.h` before recompiling.

**Make**: If GNU make breaks after libc upgrades, read the libc release notes. When upgrading to libc-5.3.9, apply the provided patches to make. This is a libc issue, not a kernel issue.

**Xterm**: Libc upgrades can break xterm. Recompile xterm if needed.

## Additional Features in 2.0.x

- **Loop Devices**: Mount files as filesystems for encrypted storage. Requires updated mount utilities.
- **Multiple Device Support (md)**: Group partitions into logical devices.
- **ARP Daemon**: Gratuitous ARP support for network redundancy.
- **Disk Quotas**: User and group disk quota enforcement.
- **Process Accounting**: Track system resource usage per process.
- **Bdflush and Update**: Buffer flushing is now kernel-integrated (kflushd). Keep update daemon in init scripts but remove bdflush.
- **APM Support**: Advanced Power Management for laptop battery status and power conservation.

## Legacy Compatibility

**iBCS2**: Binary compatibility for SCO/Unix executables is available.

**DOSemu**: DOS emulation support. Follow the README.newkernels instructions to patch include files before compiling.
