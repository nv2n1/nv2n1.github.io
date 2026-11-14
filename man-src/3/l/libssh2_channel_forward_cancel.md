---
title: "libssh2_channel_forward_cancel(3)"
name: "libssh2_channel_forward_cancel"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_forward_cancel/"
description: "libssh2_channel_forward_cancel – cancel a forwarded TCP port"
---

<h2>NAME</h2>
<p> libssh2_channel_forward_cancel &#8211; cancel a forwarded TCP port</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_forward_cancel(LIBSSH2_LISTENER *listener); </p>
<h2>DESCRIPTION</h2>
<p> <i>listener</i> &#8211; Forwarding listener instance as returned by <code><a href="/docs/linux/man/3-libssh2_channel_forward_listen_ex/">libssh2_channel_forward_listen_ex</a>(3)</code> </p>
<p> Instruct the remote host to stop listening for new connections on a previously requested host/port. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_forward_listen_ex/">libssh2_channel_forward_listen_ex</a>(3)</code> </p>
<h2>Index</h2>
