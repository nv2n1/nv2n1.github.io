---
title: "Linux v0.97 Release Notes"
date: 2020-10-25 09:09:21 +0000
author: "Tony"
layout: post
canonical: https://www.systutorials.com/release-notes-for-linux-v0-97/
---

This document preserves the original release notes for Linux kernel v0.97, an early milestone in kernel development that demonstrates the rapid evolution of core subsystems in the 1990s. The content below has been reformatted from the original ASCII release notes for readability while maintaining historical accuracy.

## Changes in 0.97

**Display and graphics support**

VESA support was removed pending more comprehensive hardware validation. In its place, automatic SVGA setup patches were integrated—see the top-level Makefile for configuration details.

**IRQ handling**

The IRQ code reached a stable state and was validated across multiple machine architectures. However, not all SCSI drivers had been updated to use the new IRQ infrastructure yet, leaving room for driver-level patches.

**Serial interrupt performance**

Serial interrupt handling received optimization work, with measurable performance improvements validated through alpha testing cycles. Testing feedback ranged from positive to enthusiastic.

**Buffer cache and memory management**

Significant changes to the buffer cache and VM subsystem required updates to userspace tools. Programs like `ps` and `free` that read kernel memory directly could no longer function without source-level modifications. The kernel’s internal data structures had shifted enough that recompilation alone wouldn’t suffice.

The buffer cache now dynamically expands and contracts based on available free memory—a significant improvement over fixed allocation. Memory statistics became accessible via Shift+PrintScreen (with Ctrl+PrSc showing task information and Alt+PrSc displaying register contents).

VM code improvements eliminated several race conditions and refined out-of-memory handling through better thrashing detection. These changes made low-memory conditions less catastrophic overall.

**Filesystem superblock reorganization**

Superblock code underwent cleanup, particularly affecting the ext filesystem, which required updates to take advantage of the new layout. Further ext-specific patches were anticipated from the ext development team.

**Header file cleanup**

Include files were reorganized to reduce namespace collisions with standard C library headers, though some conflicts remained unresolved.

**Process swapping changes**

Unswappable processes were implemented, with only `init` marked as unswappable by default. This protected against low-memory situations where critical system processes could be paged out. The `init` process was also made signal-proof—unrecognized signals would simply be dropped rather than acting on them. Additional protections prevented unprivileged users from triggering machine-killing fork bombs.

**SCSI driver updates**

New SCSI drivers were integrated, increasing kernel size but made optional via configuration.

**Disk error reporting**

Floppy and hard drive drivers now produced detailed debugging output on errors, which could be verbose on reliable hardware but proved invaluable for diagnosing soft errors. Simultaneously, some older debugging output—particularly for user-mode protection violations—was removed to reduce noise.

**Minor fixes and remaining work**

Various smaller bug fixes were applied. No change diffs were generated, as the cumulative changes were substantial.

## Deferred work

**TTY driver redesign**

A more comprehensive rewrite of TTY drivers inspired by Unix streams concepts was planned but deferred due to competing priorities.

**Patch integration**

Many patches were submitted; some were merged while others were deferred. Contributors whose patches weren’t included were encouraged to resubmit against v0.97.

## Notes

The dynamic buffer code supported variable-sized buffers, but the broader system—block device drivers, filesystem implementations, and related subsystems—couldn’t yet leverage this capability. Additional development work was needed to fully capitalize on the new infrastructure.

The author solicited feedback on system performance, code clarity, and stability. While v0.97 aimed to resolve all known bugs, that goal remained aspirational rather than guaranteed.
