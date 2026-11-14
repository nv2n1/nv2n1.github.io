---
title: "vfs_prealloc(8)"
name: "vfs_prealloc"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_prealloc/"
description: "vfs_prealloc – preallocate matching files to a predetermined size"
---

<p>vfs_prealloc &#8211; preallocate matching files to a predetermined size</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = prealloc</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_prealloc VFS module preallocates files to a specified size each time a new file is created. This is useful in environments where files are of a predetermined size will be written to a disk subsystem where extending file allocations is expensive. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>prealloc:EXT = BYTES</p>
<dl>
<dd>Preallocate all files with the extension EXT to the size specified by BYTES. </p>
<p> The following suffixes may be applied to BYTES: </p>
<dl>
<dd>&bull; K &#8211; BYTES is a number of kilobytes</dl>
<dl>
<dd>&bull; M &#8211; BYTES is a number of megabytes</dl>
<dl>
<dd>&bull; G &#8211; BYTES is a number of gigabytes</dl>
</dl>
<h2>Examples</h2>
<p>A process writes TIFF files to a Samba share, and the is known these files will almost always be around 4 megabytes (4194304 bytes): </p>
<dl>
<dd>
<pre> <i>[frames]</i>
 m[blue]<code>path = /data/frames</code>m[]
 m[blue]<code>vfs objects = prealloc</code>m[]
 m[blue]<code>prealloc:tiff = 4M</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>vfs_prealloc is not supported on all platforms and filesystems. Currently only XFS filesystems on Linux and IRIX are supported.</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
