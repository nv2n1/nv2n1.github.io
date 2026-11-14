---
title: "sendto(2)"
name: "sendto"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sendto/"
description: "send, sendto, sendmsg – send a message on a socket"
---

<h2 class="name">NAME</h2>
<p> send, sendto, sendmsg &#8211; send a message on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;
ssize_t send(int sockfd, const void *buf, size_t len, int flags);
ssize_t sendto(int sockfd, const void *buf, size_t len, int flags,
               const struct sockaddr *dest_addr, socklen_t addrlen);
ssize_t sendmsg(int sockfd, const struct msghdr *msg, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The system calls <code>send</code>(), <code>sendto</code>(), and <code>sendmsg</code>() are used to transmit a message to another socket. </p>
<p> The <code>send</code>() call may be used only when the socket is in a <i>connected</i> state (so that the intended recipient is known). The only difference between <code>send</code>() and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) is the presence of <i>flags</i>. With a zero <i>flags</i> argument, <code>send</code>() is equivalent to <code><a href="/docs/linux/man/2-write/">write</a></code>(2). Also, the following call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;send(sockfd, buf, len, flags); </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sendto(sockfd, buf, len, flags, NULL, 0); </p>
<p> The argument <i>sockfd</i> is the file descriptor of the sending socket. </p>
<p> If <code>sendto</code>() is used on a connection-mode (<code>SOCK_STREAM</code>, <code>SOCK_SEQPACKET</code>) socket, the arguments <i>dest_addr</i> and <i>addrlen</i> are ignored (and the error <code>EISCONN</code> may be returned when they are not NULL and 0), and the error <code>ENOTCONN</code> is returned when the socket was not actually connected. Otherwise, the address of the target is given by <i>dest_addr</i> with <i>addrlen</i> specifying its size. For <code>sendmsg</code>(), the address of the target is given by <i>msg.msg_name</i>, with <i>msg.msg_namelen</i> specifying its size. </p>
<p> For <code>send</code>() and <code>sendto</code>(), the message is found in <i>buf</i> and has length <i>len</i>. For <code>sendmsg</code>(), the message is pointed to by the elements of the array <i>msg.msg_iov</i>. The <code>sendmsg</code>() call also allows sending ancillary data (also known as control information). </p>
<p> If the message is too long to pass atomically through the underlying protocol, the error <code>EMSGSIZE</code> is returned, and the message is not transmitted. </p>
<p> No indication of failure to deliver is implicit in a <code>send</code>(). Locally detected errors are indicated by a return value of -1. </p>
<p> When the message does not fit into the send buffer of the socket, <code>send</code>() normally blocks, unless the socket has been placed in nonblocking I/O mode. In nonblocking mode it would fail with the error <code>EAGAIN</code> or <code>EWOULDBLOCK</code> in this case. The <code><a href="/docs/linux/man/2-select/">select</a></code>(2) call may be used to determine when it is possible to send more data.</p>
<h3>The flags argument</h3>
<p> The <i>flags</i> argument is the bitwise OR of zero or more of the following flags.</p>
<dl>
<dt><code>MSG_CONFIRM</code> (since Linux 2.3.15)</p>
<dd> Tell the link layer that forward progress happened: you got a successful reply from the other side. If the link layer doesn&#8217;t get this it will regularly reprobe the neighbor (e.g., via a unicast ARP). Valid only on <code>SOCK_DGRAM</code> and <code>SOCK_RAW</code> sockets and currently implemented only for IPv4 and IPv6. See <code><a href="/docs/linux/man/7-arp/">arp</a></code>(7) for details.</p>
<dt><code>MSG_DONTROUTE</code></p>
<dd> Don&#8217;t use a gateway to send out the packet, send to hosts only on directly connected networks. This is usually used only by diagnostic or routing programs. This is defined only for protocol families that route; packet sockets don&#8217;t.</p>
<dt><code>MSG_DONTWAIT</code> (since Linux 2.2)</p>
<dd> Enables nonblocking operation; if the operation would block, <code>EAGAIN</code> or <code>EWOULDBLOCK</code> is returned. This provides similar behavior to setting the <code>O_NONBLOCK</code> flag (via the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFL</code> operation), but differs in that <code>MSG_DONTWAIT</code> is a per-call option, whereas <code>O_NONBLOCK</code> is a setting on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), which will affect all threads in the calling process and as well as other processes that hold file descriptors referring to the same open file description.</p>
<dt><code>MSG_EOR</code> (since Linux 2.2)</p>
<dd> Terminates a record (when this notion is supported, as for sockets of type <code>SOCK_SEQPACKET</code>).</p>
<dt><code>MSG_MORE</code> (since Linux 2.4.4)</p>
<dd> The caller has more data to send. This flag is used with TCP sockets to obtain the same effect as the <code>TCP_CORK</code> socket option (see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)), with the difference that this flag can be set on a per-call basis.</p>
<dt>
<dd> Since Linux 2.6, this flag is also supported for UDP sockets, and informs the kernel to package all of the data sent in calls with this flag set into a single datagram which is transmitted only when a call is performed that does not specify this flag. (See also the <code>UDP_CORK</code> socket option described in <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7).)</p>
<dt><code>MSG_NOSIGNAL</code> (since Linux 2.2)</p>
<dd> Don&#8217;t generate a <code>SIGPIPE</code> signal if the peer on a stream-oriented socket has closed the connection. The <code>EPIPE</code> error is still returned. This provides similar behavior to using <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) to ignore <code>SIGPIPE</code>, but, whereas <code>MSG_NOSIGNAL</code> is a per-call feature, ignoring <code>SIGPIPE</code> sets a process attribute that affects all threads in the process.</p>
<dt><code>MSG_OOB</code></p>
<dd> Sends <i>out-of-band</i> data on sockets that support this notion (e.g., of type <code>SOCK_STREAM</code>); the underlying protocol must also support <i>out-of-band</i> data.</dl>
<h3>sendmsg()</h3>
<p> The definition of the <i>msghdr</i> structure employed by <code>sendmsg</code>() is as follows: </p>
<p> struct msghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*msg_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Optional address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;socklen_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_namelen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec&nbsp;*msg_iov;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Scatter/gather array&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_iovlen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;elements in msg_iov&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*msg_control;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ancillary data, see below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_controllen;&nbsp;/*&nbsp;Ancillary data buffer len&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;(unused)&nbsp;*/ }; </p>
<p> The <i>msg_name</i> field is used on an unconnected socket to specify the target address for a datagram. It points to a buffer containing the address; the <i>msg_namelen</i> field should be set to the size of the address. For a connected socket, these fields should be specified as NULL and 0, respectively. </p>
<p> The <i>msg_iov</i> and <i>msg_iovlen</i> fields specify scatter-gather locations, as for <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2). </p>
<p> You may send control information (ancillary data) using the <i>msg_control</i> and <i>msg_controllen</i> members. The maximum control buffer length the kernel can process is limited per socket by the value in <i>/proc/sys/net/core/optmem_max</i>; see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). For further information on the use of ancillary data in various socket domains, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) and <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). </p>
<p> The <i>msg_flags</i> field is ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success, these calls return the number of bytes sent. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> These are some standard errors generated by the socket layer. Additional errors may be generated and returned from the underlying protocol modules; see their respective manual pages.</p>
<dl>
<dt><code>EACCES</code></p>
<dd> (For UNIX domain sockets, which are identified by pathname) Write permission is denied on the destination socket file, or search permission is denied for one of the directories the path prefix. (See <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt>
<dd> (For UDP sockets) An attempt was made to send to a network/broadcast address as though it was a unicast address.</p>
<dt><code>EAGAIN</code> or <code>EWOULDBLOCK</code></p>
<dd> The socket is marked nonblocking and the requested operation would block. POSIX.1-2001 allows either error to be returned for this case, and does not require these constants to have the same value, so a portable application should check for both possibilities.</p>
<dt><code>EAGAIN</code></p>
<dd> (Internet domain datagram sockets) The socket referred to by <i>sockfd</i> had not previously been bound to an address and, upon attempting to bind it to an ephemeral port, it was determined that all port numbers in the ephemeral port range are currently in use. See the discussion of <i>/proc/sys/net/ipv4/ip_local_port_range</i> in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>EALREADY</code></p>
<dd> Another Fast Open is in progress.</p>
<dt><code>EBADF</code></p>
<dd> <i>sockfd</i> is not a valid open file descriptor.</p>
<dt><code>ECONNRESET</code></p>
<dd> Connection reset by peer.</p>
<dt><code>EDESTADDRREQ</code></p>
<dd> The socket is not connection-mode, and no peer address is set.</p>
<dt><code>EFAULT</code></p>
<dd> An invalid user space address was specified for an argument.</p>
<dt><code>EINTR</code></p>
<dd> A signal occurred before any data was transmitted; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> Invalid argument passed.</p>
<dt><code>EISCONN</code></p>
<dd> The connection-mode socket was connected already but a recipient was specified. (Now either this error is returned, or the recipient specification is ignored.)</p>
<dt><code>EMSGSIZE</code></p>
<dd> The socket type requires that message be sent atomically, and the size of the message to be sent made this impossible.</p>
<dt><code>ENOBUFS</code></p>
<dd> The output queue for a network interface was full. This generally indicates that the interface has stopped sending, but may be caused by transient congestion. (Normally, this does not occur in Linux. Packets are just silently dropped when a device queue overflows.)</p>
<dt><code>ENOMEM</code></p>
<dd> No memory available.</p>
<dt><code>ENOTCONN</code></p>
<dd> The socket is not connected, and no target has been given.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> Some bit in the <i>flags</i> argument is inappropriate for the socket type.</p>
<dt><code>EPIPE</code></p>
<dd> The local end has been shut down on a connection oriented socket. In this case, the process will also receive a <code>SIGPIPE</code> unless <code>MSG_NOSIGNAL</code> is set.</dl>
<h2>CONFORMING TO</h2>
<p> 4.4BSD, SVr4, POSIX.1-2001. These interfaces first appeared in 4.2BSD. </p>
<p> POSIX.1-2001 describes only the <code>MSG_OOB</code> and <code>MSG_EOR</code> flags. POSIX.1-2008 adds a specification of <code>MSG_NOSIGNAL</code>. The <code>MSG_CONFIRM</code> flag is a Linux extension.</p>
<h2>NOTES</h2>
<p> According to POSIX.1-2001, the <i>msg_controllen</i> field of the <i>msghdr</i> structure should be typed as <i>socklen_t</i>, and the <i>msg_iovlen</i> field should be typed as <i>int</i>, but glibc currently types both as <i>size_t</i>. </p>
<p> See <code><a href="/docs/linux/man/2-sendmmsg/">sendmmsg</a></code>(2) for information about a Linux-specific system call that can be used to transmit multiple datagrams in a single call.</p>
<h2>BUGS</h2>
<p> Linux may return <code>EPIPE</code> instead of <code>ENOTCONN</code>.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>sendto</code>() is shown in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), <code><a href="/docs/linux/man/2-sendmmsg/">sendmmsg</a></code>(2), <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
