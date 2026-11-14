---
title: "zerofree(8)"
name: "zerofree"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zerofree/"
description: "zerofree — zero free blocks from ext2, ext3 and ext4 file-systems"
---

<p>zerofree &#8212; zero free blocks from ext2, ext3 and ext4 file-systems</p>
<h2>Synopsis</h2>
<p><code>zerofree</code> [<code>-n</code>] [<code>-v</code>] [<code>-f fillval</code>] <i>filesystem</i></p>
<h2>Description</h2>
<p><code>zerofree</code> finds the unallocated, blocks with non-zero value content in an ext2, ext3 or ext4 <i>filesystem</i> (e.g. /dev/hda1) and fills them with zeroes (or another octet of your choice).<br />
&nbsp;<br />
&nbsp; </p>
<p> Filling unused areas with zeroes is useful if the device on which this file-system resides is a disk image. In this case, depending on the type of disk image, a secondary utility may be able to reduce the size of the disk image after zerofree has been run.<br />
&nbsp; </p>
<p> Filling unused areas may also be useful with solid-state drives (SSDs). On some SSDs, filling blocks with ones (0xFF) is reported to trigger Flash block erasure by the firmware, possibly giving a write performance increase.<br />
&nbsp; </p>
<p> The usual way to achieve the same result (zeroing the unallocated blocks) is to run <code>dd</code> (1) to create a file full of zeroes that takes up the entire free space on the drive, and then delete this file. This has many disadvantages, which zerofree alleviates:</p>
<dl>
<dt> &bull;</p>
<dd>it is slow;</p>
<dt> &bull;</p>
<dd>it makes the disk image (temporarily) grow to its maximal extent;</p>
<dt> &bull;</p>
<dd>it (temporarily) uses all free space on the disk, so other concurrent write actions may fail.<br />
&nbsp;</dl>
<p> <i>filesystem</i> has to be unmounted or mounted read-only for <code>zerofree</code> to work. It will exit with an error message if the <i>filesystem</i> is mounted writable. To remount the root file-system readonly, you can first switch to single user runlevel (<code>telinit 1</code>) then use <code>mount -o remount,ro </code><i>filesystem</i>.<br />
&nbsp; </p>
<p> <code>zerofree</code> has been written to be run from GNU/Linux systems installed as guest OSes inside a virtual machine. In this case, it is typically run from within the guest system, and a utility is then run from the host system to shrink disk image (<code>VBoxManage modifyhd &#8211;compact</code>, provided with virtualbox, is able to do that for some disk image formats).<br />
&nbsp; </p>
<p> It may however be useful in other situations: for instance it can be used to make it more difficult to retrieve deleted data. Beware that securely deleting sensitive data is not in general an easy task and usually requires writing several times on the deleted blocks.<br />
&nbsp;</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Perform a dry run (do not modify the file-system);</p>
<dt><code>-v</code></p>
<dd>Be verbose: show the number of blocks modified by <code>zerofree</code> (or that would be modified, in case the <code>-n</code> is used), the number of free blocks and the total number of blocks on the filesystem;</p>
<dt><code>-f value</code></p>
<dd>Specify the octet value to fill empty blocks with (defaults to 0). Argument must be within the range 0 to 255.</dl>
<h2>See Also</h2>
<p>dd (1).</p>
<h2>Author</h2>
<p>This manual page was written by Thibaut Paumard &lt;paumard [at] users.sourceforge.net&gt; for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation.<br />
&nbsp; </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL-2.<br />
&nbsp;</p>
