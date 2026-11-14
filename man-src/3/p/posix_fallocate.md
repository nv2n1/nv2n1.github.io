---
title: "posix_fallocate(3)"
name: "posix_fallocate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-posix_fallocate/"
description: "posix_fallocate – allocate file space"
---

<p>posix_fallocate &#8211; allocate file space</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;fcntl.h&gt;

int posix_fallocate(int fd, off_t offset, off_t len);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>posix_fallocate</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The function <code>posix_fallocate</code>() ensures that disk space is allocated for the file referred to by the file descriptor <i>fd</i> for the bytes in the range starting at <i>offset</i> and continuing for <i>len</i> bytes. After a successful call to <code>posix_fallocate</code>(), subsequent writes to bytes in the specified range are guaranteed not to fail because of lack of disk space. </p>
<p> If the size of the file is less than <i>offset</i>+<i>len</i>, then the file is increased to this size; otherwise the file size is left unchanged.</p>
<h2>Return Value</h2>
<p><code>posix_fallocate</code>() returns zero on success, or an error number on failure. Note that <i>errno</i> is not set.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>fd</i> is not a valid file descriptor, or is not opened for writing.</p>
<dt><code>EFBIG</code></p>
<dd><i>offset+len</i> exceeds the maximum file size.</p>
<dt><code>EINTR</code></p>
<dd>A signal was caught during execution.</p>
<dt><code>EINVAL</code></p>
<dd><i>offset</i> was less than 0, or <i>len</i> was less than or equal to 0, or the underlying filesystem does not support the operation.</p>
<dt><code>ENODEV</code></p>
<dd><i>fd</i> does not refer to a regular file.</p>
<dt><code>ENOSPC</code></p>
<dd>There is not enough space left on the device containing the file referred to by <i>fd</i>.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd>The filesystem containing the file referred to by <i>fd</i> does not support this operation. This error code can be returned by C libraries that don&#8217;t perform the emulation shown in NOTES, such as musl libc.</p>
<dt><code>ESPIPE</code></p>
<dd><i>fd</i> refers to a pipe.</dl>
<h2>Versions</h2>
<p><code>posix_fallocate</code>() is available since glibc 2.1.94.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>posix_fallocate</code>() </td>
<td>Thread safety</td>
<td>MT-Safe (but see NOTES)
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001. </p>
<p> POSIX.1-2008 says that an implementation <i>shall</i> give the <code>EINVAL</code> error if <i>len</i> was 0, or <i>offset</i> was less than 0. POSIX.1-2001 says that an implementation <i>shall</i> give the <code>EINVAL</code> error if <i>len</i> is less than 0, or <i>offset</i> was less than 0, and <i>may</i> give the error if <i>len</i> equals zero.</p>
<h2>Notes</h2>
<p>In the glibc implementation, <code>posix_fallocate</code>() is implemented using the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) system call, which is MT-safe. If the underlying filesystem does not support <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2), then the operation is emulated with the following caveats:</p>
<dl>
<dt>*</p>
<dd>The emulation is inefficient.</p>
<dt>*</p>
<dd>There is a race condition where concurrent writes from another thread or process could be overwritten with null bytes.</p>
<dt>*</p>
<dd>There is a race condition where concurrent file size increases by another thread or process could result in a file whose size is smaller than expected.</p>
<dt>*</p>
<dd>If <i>fd</i> has been opened with the <code>O_APPEND</code> or <code>O_WRONLY</code> flags, the function fails with the error <code>EBADF</code>.</dl>
<p> In general, the emulation is not MT-safe. On Linux, applications may use <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) if they cannot tolerate the emulation caveats. In general, this is only recommended if the application plans to terminate the operation if <code>EOPNOTSUPP</code> is returned, otherwise the application itself will need to implement a fallback with all the same problems as the emulation provided by glibc.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fallocate/">fallocate</a></code>(1), <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
