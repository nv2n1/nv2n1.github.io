---
title: "socketcall(2)"
name: "socketcall"
section: "2"
letter: "s"
url: "/docs/linux/man/2-socketcall/"
description: "socketcall – socket system calls"
---

<h2 class="name">NAME</h2>
<p> socketcall &#8211; socket system calls </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;linux/net.h&gt;</code> </p>
<p> <code>int socketcall(int </code><i>call</i><code>, unsigned long *</code><i>args</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>socketcall</code>() is a common kernel entry point for the socket system calls. <i>call</i> determines which socket function to invoke. <i>args</i> points to a block containing the actual arguments, which are passed through to the appropriate call. </p>
<p> User programs should call the appropriate functions by their usual names. Only standard library implementors and kernel hackers need to know about <code>socketcall</code>(). </p>
<table>
<tr VALIGN=top>
<td><i>call</i></td>
<td>Man page
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SOCKET</code> </td>
<td> <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_BIND</code> </td>
<td> <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_CONNECT</code> </td>
<td> <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_LISTEN</code> </td>
<td> <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_ACCEPT</code> </td>
<td> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_GETSOCKNAME</code> </td>
<td> <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_GETPEERNAME</code> </td>
<td> <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SOCKETPAIR</code> </td>
<td> <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SEND</code> </td>
<td> <code><a href="/docs/linux/man/2-send/">send</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_RECV</code> </td>
<td> <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SENDTO</code> </td>
<td> <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_RECVFROM</code> </td>
<td> <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SHUTDOWN</code> </td>
<td> <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SETSOCKOPT</code> </td>
<td> <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_GETSOCKOPT</code> </td>
<td> <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SENDMSG</code> </td>
<td> <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_RECVMSG</code> </td>
<td> <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_ACCEPT4</code> </td>
<td> <code><a href="/docs/linux/man/2-accept4/">accept4</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_RECVMMSG</code> </td>
<td> <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYS_SENDMMSG</code> </td>
<td> <code><a href="/docs/linux/man/2-sendmmsg/">sendmmsg</a></code>(2)
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This call is specific to Linux, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> On a some architectures&#8212;for example, x86-64 and ARM&#8212;there is no <code>socketcall</code>() system call; instead <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), and so on really are implemented as separate system calls. </p>
<p> On x86-32, <code>socketcall</code>() was historically the only entry point for the sockets API. However, starting in Linux 4.3, direct system calls are provided on x86-32 for the sockets API. This facilitates the creation of <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) filters that filter sockets system calls (for new user-space binaries that are compiled to use the new entry points) and also provides a (very) small performance improvement.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
