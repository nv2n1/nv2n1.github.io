---
title: "Linux Kernel 4.9.60: What\u2019s New"
date: 2021-03-07 06:51:12 +0000
modified: 2026-04-11 16:12:51 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-4-9-60-release/
---

The Linux 4.9.60 stable release was published on November 2, 2017, introducing 24 fixes and improvements across 64,224 lines of code changes compared to the 4.9 baseline. This point release addresses critical security vulnerabilities, buffer overrun issues, and device driver fixes that affected several subsystems.

You can find the source code in the <a href="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git/tag/?h=v4.9.60" rel="nofollow noopener" target="_blank">linux-stable tree for 4.9.60</a> or download the <a href="https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.9.60.tar.xz" rel="nofollow noopener" target="_blank">release tarball</a> and <a href="https://www.kernel.org/pub/linux/kernel/v4.x/patch-4.9.60.xz" rel="nofollow noopener" target="_blank">patch file</a> directly from kernel.org.

## Notable Fixes and Changes

### Security Fixes

**assoc_array: Fix node-splitting CVE-2017-12193**

Commit ea6789980fdaa610d7eb63602c746bf6ec70cd2b fixed a critical bug in the generic associative array implementation that could lead to kernel NULL pointer dereference. When adding a new leaf to a full node requiring internal reorganization, the code incorrectly set pointers that would recurse back into the same node rather than linking to the newly created parent node. This manifested as:

    BUG: unable to handle kernel NULL pointer dereference at 0x0000000000000010
    IP: assoc_array_apply_edit+0x59/0xe5

The fix removes buggy special-case code and delegates to the more robust `split_node` path, which correctly handles all tree restructuring scenarios.

**eCryptfs revoked key dereference fix**

The eCryptfs subsystem failed to validate that authentication token keys weren’t revoked before dereferencing their payloads. A revoked key has a NULL payload, and though `request_key()` skips revoked keys, a race window existed where keys could be revoked before acquisition of the key semaphore. The fix adds a NULL payload check in `ecryptfs_get_key_payload_data()` and returns `-EKEYREVOKED` on failure.

### Input Device and HID Fixes

**Input: gtco out-of-bounds access**

The Wacom gtco device driver’s `parse_hid_report_descriptor()` had an insufficient bounds check in its main loop. While checking `i < length` for single-byte reads, the loop body attempted multi-byte reads without verifying sufficient buffer space remained, causing out-of-bounds memory access.

**Input: elan_i2c ACPI table expansion**

Added ELAN0611 device ID to the elan_i2c driver’s ACPI match table to support Lenovo IdeaPad 320-15IKB and IdeaPad 520 touchpads that were previously unrecognized.

**ALSA: hda/realtek ALC236/ALC3204 support**

Added initial codec support for Realtek ALC236 and ALC3204 audio codecs with proper headset microphone mode detection. A subsequent fix specifically addressed Dell laptop models using ALC236 where headset microphone functionality was non-functional.

### Filesystem and Storage Fixes

**fuse: READDIRPLUS entry skipping**

When fuse’s READDIRPLUS implementation encountered a signal interrupting directory enumeration, it incorrectly updated the directory position context after a failed `dir_emit()`, causing the subsequent read to skip one directory entry. The fix ensures context position only advances on successful directory entry emission.

**SCSI sg driver off-by-one**

A previous fix for an off-by-one error in `sg_fill_request_table()` was accidentally reintroduced during code refactoring. This affected the maximum number of SCSI generic requests that could be allocated.

**zfcp storage adapter recovery race**

The zfcp Fibre Channel driver’s error recovery code accessed uninitialized parent pointers in `zfcp_erp_action` structures during recovery trace logging. When fresh zfcp objects were added to parent lists, accessing their erp_action fields before the first recovery enqueue could dereference NULL pointers. The fix initializes all parent pointers immediately upon `zfcp_erp_action` initialization, before the container object becomes externally accessible.

### CAN Bus and Networking

**kvaser_usb message handling**

Two fixes for Kvaser CAN USB adapters:

- Ignore `CMD_FLUSH_QUEUE_REPLY` messages from Leaf v2 firmware (v4.1.844+) that switched queue flushing from asynchronous to synchronous, preventing “Unhandled message (68)” warnings
- Corrected error reporting in `kvaser_usb_flush_queue()` to print the correct return value on failure

**sun4i CAN loopback mode**

Fixed loopback mode operation by setting the correct hardware flag and removing an improper “presume” mode configuration.

**cfg80211 wireless connect/disconnect**

Improved wireless connection state machine handling:

- Prevent connection attempts to a different SSID while already connected or connecting
- Set previous BSSID for reassociation attempts even when the driver supports the connect() callback
- Retain SSID length on connection failures instead of zeroing it, preventing invalid state
- Reset SSID length properly during disconnection unless an explicit disconnected event is expected

### Driver and Subsystem Fixes

**Broadcom QSPI use-after-free**

The bcm_qspi SPI driver had inverted error handling in its probe function that could access device IDs before allocation. An additional error path label (`qspi_resource_err`) now properly sequences cleanup operations.

**fan53555 regulator I2C IDs**

The fan53555 voltage regulator driver used a wildcard I2C device ID (`syr82x`) that prevented udev from properly matching the driver module to actual devices. Corrected the ID table to match device tree descriptions: `syr827` and `syr828`.

**SPI spidev ioctl header**

The spidev user-space interface header was missing an include for `linux/ioctl.h`, causing the `SPI_IOC_MESSAGE()` macro to reference undefined `_IOC_SIZEBITS` when building against musl libc.

**xhci USB host controller**

The xhci driver’s `xhci_stop_device()` function called `xhci_queue_stop_endpoint()` without checking return values, which could fail if the hardware was already halted. This caused indefinite waits for command completion that never occurred, creating deadlock conditions. The fix checks each return value and bails out on error, also preventing command structure memory leaks.

**AMD Radeon powerplay initialization**

An uninitialized `refresh_rate` variable in AMD’s powerplay display gap configuration caused VCE ring test failures during system sleep (S3) on Polaris10 GPUs.

### Other Improvements

**Ceph distributed filesystem**

Fixed a spinlock context imbalance in `try_flush_caps()` where certain code paths exited with the lock still held, potentially causing scheduling under spinlock.

**Xen grant device mapping**

Partial gntdev mmap failures could leave cleanup data uninitialized, leading to out-of-bounds array access during subsequent unmap operations. The fix initializes required unmapping state earlier in the function.

**KVM PPC virtualization**

Fixed a kernel oops when checking `KVM_CAP_PPC_HTM` capability through the global KVM file descriptor, which passed a NULL KVM context to code expecting a valid virtual machine pointer. Now uses the `hv_enabled` fallback consistently.

**Workqueue locking refactor**

Replaced the `pool->manager_arb` mutex with a simple flag (`POOL_MANAGER_ACTIVE`) to eliminate a HARDIRQ-safe to HARDIRQ-unsafe lock ordering violation detected by lockdep. Mutex unlock operations while holding irq spinlocks are inherently unsafe and were creating potential inversion deadlock scenarios.
