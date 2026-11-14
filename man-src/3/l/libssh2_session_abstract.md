---
title: "libssh2_session_abstract(3)"
name: "libssh2_session_abstract"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_abstract/"
description: "libssh2_session_abstract – return a pointer to a session’s abstract pointer"
---

<h2>NAME</h2>
<p> libssh2_session_abstract &#8211; return a pointer to a session&#8217;s abstract pointer</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void ** libssh2_session_abstract(LIBSSH2_SESSION *session); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> Return a pointer to where the abstract pointer provided to <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> is stored. By providing a doubly de-referenced pointer, the internal storage of the session instance may be modified in place. </p>
<h2>RETURN VALUE</h2>
<p> A pointer to session internal storage whos contents point to previously provided abstract data. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
