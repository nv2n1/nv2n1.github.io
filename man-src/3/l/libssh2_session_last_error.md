---
title: "libssh2_session_last_error(3)"
name: "libssh2_session_last_error"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_last_error/"
description: "libssh2_session_last_error – get the most recent error"
---

<h2>NAME</h2>
<p> libssh2_session_last_error &#8211; get the most recent error</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_last_error(LIBSSH2_SESSION *session, char **errmsg, int *errmsg_len, int want_buf); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>errmsg</i> &#8211; If not NULL, is populated by reference with the human readable form of the most recent error message. </p>
<p> <i>errmsg_len</i> &#8211; If not NULL, is populated by reference with the length of errmsg. (The string is NUL-terminated, so the length is only useful as an optimization, to avoid calling strlen.) </p>
<p> <i>want_buf</i> &#8211; If set to a non-zero value, &quot;ownership&quot; of the errmsg buffer will be given to the calling scope. If necessary, the errmsg buffer will be duplicated. </p>
<p> Determine the most recent error condition and its cause. </p>
<h2>RETURN VALUE</h2>
<p> Numeric error code corresponding to the the Error Code constants. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_last_errno/">libssh2_session_last_errno</a>(3)</code> </p>
<h2>Index</h2>
