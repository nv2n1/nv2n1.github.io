---
title: "rsocket(7)"
name: "rsocket"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rsocket/"
---

rsocket - RDMA socket API

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rsocket.h&gt;</code></pre>

<h2>Description</h2>

RDMA socket API and protocol

<h2>Notes</h2>

Rsockets is a protocol over RDMA that supports a socket-level API for applications. Rsocket APIs are intended to match the behavior of corresponding socket calls, except where noted. Rsocket functions match the name and function signature of socket calls, with the exception that all function calls are prefixed with an 'r'. 

 The following functions are defined: 

 rsocket 

 rbind, rlisten, raccept, rconnect 

 rshutdown, rclose 

 rrecv, rrecvfrom, rrecvmsg, rread, rreadv 

 rsend, rsendto, rsendmsg, rwrite, rwritev 

 rpoll, rselect 

 rgetpeername, rgetsockname 

 rsetsockopt, rgetsockopt, rfcntl 

 Functions take the same parameters as that used for sockets. The follow capabilities and flags are supported at this time: 

 PF_INET, PF_INET6, SOCK_STREAM, SOCK_DGRAM 

 SOL_SOCKET - SO_ERROR, SO_KEEPALIVE (flag supported, but ignored), SO_LINGER, SO_OOBINLINE, SO_RCVBUF, SO_REUSEADDR, SO_SNDBUF 

 IPPROTO_TCP - TCP_NODELAY, TCP_MAXSEG 

 IPPROTO_IPV6 - IPV6_V6ONLY 

 MSG_DONTWAIT, MSG_PEEK, O_NONBLOCK 

 Rsockets provides extensions beyond normal socket routines that allow for direct placement of data into an application's buffer. This is also known as zero-copy support, since data is sent and received directly, bypassing copies into network controlled buffers. The following calls and options support direct data placement. 

 riomap, riounmap, riowrite
<dl><dt>off_t riomap(int socket, void *buf, size_t len, int prot, int flags, off_t offset)
<dd><dt>Riomap registers an application buffer with the RDMA hardware
<dd>associated with an rsocket. The buffer is registered either for local only access (PROT_NONE) or for remote write access (PROT_WRITE). When registered for remote access, the buffer is mapped to a given offset. The offset is either provided by the user, or if the user selects -1 for the offset, rsockets selects one. The remote peer may access an iomapped buffer directly by specifying the correct offset. The mapping is not guaranteed to be available until after the remote peer receives a data transfer initiated after riomap has completed.</dl>
 

 In order to enable the use of remote IO mapping calls on an rsocket, an application must set the number of IO mappings that are available to the remote peer. This may be done using the rsetsockopt RDMA_IOMAPSIZE option. By default, an rsocket does not support remote IO mappings. riounmap
<dl><dt>int riounmap(int socket, void *buf, size_t len)
<dd><dt>Riounmap removes the mapping between a buffer and an rsocket.
<dd></dl>
 

 riowrite
<dl><dt>size_t riowrite(int socket, const void *buf, size_t count, off_t offset, int flags)
<dd><dt>Riowrite allows an application to transfer data over an rsocket
<dd>directly into a remotely iomapped buffer. The remote buffer is specified through an offset parameter, which corresponds to a remote iomapped buffer. From the sender's perspective, riowrite behaves similar to rwrite. From a receiver's view, riowrite transfers are silently redirected into a pre- determined data buffer. Data is received automatically, and the receiver is not informed of the transfer. However, iowrite data is still considered part of the data stream, such that iowrite data will be written before a subsequent transfer is received. A message sent immediately after initiating an iowrite may be used to notify the receiver of the iowrite.</dl>
 

 In addition to standard socket options, rsockets supports options specific to RDMA devices and protocols. These options are accessible through rsetsockopt using SOL_RDMA option level.
<dl><dt>RDMA_SQSIZE - Integer size of the underlying send queue.
<dd><dt>RDMA_RQSIZE - Integer size of the underlying receive queue.
<dd><dt>RDMA_INLINE - Integer size of inline data.
<dd><dt>RDMA_IOMAPSIZE - Integer number of remote IO mappings supported
<dd><dt>RDMA_ROUTE - struct ibv_path_data of path record for connection.
<dd></dl>
 

 Note that rsockets fd's cannot be passed into non-rsocket calls. For applications which must mix rsocket fd's with standard socket fd's or opened files, rpoll and rselect support polling both rsockets and normal fd's. 

 Existing applications can make use of rsockets through the use of a preload library. Because rsockets implements an end-to-end protocol, both sides of a connection must use rsockets. The rdma_cm library provides such a preload library, librspreload. To reduce the chance of the preload library intercepting calls without the user's explicit knowledge, the librspreload library is installed into %libdir%/rsocket subdirectory. 

 The preload library can be used by setting LD_PRELOAD when running. Note that not all applications will work with rsockets. Support is limited based on the socket options used by the application. Support for fork() is limited, but available. To use rsockets with the preload library for applications that call fork, users must set the environment variable RDMAV_FORK_SAFE=1 on both the client and server side of the connection. In general, fork is supportable for server applications that accept a connection, then fork off a process to handle the new connection. 

 rsockets uses configuration files that give an administrator control over the default settings used by rsockets. Use files under /etc/rdma/rsocket as shown: 

 

 mem_default - default size of receive buffer(s) 

 wmem_default - default size of send buffer(s) 

 sqsize_default - default size of send queue 

 rqsize_default - default size of receive queue 

 inline_default - default size of inline data 

 iomap_size - default size of remote iomapping table 

 polling_time - default number of microseconds to poll for data before waiting 

 All configuration files should contain a single integer value. Values may be set by issuing a command similar to the following example. 

 echo 1000000 &gt; /etc/rdma/rsocket/mem_default 

 If configuration files are not available, rsockets uses internal defaults. Applications can override default values programmatically through the rsetsockopt routine.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7) 
