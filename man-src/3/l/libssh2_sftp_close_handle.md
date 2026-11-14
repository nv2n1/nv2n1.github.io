---
title: "libssh2_sftp_close_handle(3)"
name: "libssh2_sftp_close_handle"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_close_handle/"
description: "libssh2_sftp_close_handle – close filehandle"
---

<h2>NAME</h2>
<p> libssh2_sftp_close_handle &#8211; close filehandle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> int libssh2_sftp_close_handle(LIBSSH2_SFTP_HANDLE *handle); </p>
<p> int libssh2_sftp_close(LIBSSH2_SFTP_HANDLE *handle); </p>
<p> int libssh2_sftp_closedir(LIBSSH2_SFTP_HANDLE *handle); </p>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> or <code><a href="/docs/linux/man/3-libssh2_sftp_opendir/">libssh2_sftp_opendir</a>(3)</code> (which is a macro). </p>
<p> Close an active LIBSSH2_SFTP_HANDLE. Because files and directories share the same underlying storage mechanism these methods may be used interchangably. <code><a href="/docs/linux/man/3-libssh2_sftp_close/">libssh2_sftp_close</a>(3)</code> and <code><a href="/docs/linux/man/3-libssh2_sftp_closedir/">libssh2_sftp_closedir</a>(3)</code> are macros for <code><a href="/docs/linux/man/3-libssh2_sftp_close_handle/">libssh2_sftp_close_handle</a>(3)</code>. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
