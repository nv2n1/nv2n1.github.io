---
title: "vfs_offline(8)"
name: "vfs_offline"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_offline/"
description: "vfs_offline – Mark all files as offline"
---

<p>vfs_offline &#8211; Mark all files as offline</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = offline</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_offline module marks all files in the share as having the offline DOS attribute. </p>
<p> Files with the offline DOS attribute are handled differently by the Windows SMB client, as well as by Windows Explorer. In particular, Windows Explorer does not read those files for the sole purpose of drawing a thumbnail, as it normally does. This can improve user experience with some remote file systems.</p>
<h2>Examples</h2>
<p>Mark all files in a share as offline: </p>
<dl>
<dd>
<pre> <i>[remote]</i>
 m[blue]<code>vfs objects = offline</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.4 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
