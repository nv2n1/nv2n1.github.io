---
title: "libssh2_sftp_init(3)"
name: "libssh2_sftp_init"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_init/"
description: "libssh2_sftp_init – open SFTP channel for the given SSH session."
---

<h2>NAME</h2>
<p> libssh2_sftp_init &#8211; open SFTP channel for the given SSH session.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> LIBSSH2_SFTP * libssh2_sftp_init(LIBSSH2_SESSION *session); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> Open a channel and initialize the SFTP subsystem. Although the SFTP subsystem operates over the same type of channel as those exported by the Channel API, the protocol itself implements its own unique binary packet protocol which must be managed with the libssh2_sftp_*() family of functions. When an SFTP session is complete, it must be destroyed using the <code><a href="/docs/linux/man/3-libssh2_sftp_shutdown/">libssh2_sftp_shutdown</a>(3)</code> function.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to the newly allocated SFTP instance or NULL on failure.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_shutdown/">libssh2_sftp_shutdown</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
