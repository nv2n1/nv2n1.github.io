---
title: "udaddy(1)"
name: "udaddy"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udaddy/"
---

<h2>NAME</h2>

 udaddy - RDMA CM datagram setup and simple ping-pong test.

<h2>SYNOPSIS</h2>

 

 <pre><code>
udaddy[-s server_address][-b bind_address][-c connections]
      [-C message_count][-S message_size][-p port_space] udaddy -
    s server_address[-b bind_address][-c connections]
                    [-C message_count][-S message_size][-t tos][-p port_space]
</code></pre>

<h2>DESCRIPTION</h2>

 Establishes a set of unreliable RDMA datagram communication paths between two nodes using the librdmacm, optionally transfers datagrams between the nodes, then tears down the communication.

<h2>OPTIONS</h2>

<dl>
<dt>-s server_address
<dd> The network name or IP address of the server system listening for communication. The used name or address must route over an RDMA device. This option must be specified by the client.
<dt>-b bind_address
<dd> The local network address to bind to. To bind to any address with IPv6 use -b ::0 .
<dt>-c connections
<dd> The number of communication paths to establish between the client and server. The test uses unreliable datagram communication, so no actual connections are formed. (default 1)
<dt>-C message_count
<dd> The number of messages to transfer over each connection. (default 10)
<dt>-S message_size
<dd> The size of each message transferred, in bytes. This value must be smaller than the MTU of the underlying RDMA transport, or an error will occur. (default 100)
<dt>-t tos
<dd> Indicates the type of service used for the communication. Type of service is implementation dependent based on subnet configuration.
<dt>-p port_space
<dd> The port space of the datagram communication. May be either the RDMA UDP (0x0111) or IPoIB (0x0002) port space. (default RDMA_PS_UDP)</dl>

<h2>NOTES</h2>

 Basic usage is to start udaddy on a server system, then run udaddy -s server_name on a client system. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-ucmatose/">ucmatose</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1) 

<h2>Index</h2>


