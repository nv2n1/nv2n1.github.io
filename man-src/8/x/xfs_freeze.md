---
title: "xfs_freeze(8)"
name: "xfs_freeze"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_freeze/"
description: "xfs_freeze – suspend access to an XFS filesystem"
---

<p>xfs_freeze &#8211; suspend access to an XFS filesystem</p>
<h2>Synopsis</h2>
<p><code>xfs_freeze</code> [ <code>-f</code> | <code>-u</code> ] <i>mount-point</i><br />
 <code>xfs_freeze -V</code></p>
<h2>Description</h2>
<p><code>xfs_freeze</code> suspends and resumes access to an XFS filesystem (see <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5)). </p>
<p> <code>xfs_freeze</code> halts new access to the filesystem and creates a stable image on disk. <code>xfs_freeze</code> is intended to be used with volume managers and hardware RAID devices that support the creation of snapshots. </p>
<p> The <i>mount-point</i> argument is the pathname of the directory where the filesystem is mounted. The filesystem must be mounted to be frozen (see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)). </p>
<p> The <code>-f</code> flag requests the specified XFS filesystem to be frozen from new modifications. When this is selected, all ongoing transactions in the filesystem are allowed to complete, new write system calls are halted, other calls which modify the filesystem are halted, and all dirty data, metadata, and log information are written to disk. Any process attempting to write to the frozen filesystem will block waiting for the filesystem to be unfrozen. </p>
<p> Note that even after freezing, the on-disk filesystem can contain information on files that are still in the process of unlinking. These files will not be unlinked until the filesystem is unfrozen or a clean mount of the snapshot is complete. </p>
<p> The <code>-u</code> flag is used to un-freeze the filesystem and allow operations to continue. Any filesystem modifications that were blocked by the freeze are unblocked and allowed to complete. </p>
<p> The <code>-V</code> flag prints the version number and exits. </p>
<p> Unless <code>-V</code> is specified, one of <code>-f</code> or <code>-u</code> must be supplied to <code>xfs_freeze</code>.</p>
<h2>Notes</h2>
<p>A copy of a frozen XFS filesystem will usually have the same universally unique identifier (UUID) as the original, and thus may be prevented from being mounted. The XFS <code>nouuid</code> mount option can be used to circumvent this issue. </p>
<p> In Linux kernel version 2.6.29, the interface which XFS uses to freeze and unfreeze was elevated to the VFS, so that this tool can now be used on many other Linux filesystems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
