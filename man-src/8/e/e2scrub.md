---
title: "e2scrub(8)"
name: "e2scrub"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2scrub/"
description: "e2scrub – check the contents of a mounted ext[234] file system"
---

<p>e2scrub &#8211; check the contents of a mounted ext[234] file system</p>
<h2>Synopsys</h2>
<p><code>e2scrub [OPTION] MOUNTPOINT | DEVICE</code></p>
<h2>Description</h2>
<p><code>e2scrub</code> attempts to check (but not repair) all metadata in a mounted ext[234] file system if the file system resides on an LVM logical volume. The block device of the LVM logical volume can also be passed in. </p>
<p> This program snapshots the volume and runs a file system check on the snapshot to look for corruption errors. The LVM volume group must have at least 256MiB of unallocated space to dedicate to the snapshot or the logical volume will be skipped. The snapshot will be named <i>lvname</i>.e2scrub and <code>udev</code> will not create symbolic links to it under <i>/dev/disk</i>. Every attempt will be made to remove the snapshots prior to running <code>e2scrub</code>, but in a dire situation it may be necessary to remove the snapshot manually. </p>
<p> If no errors are found, <code>fstrim</code> can be called on the file system if it is mounted. If errors are found, the file system will be marked as having errors. The file system should be taken offline and <code>e2fsck</code> run as soon as possible, because <code>e2scrub</code> does not fix corruptions. If the file system is not repaired, <code>e2fsck</code> will be run before the next mount.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Print what commands <code>e2scrub</code> would execute to check the file system. (Note: the commands will not actually be executed; however, since <code>e2scrub</code> needs to run some commands to query the system to determine what commands would be executed, it still needs to be run as root.)</p>
<dt><code>-r</code></p>
<dd>Remove the e2scrub snapshot and exit without checking anything.</p>
<dt><code>-t</code></p>
<dd>Run <code><a href="/docs/linux/man/1-fstrim/">fstrim</a>(1)</code> on the mounted file system if no errors are found.</p>
<dt><code>-V</code></p>
<dd>Print version information and exit.</dl>
<h2>Exit Code</h2>
<p>The exit codes are the same as in <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8)</p>
<h2>Author</h2>
<p>Darrick J. Wong &lt;darrick.wong [at] oracle.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169;2018 Oracle. License is GPLv2+. &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl-2.0.html">http://www.gnu.org/licenses/gpl-2.0.html</a>&gt;</p>
