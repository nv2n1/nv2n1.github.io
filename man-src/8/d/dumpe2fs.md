---
title: "dumpe2fs(8)"
name: "dumpe2fs"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dumpe2fs/"
description: "dumpe2fs – dump ext2/ext3/ext4 file system information"
---

<p>dumpe2fs &#8211; dump ext2/ext3/ext4 file system information</p>
<h2>Synopsis</h2>
<p><code>dumpe2fs</code> [ <code>-bfghixV</code> ] [ <code>-o superblock=</code><i>superblock</i> ] [ <code>-o blocksize=</code><i>blocksize</i> ] <i>device</i></p>
<h2>Description</h2>
<p><code>dumpe2fs</code> prints the super block and blocks group information for the file system present on <i>device.</i> </p>
<p> <code>Note:</code> When used with a mounted file system, the printed information may be old or inconsistent.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>print the blocks which are reserved as bad in the file system.</p>
<dt><code>-o superblock=</code><i>superblock</i></p>
<dd>use the block <i>superblock</i> when examining the file system. This option is not usually needed except by a file system wizard who is examining the remains of a very badly corrupted file system.</p>
<dt><code>-o blocksize=</code><i>blocksize</i></p>
<dd>use blocks of <i>blocksize</i> bytes when examining the file system. This option is not usually needed except by a file system wizard who is examining the remains of a very badly corrupted file system.</p>
<dt><code>-f</code></p>
<dd>force dumpe2fs to display a file system even though it may have some file system feature flags which dumpe2fs may not understand (and which can cause some of dumpe2fs&#8217;s display to be suspect).</p>
<dt><code>-g</code></p>
<dd>display the group descriptor information in a machine readable colon-separated value format. The fields displayed are the group number; the number of the first block in the group; the superblock location (or -1 if not present); the range of blocks used by the group descriptors (or -1 if not present); the block bitmap location; the inode bitmap location; and the range of blocks used by the inode table.</p>
<dt><code>-h</code></p>
<dd>only display the superblock information and not any of the block group descriptor detail information.</p>
<dt><code>-i</code></p>
<dd>display the file system data from an image file created by <code>e2image</code>, using <i>device</i> as the pathname to the image file.</p>
<dt><code>-m</code></p>
<dd>If the <code>mmp</code> feature is enabled on the file system, check if <i>device</i> is in use by another node, see <code><a href="/docs/linux/man/8-e2mmpstatus/">e2mmpstatus</a></code>(8) for full details. If used together with the <code>-i</code> option, only the MMP block information is printed.</p>
<dt><code>-x</code></p>
<dd>print the detailed group information block numbers in hexadecimal format</p>
<dt><code>-V</code></p>
<dd>print the version number of <code>dumpe2fs</code> and exit.</dl>
<h2>Exit Code</h2>
<p><code>dumpe2fs</code> exits with a return code of 0 if the operation completed without errors. It will exit with a non-zero return code if there are any errors, such as problems reading a valid superblock, bad checksums, or if the device is in use by another node and <code>-m</code> is specified.</p>
<h2>Bugs</h2>
<p>You may need to know the physical file system structure to understand the output.</p>
<h2>Author</h2>
<p><code>dumpe2fs</code> was written by Remy Card &lt;Remy.Card [at] linux.org&gt;. It is currently being maintained by Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;.</p>
<h2>Availability</h2>
<p><code>dumpe2fs</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-e2mmpstatus/">e2mmpstatus</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-tune2fs/">tune2fs</a></code>(8). <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5) </p>
