---
title: "libssh2_sftp_tell(3)"
name: "libssh2_sftp_tell"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_tell/"
description: "libssh2_sftp_tell – get the current read/write position indicator for a file"
---

<h2>NAME</h2>
<p> libssh2_sftp_tell &#8211; get the current read/write position indicator for a file</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; #include &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> size_t libssh2_sftp_tell(LIBSSH2_SFTP_HANDLE *handle); </p>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code>. </p>
<p> Returns the current offset of the file handle&#8217;s internal pointer. Note that this is now deprecated. Use the newer <code><a href="/docs/linux/man/3-libssh2_sftp_tell64/">libssh2_sftp_tell64</a>(3)</code> instead!</p>
<h2>RETURN VALUE</h2>
<p> Current offset from beginning of file in bytes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_sftp_tell64/">libssh2_sftp_tell64</a>(3)</code> </p>
<h2>Index</h2>
