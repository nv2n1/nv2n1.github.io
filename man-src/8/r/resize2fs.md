---
title: "resize2fs(8)"
name: "resize2fs"
section: "8"
letter: "r"
url: "/docs/linux/man/8-resize2fs/"
description: "resize2fs – ext2/ext3/ext4 file system resizer"
---

<p>resize2fs &#8211; ext2/ext3/ext4 file system resizer</p>
<h2>Synopsis</h2>
<p><code>resize2fs</code> [ <code>-fFpPMbs</code> ] [ <code>-d</code> <i>debug-flags</i> ] [ <code>-S</code> <i>RAID-stride</i> ] [ <code>-z</code> <i>undo_file</i> ] <i>device</i> [ <i>size</i> ]</p>
<h2>Description</h2>
<p>The <code>resize2fs</code> program will resize ext2, ext3, or ext4 file systems. It can be used to enlarge or shrink an unmounted file system located on <i>device</i>. If the file system is mounted, it can be used to expand the size of the mounted file system, assuming the kernel and the file system supports on-line resizing. (Modern Linux 2.6 kernels will support on-line resize for file systems mounted using ext3 and ext4; ext3 file systems will require the use of file systems with the resize_inode feature enabled.) </p>
<p> The <i>size</i> parameter specifies the requested new size of the file system. If no units are specified, the units of the <i>size</i> parameter shall be the file system blocksize of the file system. Optionally, the <i>size</i> parameter may be suffixed by one of the following units designators: &#8216;K&#8217;, &#8216;M&#8217;, &#8216;G&#8217;, &#8216;T&#8217; (either upper-case or lower-case) or &#8216;s&#8217; for power-of-two kilobytes, megabytes, gigabytes, terabytes or 512 byte sectors respectively. The <i>size</i> of the file system may never be larger than the size of the partition. If <i>size</i> parameter is not specified, it will default to the size of the partition. </p>
<p> The <code>resize2fs</code> program does not manipulate the size of partitions. If you wish to enlarge a file system, you must make sure you can expand the size of the underlying partition first. This can be done using <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) by deleting the partition and recreating it with a larger size or using <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8), if you&#8217;re using the logical volume manager <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8). When recreating the partition, make sure you create it with the same starting disk cylinder as before! Otherwise, the resize operation will certainly not work, and you may lose your entire file system. After running <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), run resize2fs to resize the ext2 file system to use all of the space in the newly enlarged partition. </p>
<p> If you wish to shrink an ext2 partition, first use <code>resize2fs</code> to shrink the size of file system. Then you may use <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8) to shrink the size of the partition. When shrinking the size of the partition, make sure you do not make it smaller than the new size of the ext2 file system! </p>
<p> The <code>-b</code> and <code>-s</code> options enable and disable the 64bit feature, respectively. The resize2fs program will, of course, take care of resizing the block group descriptors and moving other data blocks out of the way, as needed. It is not possible to resize the file system concurrent with changing the 64bit status.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Turns on the 64bit feature, resizes the group descriptors as necessary, and moves other metadata out of the way.</p>
<dt><code>-d </code><i>debug-flags</i></p>
<dd>Turns on various resize2fs debugging features, if they have been compiled into the binary. <i>debug-flags</i> should be computed by adding the numbers of the desired features from the following list:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>2<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211; Debug block relocations</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>4<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211; Debug inode relocations</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>8<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211; Debug moving the inode table</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>16<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211; Print timing information</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>32<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211; Debug minimum file system size (-M) calculation</p>
<dt><code>-f</code></p>
<dd>Forces resize2fs to proceed with the file system resize operation, overriding some safety checks which resize2fs normally enforces.</p>
<dt><code>-F</code></p>
<dd>Flush the file system device&#8217;s buffer caches before beginning. Only really useful for doing <code>resize2fs</code> time trials.</p>
<dt><code>-M</code></p>
<dd>Shrink the file system to minimize its size as much as possible, given the files stored in the file system.</p>
<dt><code>-p</code></p>
<dd>Print out percentage completion bars for each <code>resize2fs</code> phase during an offline (non-trivial) resize operation, so that the user can keep track of what the program is doing. (For very fast resize operations, no progress bars may be displayed.)</p>
<dt><code>-P</code></p>
<dd>Print an estimate of the number of file system blocks in the file system if it is shrunk using <code>resize2fs</code>&#8216;s <code>-M</code> option and then exit.</p>
<dt><code>-s</code></p>
<dd>Turns off the 64bit feature and frees blocks that are no longer in use.</p>
<dt><code>-S </code><i>RAID-stride</i></p>
<dd>The <code>resize2fs</code> program will heuristically determine the RAID stride that was specified when the file system was created. This option allows the user to explicitly specify a RAID stride setting to be used by resize2fs instead.</p>
<dt><code>-z</code><i> undo_file</i></p>
<dd>Before overwriting a file system block, write the old contents of the block to an undo file. This undo file can be used with <a href="/docs/linux/man/8-e2undo/">e2undo</a>(8) to restore the old contents of the file system should something go wrong. If the empty string is passed as the undo_file argument, the undo file will be written to a file named resize2fs-<i>device</i>.e2undo in the directory specified via the <i>E2FSPROGS_UNDO_DIR</i> environment variable. </p>
<p> WARNING: The undo file cannot be used to recover from a power or system crash.</dl>
<h2>Known Bugs</h2>
<p>The minimum size of the file system as estimated by resize2fs may be incorrect, especially for file systems with 1k and 2k blocksizes.</p>
<h2>Author</h2>
<p><code>resize2fs</code> was written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;.</p>
<h2>Copyright</h2>
<p>Resize2fs is Copyright 1998 by Theodore Ts&#8217;o and PowerQuest, Inc. All rights reserved. As of April, 2000 <code>Resize2fs</code> may be redistributed under the terms of the GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-lvextend/">lvextend</a></code>(8) </p>
