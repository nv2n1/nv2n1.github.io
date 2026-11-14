---
title: "write(2)"
name: "write"
section: "2"
letter: "w"
url: "/docs/linux/man/2-write/"
description: "write – write to a file descriptor"
---

<h2 class="name">NAME</h2>
<p> write &#8211; write to a file descriptor </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>ssize_t write(int </code><i>fd</i><code>, const void *</code><i>buf</i><code>, size_t </code><i>count</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>write</code>() writes up to <i>count</i> bytes from the buffer starting at <i>buf</i> to the file referred to by the file descriptor <i>fd</i>. </p>
<p> The number of bytes written may be less than <i>count</i> if, for example, there is insufficient space on the underlying physical medium, or the <code>RLIMIT_FSIZE</code> resource limit is encountered (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)), or the call was interrupted by a signal handler after having written less than <i>count</i> bytes. (See also <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).) </p>
<p> For a seekable file (i.e., one to which <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) may be applied, for example, a regular file) writing takes place at the file offset, and the file offset is incremented by the number of bytes actually written. If the file was <code><a href="/docs/linux/man/2-open/">open</a></code>(2)ed with <code>O_APPEND</code>, the file offset is first set to the end of the file before writing. The adjustment of the file offset and the write operation are performed as an atomic step. </p>
<p> POSIX requires that a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) that can be proved to occur after a <code>write</code>() has returned will return the new data. Note that not all filesystems are POSIX conforming. </p>
<p> According to POSIX.1, if <i>count</i> is greater than <code>SSIZE_MAX</code>, the result is implementation-defined; see NOTES for the upper limit on Linux.</p>
<h2>RETURN VALUE</h2>
<p> On success, the number of bytes written is returned. On error, -1 is returned, and <i>errno</i> is set to indicate the cause of the error. </p>
<p> Note that a successful <code>write</code>() may transfer fewer than <i>count</i> bytes. Such partial writes can occur for various reasons; for example, because there was insufficient space on the disk device to write all of the requested bytes, or because a blocked <code>write</code>() to a socket, pipe, or similar was interrupted by a signal handler after it had transferred some, but before it had transferred all of the requested bytes. In the event of a partial write, the caller can make another <code>write</code>() call to transfer the remaining bytes. The subsequent call will either transfer further bytes or may result in an error (e.g., if the disk is now full). </p>
<p> If <i>count</i> is zero and <i>fd</i> refers to a regular file, then <code>write</code>() may return a failure status if one of the errors below is detected. If no errors are detected, or error detection is not performed, 0 will be returned without causing any other effect. If <i>count</i> is zero and <i>fd</i> refers to a file other than a regular file, the results are not specified.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The file descriptor <i>fd</i> refers to a file other than a socket and has been marked nonblocking (<code>O_NONBLOCK</code>), and the write would block. See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for further details on the <code>O_NONBLOCK</code> flag.</p>
<dt><code>EAGAIN</code> or <code>EWOULDBLOCK</code></p>
<dd> The file descriptor <i>fd</i> refers to a socket and has been marked nonblocking (<code>O_NONBLOCK</code>), and the write would block. POSIX.1-2001 allows either error to be returned for this case, and does not require these constants to have the same value, so a portable application should check for both possibilities.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor or is not open for writing.</p>
<dt><code>EDESTADDRREQ</code></p>
<dd> <i>fd</i> refers to a datagram socket for which a peer address has not been set using <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2).</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks on the filesystem containing the file referred to by <i>fd</i> has been exhausted.</p>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> is outside your accessible address space.</p>
<dt><code>EFBIG</code></p>
<dd> An attempt was made to write a file that exceeds the implementation-defined maximum file size or the process&#8217;s file size limit, or to write at a position past the maximum allowed offset.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal before any data was written; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is attached to an object which is unsuitable for writing; or the file was opened with the <code>O_DIRECT</code> flag, and either the address specified in <i>buf</i>, the value specified in <i>count</i>, or the file offset is not suitably aligned.</p>
<dt><code>EIO</code></p>
<dd> A low-level I/O error occurred while modifying the inode. This error may relate to the write-back of data written by an earlier <code>write</code>(), which may have been issued to a different file descriptor on the same file. Since Linux 4.13, errors from write-back come with a promise that they <i>may</i> be reported by subsequent. <code>write</code>() requests, and <i>will</i> be reported by a subsequent <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) (whether or not they were also reported by <code>write</code>()). An alternate cause of <code>EIO</code> on networked filesystems is when an advisory lock had been taken out on the file descriptor and this lock has been lost. See the <i>Lost locks</i> section of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for further details.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing the file referred to by <i>fd</i> has no room for the data.</p>
<dt><code>EPERM</code></p>
<dd> The operation was prevented by a file seal; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>EPIPE</code></p>
<dd> <i>fd</i> is connected to a pipe or socket whose reading end is closed. When this happens the writing process will also receive a <code>SIGPIPE</code> signal. (Thus, the write return value is seen only if the program catches, blocks or ignores this signal.)</dl>
<p> Other errors may occur, depending on the object connected to <i>fd</i>.</p>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD, POSIX.1-2001. </p>
<p> Under SVr4 a write may be interrupted and return <code>EINTR</code> at any point, not just before any data is written.</p>
<h2>NOTES</h2>
<p> The types <i>size_t</i> and <i>ssize_t</i> are, respectively, unsigned and signed integer data types specified by POSIX.1. </p>
<p> A successful return from <code>write</code>() does not make any guarantee that data has been committed to disk. On some filesystems, including NFS, it does not even guarantee that space has successfully been reserved for the data. In this case, some errors might be delayed until a future <code>write</code>(), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), or even <code><a href="/docs/linux/man/2-close/">close</a></code>(2). The only way to be sure is to call <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2) after you are done writing all your data. </p>
<p> If a <code>write</code>() is interrupted by a signal handler before any bytes are written, then the call fails with the error <code>EINTR</code>; if it is interrupted after at least one byte has been written, the call succeeds, and returns the number of bytes written. </p>
<p> On Linux, <code>write</code>() (and similar system calls) will transfer at most 0x7ffff000 (2,147,479,552) bytes, returning the number of bytes actually transferred. (This is true on both 32-bit and 64-bit systems.) </p>
<p> An error return value while performing <code>write</code>() using direct I/O does not mean the entire write has failed. Partial data may be written and the data at the file offset on which the <code>write</code>() was attempted should be considered inconsistent.</p>
<h2>BUGS</h2>
<p> According to POSIX.1-2008/SUSv4 Section XSI 2.9.7 (&quot;Thread Interactions with Regular File Operations&quot;): </p>
<dl>
<dt>
<dd> All of the following functions shall be atomic with respect to each other in the effects specified in POSIX.1-2008 when they operate on regular files or symbolic links: &#8230;</dl>
<p> Among the APIs subsequently listed are <code>write</code>() and <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2). And among the effects that should be atomic across threads (and processes) are updates of the file offset. However, on Linux before version 3.14, this was not the case: if two processes that share an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) perform a <code>write</code>() (or <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2)) at the same time, then the I/O operations were not atomic with respect updating the file offset, with the result that the blocks of data output by the two processes might (incorrectly) overlap. This problem was fixed in Linux 3.14.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2), <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
