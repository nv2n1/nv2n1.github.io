---
title: "libssh2_channel_close(3)"
name: "libssh2_channel_close"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_close/"
description: "libssh2_channel_close – close a channel"
---

<h2>NAME</h2>
<p> libssh2_channel_close &#8211; close a channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_close(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; active channel stream to set closed status on. </p>
<p> Close an active data channel. In practice this means sending an SSH_MSG_CLOSE packet to the remote host which serves as instruction that no further data will be sent to it. The remote host may still send data back until it sends its own close message in response. To wait for the remote end to close its connection as well, follow this command with <code><a href="/docs/linux/man/3-libssh2_channel_wait_closed/">libssh2_channel_wait_closed</a>(3)</code> </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
