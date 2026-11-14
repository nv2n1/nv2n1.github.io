---
title: "libssh2_sftp_read(3)"
name: "libssh2_sftp_read"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_read/"
description: "libssh2_sftp_read – read data from an SFTP handle"
---

<h2>NAME</h2>
<p> libssh2_sftp_read &#8211; read data from an SFTP handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> ssize_t libssh2_sftp_read(LIBSSH2_SFTP_HANDLE *handle, char *buffer, size_t buffer_maxlen); </p>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> is the SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>buffer</i> is a pointer to a pre-allocated buffer of at least </p>
<p> <i>buffer_maxlen</i> bytes to read data into. </p>
<p> Reads a block of data from an LIBSSH2_SFTP_HANDLE. This method is modelled after the POSIX <code><a href="/docs/linux/man/2-read/">read</a>(2)</code> function and uses the same calling semantics. <code><a href="/docs/linux/man/3-libssh2_sftp_read/">libssh2_sftp_read</a>(3)</code> will attempt to read as much as possible however it may not fill all of buffer if the file pointer reaches the end or if further reads would cause the socket to block.</p>
<h2>RETURN VALUE</h2>
<p> Number of bytes actually populated into buffer, or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_sftp_read/">libssh2_sftp_read</a>(3)</code> </p>
<h2>Index</h2>
