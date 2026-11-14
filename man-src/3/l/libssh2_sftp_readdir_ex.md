---
title: "libssh2_sftp_readdir_ex(3)"
name: "libssh2_sftp_readdir_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_readdir_ex/"
description: "libssh2_sftp_readdir_ex – read directory data from an SFTP handle"
---

<h2>NAME</h2>
<p> libssh2_sftp_readdir_ex &#8211; read directory data from an SFTP handle</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_readdir_ex(LIBSSH2_SFTP_HANDLE *handle,
                            char *buffer, size_t buffer_maxlen,
                            char *longentry, size_t longentry_maxlen,
                            LIBSSH2_SFTP_ATTRIBUTES *attrs);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Reads a block of data from a LIBSSH2_SFTP_HANDLE and returns file entry information for the next entry, if any. </p>
<p> <i>handle</i> &#8211; is the SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>buffer</i> &#8211; is a pointer to a pre-allocated buffer of at least <i>buffer_maxlen</i> bytes to read data into. </p>
<p> <i>buffer_maxlen</i> &#8211; is the length of buffer in bytes. If the length of the filename is longer than the space provided by buffer_maxlen it will be truncated to fit. </p>
<p> <i>longentry</i> &#8211; is a pointer to a pre-allocated buffer of at least <i>longentry_maxlen</i> bytes to read data into. The format of the `longname&#8217; field is unspecified by SFTP protocol. It MUST be suitable for use in the output of a directory listing command (in fact, the recommended operation for a directory listing command is to simply display this data). </p>
<p> <i>longentry_maxlen</i> &#8211; is the length of longentry in bytes. If the length of the full directory entry is longer than the space provided by <i>longentry_maxlen</i> it will be truncated to fit. </p>
<p> <i>attrs</i> &#8211; is a pointer to LIBSSH2_SFTP_ATTRIBUTES storage to populate statbuf style data into.</p>
<h2>RETURN VALUE</h2>
<p> Number of bytes actually populated into buffer (not counting the terminating zero), or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>BUG</h2>
<p> Passing in a too small buffer for &#8216;buffer&#8217; or &#8216;longentry&#8217; when receiving data only results in libssh2 1.2.7 or earlier to not copy the entire data amount, and it is not possible for the application to tell when it happens!</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<p> From 1.2.8, LIBSSH2_ERROR_BUFFER_TOO_SMALL is returned if any of the given &#8216;buffer&#8217; or &#8216;longentry&#8217; buffers are too small to fit the requested object name.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_sftp_close_handle/">libssh2_sftp_close_handle</a>(3)</code> </p>
<h2>Index</h2>
