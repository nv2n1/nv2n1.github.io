---
title: "rstream(1)"
name: "rstream"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rstream/"
---

<h2>NAME</h2>

 rstream - streaming over RDMA ping-pong test.

<h2>SYNOPSIS</h2>

 

 <pre><code>
rstream[-s server_address][-b bind_address][-f address_format]
       [-B buffer_size][-I iterations][-C transfer_count]
       [-S transfer_size][-p server_port][-T test_option]
</code></pre>

<h2>DESCRIPTION</h2>

 Uses the streaming over RDMA protocol (rsocket) to connect and exchange data between a client and server application.

<h2>OPTIONS</h2>

<dl>
<dt>-s server_address
<dd> The network name or IP address of the server system listening for connections. The used name or address must route over an RDMA device. This option must be specified by the client.
<dt>-b bind_address
<dd> The local network address to bind to.
<dt>-f address_format
<dd> Supported address formats are ip, ipv6, gid, or name.
<dt>-B buffer_size
<dd> Indicates the size of the send and receive network buffers.
<dt>-I iterations
<dd> The number of times that the specified number of messages will be exchanged between the client and server. (default 1000)
<dt>-C transfer_count
<dd> The number of messages to transfer from the client to the server and back again on each iteration. (default 1)
<dt>-S transfer_size
<dd> The size of each send transfer, in bytes. (default 1000) If 'all' is specified, rstream will run a series of tests of various sizes.
<dt>-p server_port
<dd> The server's port number.
<dt>-T test_option
<dd> Specifies test parameters. Available options are:</dl>
 

 s | socket - uses standard socket calls to transfer data 

 a | async - uses asynchronous operation (e.g. select / poll) 

 b | blocking - uses blocking calls 

 f | fork - fork server processing (forces -T s option) 

 n | nonblocking - uses non-blocking calls 

 r | resolve - use rdma cm to resolve address 

 v | verify - verifies data transfers

<h2>NOTES</h2>

 Basic usage is to start rstream on a server system, then run rstream -s server_name on a client system. By default, rstream will run a series of latency and bandwidth performance tests. Specifying a different iterations, transfer_count, or transfer_size will run a user customized test using default values where none have been specified. 

 Because this test maps RDMA resources to userspace, users must ensure that they have available system resources and permissions. See the libibverbs README file for additional details.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7) 

<h2>Index</h2>


