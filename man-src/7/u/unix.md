---
title: "unix(7)"
name: "unix"
section: "7"
letter: "u"
url: "/docs/linux/man/7-unix/"
description: "unix – sockets for local interprocess communication"
---

<p>unix &#8211; sockets for local interprocess communication</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;

#include &lt;sys/un.h&gt;
unix_socket = socket(AF_UNIX, type, 0);

error = socketpair(AF_UNIX, type, 0, int *sv);</code></pre>
<h2>Description</h2>
<p>The <code>AF_UNIX</code> (also known as <code>AF_LOCAL</code>) socket family is used to communicate between processes on the same machine efficiently. Traditionally, UNIX domain sockets can be either unnamed, or bound to a filesystem pathname (marked as being of type socket). Linux also supports an abstract namespace which is independent of the filesystem. Valid socket types in the UNIX domain are: <code>SOCK_STREAM</code>, for a stream-oriented socket; <code>SOCK_DGRAM</code>, for a datagram-oriented socket that preserves message boundaries (as on most UNIX implementations, UNIX domain datagram sockets are always reliable and don&#8217;t reorder datagrams); and (since Linux 2.6.4) <code>SOCK_SEQPACKET</code>, for a sequenced-packet socket that is connection-oriented, preserves message boundaries, and delivers messages in the order that they were sent. UNIX domain sockets support passing file descriptors or process credentials to other processes using ancillary data.</p>
<h3>Address format</h3>
<p>A UNIX domain socket address is represented in the following structure: int value;<br />
error = ioctl(unix_socket, ioctl_type, &amp;value); The <i>sun_family</i> field always contains <code>AF_UNIX</code>. On Linux, <i>sun_path</i> is 108 bytes in size; see also NOTES, below. Various systems calls (for example, <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), and <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)) take a <i>sockaddr_un</i> argument as input. Some other system calls (for example, <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), and <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)) return an argument of this type. Three types of address are distinguished in the <i>sockaddr_un</i> structure:</p>
<dl>
<dt>*</p>
<dd><i>pathname</i>: a UNIX domain socket can be bound to a null-terminated filesystem pathname using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). When the address of a pathname socket is returned (by one of the system calls noted above), its length is</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offsetof(struct sockaddr_un, sun_path)&nbsp;+&nbsp;strlen(sun_path)&nbsp;+&nbsp;1</p>
<dd>and <i>sun_path</i> contains the null-terminated pathname. (On Linux, the above <code>offsetof</code>() expression equates to the same value as <i>sizeof(sa_family_t)</i>, but some other implementations include other fields before <i>sun_path</i>, so the <code>offsetof</code>() expression more portably describes the size of the address structure.)</p>
<dd>For further details of pathname sockets, see below.</p>
<dt>*</p>
<dd><i>unnamed</i>: A stream socket that has not been bound to a pathname using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) has no name. Likewise, the two sockets created by <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2) are unnamed. When the address of an unnamed socket is returned, its length is <i>sizeof(sa_family_t)</i>, and <i>sun_path</i> should not be inspected.</p>
<dt>*</p>
<dd><i>abstract</i>: an abstract socket address is distinguished (from a pathname socket) by the fact that <i>sun_path[0]</i> is a null byte (&#8216;
