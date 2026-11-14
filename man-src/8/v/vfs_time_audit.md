---
title: "vfs_time_audit(8)"
name: "vfs_time_audit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_time_audit/"
description: "vfs_time_audit – samba vfs module to log slow VFS operations"
---

<p>vfs_time_audit &#8211; samba vfs module to log slow VFS operations</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = time_audit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The time_audit VFS module logs system calls that take longer than the number of milliseconds defined by the variable time_audit:timeout. It will log the calls and the time spent in it. </p>
<p> It&#8217;s kind of comparable with strace -T and is helpful to reveal performance problems with the underlying file and storage subsystems. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>time_audit:timeout = number of milliseconds</p>
<dl>
<dd>VFS calls that take longer than the defined number of milliseconds that should be logged. The default is 10000 (10s).</dl>
<h2>Examples</h2>
<p>This would log VFS calls that take longer than 3 seconds: </p>
<dl>
<dd>
<pre> <i>[sample_share]</i>
 m[blue]<code>path = /test/sample_share</code>m[]
 m[blue]<code>vfs objects = time_audit</code>m[]
 m[blue]<code>time_audit:timeout = 3000</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The time_audit VFS module was created with contributions from Abhidnya Chirmule.</p>
