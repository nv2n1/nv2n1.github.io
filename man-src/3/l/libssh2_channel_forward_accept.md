---
title: "libssh2_channel_forward_accept(3)"
name: "libssh2_channel_forward_accept"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_forward_accept/"
description: "libssh2_channel_forward_accept – accept a queued connection"
---

<h2>NAME</h2>
<p> libssh2_channel_forward_accept &#8211; accept a queued connection</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_CHANNEL * libssh2_channel_forward_accept(LIBSSH2_LISTENER *listener); </p>
<h2>DESCRIPTION</h2>
<p> <i>listener</i> is a forwarding listener instance as returned by <code><a href="/docs/linux/man/3-libssh2_channel_forward_listen_ex/">libssh2_channel_forward_listen_ex</a>(3)</code>.</p>
<h2>RETURN VALUE</h2>
<p> A newly allocated channel instance or NULL on failure.</p>
<h2>ERRORS</h2>
<p> When this function returns NULL use <i><a href="/docs/linux/man/3-libssh2_session_last_errno/">libssh2_session_last_errno</a>(3)</i> to extract the error code. If that code is <i>LIBSSH2_ERROR_EAGAIN</i>, the session is set to do non-blocking I/O but the call would block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_forward_listen_ex/">libssh2_channel_forward_listen_ex</a>(3)</code> </p>
<h2>Index</h2>
