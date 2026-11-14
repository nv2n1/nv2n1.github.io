---
title: "libssh2_channel_wait_eof(3)"
name: "libssh2_channel_wait_eof"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_wait_eof/"
description: "libssh2_channel_wait_eof – wait for the remote to reply to an EOF request"
---

<h2>NAME</h2>
<p> libssh2_channel_wait_eof &#8211; wait for the remote to reply to an EOF request</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_wait_eof(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> Wait for the remote end to acknowledge an EOF request. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_send_eof/">libssh2_channel_send_eof</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_eof/">libssh2_channel_eof</a>(3)</code> </p>
<h2>Index</h2>
