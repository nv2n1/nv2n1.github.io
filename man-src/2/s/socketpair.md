---
title: "socketpair(2)"
name: "socketpair"
section: "2"
letter: "s"
url: "/docs/linux/man/2-socketpair/"
description: "socketpair – create a pair of connected sockets"
---

<h2 class="name">NAME</h2>
<p> socketpair &#8211; create a pair of connected sockets </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code> /* See NOTES */<br />
 <code>#include &lt;sys/socket.h&gt;</code> </p>
<p> <code>int socketpair(int </code><i>domain</i><code>, int </code><i>type</i><code>, int </code><i>protocol</i><code>, int </code><i>sv</i><code>[2]);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>socketpair</code>() call creates an unnamed pair of connected sockets in the specified <i>domain</i>, of the specified <i>type</i>, and using the optionally specified <i>protocol</i>. For further details of these arguments, see <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2). </p>
<p> The file descriptors used in referencing the new sockets are returned in <i>sv[0]</i> and <i>sv[1]</i>. The two sockets are indistinguishable.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, <i>errno</i> is set appropriately, and <i>sv</i> is left unchanged </p>
<p> On Linux (and other systems), <code>socketpair</code>() does not modify <i>sv</i> on failure. A requirement standardizing this behavior was added in POSIX.1-2008 TC2.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAFNOSUPPORT</code></p>
<dd> The specified address family is not supported on this machine.</p>
<dt><code>EFAULT</code></p>
<dd> The address <i>sv</i> does not specify a valid part of the process address space.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The specified protocol does not support creation of socket pairs.</p>
<dt><code>EPROTONOSUPPORT</code></p>
<dd> The specified protocol is not supported on this machine.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.4BSD. <code>socketpair</code>() first appeared in 4.2BSD. It is generally portable to/from non-BSD systems supporting clones of the BSD socket layer (including System V variants).</p>
<h2>NOTES</h2>
<p> On Linux, the only supported domains for this call are <code>AF_UNIX</code> (or synonymously, <code>AF_LOCAL</code>) and <code>AF_TIPC</code> (since Linux 4.12). </p>
<p> Since Linux 2.6.27, <code>socketpair</code>() supports the <code>SOCK_NONBLOCK</code> and <code>SOCK_CLOEXEC</code> flags in the <i>type</i> argument, as described in <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2). </p>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
