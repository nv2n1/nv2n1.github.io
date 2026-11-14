---
title: "libssh2_scp_send_ex(3)"
name: "libssh2_scp_send_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_scp_send_ex/"
description: "libssh2_scp_send_ex – Send a file via SCP"
---

<h2>NAME</h2>
<p> libssh2_scp_send_ex &#8211; Send a file via SCP</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
LIBSSH2_CHANNEL *
libssh2_scp_send_ex(LIBSSH2_SESSION *session, const char *path, int mode,
                    size_t size, long mtime, long atime);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function has been deemed deprecated since libssh2 1.2.6. See <i><a href="/docs/linux/man/3-libssh2_scp_send64/">libssh2_scp_send64</a>(3)</i>. </p>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>path</i> &#8211; Full path and filename of file to transfer to. That is the remote file name. </p>
<p> <i>mode</i> &#8211; File access mode to create file with </p>
<p> <i>size</i> &#8211; Size of file being transmitted (Must be known ahead of time precisely) </p>
<p> <i>mtime</i> &#8211; mtime to assign to file being created </p>
<p> <i>atime</i> &#8211; atime to assign to file being created (Set this and mtime to zero to instruct remote host to use current time). </p>
<p> Send a file to the remote host via SCP.</p>
<h2>RETURN VALUE</h2>
<p> Pointer to a newly allocated LIBSSH2_CHANNEL instance, or NULL on errors. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SCP_PROTOCOL</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block.</p>
<h2>AVAILABILITY</h2>
<p> This function was marked deprecated in libssh2 1.2.6 as<br />
&nbsp;<wbr><i><a href="/docs/linux/man/3-libssh2_scp_send64/">libssh2_scp_send64</a>(3)</i>&nbsp;<wbr>has been introduced to replace this function.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
