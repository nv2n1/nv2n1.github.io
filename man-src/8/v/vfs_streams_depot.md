---
title: "vfs_streams_depot(8)"
name: "vfs_streams_depot"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_streams_depot/"
description: "vfs_streams_depot – EXPERIMENTAL module to store alternate data streams in a central directory."
---

<p>vfs_streams_depot &#8211; EXPERIMENTAL module to store alternate data streams in a central directory.</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = streams_depot</dl>
<h2>Description</h2>
<p>This <i>EXPERIMENTAL</i> VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_streams_depot enables storing of NTFS alternate data streams in the file system. As a normal posix file system does not support the concept of multiple data streams per file, the streams_depot module stores the data in files in a separate directory.</p>
<h2>Options</h2>
<p>streams_depot:directory = PATH</p>
<dl>
<dd>Path of the directory where the alternate data streams should be stored. Defaults to the sharepath/.streams.</dl>
<p> streams_depot:delete_lost = [ yes | no ]</p>
<dl>
<dd>In the case of an already existing data streams directory for a newly created file the streams directory will be renamed to &quot;lost-%lu&quot;, random(). With this option lost stream directories will be removed instead of renamed. </p>
<dl>
<dd>&bull; no(default) &#8211; rename lost streams to &quot;lost-%lu&quot;, random().</dl>
<dl>
<dd>&bull; yes &#8211; remove lost streams.</dl>
</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>vfs objects = streams_depot</code>m[]</pre>
</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
