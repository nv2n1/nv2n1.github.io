---
title: "xfs_rtcp(8)"
name: "xfs_rtcp"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_rtcp/"
description: "xfs_rtcp – XFS realtime copy command"
---

<p>xfs_rtcp &#8211; XFS realtime copy command</p>
<h2>Synopsis</h2>
<p><code>xfs_rtcp</code> [ <code>-e</code> <i>extsize</i> ] [ <code>-p</code> ] <i>source</i> &#8230; <i>target</i><br />
 <code>xfs_rtcp -V</code></p>
<h2>Description</h2>
<p><code>xfs_rtcp</code> copies a file to the realtime partition on an XFS filesystem. If there is more than one <i>source</i> and <i>target</i>, the final argument (the <i>target</i>) must be a directory which already exists.</p>
<h2>Options</h2>
<dl>
<dt><code>-e</code><i> extsize</i></p>
<dd>Sets the extent size of the destination realtime file.</p>
<dt><code>-p</code></p>
<dd>Use if the size of the source file is not an even multiple of the block size of the destination filesystem. When <code>-p</code> is specified <code>xfs_rtcp</code> will pad the destination file to a size which is an even multiple of the filesystem block size. This is necessary since the realtime file is created using direct I/O and the minimum I/O is the filesystem block size.</p>
<dt><code>-V</code></p>
<dd>Prints the version number and exits.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/8-mkfs-xfs/">mkfs.xfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8).</p>
<h2>Caveats</h2>
<p>Currently, realtime partitions are not supported under the Linux version of XFS, and use of a realtime partition <code>WILL CAUSE CORRUPTION</code> on the data partition. As such, this command is made available for curious <code>DEVELOPERS ONLY</code> at this point in time.</p>
