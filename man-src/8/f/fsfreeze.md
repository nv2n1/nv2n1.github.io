---
title: "fsfreeze(8)"
name: "fsfreeze"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsfreeze/"
description: "fsfreeze – suspend access to a filesystem (Ext3/4, ReiserFS, JFS, XFS)"
---

<p>fsfreeze &#8211; suspend access to a filesystem (Ext3/4, ReiserFS, JFS, XFS)</p>
<h2>Synopsis</h2>
<p><code>fsfreeze</code> <code>&#8211;freeze</code>|<code>&#8211;unfreeze</code> <i>mountpoint</i></p>
<h2>Description</h2>
<p><code>fsfreeze</code> suspends or resumes access to a filesystem. </p>
<p> <code>fsfreeze</code> halts any new access to the filesystem and creates a stable image on disk. <code>fsfreeze</code> is intended to be used with hardware RAID devices that support the creation of snapshots. </p>
<p> <code>fsfreeze</code> is unnecessary for <code>device-mapper</code> devices. The device-mapper (and LVM) automatically freezes a filesystem on the device when a snapshot creation is requested. For more details see the <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) man page. </p>
<p> The <i>mountpoint</i> argument is the pathname of the directory where the filesystem is mounted. The filesystem must be mounted to be frozen (see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)). </p>
<p> Note that access-time updates are also suspended if the filesystem is mounted with the traditional atime behavior (mount option <code>strictatime</code>, for more details see <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)).</p>
<h2>Options</h2>
<p><code>-f</code>, <code>&#8211;freeze</code></p>
<dl>
<dd>This option requests the specified a filesystem to be frozen from new modifications. When this is selected, all ongoing transactions in the filesystem are allowed to complete, new write system calls are halted, other calls which modify the filesystem are halted, and all dirty data, metadata, and log information are written to disk. Any process attempting to write to the frozen filesystem will block waiting for the filesystem to be unfrozen. </p>
<p> Note that even after freezing, the on-disk filesystem can contain information on files that are still in the process of unlinking. These files will not be unlinked until the filesystem is unfrozen or a clean mount of the snapshot is complete.</dl>
<p> <code>-u</code>, <code>&#8211;unfreeze</code></p>
<dl>
<dd>This option is used to un-freeze the filesystem and allow operations to continue. Any filesystem modifications that were blocked by the freeze are unblocked and allowed to complete.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Filesystem Support</h2>
<p>This command will work only if filesystem supports has support for freezing. List of these filesystems include (2016-12-18) <code>btrfs</code>, <code>ext2/3/4</code>, <code>f2fs</code>, <code>jfs</code>, <code>nilfs2</code>, <code>reiserfs</code>, and <code>xfs</code>. Previous list may be incomplete, as more filesystems get support. If in doubt easiest way to know if a filesystem has support is create a small loopback mount and test freezing it.</p>
<h2>Notes</h2>
<p>This man page is based on <code><a href="/docs/linux/man/8-xfs_freeze/">xfs_freeze</a></code>(8).</p>
<h2>Authors</h2>
<p>Written by Hajime Taira.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fsfreeze</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
