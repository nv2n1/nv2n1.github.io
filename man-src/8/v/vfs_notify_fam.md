---
title: "vfs_notify_fam(8)"
name: "vfs_notify_fam"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_notify_fam/"
description: "vfs_notify_fam – FAM support for file change notifications"
---

<p>vfs_notify_fam &#8211; FAM support for file change notifications</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = notify_fam</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_notify_fam module makes use of the system FAM (File Alteration Monitor) daemon to implement file change notifications for Windows clients. FAM is generally present only on IRIX and some BSD systems. </p>
<p> This module is not stackable.</p>
<h2>Examples</h2>
<p>Support FAM notifications globally: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = notify_fam</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
