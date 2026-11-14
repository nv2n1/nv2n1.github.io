---
title: "rdma_server(1)"
name: "rdma_server"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdma_server/"
---

<h2>NAME</h2>

 rdma_server - simple RDMA CM connection and ping-pong test.

<h2>SYNOPSIS</h2>

 

 <pre>
<i>rdma_server</i> [-p port]
</pre>

<h2>DESCRIPTION</h2>

 Uses synchronous librdmam calls to establish an RDMA connections between two nodes. This example is intended to provide a very simple coding example of how to use RDMA.

<h2>OPTIONS</h2>

<dl>
<dt>-p port
<dd> Changes the port number that the server listens on. By default the server listens on port 7471.</dl>

<h2>NOTES</h2>

 Basic usage is to start rdma_server, then connect to the server using the rdma_client program. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1), <a HREF="/docs/linux/man/1-rdma_client/">rdma_client</a>(1) 

<h2>Index</h2>


