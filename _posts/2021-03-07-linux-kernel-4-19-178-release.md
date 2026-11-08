---
title: "Linux Kernel 4.19.178 Released"
date: 2021-03-07 07:05:42 +0000
modified: 2026-04-11 16:12:47 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-4-19-178-release/
---

Linux kernel 4.19.178 is a stable release from the 4.19 LTS series, containing 248 patches addressing security fixes, memory leaks, and driver corrections. This release modified approximately 239,909 lines of source code compared to the base 4.19 release.

## Device Tree and Architecture Fixes

Several ARM and ARM64 device tree updates improve hardware support and thermal management:

- ARM Cortex-A55 erratum 1024718 workaround extended to all versions
- ARM64 TLB invalidation now includes proper instruction barriers via ISB after invalidating TLB in \_\_primary_switch
- Thermal interrupt configuration added for OMAP 4430
- Allwinner A64 MMC2 bus frequency limited to 150 MHz for stability
- Samsung Exynos platforms corrected PMIC interrupt trigger levels
- ARM Cortex-A55 uprobe probing returns EOPNOTSUPP for AARCH32 instructions

## Memory and Buffer Management

Several fixes address potential use-after-free and memory leak conditions:

- dm era metadata handling corrected to prevent bitset memory leaks and verify data block size consistency
- Hugetlb copy operations fixed to avoid double-free in error paths
- JFS potential integer overflow on shift operations corrected
- jffs2 use-after-free eliminated in sum_write_data()
- Buffer head reference counting fixed in isofs and affs filesystems
- Various DMA driver resource leaks plugged in error handling paths

## Network and Protocol Fixes

Network stack improvements focus on ICMP handling and device-specific corrections:

- ICMP helpers introduced for NAT’d source addresses in network device context
- GTP, sunvnet, and xfrm interface drivers now use icmp_ndo_send helper
- IPv6 ICMP compilation warning silenced for non-IPV6 builds
- TCP SO_RCVLOWAT hangs under memory pressure resolved
- BPF fib_lookup helper MTU check corrected for SKB context
- amd-xgbe link reset added when link never comes back
- mvneta per-cpu queue mapping removed for Armada 3700
- ibmvnic memory barrier protection added for long-term buffers

## Driver Updates

Multiple driver categories receive targeted fixes:

**USB**: DWC3 gadget interval configuration corrected for fullspeed interrupts and DEPCFG handling; musb runtime PM race condition fixed; serial drivers (mos7720, mos7840, ftdi_sio) corrected error codes

**Storage**: AHCI Broadcom regulator management restored; ext4 htree index checksum corruption fixed; f2fs attribute corruption prevented

**Input Devices**: Raydium touchscreen zero-length transfers blocked; ASUS Zenbook Flip added to i8042 noselftest list; PowerA Enhanced controller support added

**Media**: UVC video now accepts invalid bFormatIndex/bFrameIndex values; CX25821 DMA reallocation memleak fixed; VSP1 error handling improved

**Wireless**: ath9k debugfs nf_override data bus crash fixed; ath10k CE pipe init error handling improved; b43 N-PHY coef update fixed for revision \>= 3

## Security and Cryptography

- Blacklist flag type confusion in certs module corrected
- TPM_TIS locality acquisition and cleanup improved
- KEYS trusted module migratable=1 failure resolved
- ECDH helper enforces len \>= secret.len in decode_key()
- Seccomp missing return statement added

## Filesystem and I/O

- Ext4 htree index checksum corruption prevented
- F2fs inconsistent quota data fixed
- NTFS validates standard information attributes
- SEQ_FILE per-entry resource management documented
- Pat/memtype seq_file iteration fixed
- JFFS2 use-after-free in sum operations eliminated

## Tracing and Debugging

- Kernel panic deadlock in printk resolved
- Tracepoint unregistration no longer fails on memory allocation errors
- Perf DSO filtering corrected when map not found for sampled address
- Perf intel-pt missing CYC processing in PSB fixed

## System and Core Changes

- Capabilities write protection prevents ambiguous v3 file capabilities
- Static key false positive warnings on concurrent dec/inc eliminated
- Hotplug lock assertions added for cpuslocked() operations
- Dwarf v5 sections added to vmlinux.lds.h
- Module symbol table ignores \_GLOBAL_OFFSETTABLE for undefined symbol warnings
- KDB memory allocations hardened for robustness

For complete details on all 248 patches, consult the linux-stable repository’s 4.19.178 tag or download the full patchset directly.
