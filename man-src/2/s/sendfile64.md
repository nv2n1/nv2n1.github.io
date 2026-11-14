---
title: "sendfile64(2)"
name: "sendfile64"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sendfile64/"
description: "sendfile – transfer data between file descriptors"
---

<h2 class="name">NAME</h2>
<p> sendfile &#8211; transfer data between file descriptors </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/sendfile.h&gt;</code> </p>
<p> <code>ssize_t sendfile(int</code><i> out_fd</i><code>, int</code><i> in_fd</i><code>, off_t *</code><i></i><code>offset</code><i>, size_t</i><code> count</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> <code>sendfile</code>() copies data between one file descriptor and another. Because this copying is done within the kernel, <code>sendfile</code>() is more efficient than the combination of <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2), which would require transferring data to and from user space. </p>
<p> <i>in_fd</i> should be a file descriptor opened for reading and <i>out_fd</i> should be a descriptor opened for writing. </p>
<p> If <i>offset</i> is not NULL, then it points to a variable holding the file offset from which <code>sendfile</code>() will start reading data from <i>in_fd</i>. When <code>sendfile</code>() returns, this variable will be set to the offset of the byte following the last byte that was read. If <i>offset</i> is not NULL, then <code>sendfile</code>() does not modify the file offset of <i>in_fd</i>; otherwise the file offset is adjusted to reflect the number of bytes read from <i>in_fd</i>. </p>
<p> If <i>offset</i> is NULL, then data will be read from <i>in_fd</i> starting at the file offset, and the file offset will be updated by the call. </p>
<p> <i>count</i> is the number of bytes to copy between the file descriptors. </p>
<p> The <i>in_fd</i> argument must correspond to a file which supports <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)-like operations (i.e., it cannot be a socket). </p>
<p> In Linux kernels before 2.6.33, <i>out_fd</i> must refer to a socket. Since Linux 2.6.33 it can be any file. If it is a regular file, then <code>sendfile</code>() changes the file offset appropriately.</p>
<h2>RETURN VALUE</h2>
<p> If the transfer was successful, the number of bytes written to <i>out_fd</i> is returned. Note that a successful call to <code>sendfile</code>() may write fewer bytes than requested; the caller should be prepared to retry the call if there were unsent bytes. See also NOTES. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Nonblocking I/O has been selected using <code>O_NONBLOCK</code> and the write would block.</p>
<dt><code>EBADF</code></p>
<dd> The input file was not opened for reading or the output file was not opened for writing.</p>
<dt><code>EFAULT</code></p>
<dd> Bad address.</p>
<dt><code>EINVAL</code></p>
<dd> Descriptor is not valid or locked, or an <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)-like operation is not available for <i>in_fd</i>, or <i>count</i> is negative.</p>
<dt><code>EINVAL</code></p>
<dd> <i>out_fd</i> has the <code>O_APPEND</code> flag set. This is not currently supported by <code>sendfile</code>().</p>
<dt><code>EIO</code></p>
<dd> Unspecified error while reading from <i>in_fd</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to read from <i>in_fd</i>.</p>
<dt><code>EOVERFLOW</code></p>
<dd> <i>count</i> is too large, the operation would result in exceeding the maximum size of either the input file or the output file.</p>
<dt><code>ESPIPE</code></p>
<dd> <i>offset</i> is not NULL but the input file is not seekable.</dl>
<h2>VERSIONS</h2>
<p> <code>sendfile</code>() first appeared in Linux 2.2. The include file <i>&lt;sys/sendfile.h&gt;</i> is present since glibc 2.1.</p>
<h2>CONFORMING TO</h2>
<p> Not specified in POSIX.1-2001, nor in other standards. </p>
<p> Other UNIX systems implement <code>sendfile</code>() with different semantics and prototypes. It should not be used in portable programs.</p>
<h2>NOTES</h2>
<p> <code>sendfile</code>() will transfer at most 0x7ffff000 (2,147,479,552) bytes, returning the number of bytes actually transferred. (This is true on both 32-bit and 64-bit systems.) </p>
<p> If you plan to use <code>sendfile</code>() for sending files to a TCP socket, but need to send some header data in front of the file contents, you will find it useful to employ the <code>TCP_CORK</code> option, described in <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), to minimize the number of packets and to tune performance. </p>
<p> In Linux 2.4 and earlier, <i>out_fd</i> could also refer to a regular file; this possibility went away in the Linux 2.6.x kernel series, but was restored in Linux 2.6.33. </p>
<p> The original Linux <code>sendfile</code>() system call was not designed to handle large file offsets. Consequently, Linux 2.4 added <code>sendfile64</code>(), with a wider type for the <i>offset</i> argument. The glibc <code>sendfile</code>() wrapper function transparently deals with the kernel differences. </p>
<p> Applications may wish to fall back to <code><a href="/docs/linux/man/2-read/">read</a></code>(2)/<code><a href="/docs/linux/man/2-write/">write</a></code>(2) in the case where <code>sendfile</code>() fails with <code>EINVAL</code> or <code>ENOSYS</code>. </p>
<p> If <i>out_fd</i> refers to a socket or pipe with zero-copy support, callers must ensure the transferred portions of the file referred to by <i>in_fd</i> remain unmodified until the reader on the other end of <i>out_fd</i> has consumed the transferred data. </p>
<p> The Linux-specific <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) call supports transferring data between arbitrary file descriptors provided one (or both) of them is a pipe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-copy_file_range/">copy_file_range</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
