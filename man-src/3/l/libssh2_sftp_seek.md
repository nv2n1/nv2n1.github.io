---
title: "libssh2_sftp_seek(3)"
name: "libssh2_sftp_seek"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_seek/"
description: "libssh2_sftp_seek – set the read/write position indicator within a file"
---

<h2>NAME</h2>
<p> libssh2_sftp_seek &#8211; set the read/write position indicator within a file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
void libssh2_sftp_seek(LIBSSH2_SFTP_HANDLE *handle, size_t offset);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Deprecated function. Use <i><a href="/docs/linux/man/3-libssh2_sftp_seek64/">libssh2_sftp_seek64</a>(3)</i> instead! </p>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>offset</i> &#8211; Number of bytes from the beginning of file to seek to. </p>
<p> Move the file handle&#8217;s internal pointer to an arbitrary location. Note that libssh2 implements file pointers as a localized concept to make file access appear more POSIX like. No packets are exchanged with the server during a seek operation. The localized file pointer is simply used as a convenience offset during read/write operations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_sftp_seek64/">libssh2_sftp_seek64</a>(3)</code> </p>
<h2>Index</h2>
