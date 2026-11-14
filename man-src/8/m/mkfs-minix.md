---
title: "mkfs-minix(8)"
name: "mkfs-minix"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-minix/"
description: "mkfs.minix – make a Minix filesystem"
---

<p>mkfs.minix &#8211; make a Minix filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.minix</code> [options] <i>device</i> [<i>size-in-blocks</i>]</p>
<h2>Description</h2>
<p><code>mkfs.minix</code> creates a Linux MINIX filesystem on a device (usually a disk partition). </p>
<p> The <i>device</i> is usually of the following form: </p>
<dl>
<dd>
<pre>/dev/hda[1-8] (IDE disk 1)
/dev/hdb[1-8] (IDE disk 2)
/dev/sda[1-8] (SCSI disk 1)
/dev/sdb[1-8] (SCSI disk 2)</pre>
</dl>
<p> The device may be a block device or an image file of one, but this is not enforced. Expect not much fun on a character device :-). </p>
<p> The <i>size-in-blocks</i> parameter is the desired size of the file system, in blocks. It is present only for backwards compatibility. If omitted the size will be determined automatically. Only block counts strictly greater than 10 and strictly less than 65536 are allowed.</p>
<h2>Options</h2>
<p><code>-c</code>, <code>&#8211;check</code></p>
<dl>
<dd>Check the device for bad blocks before creating the filesystem. If any are found, the count is printed.</dl>
<p> <code>-n</code>, <code>&#8211;namelength</code> <i>length</i></p>
<dl>
<dd>Specify the maximum length of filenames. Currently, the only allowable values are 14 and 30 for file system versions 1 and 2. Version 3 allows only value 60. The default is 30.</dl>
<p> <code>&#8211;lock</code>[=<i>mode</i>]</p>
<dl>
<dd>Use exclusive BSD lock for device or file it operates. The optional argument <i>mode</i> can be <code>yes</code>, <code>no</code> (or 1 and 0) or <code>nonblock</code>. If the <i>mode</i> argument is omitted, it defaults to <code>&quot;yes&quot;</code>. This option overwrites environment variable <code>$LOCK_BLOCK_DEVICE</code>. The default is not to use any lock at all, but it&#8217;s recommended to avoid collisions with udevd or other tools.</dl>
<p> <code>-i</code>, <code>&#8211;inodes</code> <i>number</i></p>
<dl>
<dd>Specify the number of inodes for the filesystem.</dl>
<p> <code>-l</code>, <code>&#8211;badblocks</code> <i>filename</i></p>
<dl>
<dd>Read the list of bad blocks from <i>filename</i>. The file has one bad-block number per line. The count of bad blocks read is printed.</dl>
<p> <code>-1</code></p>
<dl>
<dd>Make a Minix version 1 filesystem. This is the default.</dl>
<p> <code>-2</code>, <code>-v</code></p>
<dl>
<dd>Make a Minix version 2 filesystem.</dl>
<p> <code>-3</code></p>
<dl>
<dd>Make a Minix version 3 filesystem.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit. The long option cannot be combined with other options.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Environment</h2>
<p>LOCK_BLOCK_DEVICE=&lt;mode&gt;</p>
<dl>
<dd>use exclusive BSD lock. The mode is &quot;1&quot; or &quot;0&quot;. See <code>&#8211;lock</code> for more details.</dl>
<h2>Exit Status</h2>
<p>The exit status returned by <code>mkfs.minix</code> is one of the following: </p>
<p> 0</p>
<dl>
<dd>No errors</dl>
<p> 8</p>
<dl>
<dd>Operational error</dl>
<p> 16</p>
<dl>
<dd>Usage or syntax error</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mkfs.minix</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
