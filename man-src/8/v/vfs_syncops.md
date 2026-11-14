---
title: "vfs_syncops(8)"
name: "vfs_syncops"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_syncops/"
description: "vfs_syncops – Ensure meta data operations are performed synchronously."
---

<p>vfs_syncops &#8211; Ensure meta data operations are performed synchronously.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = syncops</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> Some filesystems (even some journaled filesystems) require that a fsync() be performed on many meta data operations to ensure that the operation is guaranteed to remain in the filesystem after a power failure. This is particularly important for some cluster filesystems which are participating in a node failover system with clustered Samba. On those filesystems the vfs_syncops VFS module provides a way to perform those operations safely. </p>
<p> This module is stackable.</p>
<h2>Configuration</h2>
<p>Most of the performance loss with the vfs_syncops VFS module is in fsync on close(). You can disable that with syncops:onclose = no that can be set either globally or per share. </p>
<p> On certain filesystems that only require the last data written to be fsync()&#8217;ed, you can disable the metadata synchronization of this module with syncops:onmeta = no. This option can be set either globally or per share. </p>
<p> The vfs_syncops VFS module can also be disabled completely for a share with syncops:disable = true.</p>
<h2>Examples</h2>
<p>Add syncops functionality for [share]: </p>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>path = /data/share</code>m[]
 m[blue]<code>vfs objects = syncops</code>m[]
 m[blue]<code>syncops:onclose = no</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.1.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
