---
title: "Linux Kernel 5.4.102 Released"
date: 2021-03-07 06:54:22 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-5-4-102-release/
---

This post covers the changes, bugfixes, and new features in Linux kernel 5.4.102. The release includes 338 patches totaling approximately 160,715 lines of changed or added source code compared to the 5.4 baseline.

You can find the source code in the <a href="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/" rel="nofollow noopener" target="_blank">linux-stable tree</a>, or download the <a href="https://www.kernel.org/pub/linux/kernel/v5.x/" rel="nofollow noopener" target="_blank">5.4.102 release package</a> directly. The <a href="https://www.kernel.org/pub/linux/kernel/v5.x/" rel="nofollow noopener" target="_blank">patch bundle</a> is also available for those applying incremental updates.

## Architecture-Specific Fixes

Several architecture-specific issues were addressed:

- **ARM/ARM64**: Added missing ISB after TLB invalidation in `__primary_switch`, fixed uprobe support for AARCH32 instruction probing, corrected PMIC interrupt trigger levels across multiple Exynos and other ARM boards, and extended erratum 1024718 workarounds to all Cortex-A55 versions.
- **PowerPC**: Fixed kuep_lock missing call on syscall entry, addressed software emulation interrupt handling, corrected pseries/dlpar configure-connector delay status, and disabled 256k page size support for 47x processors.
- **SPARC**: Fixed user-triggerable oops in `clear_user()` for SPARC32 and corrected conditional COMPAT_BINFMT_ELF selection for SPARC64.
- **x86**: Forced all CPUs to exit VMX root during reboot if VMX is supported, added missing return in non-void function for seccomp, and improved .cold section suffix checking for newer GCC versions.
- **MIPS**: Properly stopped .eh_frame generation, fixed section mismatch for loongson2_sc_init, and made regulatory range comparisons explicit.

## Networking & Driver Core

Network-layer improvements included fixes for ICMPv6 handling with CONFIG_IPV6=n, netdevice context helpers for NAT’d source addresses, and resolved memory leaks in QRTR tunnel operations. Several driver-specific updates were made:

- **Storage**: Fixed write-beyond-bounds issues in dm-writecache, corrected dm-era metadata handling and bitset memory leaks, resolved btrfs extent buffer leaks, and addressed f2fs attribute handling.
- **Network drivers**: Patched amd-xgbe PHY handling, corrected mvneta queue mapping, fixed axienet deferred probe handling, and resolved bnxt_en TX disable ordering issues.
- **USB**: Fixed error codes in mos7720/mos7840 drivers, corrected dwc3 full-speed interrupt configuration, and resolved dwc2 data length handling and transfer abort logic.

## Device Drivers & Subsystems

### Media & Graphics

DRM fixes included HDMI deep color output correction for DCE 6-11, inverted DCLK polarity in sun4i TCON, and proper handling of mDP connectors in nouveau KMS. Media subsystem patches addressed sampling buffer overflow in ipu3-cio2, mbus code processing in cio2, and multiple memory leaks and error handling issues across vsp1, aspeed, tm6000, and em28xx drivers.

### Filesystems

Notable filesystem fixes:

- **ext4**: Fixed potential htree index checksum corruption.
- **AFFS**: Corrected error path buffer head release.
- **UBIFS**: Fixed memleak in initialization and error return handling.
- **JFFS2**: Resolved use-after-free in summary writing.
- **JFS**: Prevented integer overflow in shift operations.

### Crypto & Security

Addressed BigEndian handling in sun4i-ss, buffer alignment issues in aesni, missing module aliases in arm64/sha, and keyctl failures for trusted key migration. Improved SG buffer length validation in sun4i-ss and fixed kmap usage across multiple crypto drivers.

### Input & HID

Added support for PowerA Enhanced Wired Controller for Xbox Series X\|S and CometLake-H PCI IDs. Fixed wacom touch_max overwrite handling, logitech-dj keyboard event support for eQUAD step 4, and invalid snto32() input detection in HID core.

### Clock, Regulator & Power Management

Fixed APLL calculation on Aspeed AST2600-A2, corrected Alpha PLL type for QCom MSM8998, addressed pm8009 ldo7 regulator issues, and resolved reference count leaks across multiple regulator drivers. Clock and power management patches improved error propagation and register access patterns.

### Memory Management & RCU

Fixed potential double-free in hugetlb_register_node(), corrected pte_unmap handling, improved fastpath for compaction’s migrateblock finding, and resolved RCU deferred wake-up ordering to prevent premature idle checks.

### Tracing & Debugging

Improved perf tools DSO filtering when maps aren’t found, corrected Ampere eMag event naming, and fixed Intel PT processing for CYC and PSB packets. Debugfs became more robust against improper input and premature initialization access.

## Miscellaneous Fixes

Additional patches addressed:

- Potential overflow in mac80211 u32 multiplication
- SO_RCVLOWAT related hangs under memory pressure
- BPF fib_lookup MTU checks for SKB context
- Double-checked variable reading in bpf_lru_list without lock
- Proper resource cleanup in eeprom_93xx46 module aliasing
- HSI PM usage counter balancing
- Xen netback spurious event detection
- Bluetooth resource leaks and race conditions in btusb and hci_uart
- Multiple ACPI property matching and configfs initialization improvements
