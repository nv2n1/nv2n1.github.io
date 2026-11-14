---
title: "libssh2_userauth_authenticated(3)"
name: "libssh2_userauth_authenticated"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_authenticated/"
description: "libssh2_userauth_authenticated – return authentication status"
---

<h2>NAME</h2>
<p> libssh2_userauth_authenticated &#8211; return authentication status</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_userauth_authenticated(LIBSSH2_SESSION *session); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> Indicates whether or not the named session has been successfully authenticated. </p>
<h2>RETURN VALUE</h2>
<p> Returns 1 if authenticated and 0 if not. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
