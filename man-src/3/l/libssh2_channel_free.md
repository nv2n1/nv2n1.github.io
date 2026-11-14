---
title: "libssh2_channel_free(3)"
name: "libssh2_channel_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_free/"
description: "libssh2_channel_free – free all resources associated with a channel"
---

<h2>NAME</h2>
<p> libssh2_channel_free &#8211; free all resources associated with a channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_free(LIBSSH2_CHANNEL *channel); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Channel stream to free. </p>
<p> Release all resources associated with a channel stream. If the channel has not yet been closed with <code><a href="/docs/linux/man/3-libssh2_channel_close/">libssh2_channel_close</a>(3)</code> , it will be called automatically so that the remote end may know that it can safely free its own resources. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_close/">libssh2_channel_close</a>(3)</code> </p>
<h2>Index</h2>
