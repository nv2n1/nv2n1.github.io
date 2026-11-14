---
title: "vfs_aio_fork(8)"
name: "vfs_aio_fork"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_aio_fork/"
description: "vfs_aio_fork – implement async I/O in Samba vfs"
---

<p>vfs_aio_fork &#8211; implement async I/O in Samba vfs</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = aio_fork</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The aio_fork VFS module enables async I/O for Samba on platforms where the system level Posix AIO interface is insufficient. Posix AIO can suffer from severe limitations. For example, on some Linux versions the real-time signals that it uses are broken under heavy load. Other systems only allow AIO when special kernel modules are loaded or only allow a certain system-wide amount of async requests being scheduled. Systems based on glibc (most Linux systems) only allow a single outstanding request per file descriptor. </p>
<p> To work around all these limitations, the aio_fork module was written. It uses forked helper processes instead of the internal Posix AIO interface to create asynchronousity for read and write calls. It has no parameters, it will create helper processes when async requests come in as needed. Idle helper processes will be removed every 30 seconds. </p>
<p> This module is stackable.</p>
<h2>Examples</h2>
<p>Straight forward use: </p>
<dl>
<dd>
<pre> <i>[cooldata]</i>
 m[blue]<code>path = /data/ice</code>m[]
 m[blue]<code>vfs objects = aio_fork</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
