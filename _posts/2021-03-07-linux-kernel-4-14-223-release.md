---
title: "Linux Kernel 4.14.223 Released"
date: 2021-03-07 07:04:37 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-4-14-223-release/
---

Linux kernel 4.14.223 is a stable release in the long-term support (LTS) 4.14 series. This patch version includes 176 changes and bug fixes across 277,921 lines of code modifications compared to the base 4.14 release.

## Where to Get the Code

The source code is available from the <a href="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git" rel="nofollow noopener" target="_blank">linux-stable tree</a> with the `linux-4.14.223` tag. You can download the release tarball or the patch directly from <a href="https://www.kernel.org/releases.html" rel="nofollow noopener" target="_blank">kernel.org</a>.

To apply the patch to your 4.14 kernel:

``` bash
cd linux-4.14.y
patch -p1 < patch-4.14.223.gz
```

## Major Changes and Fixes

### Device Mapper and Storage

- **dm era**: Fixed multiple memory leaks, bitset handling, and crash recovery in the era target
- **dm era**: Corrected metadata resizing to only occur during preresume, preventing premature operations
- **btrfs**: Fixed extent buffer and reloc root leaks; improved error handling in copy operations
- **ext4**: Resolved potential htree index checksum corruption

### Networking and IP Stack

- **ICMP**: Introduced `icmp_ndo_send()` helper for proper source address handling in network device context, used across multiple drivers (sunvnet, gtp)
- **IPv6**: Fixed compilation warnings in non-IPv6 builds and optimized icmpv6_send() to avoid indirect calls
- **mlx4_core**: Added missing cleanup call in mailbox handling
- **i40e**: Fixed flow control settings overwriting during driver load; corrected IPv6 extension header processing
- **mvneta**: Removed per-CPU queue mapping for Armada 3700 to fix performance issues
- **amd-xgbe**: Reset link handling when connection fails; added PHY rx data path reset on mailbox timeout
- **bnxt_en**: Corrected TX disable and carrier off ordering

### File Systems

- **gfs2**: Fixed glock unlock handling when lvb is present
- **ocfs2**: Fixed use-after-free on error paths
- **isofs**: Improved buffer head release on error conditions
- **jffs2**: Fixed use-after-free in summary write operations
- **jfs**: Prevented potential integer overflow on bit shifts

### Memory Management

- **hugetlb**: Fixed race condition between page freeing and dissolution; resolved potential double-free in error paths
- **mm/rmap**: Fixed potential pte_unmap issue on unmapped pages

### USB and HID

- **dwc3**: Fixed DEPCFG.bInterval_m1 and dep-\>interval configuration for gadget mode
- **musb**: Fixed runtime PM race condition in queue_resume_work
- **dwc2**: Corrected xfer length handling; abort transactions on unknown errors
- **renesas_usbhs**: Cleared pipe running flag in packet pop
- **wacom HID**: Fixed touch_max value override attempts
- **option serial**: Updated device interface mapping for ZTE P685M

### Security and Crypto

- **seccomp**: Added missing return statement in non-void function
- **crypto/bcm**: Renamed conflicting device_private struct to bcm_device_private
- **crypto/sun4i-ss**: Fixed BigEndian cipher handling and improved sg length checking
- **KEYS/trusted**: Fixed migratable key handling
- **tpm_tis**: Corrected locality acquisition check

### Interrupt and Exceptions

- **sparc32**: Fixed user-triggerable oops in clear_user()
- **arm64/uprobe**: Returned EOPNOTSUPP for AARCH32 instruction probing attempts
- **printk**: Fixed deadlock when kernel panic occurs
- **gpio/pcf857x**: Fixed missing first interrupt handling

### Platform and Architecture

- **x86/reboot**: Force all CPUs to exit VMX root if VMX is supported
- **powerpc/8xx**: Fixed software emulation interrupt handling
- **powerpc/47x**: Disabled 256k page size due to compatibility issues
- **ARM/ARMv7**: Fixed decompressor SCTLR.nTLSMD handling
- **ARM/tegra**: Added power-domain for Tegra210 HDA

### Input Devices

- **i8042**: Added ASUS Zenbook Flip to noselftest list
- **xpad**: Added support for PowerA Enhanced Wired Controller for Xbox Series X\|S
- **joydev**: Prevented read overflow in ioctl handler
- **raydium_ts_i2c**: Fixed zero-length packet sending

### Watchdog and RTC

- **watchdog/mei_wdt**: Request stop on unregister to prevent hangs
- **rtc/s5m**: Selected required REGMAP_I2C dependency

### Resource Management and Error Handling

Numerous fixes throughout the kernel for resource leaks, use-after-free conditions, and proper error path cleanup in drivers across:

- Bluetooth subsystem (HCI device reference handling)
- USB gadget framework (audio request cleanup)
- ALSA audio (codec probe error handling)
- Media drivers (vsp1, tm6000, cx25821, qm1d1c0042)
- EEPROM drivers (module alias and autoprobe)
- DMA engines (hsu, fsldma resource leaks)
- Various architecture-specific code

### Security and Capability Handling

- **capabilities**: Prevented writing ambiguous v3 file capabilities
- **ima**: Fixed measurement buffer leaks on error and kexec syscall

## Stable Branch Information

4.14.223 is part of the 4.14 LTS series, which receives backported security and critical stability fixes. For production systems, verify your kernel configuration matches your workload requirements before updating. Test updates in staging environments first, particularly for storage, networking, and security-sensitive subsystems affected by these changes.
