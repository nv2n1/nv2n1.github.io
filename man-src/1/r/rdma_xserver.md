---
title: "rdma_xserver(1)"
name: "rdma_xserver"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdma_xserver/"
---

<h2>NAME</h2>

 rdma_xserver - RDMA CM communication server test program

<h2>SYNOPSIS</h2>

 

 <pre><code>
rdma_xserver[-p port][-c comm_type]
</code></pre>

<h2>DESCRIPTION</h2>

 Uses the librdmacm to establish various forms of communication and exchange data.

<h2>OPTIONS</h2>

<dl>
<dt>-p port
<dd> Changes the port number that the server listens on. By default the server listens on port 7471.
<dt>-c communication type
<dd> Specifies the type of communication established with the client program. 'r' results in using a reliable-connected QP (the default). 'x' uses extended reliable-connected XRC QPs.</dl>

<h2>NOTES</h2>

 Basic usage is to start rdma_xserver, then connect to the server using the rdma_xclient program. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1), <a HREF="/docs/linux/man/1-rdma_server/">rdma_server</a>(1), <a HREF="/docs/linux/man/1-rdma_xclient/">rdma_xclient</a>(1) 

<h2>Index</h2>


