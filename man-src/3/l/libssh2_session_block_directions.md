---
title: "libssh2_session_block_directions(3)"
name: "libssh2_session_block_directions"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_block_directions/"
description: "libssh2_session_block_directions – get directions to wait for"
---

<h2>NAME</h2>
<p> libssh2_session_block_directions &#8211; get directions to wait for</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_session_block_directions(LIBSSH2_SESSION *session);</p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> When any of libssh2 functions return <code>LIBSSH2_ERROR_EAGAIN</code> an application should wait for the socket to have data available for reading or writing. Depending on the return value of <i><a href="/docs/linux/man/3-libssh2_session_block_directions/">libssh2_session_block_directions</a>(3)</i> an application should wait for read, write or both.</p>
<h2>RETURN VALUE</h2>
<p> Returns the set of directions as a binary mask. Can be a combination of: </p>
<p> LIBSSH2_SESSION_BLOCK_INBOUND: Inbound direction blocked. </p>
<p> LIBSSH2_SESSION_BLOCK_OUTBOUND: Outbound direction blocked. </p>
<p> Application should wait for data to be available for socket prior to calling a libssh2 function again. If <code>LIBSSH2_SESSION_BLOCK_INBOUND</code> is set select should contain the session socket in readfds set. Correspondingly in case of <code>LIBSSH2_SESSION_BLOCK_OUTBOUND</code> writefds set should contain the socket.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.0 </p>
<h2>Index</h2>
