---
title: "vfs_readahead(8)"
name: "vfs_readahead"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_readahead/"
description: "vfs_readahead – pre-load the kernel buffer cache"
---

<p>vfs_readahead &#8211; pre-load the kernel buffer cache</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = readahead</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> This vfs_readahead VFS module detects read requests at multiples of a given offset (hex 0x80000 by default) and then tells the kernel via either the readahead system call (on Linux) or the posix_fadvise system call to pre-fetch this data into the buffer cache. </p>
<p> This module is useful for Windows Vista clients reading data using the Windows Explorer program, which asynchronously does multiple file read requests at offset boundaries of 0x80000 bytes. </p>
<p> The offset multiple used is given by the readahead:offset option, which defaults to 0x80000. </p>
<p> The size of the disk read operations performed by vfs_readahead is determined by the readahead:length option. By default this is set to the same value as the readahead:offset option and if not set explicitly will use the current value of readahead:offset. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>readahead:offset = BYTES</p>
<dl>
<dd>The offset multiple that causes readahead to be requested of the kernel buffer cache.</dl>
<p> readahead:length = BYTES</p>
<dl>
<dd>The number of bytes requested to be read into the kernel buffer cache on each readahead call.</dl>
<p> The following suffixes may be applied to BYTES: </p>
<dl>
<dd>&bull; K &#8211; BYTES is a number of kilobytes</dl>
<dl>
<dd>&bull; M &#8211; BYTES is a number of megabytes</dl>
<dl>
<dd>&bull; G &#8211; BYTES is a number of gigabytes</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre> <i>[hypothetical]</i>
 m[blue]<code>vfs objects = readahead</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
