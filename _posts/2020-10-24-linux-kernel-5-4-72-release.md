---
title: "Linux 5.4.72 Kernel Release Notes"
date: 2020-10-24 14:29:21 +0000
layout: post
canonical: https://www.systutorials.com/linux-kernel-5-4-72-release/
---

Linux 5.4.72 is a stable kernel update containing 23 commits and approximately 126,508 lines of code changes compared to the base 5.4 release. This release focuses on critical security and stability fixes across cryptography, filesystem, USB, Bluetooth, and architecture-specific code paths.

## Cryptography and Security Fixes

### QAT cipher validation

Added length validation for AEAD AES-CBC-HMAC operations in the Intel QuickAssist Technology driver. The fix returns `EINVAL` for `authenc(hmac(sha1),cbc(aes))`, `authenc(hmac(sha256),cbc(aes))`, and `authenc(hmac(sha512),cbc(aes))` when the cipher length is not a multiple of the AES block size. This prevents undefined device behavior on malformed input.

### Broadcom SPU crypto validation

The Broadcom SPU driver’s GCM/CCM setkey function now properly validates key length before copying and salt manipulation. The fix ensures the key is at least as long as the salt, preventing buffer overflows and crashes from crafted input.

### Bluetooth encryption security

Bluetooth connections now disconnect if E0 encryption is negotiated for Level 4 security requirements. Per the Bluetooth 5.2 specification, Level 4 requires FIPS-approved algorithms only; E0 is explicitly disallowed. The kernel now enforces this requirement and terminates the connection if a remote device attempts E0 encryption at this level.

## Filesystem Fixes

### ReiserFS crash prevention

Two critical reiserfs fixes address crashes during mount operations with specially crafted filesystem images:

- Fixed an oops when reiserfs attempts to verify XATTR_ROOT directory lookup. The xattr code would recurse back during ACL permission checks, causing a crash. The fix bails from `reiserfs_xattr_get()` if xattrs are not yet initialized.
- Fixed improper inode key initialization in `reiserfs_read_locked_inode()`. The code now uses the `_make_cpu_key()` macro to properly initialize all key members, preventing uninitialized memory access.

## USB and Device Support

### USB serial driver updates

Several USB device ID additions improve hardware compatibility:

- **ftdi_sio**: Added support for FreeCalypso JTAG+UART adapters based on FT2232, allowing proper ttyUSB device creation for Channel B while preventing bogus device creation for JTAG channel A.
- **pl2303**: Added support for HP LD381 devices using the pl2303GC chipset.
- **option**: Added Telit FT980-KS device composition (0x1054) with rndis, diag, adb, nmea, and dual modem channels.
- **option**: Added Cellient MPL200 card device IDs.

### USB endpoint validation

The staging comedi driver now validates the `wMaxPacketSize` field of discovered USB endpoints. A value of 0 is rejected as invalid, preventing potential issues with devices that incorrectly report zero-sized endpoints.

### Media device refcounting

Fixed incorrect refcounting logic in the usbtv driver that could cause premature device freeing. The fix properly distinguishes between V4L and USB refcounting in error handling paths.

## Bluetooth Subsystem Improvements

### Connection state management

Fixed a regression in `hci_encrypt_cfm()` that caused incorrect connection state updates. The condition for updating connection state was inverted—the status should be updated only when no status is currently set. This fixes connection state flapping issues reported with Bluetooth headsets.

### Encryption handling consolidation

The `hci_encrypt_cfm()` function now consolidates encryption handling by calling `hci_connect_cfm()` when the connection state is `BT_CONFIG`, simplifying caller logic.

### L2CAP channel filtering

L2CAP channels that aren’t socket-based (such as A2MP channels) no longer invoke `sk_filter()`, which would crash due to accessing invalid socket pointers. A new callback mechanism allows channels to implement their own filtering logic if needed.

### A2MP protocol fixes

Fixed uninitialized stack variables in A2MP protocol handlers that could cause unpredictable behavior with AMP controller management messages.

### Bluetooth settings validation

The MGMT subsystem now correctly checks if `BT_HS` (Bluetooth High Speed) is enabled before reporting it as supported, preventing exposure of unsupported features to userspace.

## Architecture and Build Fixes

### ARM build tooling

The ARM architecture now uses the proper `$(NM)` variable instead of hardcoded `$(CROSS_COMPILE)nm`, enabling builds with alternative toolchains like LLVM’s llvm-nm. This fixes build failures when the nm executable is explicitly overridden.

### ACPI event device

The ACPI Generic Event Device (GED) driver is now always built in rather than conditionally compiled for reduced hardware platforms. This allows dynamic detection of hardware-reduced platforms on systems supporting both fixed and reduced ACPI modes.

## Storage and Filesystem Management

### Btrfs block group read-only handling

Fixed `inc_block_group_ro()` to account for metadata overcommit when determining if a block group can be marked read-only. The previous logic only worked for data; metadata would almost always fail the check due to intentional overcommitment. The fix exports `btrfs_can_overcommit()` and checks if sufficient space exists to absorb the block group’s remaining free space.

### Btrfs space calculation

Simplified space overcommit checks by removing the unnecessary `system_chunk` parameter from `can_overcommit()`. The function can determine space info type directly from flags, reducing complexity and potential bugs.

## Performance Analysis Tools

### Perf cs-etm variable scoping

Moved the `traceid_list` global variable definition from the header file cs-etm.h to cs-etm.c. Multiple inclusions of the header file could trigger compiler warnings or errors about multiple definitions. This follows proper C practices for global variable scope.

## Building and Testing

To build kernel 5.4.72, download the source from the Linux kernel repository or linux-stable tree. The release was tested by the Linux Kernel Functional Testing (LKFT) project, Nvidia, and other kernel maintainers.

For production deployments, verify that your hardware and drivers are compatible with this release and test thoroughly in non-critical environments before rolling out system-wide.
