---
title: "libssh2_sftp_open_ex(3)"
name: "libssh2_sftp_open_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_open_ex/"
description: "libssh2_sftp_open – open filehandle for file on SFTP."
---

<h2>NAME</h2>
<p> libssh2_sftp_open &#8211; open filehandle for file on SFTP.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
LIBSSH2_SFTP_HANDLE *
libssh2_sftp_open_ex(LIBSSH2_SFTP *sftp, const char *filename,
                     unsigned int filename_len, unsigned long flags,
                     long mode, int open_type);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <i><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</i> </p>
<p> <i>filename</i> &#8211; Remote file/directory resource to open </p>
<p> <i>filename_len</i> &#8211; Length of filename </p>
<p> <i>flags</i> &#8211; Any reasonable combination of the LIBSSH2_FXF_* constants:</p>
<dl>
<dt>
<dd>
<dl>
<dt>LIBSSH2_FXF_READ</p>
<dd> Open the file for reading.</p>
<dt>LIBSSH2_FXF_WRITE</p>
<dd> Open the file for writing. If both this and LIBSSH2_FXF_READ are specified, the file is opened for both reading and writing.</p>
<dt>LIBSSH2_FXF_APPEND</p>
<dd> Force all writes to append data at the end of the file.</p>
<dt>LIBSSH2_FXF_CREAT,</p>
<dd> If this flag is specified, then a new file will be created if one does not already exist (if LIBSSH2_FXF_TRUNC is specified, the new file will be truncated to zero length if it previously exists)</p>
<dt>LIBSSH2_FXF_TRUNC</p>
<dd> Forces an existing file with the same name to be truncated to zero length when creating a file by specifying LIBSSH2_FXF_CREAT. LIBSSH2_FXF_CREAT MUST also be specified if this flag is used.</p>
<dt>LIBSSH2_FXF_EXCL</p>
<dd> Causes the request to fail if the named file already exists. LIBSSH2_FXF_CREAT MUST also be specified if this flag is used. </p>
</dl>
</dl>
<p> <i>mode</i> &#8211; POSIX file permissions to assign if the file is being newly created. See the LIBSSH2_SFTP_S_* convenience defines in &lt;libssh2_s<a href="ftp://ftp.h">ftp.h</a>&gt; </p>
<p> <i>open_type</i> &#8211; Either of LIBSSH2_SFTP_OPENFILE (to open a file) or LIBSSH2_SFTP_OPENDIR (to open a directory).</p>
<h2>RETURN VALUE</h2>
<p> A pointer to the newly created LIBSSH2_SFTP_HANDLE instance or NULL on failure.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call would block.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_close_handle/">libssh2_sftp_close_handle</a>(3)</code> </p>
<h2>Index</h2>
