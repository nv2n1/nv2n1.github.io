---
title: "libssh2_sftp_fstatvfs(3)"
name: "libssh2_sftp_fstatvfs"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_fstatvfs/"
description: "libssh2_sftp_statvfs, libssh2_sftp_fstatvfs – get file system statistics"
---

<h2>NAME</h2>
<p> libssh2_sftp_statvfs, libssh2_sftp_fstatvfs &#8211; get file system statistics</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_statvfs(LIBSSH2_SFTP *sftp, const char *path,
                         size_t path_len, LIBSSH2_SFTP_STATVFS *st);
int libssh2_sftp_fstatvfs(LIBSSH2_SFTP_HANDLE *handle,
                          LIBSSH2_SFTP_STATVFS *st)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions provide <a href="/docs/linux/man/2-statvfs/">statvfs</a>(2)-like operations and require statvfs [at] openssh.com and fstatvfs [at] openssh.com extension support on the server. </p>
<p> <i>sftp</i> &#8211; SFTP instance as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_init/">libssh2_sftp_init</a>(3)</code> </p>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>path</i> &#8211; full path of any file within the mounted file system. </p>
<p> <i>path_len</i> &#8211; length of the full path. </p>
<p> <i>st</i> &#8211; Pointer to a LIBSSH2_SFTP_STATVFS structure to place file system statistics into. </p>
<h2>DATA TYPES</h2>
<p> LIBSSH2_SFTP_STATVFS is a typedefed struct that is defined as below </p>
<pre><code>
struct _LIBSSH2_SFTP_STATVFS {
    libssh2_uint64_t f_bsize;   /* file system block size */
    libssh2_uint64_t f_frsize;  /* fragment size */
    libssh2_uint64_t f_blocks;  /* size of fs in f_frsize units */
    libssh2_uint64_t f_bfree;   /* # free blocks */
    libssh2_uint64_t f_bavail;  /* # free blocks for non-root */
    libssh2_uint64_t f_files;   /* # inodes */
    libssh2_uint64_t f_ffree;   /* # free inodes */
    libssh2_uint64_t f_favail;  /* # free inodes for non-root */
    libssh2_uint64_t f_fsid;    /* file system ID */
    libssh2_uint64_t f_flag;    /* mount flags */
    libssh2_uint64_t f_namemax; /* maximum filename length */
};
</code></pre>
<p> It is unspecified whether all members of the returned struct have meaningful values on all file systems. </p>
<p> The field <i>f_flag</i> is a bit mask. Bits are defined as follows:</p>
<dl>
<dt>LIBSSH2_SFTP_ST_RDONLY</p>
<dd> Read-only file system.</p>
<dt>LIBSSH2_SFTP_ST_NOSUID</p>
<dd> Set-user-ID/set-group-ID bits are ignored by <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). </p>
</dl>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success or negative on failure. If used in non-blocking mode, it returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.6</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
