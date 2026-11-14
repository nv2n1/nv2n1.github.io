---
title: "vfs_cacheprime(8)"
name: "vfs_cacheprime"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_cacheprime/"
description: "vfs_cacheprime – prime the kernel file data cache"
---

<p>vfs_cacheprime &#8211; prime the kernel file data cache</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = cacheprime</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_cacheprime VFS module reads chunks of file data near the range requested by clients in order to make sure the data is present in the kernel file data cache at the time when it is actually requested by clients. </p>
<p> The size of the disk read operations performed by vfs_cacheprime is determined by the cacheprime:rsize option. All disk read operations are aligned on boundaries that are a multiple of this size. Each range of the file data is primed at most once during the time the client has the file open. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>cacheprime:rsize = BYTES</p>
<dl>
<dd>The number of bytes with which to prime the kernel data cache. </p>
<p> The following suffixes may be applied to BYTES: </p>
<dl>
<dd>&bull; K &#8211; BYTES is a number of kilobytes</dl>
<dl>
<dd>&bull; M &#8211; BYTES is a number of megabytes</dl>
<dl>
<dd>&bull; G &#8211; BYTES is a number of gigabytes</dl>
</dl>
<h2>Examples</h2>
<p>For a hypothetical disk array, it is necessary to ensure that all read operations are of size 1 megabyte (1048576 bytes), and aligned on 1 megabyte boundaries: </p>
<dl>
<dd>
<pre> <i>[hypothetical]</i>
 m[blue]<code>vfs objects = cacheprime</code>m[]
 m[blue]<code>cacheprime:rsize = 1M</code>m[]</pre>
</dl>
<h2>Caveats</h2>
<p>cacheprime is not a substitute for a general-purpose readahead mechanism. It is intended for use only in very specific environments where disk operations must be aligned and sized to known values (as much as that is possible).</p>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
