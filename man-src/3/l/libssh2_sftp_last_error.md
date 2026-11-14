---
title: "libssh2_sftp_last_error(3)"
name: "libssh2_sftp_last_error"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_last_error/"
description: "libssh2_sftp_last_error – return the last SFTP-specific error code"
---

<h2>NAME</h2>
<p> libssh2_sftp_last_error &#8211; return the last SFTP-specific error code</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> unsigned long libssh2_sftp_last_error(LIBSSH2_SFTP *sftp); </p>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> Returns the last error code produced by the SFTP layer. Note that this only returns a sensible error code if libssh2 returned LIBSSH2_ERROR_SFTP_PROTOCOL in a previous call. Using <code><a href="/docs/linux/man/3-libssh2_sftp_last_error/">libssh2_sftp_last_error</a>(3)</code> without a preceding SFTP protocol error, it will return an unspecified value. </p>
<h2>RETURN VALUE</h2>
<p> Current error code state of the SFTP instance. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
