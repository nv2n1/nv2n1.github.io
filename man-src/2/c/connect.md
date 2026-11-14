---
title: "connect(2)"
name: "connect"
section: "2"
letter: "c"
url: "/docs/linux/man/2-connect/"
description: "connect – initiate a connection on a socket"
---

<h2 class="name">NAME</h2>
<p> connect &#8211; initiate a connection on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt; /* See NOTES */
int connect(int sockfd, const struct sockaddr *addr,
            socklen_t addrlen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>connect</code>() system call connects the socket referred to by the file descriptor <i>sockfd</i> to the address specified by <i>addr</i>. The <i>addrlen</i> argument specifies the size of <i>addr</i>. The format of the address in <i>addr</i> is determined by the address space of the socket <i>sockfd</i>; see <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) for further details. </p>
<p> If the socket <i>sockfd</i> is of type <code>SOCK_DGRAM</code>, then <i>addr</i> is the address to which datagrams are sent by default, and the only address from which datagrams are received. If the socket is of type <code>SOCK_STREAM</code> or <code>SOCK_SEQPACKET</code>, this call attempts to make a connection to the socket that is bound to the address specified by <i>addr</i>. </p>
<p> Some protocol sockets (e.g., UNIX domain stream sockets) may successfully <code>connect</code>() only once. </p>
<p> Some protocol sockets (e.g., datagram sockets in the UNIX and Internet domains) may use <code>connect</code>() multiple times to change their association. </p>
<p> Some protocol sockets (e.g., TCP sockets as well as datagram sockets in the UNIX and Internet domains) may dissolve the association by connecting to an address with the <i>sa_family</i> member of <i>sockaddr</i> set to <code>AF_UNSPEC</code>; thereafter, the socket can be connected to another address. (<code>AF_UNSPEC</code> is supported on Linux since kernel 2.2.)</p>
<h2>RETURN VALUE</h2>
<p> If the connection or binding succeeds, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The following are general socket errors only. There may be other domain-specific error codes.</p>
<dl>
<dt><code>EACCES</code></p>
<dd> For UNIX domain sockets, which are identified by pathname: Write permission is denied on the socket file, or search permission is denied for one of the directories in the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EACCES</code>, <code>EPERM</code></p>
<dd> The user tried to connect to a broadcast address without having the socket broadcast flag enabled or the connection request failed because of a local firewall rule.</p>
<dt>
<dd> <code>EACCES</code> can also be returned if an SELinux policy denied a connection (for example, if there is a policy saying that an HTTP proxy can only connect to ports associated with HTTP servers, and the proxy tries to connect to a different port). dd</p>
<dt><code>EADDRINUSE</code></p>
<dd> Local address is already in use.</p>
<dt><code>EADDRNOTAVAIL</code></p>
<dd> (Internet domain sockets) The socket referred to by <i>sockfd</i> had not previously been bound to an address and, upon attempting to bind it to an ephemeral port, it was determined that all port numbers in the ephemeral port range are currently in use. See the discussion of <i>/proc/sys/net/ipv4/ip_local_port_range</i> in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>EAFNOSUPPORT</code></p>
<dd> The passed address didn&#8217;t have the correct address family in its <i>sa_family</i> field.</p>
<dt><code>EAGAIN</code></p>
<dd> For nonblocking UNIX domain sockets, the socket is nonblocking, and the connection cannot be completed immediately. For other socket families, there are insufficient entries in the routing cache.</p>
<dt><code>EALREADY</code></p>
<dd> The socket is nonblocking and a previous connection attempt has not yet been completed.</p>
<dt><code>EBADF</code></p>
<dd> <i>sockfd</i> is not a valid open file descriptor.</p>
<dt><code>ECONNREFUSED</code></p>
<dd> A <code>connect</code>() on a stream socket found no one listening on the remote address.</p>
<dt><code>EFAULT</code></p>
<dd> The socket structure address is outside the user&#8217;s address space.</p>
<dt><code>EINPROGRESS</code></p>
<dd> The socket is nonblocking and the connection cannot be completed immediately. (UNIX domain sockets failed with <code>EAGAIN</code> instead.) It is possible to <code><a href="/docs/linux/man/2-select/">select</a></code>(2) or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) for completion by selecting the socket for writing. After <code><a href="/docs/linux/man/2-select/">select</a></code>(2) indicates writability, use <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read the <code>SO_ERROR</code> option at level <code>SOL_SOCKET</code> to determine whether <code>connect</code>() completed successfully (<code>SO_ERROR</code> is zero) or unsuccessfully (<code>SO_ERROR</code> is one of the usual error codes listed here, explaining the reason for the failure).</p>
<dt><code>EINTR</code></p>
<dd> The system call was interrupted by a signal that was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EISCONN</code></p>
<dd> The socket is already connected.</p>
<dt><code>ENETUNREACH</code></p>
<dd> Network is unreachable.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</p>
<dt><code>EPROTOTYPE</code></p>
<dd> The socket type does not support the requested communications protocol. This error can occur, for example, on an attempt to connect a UNIX domain datagram socket to a stream socket.</p>
<dt><code>ETIMEDOUT</code></p>
<dd> Timeout while attempting connection. The server may be too busy to accept new connections. Note that for IP sockets the timeout may be very long when syncookies are enabled on the server.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD, (connect<code>()</code> first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> For background on the <i>socklen_t</i> type, see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
<p> If <code>connect</code>() fails, consider the state of the socket as unspecified. Portable applications should close the socket and create a new one for reconnecting.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>connect</code>() is shown in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
