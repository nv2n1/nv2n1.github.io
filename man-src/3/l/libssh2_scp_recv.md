---
title: "libssh2_scp_recv(3)"
name: "libssh2_scp_recv"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_scp_recv/"
description: "libssh2_scp_recv – request a remote file via SCP"
---

<h2>NAME</h2>
<p> libssh2_scp_recv &#8211; request a remote file via SCP</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_CHANNEL * libssh2_scp_recv(LIBSSH2_SESSION *session, const char *path, struct stat *sb); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>path</i> &#8211; Full path and filename of file to transfer. That is the remote file name. </p>
<p> <i>sb</i> &#8211; Populated with remote file&#8217;s size, mode, mtime, and atime </p>
<p> Request a file from the remote host via SCP.</p>
<h2>RETURN VALUE</h2>
<p> Pointer to a newly allocated LIBSSH2_CHANNEL instance, or NULL on errors.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SCP_PROTOCOL</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
