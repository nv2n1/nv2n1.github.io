---
title: "fsck-xfs(8)"
name: "fsck-xfs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-xfs/"
description: "fsck.xfs – do nothing, successfully"
---

<p>fsck.xfs &#8211; do nothing, successfully</p>
<h2>Synopsis</h2>
<p><code>fsck.xfs</code> [ <i>filesys</i> &#8230; ]</p>
<h2>Description</h2>
<p><code>fsck.xfs</code> is called by the generic Linux <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8) program at startup to check and repair an XFS filesystem. XFS is a journaling filesystem and performs recovery at <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) time if necessary, so <code>fsck.xfs</code> simply exits with a zero exit status. </p>
<p> If you wish to check the consistency of an XFS filesystem, or repair a damaged or corrupt XFS filesystem, see <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8). </p>
<p> However, the system administrator can force <code>fsck.xfs</code> to run <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8) at boot time by creating a /forcefsck file or booting the system with &quot;fsck.mode=force&quot; on the kernel command line.</p>
<h2>Files</h2>
<p><i>/etc/fstab</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-xfs_repair/">xfs_repair</a></code>(8). </p>
