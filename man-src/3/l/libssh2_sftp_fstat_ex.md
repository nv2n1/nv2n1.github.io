---
title: "libssh2_sftp_fstat_ex(3)"
name: "libssh2_sftp_fstat_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_fstat_ex/"
description: "libssh2_sftp_fstat_ex – get or set attributes on an SFTP file handle"
---

<h2>NAME</h2>
<p> libssh2_sftp_fstat_ex &#8211; get or set attributes on an SFTP file handle</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#include &lt;libssh2_sftp.h&gt;
int libssh2_sftp_fstat_ex(LIBSSH2_SFTP_HANDLE *handle,
                          LIBSSH2_SFTP_ATTRIBUTES *attrs, int setstat)
#define libbssh2_sftp_fstat(handle, attrs) \
    libssh2_sftp_fstat_ex((handle), (attrs), 0)
#define libssh2_sftp_fsetstat(handle, attrs) \
    libssh2_sftp_fstat_ex((handle), (attrs), 1)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>handle</i> &#8211; SFTP File Handle as returned by <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<p> <i>attrs</i> &#8211; Pointer to an LIBSSH2_SFTP_ATTRIBUTES structure to set file metadata from or into depending on the value of setstat. </p>
<p> <i>setstat</i> &#8211; When non-zero, the file&#8217;s metadata will be updated with the data found in attrs according to the values of attrs-&gt;flags and other relevant member attributes. </p>
<p> Get or Set statbuf type data for a given LIBSSH2_SFTP_HANDLE instance.</p>
<h2>DATA TYPES</h2>
<p> LIBSSH2_SFTP_ATTRIBUTES is a typedefed struct that is defined as below </p>
<pre><code>
struct _LIBSSH2_SFTP_ATTRIBUTES {
    /* If flags &amp; ATTR_* bit is set, then the value in this
     * struct will be meaningful Otherwise it should be ignored
     */
    unsigned long flags;
    /* size of file, in bytes */
    libssh2_uint64_t filesize;
    /* numerical representation of the user and group owner of
     * the file
     */
    unsigned long uid, gid;
    /* bitmask of permissions */
    unsigned long permissions;
    /* access time and modified time of file */
    unsigned long atime, mtime;
};
</code></pre>
<p> You will find a full set of defines and macros to identify flags and permissions on the <code>libssh2_s<a href="ftp://ftp.h">ftp.h</a></code> header file, but some of the most common ones are: </p>
<p> To check for specific user permissions, the set of defines are in the pattern LIBSSH2_SFTP_S_I&lt;action&gt;&lt;who&gt; where &lt;action&gt; is R, W or X for read, write and excutable and &lt;who&gt; is USR, GRP and OTH for user, group and other. So, you check for a user readable file, use the bit <i>LIBSSH2_SFTP_S_IRUSR</i> while you want to see if it is executable for other, you use <i>LIBSSH2_SFTP_S_IXOTH</i> and so on. </p>
<p> To check for specific file types, you would previously (before libssh2 1.2.5) use the standard posix S_IS***() macros, but since 1.2.5 libssh2 offers its own set of macros for this functionality:</p>
<dl>
<dt>LIBSSH2_SFTP_S_ISLNK</p>
<dd> Test for a symbolic link</p>
<dt>LIBSSH2_SFTP_S_ISREG</p>
<dd> Test for a regular file</p>
<dt>LIBSSH2_SFTP_S_ISDIR</p>
<dd> Test for a directory</p>
<dt>LIBSSH2_SFTP_S_ISCHR</p>
<dd> Test for a character special file</p>
<dt>LIBSSH2_SFTP_S_ISBLK</p>
<dd> Test for a block special file</p>
<dt>LIBSSH2_SFTP_S_ISFIFO</p>
<dd> Test for a pipe or FIFO special file</p>
<dt>LIBSSH2_SFTP_S_ISSOCK</p>
<dd> Test for a socket</dl>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_SFTP_PROTOCOL</i> &#8211; An invalid SFTP protocol response was received on the socket, or an SFTP operation caused an errorcode to be returned by the server.</p>
<h2>AVAILABILITY</h2>
<p> This function has been around since forever, but most of the LIBSSH2_SFTP_S_* defines were introduced in libssh2 0.14 and the LIBSSH2_SFTP_S_IS***() macros were introduced in libssh2 1.2.5.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_open_ex/">libssh2_sftp_open_ex</a>(3)</code> </p>
<h2>Index</h2>
