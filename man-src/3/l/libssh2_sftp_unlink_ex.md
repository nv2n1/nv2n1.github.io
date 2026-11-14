---
title: "libssh2_sftp_unlink_ex(3)"
name: "libssh2_sftp_unlink_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_unlink_ex/"
description: "libssh2_sftp_unlink_ex – unlink an SFTP file"
---

<h2>NAME</h2>
<p> libssh2_sftp_unlink_ex &#8211; unlink an SFTP file</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> int libssh2_sftp_unlink_ex(LIBSSH2_SFTP *sftp, const char *filename, unsigned int filename_len); </p>
<p> int libssh2_sftp_unlink(LIBSSH2_SFTP *sftp, const char *filename); </p>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>filename</i> &#8211; Path and name of the existing filesystem entry </p>
<p> <i>filename_len</i> &#8211; Length of the path and name of the existing filesystem entry </p>
<p> Unlink (delete) a file from the remote filesystem. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
