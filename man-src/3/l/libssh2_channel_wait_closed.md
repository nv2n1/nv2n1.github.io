---
title: "libssh2_channel_wait_closed(3)"
name: "libssh2_channel_wait_closed"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_wait_closed/"
description: "libssh2_channel_wait_closed – wait for the remote to close the channel"
---

<h2>NAME</h2>
<p> libssh2_channel_wait_closed &#8211; wait for the remote to close the channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_wait_closed(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> Enter a temporary blocking state until the remote host closes the named channel. Typically sent after <i><a href="/docs/linux/man/3-libssh2_channel_close/">libssh2_channel_close</a>(3)</i> in order to examine the exit status. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_send_eof/">libssh2_channel_send_eof</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_eof/">libssh2_channel_eof</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_wait_eof/">libssh2_channel_wait_eof</a>(3)</code> </p>
<h2>Index</h2>
