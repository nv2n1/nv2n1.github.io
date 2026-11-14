---
title: "libssh2_session_startup(3)"
name: "libssh2_session_startup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_startup/"
description: "libssh2_session_startup – begin transport layer"
---

<h2>NAME</h2>
<p> libssh2_session_startup &#8211; begin transport layer</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_startup(LIBSSH2_SESSION *session, int socket);</p>
<h2>DESCRIPTION</h2>
<p> Starting in libssh2 version 1.2.8 this function is considered deprecated. Use <i><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</i> instead. </p>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>socket</i> &#8211; Connected socket descriptor. Typically a TCP connection though the protocol allows for any reliable transport and the library will attempt to use any berkeley socket. </p>
<p> Begin transport layer protocol negotiation with the connected host.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, negative on failure.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_SOCKET_NONE</i> &#8211; The socket is invalid. </p>
<p> <i>LIBSSH2_ERROR_BANNER_SEND</i> &#8211; Unable to send banner to remote host. </p>
<p> <i>LIBSSH2_ERROR_KEX_FAILURE</i> &#8211; &gt;Encryption key exchange with the remote host failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_DISCONNECT</i> &#8211; The socket was disconnected. </p>
<p> <i>LIBSSH2_ERROR_PROTO</i> &#8211; An invalid SSH protocol response was received on the socket. </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_free/">libssh2_session_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
