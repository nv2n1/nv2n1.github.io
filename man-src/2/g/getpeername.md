---
title: "getpeername(2)"
name: "getpeername"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getpeername/"
description: "getpeername – get name of connected peer socket"
---

<h2 class="name">NAME</h2>
<p> getpeername &#8211; get name of connected peer socket </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/socket.h&gt;</code> </p>
<p> <code>int getpeername(int </code><i>sockfd</i><code>, struct sockaddr *</code><i>addr</i><code>, socklen_t *</code><i>addrlen</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getpeername</code>() returns the address of the peer connected to the socket <i>sockfd</i>, in the buffer pointed to by <i>addr</i>. The <i>addrlen</i> argument should be initialized to indicate the amount of space pointed to by <i>addr</i>. On return it contains the actual size of the name returned (in bytes). The name is truncated if the buffer provided is too small. </p>
<p> The returned address is truncated if the buffer provided is too small; in this case, <i>addrlen</i> will return a value greater than was supplied to the call.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> The argument <i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> The <i>addr</i> argument points to memory not in a valid part of the process address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addrlen</i> is invalid (e.g., is negative).</p>
<dt><code>ENOBUFS</code></p>
<dd> Insufficient resources were available in the system to perform the operation.</p>
<dt><code>ENOTCONN</code></p>
<dd> The socket is not connected.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (<code>getpeername</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> For background on the <i>socklen_t</i> type, see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
<p> For stream sockets, once a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) has been performed, either socket can call <code>getpeername</code>() to obtain the address of the peer socket. On the other hand, datagram sockets are connectionless. Calling <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) on a datagram socket merely sets the peer address for outgoing datagrams sent with <code><a href="/docs/linux/man/2-write/">write</a></code>(2) or <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2). The caller of <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) can use <code>getpeername</code>() to obtain the peer address that it earlier set for the socket. However, the peer socket is unaware of this information, and calling <code>getpeername</code>() on the peer socket will return no useful information (unless a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) call was also executed on the peer). Note also that the receiver of a datagram can obtain the address of the sender when using <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
