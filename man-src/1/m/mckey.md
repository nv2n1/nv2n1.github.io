---
title: "mckey(1)"
name: "mckey"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mckey/"
---

<h2>NAME</h2>

 mckey - RDMA CM multicast setup and simple data transfer test.

<h2>SYNOPSIS</h2>

 

 <pre><code>
mckey - m multicast_address[-s][-b bind_address][-c connections][-C message_count][-S message_size][-p port_space] mckey - m multicast_address - s[-b bind_address][-c connections][-C message_count][-S message_size][-p port_space] mckey - M unmapped_multicast_address - b bind_address[-s][-c connections][-C message_count][-S message_size][-p port_space]
</code></pre>

<h2>DESCRIPTION</h2>

 Establishes a set of RDMA multicast communication paths between nodes using the librdmacm, optionally transfers datagrams to receiving nodes, then tears down the communication.

<h2>OPTIONS</h2>

<dl>
<dt>-m multicast_address
<dd> IP multicast address to join.
<dt>-M unmapped_multicast_address
<dd> RDMA transport specific multicast address to join.
<dt>-s
<dd> Send datagrams to the multicast group.
<dt>-b bind_address
<dd> The local network address to bind to.
<dt>-c connections
<dd> The number of QPs to join the multicast group. (default 1)
<dt>-C message_count
<dd> The number of messages to transfer over each connection. (default 10)
<dt>-S message_size
<dd> The size of each message transferred, in bytes. This value must be smaller than the MTU of the underlying RDMA transport, or an error will occur. (default 100)
<dt>-p port_space
<dd> The port space of the datagram communication. May be either the RDMA UDP (0x0111) or IPoIB (0x0002) port space. (default RDMA_PS_UDP)</dl>

<h2>NOTES</h2>

 Basic usage is to start mckey -m multicast_address on a server system, then run mckey -m multicast_address -s on a client system. 

 Unique Infiniband SA assigned multicast GIDs can be retrived by invoking mckey with a zero MGID or IP address. (Example, -M 0 or -m 0.0.0.0). The assigned address will be displayed to allow mckey clients to join the created group. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-ucmatose/">ucmatose</a>(1), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1) 

<h2>Index</h2>


