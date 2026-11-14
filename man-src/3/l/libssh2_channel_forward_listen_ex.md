---
title: "libssh2_channel_forward_listen_ex(3)"
name: "libssh2_channel_forward_listen_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_forward_listen_ex/"
description: "libssh2_channel_forward_listen_ex – listen to inbound connections"
---

<h2>NAME</h2>
<p> libssh2_channel_forward_listen_ex &#8211; listen to inbound connections</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_LISTENER * libssh2_channel_forward_listen_ex(LIBSSH2_SESSION *session, char *host, int port, int *bound_port, int queue_maxsize); </p>
<p> LIBSSH2_LISTENER * libssh2_channel_forward_listen(LIBSSH2_SESSION *session, int port); </p>
<h2>DESCRIPTION</h2>
<p> Instruct the remote SSH server to begin listening for inbound TCP/IP connections. New connections will be queued by the library until accepted by <i><a href="/docs/linux/man/3-libssh2_channel_forward_accept/">libssh2_channel_forward_accept</a>(3)</i>. </p>
<p> <i>session</i> &#8211; instance as returned by libssh2_session_init(). </p>
<p> <i>host</i> &#8211; specific address to bind to on the remote host. Binding to 0.0.0.0 (default when NULL is passed) will bind to all available addresses. </p>
<p> <i>port</i> &#8211; port to bind to on the remote host. When 0 is passed, the remote host will select the first available dynamic port. </p>
<p> <i>bound_port</i> &#8211; Populated with the actual port bound on the remote host. Useful when requesting dynamic port numbers. </p>
<p> <i>queue_maxsize</i> &#8211; Maximum number of pending connections to queue before rejecting further attempts. </p>
<p> <i><a href="/docs/linux/man/3-libssh2_channel_forward_listen/">libssh2_channel_forward_listen</a>(3)</i> is a macro.</p>
<h2>RETURN VALUE</h2>
<p> A newly allocated LIBSSH2_LISTENER instance or NULL on failure.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_PROTO</i> &#8211; An invalid SSH protocol response was received on the socket. </p>
<p> <i>LIBSSH2_ERROR_REQUEST_DENIED</i> &#8211; The remote server refused the request. </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_forward_accept/">libssh2_channel_forward_accept</a>(3)</code> </p>
<h2>Index</h2>
