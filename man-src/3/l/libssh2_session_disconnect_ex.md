---
title: "libssh2_session_disconnect_ex(3)"
name: "libssh2_session_disconnect_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_disconnect_ex/"
description: "libssh2_session_disconnect_ex – terminate transport layer"
---

<h2>NAME</h2>
<p> libssh2_session_disconnect_ex &#8211; terminate transport layer</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_disconnect_ex(LIBSSH2_SESSION *session, int reason, const char *description, const char *lang); </p>
<p> int libssh2_session_disconnect(LIBSSH2_SESSION *session, const char *description); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>reason</i> &#8211; One of the Disconnect Reason constants. </p>
<p> <i>description</i> &#8211; Human readable reason for disconnection. </p>
<p> <i>lang</i> &#8211; Localization string describing the langauge/encoding of the description provided. </p>
<p> Send a disconnect message to the remote host associated with <i>session</i>, along with a <i>reason</i> symbol and a verbose <i>description</i>. </p>
<p> As a convenience, the macro <code><a href="/docs/linux/man/3-libssh2_session_disconnect/">libssh2_session_disconnect</a>(3)</code> is provided. It calls <code><a href="/docs/linux/man/3-libssh2_session_disconnect_ex/">libssh2_session_disconnect_ex</a>(3)</code> with <i>reason</i> set to SSH_DISCONNECT_BY_APPLICATION and <i>lang</i> set to an empty string. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
