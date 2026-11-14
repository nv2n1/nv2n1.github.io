---
title: "libssh2_channel_set_blocking(3)"
name: "libssh2_channel_set_blocking"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_set_blocking/"
description: "libssh2_channel_set_blocking – set or clear blocking mode on channel"
---

<h2>NAME</h2>
<p> libssh2_channel_set_blocking &#8211; set or clear blocking mode on channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_channel_set_blocking(LIBSSH2_CHANNEL *channel, int blocking);</p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; channel stream to set or clean blocking status on. </p>
<p> <i>blocking</i> &#8211; Set to a non-zero value to make the channel block, or zero to make it non-blocking. </p>
<p> Currently this is just a short cut call to <code><a href="/docs/linux/man/3-libssh2_session_set_blocking/">libssh2_session_set_blocking</a>(3)</code> and therefore will affect the session and all channels.</p>
<h2>RETURN VALUE</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_set_blocking/">libssh2_session_set_blocking</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_read_ex/">libssh2_channel_read_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_write_ex/">libssh2_channel_write_ex</a>(3)</code> </p>
<h2>Index</h2>
