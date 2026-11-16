---
title: "ucmatose(1)"
name: "ucmatose"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ucmatose/"
---

<h2>NAME</h2>

 ucmatose - RDMA CM connection and simple ping-pong test.

<h2>SYNOPSIS</h2>

 

 <pre><code>
ucmatose[-s server_address][-b bind_address]
        [-f address_format][-P port_space]
        [-c connections][-C message_count][-S message_size] ucmatose -
    s server_address[-b bind_address]
                    [-f address_format][-P port_space]
                    [-c connections][-C message_count][-S message_size][-t tos]
</code></pre>

<h2>DESCRIPTION</h2>

 Establishes a set of reliable RDMA connections between two nodes using the librdmacm, optionally transfers data between the nodes, then disconnects.

<h2>OPTIONS</h2>

<dl>
<dt>-s server_address
</dt><dd> The network name or IP address of the server system listening for connections. The used name or address must route over an RDMA device. This option must be specified by the client.
</dd><dt>-b bind_address
</dt><dd> The local network address to bind to. To bind to any address with IPv6 use -b ::0 .
</dd><dt>-f address_format
</dt><dd> Specifies the format of the server and bind address. Be default, the format is determined by getaddrinfo() as either being a hostname, an IPv4 address, or an IPv6 address. This option may be used to indicate that a specific address format has been provided. Supported address_format values are: name, ip, ipv6, and gid.
</dd><dt>-P port_space
</dt><dd> Specifies the port space for the connection. Be default, the port space is the RDMA TCP port space. (Note that the RDMA port space may be separate from that used for IP.) Supported port_space values are: tcp and ib.
</dd><dt>-c connections
</dt><dd> The number of connections to establish between the client and server. (default 1)
</dd><dt>-C message_count
</dt><dd> The number of messages to transfer over each connection. (default 10)
</dd><dt>-S message_size
</dt><dd> The size of each message transferred, in bytes. (default 100)
</dd><dt>-t tos
</dt><dd> Indicates the type of service used for the communication. Type of service is implementation dependent based on subnet configuration.
</dd><dt>-m
</dt><dd> Tests event channel migration. Migrates all communication identifiers to a different event channel for disconnect events.</dd></dl>

<h2>NOTES</h2>

 Basic usage is to start ucmatose on a server system, then run ucmatose -s server_name on a client system. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1), <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1) 

<h2>Index</h2>


