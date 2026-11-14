---
title: "libssh2_sftp_stat_ex(3)"
name: "libssh2_sftp_stat_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_stat_ex/"
description: "libssh2_sftp_stat_ex – get status about an SFTP file"
---

<h2>NAME</h2>
<p> libssh2_sftp_stat_ex &#8211; get status about an SFTP file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_stat_ex(LIBSSH2_SFTP *sftp, const char *path,
                         unsigned int path_len, int stat_type,
                         LIBSSH2_SFTP_ATTRIBUTES *attrs);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>path</i> &#8211; Remote filesystem object to stat/lstat/setstat. </p>
<p> <i>path_len</i> &#8211; Length of the name of the remote filesystem object to stat/lstat/setstat. </p>
<p> <i>stat_type</i> &#8211; One of the three constants specifying the type of stat operation to perform: </p>
<p> <code>LIBSSH2_SFTP_STAT</code>: performs <a href="/docs/linux/man/2-stat/">stat</a>(2) operation<br />
 <code>LIBSSH2_SFTP_LSTAT</code>: performs <a href="/docs/linux/man/2-lstat/">lstat</a>(2) operation<br />
 <code>LIBSSH2_SFTP_SETSTAT</code>: performs operation to set stat info on file </p>
<p> <i>attrs</i> &#8211; Pointer to a <code>LIBSSH2_SFTP_ATTRIBUTES</code> structure to set file metadata from or into depending on the value of stat_type. </p>
<p> Get or Set statbuf type data on a remote filesystem object. When getting statbuf data, <code><a href="/docs/linux/man/3-libssh2_sftp_stat/">libssh2_sftp_stat</a>(3)</code> will follow all symlinks, while <code><a href="/docs/linux/man/3-libssh2_sftp_lstat/">libssh2_sftp_lstat</a>(3)</code> will return data about the object encountered, even if that object happens to be a symlink. </p>
<p> The LIBSSH2_SFTP_ATTRIBUTES struct looks like this: </p>
<pre><code>
struct LIBSSH2_SFTP_ATTRIBUTES {
    /* If flags &amp; ATTR_* bit is set, then the value in this struct will be
     * meaningful Otherwise it should be ignored
     */
    unsigned long flags;
    libssh2_uint64_t filesize;
    unsigned long uid;
    unsigned long gid;
    unsigned long permissions;
    unsigned long atime;
    unsigned long mtime;
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<h2>Index</h2>
