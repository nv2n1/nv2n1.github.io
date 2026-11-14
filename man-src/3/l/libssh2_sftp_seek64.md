---
title: "libssh2_sftp_seek64(3)"
name: "libssh2_sftp_seek64"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_seek64/"
description: "libssh2_sftp_seek64 – set the read/write position within a file"
---

<h2>NAME</h2>
<p> libssh2_sftp_seek64 &#8211; set the read/write position within a file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
void libssh2_sftp_seek64(LIBSSH2_SFTP_HANDLE *handle,
                         libssh2_uint64_t offset);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>offset</i> &#8211; Number of bytes from the beginning of file to seek to. </p>
<p> Move the file handle&#8217;s internal pointer to an arbitrary location. libssh2 implements file pointers as a localized concept to make file access appear more POSIX like. No packets are exchanged with the server during a seek operation. The localized file pointer is simply used as a convenience offset during read/write operations. </p>
<p> You MUST NOT seek during writing or reading a file with SFTP, as the internals use outstanding packets and changing the &quot;file position&quot; during transit will results in badness.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
