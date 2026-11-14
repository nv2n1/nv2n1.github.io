---
title: "libssh2_session_free(3)"
name: "libssh2_session_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_free/"
description: "libssh2_session_free – frees resources associated with a session instance"
---

<h2>NAME</h2>
<p> libssh2_session_free &#8211; frees resources associated with a session instance</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_free(LIBSSH2_SESSION *session);</p>
<h2>DESCRIPTION</h2>
<p> Frees all resources associated with a session instance. Typically called after <code><a href="/docs/linux/man/3-libssh2_session_disconnect_ex/">libssh2_session_disconnect_ex</a>(3)</code></p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_session_disconnect_ex/">libssh2_session_disconnect_ex</a>(3)</code> </p>
<h2>Index</h2>
