---
title: "libssh2_sftp_shutdown(3)"
name: "libssh2_sftp_shutdown"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_shutdown/"
description: "libssh2_sftp_shutdown – shut down an SFTP session"
---

<h2>NAME</h2>
<p> libssh2_sftp_shutdown &#8211; shut down an SFTP session</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> int libssh2_sftp_shutdown(LIBSSH2_SFTP *sftp); </p>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> Destroys a previously initialized SFTP session and frees all resources associated with it. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
