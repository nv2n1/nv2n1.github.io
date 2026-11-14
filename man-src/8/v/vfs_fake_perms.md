---
title: "vfs_fake_perms(8)"
name: "vfs_fake_perms"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_fake_perms/"
description: "vfs_fake_perms – enable read only Roaming Profiles"
---

<p>vfs_fake_perms &#8211; enable read only Roaming Profiles</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = fake_perms</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_fake_perms VFS module was created to allow Roaming Profile files and directories to be set (on the Samba server under UNIX) as read only. This module will, if installed on the Profiles share, report to the client that the Profile files and directories are writeable. This satisfies the client even though the files will never be overwritten as the client logs out or shuts down. </p>
<p> This module is stackable.</p>
<h2>Examples</h2>
<dl>
<dd>
<pre> <i>[Profiles]</i>
 m[blue]<code>path = /profiles</code>m[]
 m[blue]<code>vfs objects = fake_perms</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
