---
title: "libssh2_session_set_blocking(3)"
name: "libssh2_session_set_blocking"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_set_blocking/"
description: "libssh2_session_set_blocking – set or clear blocking mode on session"
---

<h2>NAME</h2>
<p> libssh2_session_set_blocking &#8211; set or clear blocking mode on session</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_session_set_blocking(LIBSSH2_SESSION *session, int blocking); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>blocking</i> &#8211; Set to a non-zero value to make the channel block, or zero to make it non-blocking. </p>
<p> Set or clear blocking mode on the selected on the session. This will instantly affect any channels associated with this session. If a read is performed on a session with no data currently available, a blocking session will wait for data to arrive and return what it receives. A non-blocking session will return immediately with an empty buffer. If a write is performed on a session with no room for more data, a blocking session will wait for room. A non-blocking session will return immediately without writing anything. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
