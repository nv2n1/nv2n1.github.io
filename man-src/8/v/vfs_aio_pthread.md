---
title: "vfs_aio_pthread(8)"
name: "vfs_aio_pthread"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_aio_pthread/"
description: "vfs_aio_pthread – implement async I/O in Samba vfs using a pthread pool"
---

<p>vfs_aio_pthread &#8211; implement async I/O in Samba vfs using a pthread pool</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = aio_pthread</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The aio_pthread VFS module enables asynchronous I/O for Samba on platforms which have the pthreads API available, without using the Posix AIO interface. Posix AIO can suffer from severe limitations. For example, on some Linux versions the real-time signals that it uses are broken under heavy load. Other systems only allow AIO when special kernel modules are loaded or only allow a certain system-wide amount of async requests being scheduled. Systems based on glibc (most Linux systems) only allow a single outstanding request per file descriptor which essentially makes Posix AIO useless on systems using the glibc implementation. </p>
<p> To work around all these limitations, the aio_pthread module was written. It uses a pthread pool instead of the internal Posix AIO interface to allow read and write calls to be process asynchronously. A pthread pool is created which expands dynamically by creating new threads as work is given to it to a maximum of 100 threads per smbd process. To change this limit see the &quot;aio num threads&quot; parameter below. New threads are not created if idle threads are available when a new read or write request is received, the new work is given to an existing idle thread. Threads terminate themselves if idle for one second. </p>
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
 m[blue]<code>vfs objects = aio_pthread</code>m[]</pre>
</dl>
<h2>Options</h2>
<p>aio_pthread:aio num threads = INTEGER</p>
<dl>
<dd>Limit the maximum number of threads per smbd that will be created in the thread pool to service IO requests. </p>
<p> By default this is set to 100.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4.0 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
