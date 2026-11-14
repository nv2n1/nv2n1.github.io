---
title: "getentropy(3)"
name: "getentropy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getentropy/"
description: "getentropy – fill a buffer with random bytes"
---

<h2 class="name">NAME</h2>
<p> getentropy &#8211; fill a buffer with random bytes </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getentropy(void *</code><i>buffer</i><code>, size_t </code><i>length</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getentropy</code>(): </p>
<dl>
<dt>
<dd> _DEFAULT_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>getentropy</code>() function writes <i>length</i> bytes of high-quality random data to the buffer starting at the location pointed to by <i>buffer</i>. The maximum permitted value for the <i>length</i> argument is 256. </p>
<p> A successful call to <code>getentropy</code>() always provides the requested number of bytes of entropy.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns zero. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Part or all of the buffer specified by <i>buffer</i> and <i>length</i> is not in valid addressable memory.</p>
<dt><code>EIO</code></p>
<dd> <i>length</i> is greater than 256.</p>
<dt><code>EIO</code></p>
<dd> An unspecified error occurred while trying to overwrite <i>buffer</i> with random data.</p>
<dt><code>ENOSYS</code></p>
<dd> This kernel version does not implement the <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) system call required to implement this function.</dl>
<h2>VERSIONS</h2>
<p> The <code>getentropy</code>() function first appeared in glibc 2.25.</p>
<h2>CONFORMING TO</h2>
<p> This function is nonstandard. It is also present on OpenBSD.</p>
<h2>NOTES</h2>
<p> The <code>getentropy</code>() function is implemented using <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2). </p>
<p> Whereas the glibc wrapper makes <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) a cancellation point, <code>getentropy</code>() is not a cancellation point. </p>
<p> <code>getentropy</code>() is also declared in <code>&lt;sys/random.h&gt;</code>. (No feature test macro need be defined to obtain the declaration from that header file.) </p>
<p> A call to <code>getentropy</code>() may block if the system has just booted and the kernel has not yet collected enough randomness to initialize the entropy pool. In this case, <code>getentropy</code>() will keep blocking even if a signal is handled, and will return only once the entropy pool has been initialized.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2), <code><a href="/docs/linux/man/4-urandom/">urandom</a></code>(4), <code><a href="/docs/linux/man/7-random/">random</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
