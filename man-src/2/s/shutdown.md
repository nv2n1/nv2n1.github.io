---
title: "shutdown(2)"
name: "shutdown"
section: "2"
letter: "s"
url: "/docs/linux/man/2-shutdown/"
description: "shutdown – shut down part of a full-duplex connection"
---

<h2 class="name">NAME</h2>
<p> shutdown &#8211; shut down part of a full-duplex connection </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/socket.h&gt;</code> </p>
<p> <code>int shutdown(int </code><i>sockfd</i><code>, int </code><i>how</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>shutdown</code>() call causes all or part of a full-duplex connection on the socket associated with <i>sockfd</i> to be shut down. If <i>how</i> is <code>SHUT_RD</code>, further receptions will be disallowed. If <i>how</i> is <code>SHUT_WR</code>, further transmissions will be disallowed. If <i>how</i> is <code>SHUT_RDWR</code>, further receptions and transmissions will be disallowed.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid value was specified in <i>how</i> (but see BUGS).</p>
<dt><code>ENOTCONN</code></p>
<dd> The specified socket is not connected.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.4BSD (<code>shutdown</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> The constants <code>SHUT_RD</code>, <code>SHUT_WR</code>, <code>SHUT_RDWR</code> have the value 0, 1, 2, respectively, and are defined in <i>&lt;sys/socket.h&gt;</i> since glibc-2.1.91.</p>
<h2>BUGS</h2>
<p> Checks for the validity of <i>how</i> are done in domain-specific code, and before Linux 3.7 not all domains performed these checks. Most notably, UNIX domain sockets simply ignored invalid values. This problem was fixed for UNIX domain sockets in Linux 3.7.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
