---
title: "listen(2)"
name: "listen"
section: "2"
letter: "l"
url: "/docs/linux/man/2-listen/"
description: "listen – listen for connections on a socket"
---

<h2 class="name">NAME</h2>
<p> listen &#8211; listen for connections on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt; /* See NOTES */
int listen(int sockfd, int backlog);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>listen</code>() marks the socket referred to by <i>sockfd</i> as a passive socket, that is, as a socket that will be used to accept incoming connection requests using <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
<p> The <i>sockfd</i> argument is a file descriptor that refers to a socket of type <code>SOCK_STREAM</code> or <code>SOCK_SEQPACKET</code>. </p>
<p> The <i>backlog</i> argument defines the maximum length to which the queue of pending connections for <i>sockfd</i> may grow. If a connection request arrives when the queue is full, the client may receive an error with an indication of <code>ECONNREFUSED</code> or, if the underlying protocol supports retransmission, the request may be ignored so that a later reattempt at connection succeeds.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EADDRINUSE</code></p>
<dd> Another socket is already listening on the same port.</p>
<dt><code>EADDRINUSE</code></p>
<dd> (Internet domain sockets) The socket referred to by <i>sockfd</i> had not previously been bound to an address and, upon attempting to bind it to an ephemeral port, it was determined that all port numbers in the ephemeral port range are currently in use. See the discussion of <i>/proc/sys/net/ipv4/ip_local_port_range</i> in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>EBADF</code></p>
<dd> The argument <i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The socket is not of a type that supports the <code>listen</code>() operation.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.4BSD (<code>listen</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> To accept connections, the following steps are performed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> A socket is created with <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2).</p>
<dt>2.</p>
<dd> The socket is bound to a local address using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), so that other sockets may be <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)ed to it.</p>
<dt>3.</p>
<dd> A willingness to accept incoming connections and a queue limit for incoming connections are specified with <code>listen</code>().</p>
<dt>4.</p>
<dd> Connections are accepted with <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2).</dl>
</dl>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> The behavior of the <i>backlog</i> argument on TCP sockets changed with Linux 2.2. Now it specifies the queue length for <i>completely</i> established sockets waiting to be accepted, instead of the number of incomplete connection requests. The maximum length of the queue for incomplete sockets can be set using <i>/proc/sys/net/ipv4/tcp_max_syn_backlog</i>. When syncookies are enabled there is no logical maximum length and this setting is ignored. See <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7) for more information. </p>
<p> If the <i>backlog</i> argument is greater than the value in <i>/proc/sys/net/core/somaxconn</i>, then it is silently truncated to that value. Since Linux 5.4, the default in this file is 4096; in earlier kernels, the default value is 128. In kernels before 2.4.25, this limit was a hard coded value, <code>SOMAXCONN</code>, with the value 128.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
