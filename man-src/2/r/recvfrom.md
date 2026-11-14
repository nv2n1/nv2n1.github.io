---
title: "recvfrom(2)"
name: "recvfrom"
section: "2"
letter: "r"
url: "/docs/linux/man/2-recvfrom/"
description: "recv, recvfrom, recvmsg – receive a message from a socket"
---

<h2 class="name">NAME</h2>
<p> recv, recvfrom, recvmsg &#8211; receive a message from a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;
ssize_t recv(int sockfd, void *buf, size_t len, int flags);
ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags,
                 struct sockaddr *src_addr, socklen_t *addrlen);
ssize_t recvmsg(int sockfd, struct msghdr *msg, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>recv</code>(), <code>recvfrom</code>(), and <code>recvmsg</code>() calls are used to receive messages from a socket. They may be used to receive data on both connectionless and connection-oriented sockets. This page first describes common features of all three system calls, and then describes the differences between the calls. </p>
<p> The only difference between <code>recv</code>() and <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is the presence of <i>flags</i>. With a zero <i>flags</i> argument, <code>recv</code>() is generally equivalent to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) (but see NOTES). Also, the following call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;recv(sockfd, buf, len, flags); </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;recvfrom(sockfd, buf, len, flags, NULL, NULL); </p>
<p> All three calls return the length of the message on successful completion. If a message is too long to fit in the supplied buffer, excess bytes may be discarded depending on the type of socket the message is received from. </p>
<p> If no messages are available at the socket, the receive calls wait for a message to arrive, unless the socket is nonblocking (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)), in which case the value -1 is returned and the external variable <i>errno</i> is set to <code>EAGAIN</code> or <code>EWOULDBLOCK</code>. The receive calls normally return any data available, up to the requested amount, rather than waiting for receipt of the full amount requested. </p>
<p> An application can use <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) to determine when more data arrives on a socket.</p>
<h3>The flags argument</h3>
<p> The <i>flags</i> argument is formed by ORing one or more of the following values:</p>
<dl>
<dt><code>MSG_CMSG_CLOEXEC</code> (<code>recvmsg</code>() only; since Linux 2.6.23)</p>
<dd> Set the close-on-exec flag for the file descriptor received via a UNIX domain file descriptor using the <code>SCM_RIGHTS</code> operation (described in <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)). This flag is useful for the same reasons as the <code>O_CLOEXEC</code> flag of <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>MSG_DONTWAIT</code> (since Linux 2.2)</p>
<dd> Enables nonblocking operation; if the operation would block, the call fails with the error <code>EAGAIN</code> or <code>EWOULDBLOCK</code>. This provides similar behavior to setting the <code>O_NONBLOCK</code> flag (via the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFL</code> operation), but differs in that <code>MSG_DONTWAIT</code> is a per-call option, whereas <code>O_NONBLOCK</code> is a setting on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), which will affect all threads in the calling process and as well as other processes that hold file descriptors referring to the same open file description.</p>
<dt><code>MSG_ERRQUEUE</code> (since Linux 2.2)</p>
<dd> This flag specifies that queued errors should be received from the socket error queue. The error is passed in an ancillary message with a type dependent on the protocol (for IPv4 <code>IP_RECVERR</code>). The user should supply a buffer of sufficient size. See <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3) and <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) for more information. The payload of the original packet that caused the error is passed as normal data via <i>msg_iovec</i>. The original destination address of the datagram that caused the error is supplied via <i>msg_name</i>.</p>
<dt>
<dd> The error is supplied in a <i>sock_extended_err</i> structure:</p>
<dt>
<dd> #define SO_EE_ORIGIN_NONE 0 #define SO_EE_ORIGIN_LOCAL 1 #define SO_EE_ORIGIN_ICMP 2 #define SO_EE_ORIGIN_ICMP6 3 </p>
<p> struct sock_extended_err {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_errno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Error number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_origin;&nbsp;<wbr>&nbsp;/*&nbsp;Where the error originated&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_pad;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Padding&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_info;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Additional information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_data;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Other data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;More data may follow&nbsp;*/ }; </p>
<p> struct sockaddr *SO_EE_OFFENDER(struct sock_extended_err *);</p>
<dt>
<dd> <i>ee_errno</i> contains the <i>errno</i> number of the queued error. <i>ee_origin</i> is the origin code of where the error originated. The other fields are protocol-specific. The macro <code>SOCK_EE_OFFENDER</code> returns a pointer to the address of the network object where the error originated from given a pointer to the ancillary message. If this address is not known, the <i>sa_family</i> member of the <i>sockaddr</i> contains <code>AF_UNSPEC</code> and the other fields of the <i>sockaddr</i> are undefined. The payload of the packet that caused the error is passed as normal data.</p>
<dt>
<dd> For local errors, no address is passed (this can be checked with the <i>cmsg_len</i> member of the <i>cmsghdr</i>). For error receives, the <code>MSG_ERRQUEUE</code> flag is set in the <i>msghdr</i>. After an error has been passed, the pending socket error is regenerated based on the next queued error and will be passed on the next socket operation.</p>
<dt><code>MSG_OOB</code></p>
<dd> This flag requests receipt of out-of-band data that would not be received in the normal data stream. Some protocols place expedited data at the head of the normal data queue, and thus this flag cannot be used with such protocols.</p>
<dt><code>MSG_PEEK</code></p>
<dd> This flag causes the receive operation to return data from the beginning of the receive queue without removing that data from the queue. Thus, a subsequent receive call will return the same data.</p>
<dt><code>MSG_TRUNC</code> (since Linux 2.2)</p>
<dd> For raw (<code>AF_PACKET</code>), Internet datagram (since Linux 2.4.27/2.6.8), netlink (since Linux 2.6.22), and UNIX datagram (since Linux 3.4) sockets: return the real length of the packet or datagram, even when it was longer than the passed buffer.</p>
<dt>
<dd> For use with Internet stream sockets, see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7).</p>
<dt><code>MSG_WAITALL</code> (since Linux 2.2)</p>
<dd> This flag requests that the operation block until the full request is satisfied. However, the call may still return less data than requested if a signal is caught, an error or disconnect occurs, or the next data to be received is of a different type than that returned. This flag has no effect for datagram sockets.</dl>
<h3>recvfrom()</h3>
<p> <code>recvfrom</code>() places the received message into the buffer <i>buf</i>. The caller must specify the size of the buffer in <i>len</i>. </p>
<p> If <i>src_addr</i> is not NULL, and the underlying protocol provides the source address of the message, that source address is placed in the buffer pointed to by <i>src_addr</i>. In this case, <i>addrlen</i> is a value-result argument. Before the call, it should be initialized to the size of the buffer associated with <i>src_addr</i>. Upon return, <i>addrlen</i> is updated to contain the actual size of the source address. The returned address is truncated if the buffer provided is too small; in this case, <i>addrlen</i> will return a value greater than was supplied to the call. </p>
<p> If the caller is not interested in the source address, <i>src_addr</i> and <i>addrlen</i> should be specified as NULL.</p>
<h3>recv()</h3>
<p> The <code>recv</code>() call is normally used only on a <i>connected</i> socket (see <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)). It is equivalent to the call: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;recvfrom(fd, buf, len, flags, NULL, 0);</p>
<h3>recvmsg()</h3>
<p> The <code>recvmsg</code>() call uses a <i>msghdr</i> structure to minimize the number of directly supplied arguments. This structure is defined as follows in <i>&lt;sys/socket.h&gt;</i>: </p>
<p> struct iovec { /* Scatter/gather array items */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*iov_base;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t iov_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes to transfer&nbsp;*/ }; </p>
<p> struct msghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*msg_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Optional address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;socklen_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_namelen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec&nbsp;*msg_iov;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Scatter/gather array&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_iovlen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;elements in msg_iov&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*msg_control;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ancillary data, see below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_controllen;&nbsp;/*&nbsp;Ancillary data buffer len&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags on received message&nbsp;*/ }; </p>
<p> The <i>msg_name</i> field points to a caller-allocated buffer that is used to return the source address if the socket is unconnected. The caller should set <i>msg_namelen</i> to the size of this buffer before this call; upon return from a successful call, <i>msg_namelen</i> will contain the length of the returned address. If the application does not need to know the source address, <i>msg_name</i> can be specified as NULL. </p>
<p> The fields <i>msg_iov</i> and <i>msg_iovlen</i> describe scatter-gather locations, as discussed in <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2). </p>
<p> The field <i>msg_control</i>, which has length <i>msg_controllen</i>, points to a buffer for other protocol control-related messages or miscellaneous ancillary data. When <code>recvmsg</code>() is called, <i>msg_controllen</i> should contain the length of the available buffer in <i>msg_control</i>; upon return from a successful call it will contain the length of the control message sequence. </p>
<p> The messages are of the form: </p>
<p> struct cmsghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t cmsg_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Data byte count, including header<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(type is socklen_t in POSIX)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cmsg_level;&nbsp;<wbr>&nbsp;/*&nbsp;Originating protocol&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cmsg_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Protocol-specific type&nbsp;*/ /* followed by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char cmsg_data[];&nbsp;*/ }; </p>
<p> Ancillary data should be accessed only by the macros defined in <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3). </p>
<p> As an example, Linux uses this ancillary data mechanism to pass extended errors, IP options, or file descriptors over UNIX domain sockets. For further information on the use of ancillary data in various socket domains, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) and <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). </p>
<p> The <i>msg_flags</i> field in the <i>msghdr</i> is set on return of <code>recvmsg</code>(). It can contain several flags:</p>
<dl>
<dt><code>MSG_EOR</code></p>
<dd> indicates end-of-record; the data returned completed a record (generally used with sockets of type <code>SOCK_SEQPACKET</code>).</p>
<dt><code>MSG_TRUNC</code></p>
<dd> indicates that the trailing portion of a datagram was discarded because the datagram was larger than the buffer supplied.</p>
<dt><code>MSG_CTRUNC</code></p>
<dd> indicates that some control data was discarded due to lack of space in the buffer for ancillary data.</p>
<dt><code>MSG_OOB</code></p>
<dd> is returned to indicate that expedited or out-of-band data was received.</p>
<dt><code>MSG_ERRQUEUE</code></p>
<dd> indicates that no data was received but an extended error from the socket error queue.</dl>
<h2>RETURN VALUE</h2>
<p> These calls return the number of bytes received, or -1 if an error occurred. In the event of an error, <i>errno</i> is set to indicate the error. </p>
<p> When a stream socket peer has performed an orderly shutdown, the return value will be 0 (the traditional &quot;end-of-file&quot; return). </p>
<p> Datagram sockets in various domains (e.g., the UNIX and Internet domains) permit zero-length datagrams. When such a datagram is received, the return value is 0. </p>
<p> The value 0 may also be returned if the requested number of bytes to receive from a stream socket was 0.</p>
<h2>ERRORS</h2>
<p> These are some standard errors generated by the socket layer. Additional errors may be generated and returned from the underlying protocol modules; see their manual pages.</p>
<dl>
<dt><code>EAGAIN</code> or <code>EWOULDBLOCK</code></p>
<dd> The socket is marked nonblocking and the receive operation would block, or a receive timeout had been set and the timeout expired before data was received. POSIX.1 allows either error to be returned for this case, and does not require these constants to have the same value, so a portable application should check for both possibilities.</p>
<dt><code>EBADF</code></p>
<dd> The argument <i>sockfd</i> is an invalid file descriptor.</p>
<dt><code>ECONNREFUSED</code></p>
<dd> A remote host refused to allow the network connection (typically because it is not running the requested service).</p>
<dt><code>EFAULT</code></p>
<dd> The receive buffer pointer(s) point outside the process&#8217;s address space.</p>
<dt><code>EINTR</code></p>
<dd> The receive was interrupted by delivery of a signal before any data was available; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> Invalid argument passed.</p>
<dt><code>ENOMEM</code></p>
<dd> Could not allocate memory for <code>recvmsg</code>().</p>
<dt><code>ENOTCONN</code></p>
<dd> The socket is associated with a connection-oriented protocol and has not been connected (see <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) and <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)).</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.4BSD (these interfaces first appeared in 4.2BSD). </p>
<p> POSIX.1 describes only the <code>MSG_OOB</code>, <code>MSG_PEEK</code>, and <code>MSG_WAITALL</code> flags.</p>
<h2>NOTES</h2>
<p> If a zero-length datagram is pending, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code>recv</code>() with a <i>flags</i> argument of zero provide different behavior. In this circumstance, <code><a href="/docs/linux/man/2-read/">read</a></code>(2) has no effect (the datagram remains pending), while <code>recv</code>() consumes the pending datagram. </p>
<p> The <i>socklen_t</i> type was invented by POSIX. See also <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
<p> According to POSIX.1, the <i>msg_controllen</i> field of the <i>msghdr</i> structure should be typed as <i>socklen_t</i>, and the <i>msg_iovlen</i> field should be typed as <i>int</i>, but glibc currently types both as <i>size_t</i>. </p>
<p> See <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2) for information about a Linux-specific system call that can be used to receive multiple datagrams in a single call.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>recvfrom</code>() is shown in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3), <code><a href="/docs/linux/man/3-sockatmark/">sockatmark</a></code>(3), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
