---
title: "vfs_xattr_tdb(8)"
name: "vfs_xattr_tdb"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_xattr_tdb/"
description: "vfs_xattr_tdb – Save Extended Attributes (EAs) in a tdb file"
---

<p>vfs_xattr_tdb &#8211; Save Extended Attributes (EAs) in a tdb file</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = xattr_tdb</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_xattr_tdb VFS module stores Extended Attributes (EAs) in a tdb file. This enables the usage of Extended Attributes on OS and filesystems which do not support Extended Attributes by themselves. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>xattr_tdb:file = PATH</p>
<dl>
<dd>Name of the tdb file the EAs are stored in. If this option is not set, the default filename xattr.tdb is used.</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
