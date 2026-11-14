---
title: "libssh2_sftp_mkdir_ex(3)"
name: "libssh2_sftp_mkdir_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_mkdir_ex/"
description: "libssh2_sftp_mkdir_ex – create a directory on the remote file system"
---

<h2>NAME</h2>
<p> libssh2_sftp_mkdir_ex &#8211; create a directory on the remote file system</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> int libssh2_sftp_mkdir_ex(LIBSSH2_SFTP *sftp, const char *path, unsigned int path_len, long mode); </p>
<p> int libssh2_sftp_mkdir(LIBSSH2_SFTP *sftp, const char *path, long mode);</p>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>path</i> &#8211; full path of the new directory to create. Note that the new directory&#8217;s parents must all exist priot to making this call. </p>
<p> <i>path_len</i> &#8211; length of the full path of the new directory to create. </p>
<p> <i>mode</i> &#8211; directory creation mode (e.g. 0755). </p>
<p> Create a directory on the remote file system.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
