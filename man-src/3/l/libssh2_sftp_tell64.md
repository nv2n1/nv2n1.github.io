---
title: "libssh2_sftp_tell64(3)"
name: "libssh2_sftp_tell64"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_tell64/"
description: "libssh2_sftp_tell64 – get the current read/write position indicator for a file"
---

<h2>NAME</h2>
<p> libssh2_sftp_tell64 &#8211; get the current read/write position indicator for a file</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> libssh2_uint64_t libssh2_sftp_tell64(LIBSSH2_SFTP_HANDLE *handle); </p>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> Identify the current offset of the file handle&#8217;s internal pointer.</p>
<h2>RETURN VALUE</h2>
<p> Current offset from beginning of file in bytes.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_sftp_tell/">libssh2_sftp_tell</a>(3)</code> </p>
<h2>Index</h2>
