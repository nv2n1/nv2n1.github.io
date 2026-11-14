---
title: "vfs_worm(8)"
name: "vfs_worm"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_worm/"
description: "vfs_worm – disallows writes for older file"
---

<p>vfs_worm &#8211; disallows writes for older file</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = worm</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_worm module controls the writability of files and folders depending on their change time and a adjustable grace period. </p>
<p> If the change time of a file or directory is older than the specified grace period, the write access will be denied, independent of further access controls (e.g. by the filesystem). </p>
<p> In the case that the grace period is not exceed, the worm module will not impact any access controls.</p>
<h2>Options</h2>
<p>worm:grace_period = SECONDS</p>
<dl>
<dd>Period in seconds which defines the time how long the write access should be handled by the normal access controls. After this grace period the file or directory becomes read only.</dl>
<h2>Examples</h2>
<p>Deny the write access to files and folders, which are older than five minutes (300 seconds): </p>
<dl>
<dd>
<pre> <i>[wormshare]</i>
 m[blue]<code>vfs objects = worm</code>m[]
 m[blue]<code>worm:grace_period = 300</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.2 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
