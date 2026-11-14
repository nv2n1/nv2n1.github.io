---
title: "libssh2_sftp_rmdir_ex(3)"
name: "libssh2_sftp_rmdir_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_rmdir_ex/"
description: "libssh2_sftp_rmdir_ex – remove an SFTP directory"
---

<h2>NAME</h2>
<p> libssh2_sftp_rmdir_ex &#8211; remove an SFTP directory</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_rmdir_ex(LIBSSH2_SFTP *sftp, const char *path,
                          unsigned int path_len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Remove a directory from the remote file system. </p>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>sourcefile</i> &#8211; Full path of the existing directory to remove. </p>
<p> <i>sourcefile_len</i> &#8211; Length of the full path of the existing directory to remove.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
