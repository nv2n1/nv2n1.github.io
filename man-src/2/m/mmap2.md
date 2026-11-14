---
title: "mmap2(2)"
name: "mmap2"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mmap2/"
description: "mmap2 – map files or devices into memory"
---

<h2 class="name">NAME</h2>
<p> mmap2 &#8211; map files or devices into memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/mman.h&gt;
void *mmap2(void *addr, size_t length, int prot,
            int flags, int fd, off_t pgoffset);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is probably not the system call that you are interested in; instead, see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), which describes the glibc wrapper function that invokes this system call. </p>
<p> The <code>mmap2</code>() system call provides the same interface as <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), except that the final argument specifies the offset into the file in 4096-byte units (instead of bytes, as is done by <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). This enables applications that use a 32-bit <i>off_t</i> to map large files (up to 2^44 bytes).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>mmap2</code>() returns a pointer to the mapped area. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Problem with getting the data from user space.</p>
<dt><code>EINVAL</code></p>
<dd> (Various platforms where the page size is not 4096 bytes.) <i>offset&nbsp;*&nbsp;4096</i> is not a multiple of the system page size.</dl>
<p> <code>mmap2</code>() can also return any of the errors described in <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> <code>mmap2</code>() is available since Linux 2.3.31.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> On architectures where this system call is present, the glibc <code>mmap</code>() wrapper function invokes this system call rather than the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call. </p>
<p> This system call does not exist on x86-64. </p>
<p> On ia64, the unit for <i>offset</i> is actually the system page size, rather than 4096 bytes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
