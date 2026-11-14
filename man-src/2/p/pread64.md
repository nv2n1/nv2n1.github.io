---
title: "pread64(2)"
name: "pread64"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pread64/"
description: "pread, pwrite – read from or write to a file descriptor at a given offset"
---

<h2 class="name">NAME</h2>
<p> pread, pwrite &#8211; read from or write to a file descriptor at a given offset </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>ssize_t pread(int </code><i>fd</i><code>, void *</code><i>buf</i><code>, size_t </code><i>count</i><code>, off_t </code><i>offset</i><code>);</code> </p>
<p> <code>ssize_t pwrite(int </code><i>fd</i><code>, const void *</code><i>buf</i><code>, size_t </code><i>count</i><code>, off_t </code><i>offset</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>pread</code>(), <code>pwrite</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
 || /* Since glibc 2.12: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dl>
<h2>DESCRIPTION</h2>
<p> <code>pread</code>() reads up to <i>count</i> bytes from file descriptor <i>fd</i> at offset <i>offset</i> (from the start of the file) into the buffer starting at <i>buf</i>. The file offset is not changed. </p>
<p> <code>pwrite</code>() writes up to <i>count</i> bytes from the buffer starting at <i>buf</i> to the file descriptor <i>fd</i> at offset <i>offset</i>. The file offset is not changed. </p>
<p> The file referenced by <i>fd</i> must be capable of seeking.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>pread</code>() returns the number of bytes read (a return of zero indicates end of file) and <code>pwrite</code>() returns the number of bytes written. </p>
<p> Note that it is not an error for a successful call to transfer fewer bytes than requested (see <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2)). </p>
<p> On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>pread</code>() can fail and set <i>errno</i> to any error specified for <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). <code>pwrite</code>() can fail and set <i>errno</i> to any error specified for <code><a href="/docs/linux/man/2-write/">write</a></code>(2) or <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> The <code>pread</code>() and <code>pwrite</code>() system calls were added to Linux in version 2.1.60; the entries in the i386 system call table were added in 2.1.69. C library support (including emulation using <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) on older kernels without the system calls) was added in glibc 2.1.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> The <code>pread</code>() and <code>pwrite</code>() system calls are especially useful in multithreaded applications. They allow multiple threads to perform I/O on the same file descriptor without being affected by changes to the file offset by other threads.</p>
<h3>C library/kernel differences</h3>
<p> On Linux, the underlying system calls were renamed in kernel 2.6: <code>pread</code>() became <code>pread64</code>(), and <code>pwrite</code>() became <code>pwrite64</code>(). The system call numbers remained the same. The glibc <code>pread</code>() and <code>pwrite</code>() wrapper functions transparently deal with the change. </p>
<p> On some 32-bit architectures, the calling signature for these system calls differ, for the reasons described in <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>BUGS</h2>
<p> POSIX requires that opening a file with the <code>O_APPEND</code> flag should have no effect on the location at which <code>pwrite</code>() writes data. However, on Linux, if a file is opened with <code>O_APPEND</code>, <code>pwrite</code>() appends data to the end of the file, regardless of the value of <i>offset</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
