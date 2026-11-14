---
title: "vfs_linux_xfs_sgid(8)"
name: "vfs_linux_xfs_sgid"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_linux_xfs_sgid/"
description: "vfs_linux_xfs_sgid"
---

<p>vfs_linux_xfs_sgid</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = linux_xfs_sgid</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> vfs_linux_xfs_sgid is a VFS module to work around an old Linux XFS bug that still exists: Under certain circumstances the SGID bit is not inherited (<a rel="nofollow" href="http://oss.sgi.com/bugzilla/show_bug.cgi?id=280">http://oss.sgi.com/bugzilla/show_bug.cgi?id=280</a>). The vfs_linux_xfs_sgid VFS module will work around this bug by manually setting the SGID bit after a mkdir if the parent directory had the SGID bit set. </p>
<p> This module is stackable.</p>
<h2>Examples</h2>
<p>Add syncops functionality for [share]: </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = linux_xfs_sgid</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.1.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
