---
title: "fsck-minix(8)"
name: "fsck-minix"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-minix/"
description: "fsck.minix – check consistency of Minix filesystem"
---

<p>fsck.minix &#8211; check consistency of Minix filesystem</p>
<h2>Synopsis</h2>
<p><code>fsck.minix</code> [options] <i>device</i></p>
<h2>Description</h2>
<p><code>fsck.minix</code> performs a consistency check for the Linux MINIX filesystem. The program assumes the filesystem is quiescent. <code>fsck.minix</code> should not be used on a mounted device unless you can be sure nobody is writing to it. Remember that the kernel can write to device when it searches for files. The <i>device</i> name will usually have the following form:</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td> /dev/hda[1-63] </td>
<td> IDE disk 1
</td>
</tr>
<tr VALIGN=top>
<td> /dev/hdb[1-63] </td>
<td> IDE disk 2
</td>
</tr>
<tr VALIGN=top>
<td> /dev/sda[1-15] </td>
<td> SCSI disk 1
</td>
</tr>
<tr VALIGN=top>
<td> /dev/sdb[1-15] </td>
<td> SCSI disk 2
</td>
</tr>
</table>
<p>  If the filesystem was changed, i.e., repaired, then <code>fsck.minix</code> will print &quot;FILE SYSTEM HAS CHANGED&quot; and will <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2) three times before exiting. There is <i>no</i> need to reboot after check.</p>
<h2>Warning</h2>
<p><code>fsck.minix</code> should <code>not</code> be used on a mounted filesystem. Using <code>fsck.minix</code> on a mounted filesystem is very dangerous, due to the possibility that deleted files are still in use, and can seriously damage a perfectly good filesystem! If you absolutely have to run <code>fsck.minix</code> on a mounted filesystem, such as the root filesystem, make sure nothing is writing to the disk, and that no files are &quot;zombies&quot; waiting for deletion.</p>
<h2>Options</h2>
<p><code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>List all filenames.</dl>
<p> <code>-r</code>, <code>&#8211;repair</code></p>
<dl>
<dd>Perform interactive repairs.</dl>
<p> <code>-a</code>, <code>&#8211;auto</code></p>
<dl>
<dd>Perform automatic repairs. This option implies <code>&#8211;repair</code> and serves to answer all of the questions asked with the default. Note that this can be extremely dangerous in the case of extensive filesystem damage.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Be verbose.</dl>
<p> <code>-s</code>, <code>&#8211;super</code></p>
<dl>
<dd>Output super-block information.</dl>
<p> <code>-m</code>, <code>&#8211;uncleared</code></p>
<dl>
<dd>Activate MINIX-like &quot;mode not cleared&quot; warnings.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Force a filesystem check even if the filesystem was marked as valid. Marking is done by the kernel when the filesystem is unmounted.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Diagnostics</h2>
<p>There are numerous diagnostic messages. The ones mentioned here are the most commonly seen in normal usage. </p>
<p> If the device does not exist, <code>fsck.minix</code> will print &quot;unable to read super block&quot;. If the device exists, but is not a MINIX filesystem, <code>fsck.minix</code> will print &quot;bad magic number in super-block&quot;.</p>
<h2>Exit Status</h2>
<p>The exit status returned by <code>fsck.minix</code> is the sum of the following: </p>
<p> <code>0</code></p>
<dl>
<dd>No errors</dl>
<p> <code>3</code></p>
<dl>
<dd>Filesystem errors corrected, system should be rebooted if filesystem was mounted</dl>
<p> <code>4</code></p>
<dl>
<dd>Filesystem errors left uncorrected</dl>
<p> <code>7</code></p>
<dl>
<dd>Combination of exit statuses 3 and 4</dl>
<p> <code>8</code></p>
<dl>
<dd>Operational error</dl>
<p> <code>16</code></p>
<dl>
<dd>Usage or syntax error</dl>
<h2>Authors</h2>
<p>Exit status values by Added support for filesystem valid flag: Check to prevent fsck of mounted filesystem added by Minix v2 fs support by updated by Portability patch by</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-fsck-ext2/">fsck.ext2</a></code>(8), <code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-ext2/">mkfs.ext2</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-minix/">mkfs.minix</a></code>(8), <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fsck.minix</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
