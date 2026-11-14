---
title: "libssh2_session_last_errno(3)"
name: "libssh2_session_last_errno"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_last_errno/"
description: "libssh2_session_last_errno – get the most recent error number"
---

<h2>NAME</h2>
<p> libssh2_session_last_errno &#8211; get the most recent error number</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_last_errno(LIBSSH2_SESSION *session); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> Determine the most recent error condition. </p>
<h2>RETURN VALUE</h2>
<p> Numeric error code corresponding to the the Error Code constants. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_last_error/">libssh2_session_last_error</a>(3)</code> </p>
<h2>Index</h2>
