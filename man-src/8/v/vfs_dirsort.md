---
title: "vfs_dirsort(8)"
name: "vfs_dirsort"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_dirsort/"
description: "vfs_dirsort – Sort directory contents"
---

<p>vfs_dirsort &#8211; Sort directory contents</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = dirsort</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_dirsort module sorts directory entries alphabetically before sending them to the client. </p>
<p> Please be aware that adding this module might have negative performance implications for large directories.</p>
<h2>Examples</h2>
<p>Sort directories for all shares: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>vfs objects = dirsort</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
