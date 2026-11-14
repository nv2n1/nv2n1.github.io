---
title: "rping(1)"
name: "rping"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rping/"
---

<h2>NAME</h2>

 rping - RDMA CM connection and RDMA ping-pong test.

<h2>SYNOPSIS</h2>

 

 <pre><code>
rping - s[-v][-V][-d][-P][-a address][-p port][-C message_count][-S message_size] rping - c[-v][-V][-d] - a address[-p port][-C message_count][-S message_size]
</code></pre>

<h2>DESCRIPTION</h2>

 Establishes a reliable RDMA connection between two nodes using the librdmacm, optionally performs RDMA transfers between the nodes, then disconnects.

<h2>OPTIONS</h2>

<dl>
<dt>-s
<dd> Run as the server.
<dt>-c
<dd> Run as the client.
<dt>-a address
<dd> On the server, specifies the network address to bind the connection to. To bind to any address with IPv6 use -a ::0 . On the client, specifies the server address to connect to.
<dt>-p
<dd> Port number for listening server.
<dt>-v
<dd> Display ping data.
<dt>-V
<dd> Validate ping data.
<dt>-d
<dd> Display debug information.
<dt>-C message_count
<dd> The number of messages to transfer over each connection. (default infinite)
<dt>-S message_size
<dd> The size of each message transferred, in bytes. (default 100)
<dt>-P
<dd> Run the server in persistent mode. This allows multiple rping clients to connect to a single server instance. The server will run until killed.</dl>

<h2>NOTES</h2>

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-ucmatose/">ucmatose</a>(1), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1) 

<h2>Index</h2>


