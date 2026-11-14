---
title: "vfs_netatalk(8)"
name: "vfs_netatalk"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_netatalk/"
description: "vfs_netatalk – hide .AppleDouble files from CIFS clients"
---

<p>vfs_netatalk &#8211; hide .AppleDouble files from CIFS clients</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = netatalk</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_netatalk VFS module dynamically hides .AppleDouble files, preventing spurious errors on some CIFS clients. .AppleDouble files may be created by historic implementations of AFP (Apple Filing Protocol) on servers. </p>
<p> This module is stackable.</p>
<h2>Examples</h2>
<p>Hide .AppleDouble files on the [data] share: </p>
<dl>
<dd>
<pre> <i>[data]</i>
 m[blue]<code>vfs objects = netatalk</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>This module is largely historic and unlikely to be of use in modern networks since current Apple systems are able to mount CIFS shares natively.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
