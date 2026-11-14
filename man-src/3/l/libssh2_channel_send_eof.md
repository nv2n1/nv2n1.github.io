---
title: "libssh2_channel_send_eof(3)"
name: "libssh2_channel_send_eof"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_send_eof/"
description: "libssh2_channel_send_eof – send EOF to remote server"
---

<h2>NAME</h2>
<p> libssh2_channel_send_eof &#8211; send EOF to remote server</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_send_eof(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> Tell the remote host that no further data will be sent on the specified channel. Processes typically interpret this as a closed stdin descriptor. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_wait_eof/">libssh2_channel_wait_eof</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_eof/">libssh2_channel_eof</a>(3)</code> </p>
<h2>Index</h2>
