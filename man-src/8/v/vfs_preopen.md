---
title: "vfs_preopen(8)"
name: "vfs_preopen"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_preopen/"
description: "vfs_preopen – Hide read latencies for applications reading numbered files"
---

<p>vfs_preopen &#8211; Hide read latencies for applications reading numbered files</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = preopen</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> This module assists applications that want to read numbered files in sequence with very strict latency requirements. One area where this happens in video streaming applications that want to read one file per frame. </p>
<p> When you use this module, a number of helper processes is started that speculatively open files and read a number of bytes to prime the file system cache, so that later on when the real application&#8217;s request comes along, no disk access is necessary. </p>
<p> This module is stackable.</p>
<h2>Options</h2>
<p>preopen:names = /pattern/</p>
<dl>
<dd>preopen:names specifies the file name pattern which should trigger the preopen helpers to do their work. We assume that the files are numbered incrementally. So if your file names are numbered FRAME00000.frm FRAME00001.frm and so on you would list them as preopen:names=/FRAME*.frm/</dl>
<p> preopen:num_bytes = BYTES</p>
<dl>
<dd>Specifies the number of bytes the helpers should speculatively read, defaults to 1.</dl>
<p> preopen:helpers = NUM-PROCS</p>
<dl>
<dd>Number of forked helper processes, defaults to 1.</dl>
<p> preopen:queuelen = NUM-FILES</p>
<dl>
<dd>Number of files that should be speculatively opened. Defaults to the 10 subsequent files.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The PREOPEN VFS module was created with contributions from Volker Lendecke and the developers at IBM.</p>
