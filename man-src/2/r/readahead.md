---
title: "readahead(2)"
name: "readahead"
section: "2"
letter: "r"
url: "/docs/linux/man/2-readahead/"
description: "readahead – initiate file readahead into page cache"
---

<h2 class="name">NAME</h2>
<p> readahead &#8211; initiate file readahead into page cache </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
ssize_t readahead(int fd, off64_t offset, size_t count);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>readahead</code>() initiates readahead on a file so that subsequent reads from that file will be satisfied from the cache, and not block on disk I/O (assuming the readahead was initiated early enough and that other activity on the system did not in the meantime flush pages from the cache). </p>
<p> The <i>fd</i> argument is a file descriptor identifying the file which is to be read. The <i>offset</i> argument specifies the starting point from which data is to be read and <i>count</i> specifies the number of bytes to be read. I/O is performed in whole pages, so that <i>offset</i> is effectively rounded down to a page boundary and bytes are read up to the next page boundary greater than or equal to <i>(offset+count)</i>. <code>readahead</code>() does not read beyond the end of the file. The file offset of the open file description referred to by the file descriptor <i>fd</i> is left unchanged.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>readahead</code>() returns 0; on failure, -1 is returned, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor or is not open for reading.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> does not refer to a file type to which <code>readahead</code>() can be applied.</dl>
<h2>VERSIONS</h2>
<p> The <code>readahead</code>() system call appeared in Linux 2.4.13; glibc support has been provided since version 2.3.</p>
<h2>CONFORMING TO</h2>
<p> The <code>readahead</code>() system call is Linux-specific, and its use should be avoided in portable applications.</p>
<h2>NOTES</h2>
<p> On some 32-bit architectures, the calling signature for this system call differs, for the reasons described in <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>BUGS</h2>
<p> <code>readahead</code>() attempts to schedule the reads in the background and return immediately. However, it may block while it reads the filesystem metadata needed to locate the requested blocks. This occurs frequently with ext[234] on large files using indirect blocks instead of extents, giving the appearance that the call blocks until the requested data has been read.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
