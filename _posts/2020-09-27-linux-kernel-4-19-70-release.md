---
title: "Linux Kernel 4.19.70 Released"
date: 2020-09-27 12:55:44 +0000
author: "Tony"
layout: post
canonical: https://www.systutorials.com/linux-kernel-4-19-70-release/
---

Linux kernel 4.19.70 is a stable release containing 95 fixes and improvements across multiple subsystems. This release addresses critical issues in audio, networking, storage, virtualization, DMA handling, and various device drivers.

## Major Fixes

### Audio and Sound

**ALSA USB Audio Improvements**

The release includes several USB audio enhancements. A quirk was added for Behringer UFX1604 to apply implicit feedback like the UFX1204 model, fixing noisy playback issues. An invalid NULL pointer check in `snd_emuusb_set_samplerate()` was corrected—the check was occurring after a `container_of()` call which always returns a valid pointer, so the validation was moved earlier in the function.

A critical fix prevents potential concurrent access to deleted audio sequencer pools. The `snd_seq_ioctl_get_client_pool()` function now properly acquires locks before accessing the input pool, preventing crashes when the pool is resized via ioctl while being accessed.

**HDA Codec Fixes**

An inverted logic bug in Conexant GPIO mic mute LED handling was fixed. The “enabled” parameter historically referred to device input/output state, not the LED indicator itself. After LED helper function changes, the logic became inverted, causing the LED to display opposite state. This has been corrected in `cxt_update_gpio_led()`.

### Networking

**TCP and Socket Handling**

A race condition in TCP socket handling was addressed where `EPOLLOUT` events could be missed under memory pressure. The fix ensures `SOCK_NOSPACE` is always set when `-EAGAIN` is returned, regardless of blocking mode status. This mirrors proper behavior in blocking and non-blocking scenarios.

SMC sockets now correctly raise `EPOLLOUT` by setting `SOCK_NOSPACE` on write timeout for both blocking sockets with `SO_SNDTIMEO` and non-blocking sockets, ensuring edge-triggered epoll() mode works reliably.

**IPv4 and IPv6**

A null pointer dereference in `__icmp_send()` was fixed. The `rt->dst.dev` can be NULL with tunnel metadata mode (GRE, etc.), causing crashes. The fix uses `skb->dev` as a fallback when `rt->dst.dev` is unavailable.

IPv6 route type handling now defaults to `RTN_UNICAST` when not explicitly set, restoring pre-4.19 behavior. This fixes issues where routes were installed with type 0 (`RTN_UNSPEC`) instead of unicast, particularly affecting legacy ioctl-based interfaces and netlink tools that don’t require `rtm_type`.

IPv6 multicast address addition is now allowed when the `IFA_F_MCAUTOJOIN` flag is set, fixing a regression where multicast addresses were always rejected in `ipv6_add_addr()` even with the proper flag.

**TLS Socket Issues**

TLS socket closing now properly restores the original `sk_write_space` callback instead of leaving a dangling pointer. When TX mode is disabled, `ctx->sk_write_space` is NULL, so the fix checks if the current pointer is the TLS-specific one before attempting restoration.

A return value bug in `tls_sw_sendmsg()` and `tls_sw_sendpage()` was corrected where `tls_complete_pending_work()` failures were being silently ignored.

### Storage and Block Devices

**NVMe Multipath and Device Handling**

A critical deadlock was fixed that occurred when passthrough commands were sent to multipath devices. The issue involved freezing namespace request queues without freezing the corresponding mpath node queue, causing I/O to block indefinitely. The fix freezes all subsystem namespace head request queues before executing passthrough commands.

NVMe async probe and device removal now synchronize properly, preventing races where a controller in NEW state could fail to transition to DELETING during removal.

The nvme-loop driver now flushes `nvme_delete_wq` when removing ports, ensuring controllers being deleted won’t access freed port memory.

Multipath namespace gendisk revalidation was fixed to actually update visible block device capacity, enabling online filesystem expansion on multipath NVMe devices.

**USB Storage**

Realtek USB storage auto-delink support is now whitelisted for specific device IDs (0x0138, 0x0158, 0x0159) rather than unconditionally enabled, preventing breakage of newer devices. The module parameter documentation was clarified to reflect that `auto_delink_en=false` lets firmware control delink rather than disabling it completely.

A new JMS567 revision (0x0117) was added to the device quirks list due to identical issues as earlier revisions.

### Virtualization and Hypervisor

**KVM Fixes**

ARM VGIC handling was corrected to treat SGI (Software Generated Interrupt) bits in pending registers as write-ignore per ARM specifications.

A potential deadlock in the VGIC was fixed where `merge_final()` in `list_sort()` could cause comparison callbacks to be called with identical elements, deadlocking in `vgic_irq_cmp()` when the active pending list exceeded 256 entries.

PPC Book3S guest-to-user translation error handling was fixed to properly unlock SRCU and rmap locks during early handler exits.

x86 KVM now prevents RIP advancement and single-step injection when instruction emulation faults, fixing infinite loops when invalid `SYSCALL` instructions with `EFLAGS.TF=1` are encountered.

KVM x86 APIC logical destination map population now correctly skips when APIC is not software-enabled, preventing invalid map entries from overwriting valid ones during kdump initialization.

**Xen Hypervisor**

Memory leaks in xen/blkback were fixed by properly cleaning up allocated requests and regions when `xen_blkif_map()` fails during probe.

### DMA and Device Bus

**DMA Handling**

IOMMU DMA scatterlist segment merging was fixed to handle devices with `max_segment_size=UINT_MAX`. Unsigned integer overflow during length checking caused bogus truncated `dma_length` values for merged segments exceeding 4GB.

STM32 MDMA interrupt handler now properly checks for NULL channel pointer before dereferencing it in error messages.

OMAP DMA frame index register handling was corrected—the FI value was incorrectly calculated, missing the “minus 1” required by OMAP TRM specifications. The fix applies to both omap-dma.c and removes the workaround from omap_vout_vrfb.c.

**Device Bus and Control**

HISI LPC bus driver now properly cleans up logical PIO ranges and removes child devices on driver removal, preventing use-after-free crashes and memory leaks.

Logical PIO range registration code was restructured to avoid overlaps when unregistering regions, and proper RCU locking was added around list traversal operations.

### USB Host and Gadget

**USB Host Controller**

OHCI shutdown now properly synchronizes with interrupt handlers by holding spin locks, preventing race conditions where interrupts could re-enable processing after shutdown on certain hardware.

xHCI R-Car controller now properly matches “renesas” (not “renensas”) in compatible strings, fixing coverage for RZ/G1M and RZ/G1N platforms.

XHCI extended capability drivers now work correctly by using managed device resources in PCI probe, ensuring proper resource cleanup order on removal.

Faraday FOTG2 host controller restarts after port reset on Gemini SoC to work around hardware stalling issues.

**USB Gadget**

Mass storage gadget race conditions between `fsg_disable()` and `fsg_set_alt()` were fixed by using a state argument instead of `new_fsg` pointer, ensuring consistency between dequeued state and the observed value.

Composite gadget driver now clears the suspended flag on reset or disconnect, properly handling out-of-suspend transitions with reconnection.

CDC-WDM driver race between write and disconnect was fixed by checking both `WDM_IN_USE` and `WDM_DISCONNECTED` flags in flush() and never clearing `WDM_IN_USE`.

### Cryptography and Security

**Crypto Accelerators**

CCP (AMD Secure Processor) device handling was fixed to check for valid pointer before accessing structure members during suspend/resume when the device is unconfigured.

VMCI doorbell reference counting was corrected to release resources if `schedule_work()` indicates work is already queued, preventing the reference from being held indefinitely.

### Graphics and Display

**Intel i915 Graphics**

DMA segment size is now properly configured to `UINT_MAX` with `dma_set_max_seg_size()`, silencing spurious DMA-API debug warnings on kernels with `CONFIG_DMA_API_DEBUG_SG`.

Broadwell EU computation was fixed—`subslice_mask` is indexed by slice, not subslice.

GGTT deballoon in Linux guest VMs now checks for valid `drm_mm_node` before removal, preventing NULL pointer dereference when unloading the i915 driver.

**AMD GPU**

Dell Latitude 5495 now correctly uses ATPX for dGPU power control instead of `_PR3`, saving approximately 5W when the dGPU is runtime-suspended.

**AST Display Driver**

Standard VGA I/O decode is now disabled during probe to prevent concurrent access from other threads, avoiding system hangs during reboot tests.

**Display Bridges**

TFP410 bridge `get_modes()` now properly frees EDID blob allocated by `drm_get_edid()`, fixing memory leaks.

### Core Kernel and Tracing

**Ftrace and Dynamic Tracing**

Function probe registration now checks for successful hash allocation before dereferencing, preventing NULL pointer issues.

The race between adding function probes and reading existing probes is now documented with appropriate comments, and probes with `EMPTY_HASH` are properly handled.

`t_probe_next()` now safely handles NULL `filter_hash` when probes are being initialized, preventing crashes during filter file reads concurrent with probe registration.

### Kernel Compilation and Build

**Build Fixes**

zsmalloc now builds correctly with `CONFIG_COMPACTION=n` by fixing function call compatibility.

### Perf and Monitoring

**Performance Monitoring**

x86 APIC Local Destination Register (LDR) is now properly cleared during cleanup, fixing destination mapping corruption in 32-bit KVM guests during kdump initialization.

bigsmp APIC mode no longer incorrectly initializes LDR and DFR when physical destination mode is in use, fixing APIC calibration hangs in kdump.

### Debugging and Instrumentation

**Intel Trace Hub**

Tiger Lake Point and additional Lewisburg PCH device IDs are now supported for Intel Trace Hub functionality.

**STM Class**

Double-free in `stm_source_register_device()` error path was fixed by removing unnecessary kfree() call that would duplicate the release from `put_device()`.

### Architecture-Specific Fixes

**x86 Architecture**

Spectre v1 mitigation in ptrace was correctly backported, fixing an incomplete merge from upstream.

32-bit userspace mode detection on 64-bit kernels now uses `user_64bit_mode()` instead of `in_ia32_syscall()`, fixing uretprobe crashes by correctly preserving return addresses.

**ARM64 Architecture**

ARM64 page granule sizes are no longer treated as strict mismatches, allowing systems with heterogeneous CPU granule support (like Amlogic S922X) to boot without kernel taint.

### File Systems

**AFS (Andrew File System)**

`afs_d_revalidate()` no longer unconditionally updates `d_fsdata` without holding locks—it now only updates when the directory version actually changes.

`afs_put_read()` now safely handles NULL `req->pages` before array access, preventing null pointer dereference.

AFS volume location entry parsing now uses the correct index for populating return site arrays, fixing `EDESTADDRREQ` errors.

CB.ProbeUuid RPC handler now replies correctly with empty response for success (not integer 0), preventing fileserver association errors and lost callbacks.

### Device Drivers and Miscellaneous

**Memory Management**

zsmalloc race condition during pool destruction is now properly handled with correct build support.

**I2C Drivers**

Emev2 and R-Car I2C slave support now properly synchronizes interrupt handlers before clearing slave device pointers, preventing races during unregistration.

AMD Family 16h Model 30h SMBus port selection now works correctly by checking PCI revision ID to distinguish between Bolton and Family 16h devices.

**Watchdog**

BCM2835 watchdog module autoloading is restored via proper device alias after MFD migration.

**Display and Audio Support**

MEI (Management Engine Interface) adds Tiger Lake Point device ID support.

**HyperV Tools**

KVP and VSS daemon exit codes are now correct (0 for `--help`), and lsvmbus Python code follows pep8/flake8 style guidelines.

**Miscellaneous Device Support**

Panelboard auxdisplay driver now properly cleans up scan timer when `misc_register()` fails.

SoundWire Cadence master controller register definitions for `INTSTAT0`/`INTSTAT1` and `SLAVE_STATE` are corrected.

## Summary

Linux 4.19.70 represents a focused stable release addressing critical bugs across audio, networking, storage, virtualization, and device driver subsystems. The fixes emphasize proper synchronization, resource cleanup, null pointer safety, and hardware compatibility, making this a recommended update for production systems running the 4.19 LTS branch.
