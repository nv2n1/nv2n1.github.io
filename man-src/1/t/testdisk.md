---
title: "testdisk(1)"
name: "testdisk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-testdisk/"
description: "testdisk – Scan and repair disk partitions"
---

<h2>NAME</h2>
<p> testdisk &#8211; Scan and repair disk partitions</p>
<h2>SYNOPSIS</h2>
<p> <code>testdisk [/log] [/debug] [/dump] [device|image.dd|image.e01]</code> </p>
<p> <code>testdisk /version</code> </p>
<p> <code>testdisk /list [/log]</code></p>
<h2>DESCRIPTION</h2>
<p><code>TestDisk</code>&nbsp;<wbr>checks and recovers lost partitions<br />
It works with :<br />
&#8211; BeFS&nbsp;<wbr>(BeOS)<br />
&#8211; BSD disklabel&nbsp;<wbr>(FreeBSD/OpenBSD/NetBSD)<br />
&#8211; CramFS, Compressed File System<br />
&#8211; DOS/Windows FAT12, FAT16 and FAT32<br />
&#8211; HFS and HFS+, Hierarchical File System<br />
&#8211; JFS, IBM&#8217;s Journaled File System<br />
&#8211; Linux Ext2 and Ext3<br />
&#8211; Linux Raid<br />
&nbsp;<wbr>&nbsp;<wbr>RAID 1: mirroring<br />
&nbsp;<wbr>&nbsp;<wbr>RAID 4: striped array with parity device<br />
&nbsp;<wbr>&nbsp;<wbr>RAID 5: striped array with distributed parity information<br />
&nbsp;<wbr>&nbsp;<wbr>RAID 6: striped array with distributed dual redundancy information&nbsp;<wbr><br />
&#8211; Linux Swap&nbsp;<wbr>(versions 1 and 2)<br />
&#8211; LVM and LVM2, Linux Logical Volume Manager<br />
&#8211; Mac partition map<br />
&#8211; Novell Storage Services NSS<br />
&#8211; NTFS&nbsp;<wbr>(Windows NT/2K/XP/2003/Vista)<br />
&#8211; ReiserFS 3.5, 3.6 and 4<br />
&#8211; Sun Solaris i386 disklabel<br />
&#8211; Unix File System UFS and UFS2&nbsp;<wbr>(Sun/BSD/&#8230;)<br />
&#8211; XFS, SGI&#8217;s Journaled File System&nbsp;<wbr></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>/log</code></p>
<dd> create a testdisk.log file</p>
<dt><code>/debug</code></p>
<dd> add debug information</p>
<dt><code>/dump</code></p>
<dd> dump raw sectors</p>
<dt><code>/list</code></p>
<dd> display current partitions</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fdisk/">fdisk</a></code>(1), <code><a href="/docs/linux/man/1-photorec/">photorec</a>(1).</code> <code>.SH</code>AUTHOR TestDisk 6.11, Data Recovery Utility, April 2009<br />
 Christophe GRENIER &lt;grenier [at] cgsecurity.org&gt;<br />
 <a rel="nofollow" href="http://www.cgsecurity.org">http://www.cgsecurity.org</a> </p>
<h2>Index</h2>
