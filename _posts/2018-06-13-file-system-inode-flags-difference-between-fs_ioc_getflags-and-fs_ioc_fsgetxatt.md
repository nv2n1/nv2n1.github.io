---
title: "Understanding Linux Inode Flags: FS_IOC_GETFLAGS vs FS_IOC_FSGETXATTR"
date: 2018-06-13 02:21:25 +0000
author: "sameerkhurd"
layout: post
categories: [linux-systems-administration]
canonical: /file-system-inode-flags-difference-between-fs_ioc_getflags-and-fs_ioc_fsgetxatt/
---

Both `FS_IOC_GETFLAGS` and `FS_IOC_FSGETXATTR` retrieve inode attributes, but they differ in scope, design, and what they’re meant to expose. Understanding which to use depends on your filesystem, compatibility requirements, and what metadata you actually need.

## Historical context and design constraints

`FS_IOC_GETFLAGS` originated with ext2/ext3 as a simple interface to query inode flags. It became so widely adopted that other filesystems implemented it to maintain compatibility with `chattr` and `lsattr` tools. The problem: these 32-bit flags serve double duty as both the userspace API and the on-disk encoding in ext2/3/4, making extension difficult. With 31 bits already allocated (one reserved), we’re effectively at capacity.

`FS_IOC_FSGETXATTR` started as an XFS-specific interface but was promoted to a generic filesystem API. It’s structured with explicit padding fields, designed from the ground up to allow future expansion without breaking existing tools.

## What each interface exposes

### FS_IOC_GETFLAGS

Returns a single 32-bit integer encoding binary flags. Common flags include:

- `FS_IMMUTABLE_FL` (0x00000010) — file cannot be modified or deleted
- `FS_APPEND_FL` (0x00000020) — file can only be appended to
- `FS_NODUMP_FL` (0x00000040) — exclude from backups
- `FS_NOATIME_FL` (0x00000080) — don’t update access time
- `FS_DIRSYNC_FL` (0x00010000) — synchronous directory updates
- `FS_ENCRYPT_FL` (0x00000800) — file encryption enabled
- `FS_VERITY_FL` (0x00100000) — fs-verity enabled
- `FS_DAX_FL` (0x01000000) — direct access mode (XFS)
- `FS_CASEFOLD_FL` (0x40000000) — case-insensitive directory
- `FS_NOCOW_FL` (0x00800000) — no copy-on-write (btrfs)

Many of these are filesystem-specific despite being exposed through a generic interface.

### FS_IOC_FSGETXATTR

Returns a structured record with room for future growth:

``` c
struct fsxattr {
    __u32 fsx_xflags;      /* extended flags */
    __u32 fsx_extsize;     /* extent size for data allocation */
    __u32 fsx_nextents;    /* number of extents */
    __u32 fsx_projid;      /* project ID for quota tracking */
    __u32 fsx_cowextsize;  /* copy-on-write extent size */
    unsigned char fsx_pad[8];
};
```

This structure exposes not just flags but also operational metadata: extent configuration, project IDs for quota management, and extent counts. The padding is intentional, allowing kernel developers to add fields without breaking userspace ABI compatibility.

## Key differences in practice

**Flag availability:** `FS_IOC_GETFLAGS` exposes a superset of flags across all filesystems, but not all flags are meaningful on all filesystems. ext4 ignores `FS_DAX_FL`, btrfs ignores `FS_PROJINHERIT_FL`, and so on. `FS_IOC_FSGETXATTR` is more conservative—it exposes flags and metadata that are actually relevant to the underlying filesystem.

**Extent and quota data:** Only `FS_IOC_FSGETXATTR` provides extent sizing and project ID information. If you need to understand how a file is allocated or check its project quota assignment, you need this call.

**Backward compatibility:** Older tools expect `FS_IOC_GETFLAGS`. If your environment uses legacy scripts relying on `chattr` and `lsattr`, you may need to support it even on modern systems.

**Future extensibility:** `FS_IOC_GETFLAGS` is effectively out of bits. New functionality goes into `FS_IOC_FSGETXATTR` or new specialized ioctl calls. The kernel team made a deliberate choice to move forward with structured APIs rather than bit-packing.

## When to use each

**Use `FS_IOC_GETFLAGS` for:**

- Checking immutability or append-only status on any filesystem
- Maintaining compatibility with existing `chattr`/`lsattr` workflows
- Simple flag queries where you don’t need extent or quota metadata
- Legacy system administration scripts

**Use `FS_IOC_FSGETXATTR` for:**

- New applications or tools you’re building
- Working with XFS and needing extent sizing or project ID information
- Quota management scenarios
- Future-proof code that doesn’t require backward compatibility with older userspace tools

## Usage examples

Check flags with `FS_IOC_GETFLAGS`:

``` bash
lsattr /path/to/file
```

Set immutable flag:

``` bash
chattr +i /path/to/file
```

Query with `FS_IOC_FSGETXATTR`:

``` bash
xfs_io -c stat /path/to/file
```

Programmatic query in C:

``` c
#include <sys/ioctl.h>
#include <linux/fs.h>

struct fsxattr attr;
if (ioctl(fd, FS_IOC_FSGETXATTR, &attr) < 0) {
    perror("ioctl");
    return -1;
}
printf("Flags: 0x%x, Project ID: %u\n", attr.fsx_xflags, attr.fsx_projid);
```

For `FS_IOC_GETFLAGS`:

``` c
unsigned int flags;
if (ioctl(fd, FS_IOC_GETFLAGS, &flags) < 0) {
    perror("ioctl");
    return -1;
}
printf("Flags: 0x%x\n", flags);
```

## Recommendation

For new development and modern systems, prefer `FS_IOC_FSGETXATTR`. It’s the direction the kernel is moving, it provides richer metadata, and it won’t force you into API dead ends as filesystems evolve. Use `FS_IOC_GETFLAGS` only when you have explicit compatibility requirements or are working in constrained environments that can’t use newer interfaces.
