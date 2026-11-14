---
title: "getsockname(2)"
name: "getsockname"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getsockname/"
description: "getsockname – get socket name"
---

<h2 class="name">NAME</h2>
<p> getsockname &#8211; get socket name </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
int getsockname(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>getsockname</code>() returns the current address to which the socket <i>sockfd</i> is bound, in the buffer pointed to by <i>addr</i>. The <i>addrlen</i> argument should be initialized to indicate the amount of space (in bytes) pointed to by <i>addr</i>. On return it contains the actual size of the socket address. </p>
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
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (<code>getsockname</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> For background on the <i>socklen_t</i> type, see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a></code>(3), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
