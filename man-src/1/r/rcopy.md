---
title: "rcopy(1)"
name: "rcopy"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcopy/"
---

<h2>NAME</h2>

 rcopy - simple file copy over RDMA.

<h2>SYNOPSIS</h2>

 

 <pre><code>
rcopy source server[:destination][-p port] rcopy[-p port]
</code></pre>

<h2>DESCRIPTION</h2>

 Uses sockets over RDMA interface to copy a source file to the specified destination.

<h2>OPTIONS</h2>

<dl>
<dt>ource
<dd> The name and path of the source file to copy.
<dt>erver
<dd> The name or address of the destination server.
<dt>:destination
<dd> An optional destination filename and path. If not given, the destination filename will match that of the source.
<dt>-p server_port
<dd> The server's port number.
<dt></dl>

<h2>NOTES</h2>

<dd> Basic usage is to start rcopy on a server system, then run rcopy sourcefile servername. The server application will continue to run after copying the file, but is currently single-threaded. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7) 

<h2>Index</h2>


