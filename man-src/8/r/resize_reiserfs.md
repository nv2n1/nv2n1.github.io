---
title: "resize_reiserfs(8)"
name: "resize_reiserfs"
section: "8"
letter: "r"
url: "/docs/linux/man/8-resize_reiserfs/"
description: "resize_reiserfs – resizer tool for the ReiserFS filesystem"
---

<p>resize_reiserfs &#8211; resizer tool for the ReiserFS filesystem</p>
<h2>Synopsis</h2>
<p><code>resize_reiserfs</code> [ <code>-s</code> <i></i>[<code>+</code>|<code>&#8211;</code>]<i>size</i><code>[K</code>|<code>M</code>|<code>G</code>] ] [ <code>-j</code> <i></i><i>dev</i> ] [ <code>-fqv</code> ] <i>device</i></p>
<h2>Description</h2>
<p>The <code>resize_reiserfs</code> tool resizes an unmounted reiserfs file system. It enlarges or shrinks an reiserfs file system located on a <i>device</i> so that it will have <i>size</i> bytes or size=old_size +(-) <i>size</i> bytes if the + or &#8211; prefix is used. If the <code>-s</code> option is not specified, the filesystem will be resized to fill the given device. The <i>size</i> parameter may have one of the optional modifiers <code>K</code>, <code>M</code>, <code>G</code>, which means the <i>size</i> parameter is given in kilo-, mega-, gigabytes respectively. The <code>resize_reiserfs</code> program does not manipulate the size of the device. If you wish to enlarge a filesystem, you must make sure you expand the underlying device first. This can be done using <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8) for partitions, by deleting the partition and recreating it with a larger size (assuming there is free space <i>after</i> the partition in question). Make sure you re-create it with the same starting disk cylinder as before! Otherwise, the resize operation will certainly not work, and you may lose your entire filesystem. The <code>resize_reiserfs</code> program allows to grow a reiserfs on-line if there is a free space on block <i>device.</i> If you wish to shrink a reiserfs partition, first use <code>resize_reiserfs</code> to shrink the file system. You may then use <code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8) to shrink the device. When shrinking the size of the device, make sure you do not make it smaller than the reduced size of the reiserfs filesystem. </p>
<h2>Options</h2>
<dl>
<dt><code>-s&nbsp;[+|-]</code><i>size</i></p>
<dd>Set the new size in bytes.</p>
<dt><code>-j&nbsp;</code><i>dev</i></p>
<dd>Set the journal device name.</p>
<dt><code>-f</code></p>
<dd>Force, do not perform checks.</p>
<dt><code>-q</code></p>
<dd>Do not print anything but error messages.</p>
<dt><code>-v</code></p>
<dd>Turn on extra progress status messages (default). </p>
</dl>
<h2>Return Values</h2>
<p>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Resizing successful.</p>
<dl>
<dt>-1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Resizing not successful.</p>
<dd></dl>
<h2>Examples</h2>
<p>The following example shows how to test <code>resize_reiserfs</code>. Suppose 2Gb reiserfs filesystem is created on the device /dev/hda8 and is mounted on /mnt. For shrinking the device we need to unmount it first, then run <code>resize_reiserfs</code> with a <i>size </i> parameter (in this case -1Gb): df<br />
 umount /mnt<br />
 resize_reiserfs -s -1G /dev/hda8<br />
 mount /dev/hda8 /mnt<br />
 df /mnt </p>
<h2>Author</h2>
<p>This version of <code>resize_reiserfs</code> has been written by Alexander Zarochentcev &lt;zam [at] namesys.com&gt;.</p>
<h2>Bugs</h2>
<p>Please report bugs to the ReiserFS developers &lt;reiserfs-devel [at] vger.kernel.org&gt;, providing as much information as possible&#8211;your hardware, kernel, patches, settings, all printed messages; check the syslog file for any related information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cfdisk/">cfdisk</a></code>(8), <code><a href="/docs/linux/man/8-reiserfsck/">reiserfsck</a></code>(8), <code><a href="/docs/linux/man/8-debugreiserfs/">debugreiserfs</a></code>(8) </p>
