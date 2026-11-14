---
title: "libssh2_sftp_symlink_ex(3)"
name: "libssh2_sftp_symlink_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_symlink_ex/"
description: "libssh2_sftp_symlink_ex – read or set a symbolic link"
---

<h2>NAME</h2>
<p> libssh2_sftp_symlink_ex &#8211; read or set a symbolic link</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_symlink_ex(LIBSSH2_SFTP *sftp, const char *path,
                            unsigned int path_len, char *target,
                            unsigned int target_len, int link_type);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create a symlink or read out symlink information from the remote side. </p>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>path</i> &#8211; Remote filesystem object to create a symlink from or resolve. </p>
<p> <i>path_len</i> &#8211; Length of the name of the remote filesystem object to create a symlink from or resolve. </p>
<p> <i>target</i> &#8211; a pointer to a buffer. The buffer has different uses depending what the <i>link_type</i> argument is set to.<br />
 <code>LIBSSH2_SFTP_SYMLINK</code>: Remote filesystem object to link to.<br />
 <code>LIBSSH2_SFTP_READLINK</code>: Pre-allocated buffer to resolve symlink target into.<br />
 <code>LIBSSH2_SFTP_REALPATH</code>: Pre-allocated buffer to resolve realpath target into. </p>
<p> <i>target_len</i> &#8211; Length of the name of the remote filesystem target object. </p>
<p> <i>link_type</i> &#8211; One of the three previously mentioned constants which determines the resulting behavior of this function. </p>
<p> These are convenience macros: </p>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_symlink/">libssh2_sftp_symlink</a>(3)</code> : Create a symbolic link between two filesystem objects.<br />
 <code><a href="/docs/linux/man/3-libssh2_sftp_readlink/">libssh2_sftp_readlink</a>(3)</code> : Resolve a symbolic link filesystem object to its next target.<br />
 <code><a href="/docs/linux/man/3-libssh2_sftp_realpath/">libssh2_sftp_realpath</a>(3)</code> : Resolve a complex, relative, or symlinked filepath to its effective target.</p>
<h2>RETURN VALUE</h2>
<p> When using LIBSSH2_SFTP_SYMLINK, this funtion returns 0 on success or negative on failure. </p>
<p> When using LIBSSH2_SFTP_READLINK or LIBSSH2_SFTP_REALPATH, it returns the number of bytes it copied to the target buffer (not including the terminating zero) or negative on failure. </p>
<p> It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<p> From 1.2.8, LIBSSH2_ERROR_BUFFER_TOO_SMALL is returned if the given &#8216;target&#8217; buffer is too small to fit the requested object name.</p>
<h2>BUG</h2>
<p> Passing in a too small buffer when receiving data only results in libssh2 1.2.7 or earlier to not copy the entire data amount, and it is not possible for the application to tell when it happens!</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
