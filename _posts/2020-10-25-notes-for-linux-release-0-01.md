---
title: "Linux 0.01 Release Notes"
date: 2020-10-25 05:12:39 +0000
modified: 2026-04-11 16:13:21 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /notes-for-linux-release-0-01/
---

This document preserves the original release notes for Linux kernel version 0.01, the first public release by Linus Torvalds in 1991. These notes provide historical context on the early design decisions and limitations of what would become the world’s most widely used operating system kernel.

## Contents

The 0.01 distribution included:

- `linux-0.01.tar.Z` — kernel source code
- `bash.Z` — compressed bash binary for testing
- `update.Z` — compressed update utility
- `RELNOTES-0.01` — this release notes file

## Initial Release Notes

### What This Is

A free Unix-like kernel for 386-based AT machines with full source code included. The version number (0.01) made clear this was pre-alpha software—early adopters interested in kernel internals rather than a production system.

Hardware requirements were minimal by necessity:

- 386 or later processor
- VGA/EGA display
- AT-style IDE hard disk controller
- PS/2 or serial keyboard

The Finnish keyboard was hard-wired into the assembly code due to Torvalds’ hardware availability at the time. Support for other keyboard layouts required modifying `kernel/keyboard.s`.

A working system required bootstrapping from Minix, since Linux lacked essential support utilities at this stage. The kernel itself was complete, but the ecosystem was nearly empty.

### License and Distribution

The kernel was distributed under terms requiring:

- Full source code availability at no cost
- Intact copyright notices
- No distribution fees of any kind

This preceded the GPL by several years. Most surrounding tools (shells, compilers, libraries) were GNU software under copyleft and distributed separately.

## Technical Design

### Core Architecture Decisions

Linux was developed on Minix but diverged significantly. Key design choices included:

**Traditional system calls, not message passing.** Unlike microkernel designs, Linux used direct syscall invocation. This meant simpler synchronization but required careful handling of concurrent kernel activity.

**Multithreaded filesystem.** The filesystem could handle multiple concurrent requests, unlike Minix’s single-threaded design. This required careful race condition handling through double-checking allocations in `fs/buffer.c` and `fs/inode.c` rather than broad locking.

**Minimal context switches.** Tasks switched only when necessary, not on every operation. This simplified floating-point (387) support and reduced overhead.

**Exposed interrupts.** Device drivers were primarily interrupt handlers, visible and manageable as normal kernel code rather than hidden abstractions.

**Unified kernel address space.** No separation between kernel, filesystem, and memory management subsystems. Code lived in separate directories (`kernel/`, `fs/`, `mm/`) but executed in the same address space, trading modularity for simplicity.

### Memory Management

The memory subsystem was deliberately minimal—just `memory.c` and `page.s`, a few hundred lines total.

The i386 virtual address space (4GB) was divided into 64 segments of 64MB each. The first segment held the kernel with physical memory identity-mapped. User tasks received individual segments.

Paging handled demand loading and copy-on-write for forked processes. The kernel didn’t actively allocate pages—it wrote to user space and let the paging system handle faults reactively. This passivity made memory management simple and robust.

### Filesystem

Linux used the Minix filesystem format for practical compatibility. This enabled cross-compilation from Minix systems and mounting Minix partitions.

The critical difference was implementation: Minix had a single-threaded filesystem, Linux didn’t. Multi-threading brought complexity but enabled concurrent I/O and better process scheduling. Race conditions were addressed by avoiding locks entirely (except during physical device access) and relying on atomic kernel operations when tasks don’t call `sleep()`.

The tradeoff was explicit: no deadlocks possible, but race conditions could occur nearly everywhere and required careful handling.

### Task Structure

A single unified data structure represented all task information rather than scattered control blocks. This simplified scheduling and exception handling.

All faults resulted in exit code 11 (segmentation fault). The system proved relatively stable—the `crashme` stress test hadn’t crashed it yet.

## Building and Installation

Configuration happened in `include/linux/config.h` with hardware-specific defines. The bootloader needed customization in `boot/boot.s` to specify the A-floppy device type.

Building was straightforward:

``` bash
make
```

This produced an `Image` file suitable for copying to a 1.44MB floppy:

``` bash
cp Image /dev/fd0
```

Essential binaries (`bash`, `update`) had to be placed in `/bin` on the root filesystem. The kernel invoked `/bin/sh` at startup, so bash had to be installed with that name.

## Historical Context

This 0.01 release was explicitly a source snapshot for study, not production software. Linus noted the system would change substantially before a 1.0 release and encouraged developers to contact him with questions and bug reports.

The design philosophy was pragmatic: get it working fast, keep it simple, stay powerful enough for Unix software compatibility. Decisions favoring implementation speed over modularity proved sound—the codebase was maintainable and correct.

The fundamental architecture established here persisted through decades of Linux development, despite scaling to support billions of devices and vastly more complex hardware. The core principles of efficient system calls, pageable virtual memory, and interrupt-driven I/O remain central to modern Linux kernels.
