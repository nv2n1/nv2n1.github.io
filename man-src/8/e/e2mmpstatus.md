---
title: "e2mmpstatus(8)"
name: "e2mmpstatus"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e2mmpstatus/"
description: "e2mmpstatus – Check MMP status of an ext4 file system"
---

<p>e2mmpstatus &#8211; Check MMP status of an ext4 file system</p>
<h2>Synopsis</h2>
<p><code>e2mmpstatus</code> [<code>-i</code>] &lt;<i>file</i>system<i>&gt;</i></p>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>prints out the MMP information rather than check it.</dl>
<h2>Description</h2>
<p><code>e2mmpstatus</code> is used to check Multiple-Mount Protection (MMP) status of an ext4 file system with the <code>mmp</code> feature enabled. The specified <i>file system</i> can be a device name (e.g. <i>/dev/hdc1</i>, <i>/dev/sdb2</i>), or an ext4 file system label or UUID, for example <code>UUID=8868abf6-88c5-4a83-98b8-bfc24057f7bd</code> or <code>LABEL=root</code>. By default, the <code>e2mmpstatus</code> program checks whether it is safe to mount the file system without taking the risk of mounting it more than once. </p>
<p> MMP (multiple-mount protection) is a feature that adds protection against the file system being modified simultaneously by more than one node. It is NOT safe to mount a file system when one of the following conditions is true:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>1. e2fsck is running on the file system.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>2. the file system is in use by another node.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>3. The MMP block is corrupted or cannot be read for some reason.</p>
<p> The <code>e2mmpstatus</code> program might wait for some time to see whether the MMP block is being updated by any node during this period. The time taken depends on how frequently the MMP block is being written by the other node.</p>
<h2>Exit Code</h2>
<p>The exit code returned by <code>e2mmpstatus</code> is 0 when it is safe to mount the file system, 1 when the MMP block shows the file system is in use on another node and it is NOT safe to mount the file system, and 2 if some other failure occurred that prevents the check from properly detecting the current MMP status.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dumpe2fs/">dumpe2fs</a></code>(8), <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), </p>
