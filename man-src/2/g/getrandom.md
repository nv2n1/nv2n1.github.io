---
title: "getrandom(2)"
name: "getrandom"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getrandom/"
description: "getrandom – obtain a series of random bytes"
---

<h2 class="name">NAME</h2>
<p> getrandom &#8211; obtain a series of random bytes </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/random.h&gt;</code> </p>
<p> <code>ssize_t getrandom(void *buf</code><i>, size_t </i><code>buflen</code><i>, unsigned int </i><code>flags</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>getrandom</code>() system call fills the buffer pointed to by <i>buf</i> with up to <i>buflen</i> random bytes. These bytes can be used to seed user-space random number generators or for cryptographic purposes. </p>
<p> By default, <code>getrandom</code>() draws entropy from the <i>urandom</i> source (i.e., the same source as the <i>/dev/urandom</i> device). This behavior can be changed via the <i>flags</i> argument. </p>
<p> If the <i>urandom</i> source has been initialized, reads of up to 256 bytes will always return as many bytes as requested and will not be interrupted by signals. No such guarantees apply for larger buffer sizes. For example, if the call is interrupted by a signal handler, it may return a partially filled buffer, or fail with the error <code>EINTR</code>. </p>
<p> If the <i>urandom</i> source has not yet been initialized, then <code>getrandom</code>() will block, unless <code>GRND_NONBLOCK</code> is specified in <i>flags</i>. </p>
<p> The <i>flags</i> argument is a bit mask that can contain zero or more of the following values ORed together:</p>
<dl>
<dt><code>GRND_RANDOM</code></p>
<dd> If this bit is set, then random bytes are drawn from the <i>random</i> source (i.e., the same source as the <i>/dev/random</i> device) instead of the <i>urandom</i> source. The <i>random</i> source is limited based on the entropy that can be obtained from environmental noise. If the number of available bytes in the <i>random</i> source is less than requested in <i>buflen</i>, the call returns just the available random bytes. If no random bytes are available, the behavior depends on the presence of <code>GRND_NONBLOCK</code> in the <i>flags</i> argument.</p>
<dt><code>GRND_NONBLOCK</code></p>
<dd> By default, when reading from the <i>random</i> source, <code>getrandom</code>() blocks if no random bytes are available, and when reading from the <i>urandom</i> source, it blocks if the entropy pool has not yet been initialized. If the <code>GRND_NONBLOCK</code> flag is set, then <code>getrandom</code>() does not block in these cases, but instead immediately returns -1 with <i>errno</i> set to <code>EAGAIN</code>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>getrandom</code>() returns the number of bytes that were copied to the buffer <i>buf</i>. This may be less than the number of bytes requested via <i>buflen</i> if either <code>GRND_RANDOM</code> was specified in <i>flags</i> and insufficient entropy was present in the <i>random</i> source or the system call was interrupted by a signal. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The requested entropy was not available, and <code>getrandom</code>() would have blocked if the <code>GRND_NONBLOCK</code> flag was not set.</p>
<dt><code>EFAULT</code></p>
<dd> The address referred to by <i>buf</i> is outside the accessible address space.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal handler; see the description of how interrupted <code><a href="/docs/linux/man/2-read/">read</a></code>(2) calls on &quot;slow&quot; devices are handled with and without the <code>SA_RESTART</code> flag in the <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) man page.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid flag was specified in <i>flags</i>.</p>
<dt><code>ENOSYS</code></p>
<dd> The glibc wrapper function for <code>getrandom</code>() determined that the underlying kernel does not implement this system call.</dl>
<h2>VERSIONS</h2>
<p> <code>getrandom</code>() was introduced in version 3.17 of the Linux kernel. Support was added to glibc in version 2.25.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> For an overview and comparison of the various interfaces that can be used to obtain randomness, see <code><a href="/docs/linux/man/7-random/">random</a></code>(7). </p>
<p> Unlike <i>/dev/random</i> and <i>/dev/urandom</i>, <code>getrandom</code>() does not involve the use of pathnames or file descriptors. Thus, <code>getrandom</code>() can be useful in cases where <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) makes <i>/dev</i> pathnames invisible, and where an application (e.g., a daemon during start-up) closes a file descriptor for one of these files that was opened by a library.</p>
<h3>Maximum number of bytes returned</h3>
<p> As of Linux 3.19 the following limits apply:</p>
<dl>
<dt>*</p>
<dd> When reading from the <i>urandom</i> source, a maximum of 33554431 bytes is returned by a single call to <code>getrandom</code>() on systems where <i>int</i> has a size of 32 bits.</p>
<dt>*</p>
<dd> When reading from the <i>random</i> source, a maximum of 512 bytes is returned.</dl>
<h3>Interruption by a signal handler</h3>
<p> When reading from the <i>urandom</i> source (<code>GRND_RANDOM</code> is not set), <code>getrandom</code>() will block until the entropy pool has been initialized (unless the <code>GRND_NONBLOCK</code> flag was specified). If a request is made to read a large number of bytes (more than 256), <code>getrandom</code>() will block until those bytes have been generated and transferred from kernel memory to <i>buf</i>. When reading from the <i>random</i> source (<code>GRND_RANDOM</code> is set), <code>getrandom</code>() will block until some random bytes become available (unless the <code>GRND_NONBLOCK</code> flag was specified). </p>
<p> The behavior when a call to <code>getrandom</code>() that is blocked while reading from the <i>urandom</i> source is interrupted by a signal handler depends on the initialization state of the entropy buffer and on the request size, <i>buflen</i>. If the entropy is not yet initialized, then the call fails with the <code>EINTR</code> error. If the entropy pool has been initialized and the request size is large (<i>buflen</i>&nbsp;&gt;&nbsp;256), the call either succeeds, returning a partially filled buffer, or fails with the error <code>EINTR</code>. If the entropy pool has been initialized and the request size is small (<i>buflen</i>&nbsp;&lt;=&nbsp;256), then <code>getrandom</code>() will not fail with <code>EINTR</code>. Instead, it will return all of the bytes that have been requested. </p>
<p> When reading from the <i>random</i> source, blocking requests of any size can be interrupted by a signal handler (the call fails with the error <code>EINTR</code>). </p>
<p> Using <code>getrandom</code>() to read small buffers (&lt;=&nbsp;256 bytes) from the <i>urandom</i> source is the preferred mode of usage. </p>
<p> The special treatment of small values of <i>buflen</i> was designed for compatibility with OpenBSD&#8217;s <code><a href="/docs/linux/man/3-getentropy/">getentropy</a></code>(3), which is nowadays supported by glibc. </p>
<p> The user of <code>getrandom</code>() <i>must</i> always check the return value, to determine whether either an error occurred or fewer bytes than requested were returned. In the case where <code>GRND_RANDOM</code> is not specified and <i>buflen</i> is less than or equal to 256, a return of fewer bytes than requested should never happen, but the careful programmer will check for this anyway!</p>
<h2>BUGS</h2>
<p> As of Linux 3.19, the following bug exists:</p>
<dl>
<dt>*</p>
<dd> Depending on CPU load, <code>getrandom</code>() does not react to interrupts before reading all bytes requested.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getentropy/">getentropy</a></code>(3), <code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/4-urandom/">urandom</a></code>(4), <code><a href="/docs/linux/man/7-random/">random</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
