---
title: "read(2)"
name: "read"
section: "2"
letter: "r"
url: "/docs/linux/man/2-read/"
description: "read – read from a file descriptor"
---

<h2 class="name">NAME</h2>
<p> read &#8211; read from a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
ssize_t read(int fd, void *buf, size_t count);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>read</code>() attempts to read up to <i>count</i> bytes from file descriptor <i>fd</i> into the buffer starting at <i>buf</i>. </p>
<p> On files that support seeking, the read operation commences at the file offset, and the file offset is incremented by the number of bytes read. If the file offset is at or past the end of file, no bytes are read, and <code>read</code>() returns zero. </p>
<p> If <i>count</i> is zero, <code>read</code>() <i>may</i> detect the errors described below. In the absence of any errors, or if <code>read</code>() does not check for errors, a <code>read</code>() with a <i>count</i> of 0 returns zero and has no other effects. </p>
<p> According to POSIX.1, if <i>count</i> is greater than <code>SSIZE_MAX</code>, the result is implementation-defined; see NOTES for the upper limit on Linux.</p>
<h2>RETURN VALUE</h2>
<p> On success, the number of bytes read is returned (zero indicates end of file), and the file position is advanced by this number. It is not an error if this number is smaller than the number of bytes requested; this may happen for example because fewer bytes are actually available right now (maybe because we were close to end-of-file, or because we are reading from a pipe, or from a terminal), or because <code>read</code>() was interrupted by a signal. See also NOTES. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately. In this case, it is left unspecified whether the file position (if any) changes.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The file descriptor <i>fd</i> refers to a file other than a socket and has been marked nonblocking (<code>O_NONBLOCK</code>), and the read would block. See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for further details on the <code>O_NONBLOCK</code> flag.</p>
<dt><code>EAGAIN</code> or <code>EWOULDBLOCK</code></p>
<dd> The file descriptor <i>fd</i> refers to a socket and has been marked nonblocking (<code>O_NONBLOCK</code>), and the read would block. POSIX.1-2001 allows either error to be returned for this case, and does not require these constants to have the same value, so a portable application should check for both possibilities.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor or is not open for reading.</p>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> is outside your accessible address space.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal before any data was read; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is attached to an object which is unsuitable for reading; or the file was opened with the <code>O_DIRECT</code> flag, and either the address specified in <i>buf</i>, the value specified in <i>count</i>, or the file offset is not suitably aligned.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> was created via a call to <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2) and the wrong size buffer was given to <code>read</code>(); see <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2) for further information.</p>
<dt><code>EIO</code></p>
<dd> I/O error. This will happen for example when the process is in a background process group, tries to read from its controlling terminal, and either it is ignoring or blocking <code>SIGTTIN</code> or its process group is orphaned. It may also occur when there is a low-level I/O error while reading from a disk or tape. A further possible cause of <code>EIO</code> on networked filesystems is when an advisory lock had been taken out on the file descriptor and this lock has been lost. See the <i>Lost locks</i> section of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for further details.</p>
<dt><code>EISDIR</code></p>
<dd> <i>fd</i> refers to a directory.</dl>
<p> Other errors may occur, depending on the object connected to <i>fd</i>.</p>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD, POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> The types <i>size_t</i> and <i>ssize_t</i> are, respectively, unsigned and signed integer data types specified by POSIX.1. </p>
<p> On Linux, <code>read</code>() (and similar system calls) will transfer at most 0x7ffff000 (2,147,479,552) bytes, returning the number of bytes actually transferred. (This is true on both 32-bit and 64-bit systems.) </p>
<p> On NFS filesystems, reading small amounts of data will update the timestamp only the first time, subsequent calls may not do so. This is caused by client side attribute caching, because most if not all NFS clients leave <i>st_atime</i> (last file access time) updates to the server, and client side reads satisfied from the client&#8217;s cache will not cause <i>st_atime</i> updates on the server as there are no server-side reads. UNIX semantics can be obtained by disabling client-side attribute caching, but in most situations this will substantially increase server load and decrease performance.</p>
<h2>BUGS</h2>
<p> According to POSIX.1-2008/SUSv4 Section XSI 2.9.7 (&quot;Thread Interactions with Regular File Operations&quot;): </p>
<dl>
<dt>
<dd> All of the following functions shall be atomic with respect to each other in the effects specified in POSIX.1-2008 when they operate on regular files or symbolic links: &#8230;</dl>
<p> Among the APIs subsequently listed are <code>read</code>() and <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2). And among the effects that should be atomic across threads (and processes) are updates of the file offset. However, on Linux before version 3.14, this was not the case: if two processes that share an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) perform a <code>read</code>() (or <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2)) at the same time, then the I/O operations were not atomic with respect updating the file offset, with the result that the reads in the two processes might (incorrectly) overlap in the blocks of data that they obtained. This problem was fixed in Linux 3.14.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
