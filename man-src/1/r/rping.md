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
</dt><dd> Run as the server.
</dd><dt>-c
</dt><dd> Run as the client.
</dd><dt>-a address
</dt><dd> On the server, specifies the network address to bind the connection to. To bind to any address with IPv6 use -a ::0 . On the client, specifies the server address to connect to.
</dd><dt>-p
</dt><dd> Port number for listening server.
</dd><dt>-v
</dt><dd> Display ping data.
</dd><dt>-V
</dt><dd> Validate ping data.
</dd><dt>-d
</dt><dd> Display debug information.
</dd><dt>-C message_count
</dt><dd> The number of messages to transfer over each connection. (default infinite)
</dd><dt>-S message_size
</dt><dd> The size of each message transferred, in bytes. (default 100)
</dd><dt>-P
</dt><dd> Run the server in persistent mode. This allows multiple rping clients to connect to a single server instance. The server will run until killed.</dd></dl>

<h2>NOTES</h2>

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-ucmatose/">ucmatose</a>(1), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1) 

<h2>Index</h2>


