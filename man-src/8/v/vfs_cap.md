---
title: "vfs_cap(8)"
name: "vfs_cap"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_cap/"
description: "vfs_cap – CAP encode filenames"
---

<p>vfs_cap &#8211; CAP encode filenames</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = cap</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> CAP (Columbia Appletalk Protocol) encoding is a technique for representing non-ASCII filenames in ASCII. The vfs_cap VFS module translates filenames to and from CAP format, allowing users to name files in their native encoding. </p>
<p> CAP encoding is most commonly used in Japanese language environments. </p>
<p> This module is stackable.</p>
<h2>Examples</h2>
<p>On a system using GNU libiconv, use CAP encoding to support users in the Shift_JIS locale: </p>
<dl>
<dd>
<pre> <i>[global]</i>
 m[blue]<code>dos charset = CP932</code>m[]
 m[blue]<code>dos charset = CP932</code>m[]
 m[blue]<code>vfs objects = cap</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
