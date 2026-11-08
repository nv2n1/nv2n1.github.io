---
title: "Linux 1.0 Release Notes"
date: 2020-10-25 14:43:03 +0000
layout: post
canonical: https://www.systutorials.com/release-notes-for-linux-v1-0/
---

This document preserves the original Linux 1.0 release notes (source: linux-1.0.tar.gz), released in March 1994. It’s a snapshot of early Linux kernel development and shows the rapid pace of improvement during the pre-1.0 era. The original ASCII formatted version appears at the end of this post.

## Changes since 0.99 patchlevel 15

- Removed all the bugs, of course.
- Networking fixes.
- More changes than desired.

## Changes since 0.99 patchlevel 14

- Too many to count. The maintainer had lost release notes by this point.

## Changes since 0.99 patchlevel 13

- New kernel source layout with drivers separated into dedicated directories
- Extensive networking bug fixes and new network card drivers (Alan Cox, Donald Becker, and others)
- Sound driver added to default source distribution (Hannu Savolainen)
- Updated SCSI driver code (Eric Youngdale, Drew Eckhardt, and others)
- Read-only OS/2 filesystem support (HPFS) added (Chris Smith)
- NTP (Network Time Protocol) support (Philip Gladstone, Torsten Duwe)
- Fixed 16MB swap-area limit
- Numerous minor cleanups and bug fixes

## Changes since 0.99 patchlevel 12 and earlier

- Fixed critical memory management bug in patchlevel 12
- Switched to plain C compilation by default instead of C++
- ELF binary format support (Eric Youngdale)
- Quickport mouse driver support and PS/2 mouse driver improvements (Johan Myreen and others)
- Core dump file naming changed from `core` to `core.xxxx` where `xxxx` is the program name. Core files now properly truncate existing files before writing.
- Improved `mmap()` handling: better error returns and proper handling of non-fixed mappings for `/dev/mem`
- Workaround for malformed ARP packets that plagued the net-2d stack (packets with ethernet address bytes appearing as IP address)
- Fixed mount-point handling for `rename()` and `unlink()/rmdir()` operations with appropriate error messages
- Packet mode fixes (Charles Hedrick) that improve RFC compliance but break compatibility with old telnet/rlogin binaries
- FPU emulator patches (Bill Metzenthen) with corrected `fprem1` instruction behavior
- SCSI subsystem fixes (Drew Eckhardt, Eric Youngdale)
- Signal handling improvements in `signal.c` to properly handle multiple segments (required for Wine compatibility)
- Updated drivers from Donald Becker including 3c509 and AT1500 network drivers plus general networking fixes

## Changes since 0.99 patchlevel 11 and earlier

**Memory management overhaul**: The memory manager underwent substantial cleanup, culminating in working `mmap()` support. The kernel can now demand-load binaries over NFS with proper code/data sharing and shared library support. NFS `mmap()` implementation was handled by Jon Tombs, while core memory management improvements came from Eric Torvalds and others.

**Keyboard driver enhancements**: The keyboard driver became fully remappable, requiring new versions of `loadkeys` and `dumpkeys` utilities. The default remains US QWERTY, but users can create custom keymaps loaded at boot. Features include function key string customization, control key remapping, and special bindings for operations like console switching and system reboot. Implementation by Risto Kankkunen.

**Driver updates**:

- Network drivers updated (Donald Becker)
- Serial drivers updated (Theodore Ts’o)
- 387 FPU emulation with improved trigonometric functions and exception handling, approaching real 486 behavior (Bill Metzenthen)
- Network timer fixes and race condition elimination (Florian La Roche)
- SCSI code improvements (Eric Youngdale, others)
- Sony CDU-31A CDROM driver integration
- Mitsumi CDROM driver integration (Martin Harriss, Jon Tombs)

**Other improvements**:

- Preliminary LDT (Local Descriptor Table) support
- Named pipes and regular pipes with correct `select()` semantics
- QIC-02 tape driver (Hennus Bergman)
- Selection/copy-paste patches in default kernel

## Notable changes since patchlevel 10 or earlier

**Memory management**: Substantial `mmap()` cleanup with working `MAP_PRIVATE` support. `MAP_SHARED` limited to `/dev/mem` but proven useful for many applications. Shared library code rewritten to use `mmap()` instead of hardcoded mechanisms.

**Compilation**: Kernel now built with C++ instead of plain C. While few C++ features are actually used, this enables better type checking and type-safe linkage.

**Filesystem support**: Filesystem code refactored to support multiple block sizes, laying groundwork for future filesystems (though none yet implement variable sizes).

**Driver and subsystem improvements**:

- PTY code bug fix eliminating busy-waiting in certain conditions
- Compressed SLIP support (Charles Hedrick)
- QIC-02 tape driver (Hennus Bergman)
- Selection/clipboard support patches

**API changes**:

- `clear_bit()` function now returns previous bit state instead of error codes, making bitwise operations more logical
- `udelay()` function for short busy-wait delays (initially used only by QIC driver)
- `fork()` and scheduler changes ensuring task switches occur kernel-to-kernel only, improving portability

**Debugging**: Debugging malloc code added for memory allocation tracking.

------------------------------------------------------------------------

## Original ASCII release notes

    CHANGES since 0.99 patchlevel 15:

     - removed all the bugs, of course.
     - networking fixes.
     - more changes than I really wanted..

    CHANGES since 0.99 patchlevel 14:

     - too many to count, really.  Besides, I've lost my notes. 

    CHANGES since 0.99 patchlevel 13:

     - new kernel source layout: drivers separated
     - lots of networking bugs fixed, and new network card drivers (Alan Cox,
       Donald Becker &co)
     - sound driver added to the default source distribution (Hannu
       Savolainen)
     - updated SCSI driver code (Eric Youngdale, Drew Eckhardt &co)
     - readonly OS/2 filesystem support (HPFS) added (Chris Smith)
     - NTP support (Philip Gladstone, Torsten Duwe, ??)
     - fixed 16MB swap-area limit
     - lots of minor cleanups, buxfixes etc.

    CHANGES since 0.99 patchlevel 12 and earlier:

     - the bad memory management one-liner bug in pl12 is naturally fixed.
     - compiled with plain C by default instead of C++
     - ELF binary support (Eric Youngdale)
     - Quickport mouse support (and some changes to the PS/2 mouse driver)
       by Johan Myreen and co)
     - core file name change ("core" -> "core.xxxx" where xxxx is the name
       of the program that dumped code).  Idea from ???.  Also, core-files
       now correctly truncate any existing core file before being written.
     - some mmap() fixes: better error returns, and handling of non-fixed
       maps for /dev/mem etc.
     - one kludgy way to fix the wrong arp packets that have plagued net-2d
       (resulting in arp packets that had the first four bytes of the
       ethernet address as the IP address).
     - I fixed the mount-point handling of 'rename()' and 'unlink()/rmdir()'
       so that they should now work and/or give appropriate error messages.
       An early version of this patch was already sent to the KERNEL
       channel, which fixed the rename problem but not a similar bug with
       unlink.
     - packet mode fixes by Charles Hedrick.  Sadly, these are likely to
       break old telnet/rlogin binaries, but it had to be done in order to
       communicate correctly with the rest of the world.
     - FPU emulator patches from Bill Metzenthen.  The fprem1 insn should be
       correct now (not that anybody seems to have seen the incorrect
       behaviour..)
     - a few fixes for SCSI (Drew and Eric)
     - signal.c changes to handle multiple segments (for Wine) correctly.
     - updated drivers from Donald Becker: 3c509 and AT1500 drivers, but
       also some other drivers have been edited, and some networking fixes.

    CHANGES since 0.99 patchlevel 11 and earlier:

     - The memory manager cleanup has continued, and seems to be mostly
       ready, as proven by the ease of adding mmap() over NFS with the new
       routines.  So yes, the pl12 kernel will demand-load your binaries
       over NFS, sharing code and clean data, as well as running shared
       libraries over NFS.  Memory management by Eric and me, while the NFS
       mmap code was written by Jon Tombs,

     - ** IMPORTANT **: The keyboard driver has been enhanced even further,
       and almost everything is completely re-mappable.  This means that
       there is a new version of 'loadkeys' and 'dumpkeys' that you must use
       with this kernel or you'll have problems.  The default keyboard is
       still the US mapping, but if you want to create your own mappings
       you'll have to load them with the new binaries.  Get the 'kbd.tar.gz'
       archive from the same place you get the kernel.

       The new keymappings allow things like function key string changes,
       remapping of the control keys, and freedom to remap any of the normal
       keyboard functions: including special features like rebooting,
       console switching etc.  The keyboard remapping code has been done
       mostly by Risto Kankkunen (Risto.Kankkunen@Helsinki.FI).

     - updated network drivers by Donald Becker

     - updated serial drivers - tytso@Athena.mit.edu

     - updated 387 emulation (Bill Metzenthen).  The updated emulator code
       has more exact trigonometric functions and improved exception
       handling.  It now behaves very much like a real 486, with only small
       changes (greater accuracy, slightly different denormal NaN handling
       etc - hard to detect the differences even if you are looking for
       them).

     - network timer fixes by Florian La Roche (much cleaned up net/inet/timer.c
       and some bad race-conditions fixed).

     - Scsi code updates by Eric Youngdale and others

     - Sony CDU-31A CDROM driver by Corey Minyard added to the standard
       kernel distribution.

     - The Mitsumi CDROM driver is now part of the standard kernel.  Driver
       by Martin Harriss with patches by stud11@cc4.kuleuven.ac.be (yes, he
       probably has a real name, but no, I haven't found it) and Jon Tombs.

     - various other minor patches (preliminary ldt support etc)

    NOTABLE changes since patchlevel 10 or earlier:

     - The memory manager has been cleaned up substantially, and mmap()
       works for MAP_PRIVATE.  MAP_SHARED is still not supported for
       anything else than /dev/mem, but even so it actually is usable for a
       lot of applications.  The shared library routines have been rewritten
       to use mmap() instead of the old hardcoded behaviour.

     - The kernel is now compiled with C++ instead of plain C.  Very few
       actual C++ features are used, but even so C++ allows for more
       type-checking and type-safe linkage.

     - The filesystem routines have been cleaned up for multiple block
       sizes.  None of the filesystems use it yet, but people are working on
       it.

     - named pipes and normal pipes should hopefully have the right select()
       semantics in the presense/absense of writers.

     - QIC-02 tape driver by Hennus Bergman

     - selection patches in the default kernel

     - fixed a bug in the pty code which led to busy waiting in some
       circumstances instead of sleeping.

     - Compressed SLIP support (Charles Hedrick). See net/inet/CONFIG

     - the 'clear_bit()' function was changed to return the previous setting
       of the bit instead of the old "error-code".  This makes use of the
       bit operations more logical.

     - udelay() function for short delays (busy-waiting) added.  Used
       currently only by the QIC driver.

     - fork() and sheduler changes to make task switches happen only from
       kernel mode to kernel mode.  Cleaner and more portable than the old
       code which counted on being able to task-switch directly into user
       mode.

     - debugging malloc code.
