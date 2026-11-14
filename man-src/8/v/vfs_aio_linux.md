---
title: "vfs_aio_linux(8)"
name: "vfs_aio_linux"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_aio_linux/"
description: "vfs_aio_linux – implement async I/O in Samba vfs using Linux kernel aio calls"
---

<p>vfs_aio_linux &#8211; implement async I/O in Samba vfs using Linux kernel aio calls</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = aio_linux</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The aio_linux VFS module enables asynchronous I/O for Samba on Linux kernels that have the kernel AIO calls available without using the Posix AIO interface. Posix AIO can suffer from severe limitations. For example, on some Linux versions the real-time signals that it uses are broken under heavy load. Other systems only allow AIO when special kernel modules are loaded or only allow a certain system-wide amount of async requests being scheduled. Systems based on glibc (most Linux systems) only allow a single outstanding request per file descriptor which essentially makes Posix AIO useless on systems using the glibc implementation. </p>
<p> To work around all these limitations, the aio_linux module was written. It uses the Linux kernel AIO interface instead of the internal Posix AIO interface to allow read and write calls to be processed asynchronously. A queue size of 128 events is used by default. To change this limit set the &quot;aio num events&quot; parameter below. </p>
<p> Note that the smb.conf parameters aio read size and aio write size must also be set appropriately for this module to be active. </p>
<p> This module MUST be listed last in any module stack as the Samba VFS pread/pwrite interface is not thread-safe. This module makes direct pread and pwrite system calls and does NOT call the Samba VFS pread and pwrite interfaces.</p>
<h2>Examples</h2>
<p>Straight forward use: </p>
<dl>
<dd>
<pre> <i>[cooldata]</i>
 m[blue]<code>path = /data/ice</code>m[]
 m[blue]<code>aio read size = 1024</code>m[]
 m[blue]<code>aio write size = 1024</code>m[]
 m[blue]<code>vfs objects = aio_linux</code>m[]</pre>
</dl>
<h2>Options</h2>
<p>aio_linux:aio num events = INTEGER</p>
<dl>
<dd>Set the maximum size of the event queue that is used to limit outstanding IO requests. </p>
<p> By default this is set to 128.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
