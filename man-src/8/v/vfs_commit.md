---
title: "vfs_commit(8)"
name: "vfs_commit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_commit/"
description: "vfs_commit – flush dirty data at specified intervals"
---

<p>vfs_commit &#8211; flush dirty data at specified intervals</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = commit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_commit VFS module keeps track of the amount of data written to a file and synchronizes it to disk when a specified amount accumulates. </p>
<p> vfs_commit is useful in two circumstances. First, if you have very precious data, the impact of unexpected power loss can be minimized by a small commit:dthresh value. Secondly, write performance can be improved on some systems by flushing file data early and at regular intervals. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>commit:dthresh = BYTES</p>
<dl>
<dd>Synchronize file data each time the specified number of bytes has been written. </p>
<p> The following suffixes may be applied to BYTES: </p>
<dl>
<dd>&bull; K &#8211; BYTES is a number of kilobytes</dl>
<dl>
<dd>&bull; M &#8211; BYTES is a number of megabytes</dl>
<dl>
<dd>&bull; G &#8211; BYTES is a number of gigabytes</dl>
</dl>
<h2>Examples</h2>
<p>Synchronize the file data on the [precious] share after every 512 kilobytes (524288 bytes) of data is written: </p>
<dl>
<dd>
<pre> <i>[precious]</i>
 m[blue]<code>path = /data/precious</code>m[]
 m[blue]<code>vfs objects = commit</code>m[]
 m[blue]<code>commit:dthresh = 512K</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>On some systems, the data synchronization performed by commit may reduce performance.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
