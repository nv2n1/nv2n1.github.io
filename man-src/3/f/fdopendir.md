---
title: "fdopendir(3)"
name: "fdopendir"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdopendir/"
description: "opendir, fdopendir – open a directory"
---

<h2 class="name">NAME</h2>
<p> opendir, fdopendir &#8211; open a directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;dirent.h&gt;
#include &lt;sys/types.h&gt;
DIR *opendir(const char *name);
DIR *fdopendir(int fd);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fdopendir</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>opendir</code>() function opens a directory stream corresponding to the directory <i>name</i>, and returns a pointer to the directory stream. The stream is positioned at the first entry in the directory. </p>
<p> The <code>fdopendir</code>() function is like <code>opendir</code>(), but returns a directory stream for the directory referred to by the open file descriptor <i>fd</i>. After a successful call to <code>fdopendir</code>(), <i>fd</i> is used internally by the implementation, and should not otherwise be used by the application.</p>
<h2>RETURN VALUE</h2>
<p> The <code>opendir</code>() and <code>fdopendir</code>() functions return a pointer to the directory stream. On error, NULL is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Permission denied.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor opened for reading.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> Directory does not exist, or <i>name</i> is an empty string.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to complete the operation.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>name</i> is not a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>fdopendir</code>() is available in glibc since version 2.4.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>opendir</code>(), <code>fdopendir</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>opendir</code>() is present on SVr4, 4.3BSD, and specified in POSIX.1-2001. <code>fdopendir</code>() is specified in POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Filename entries can be read from a directory stream using <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3). </p>
<p> The underlying file descriptor of the directory stream can be obtained using <code><a href="/docs/linux/man/3-dirfd/">dirfd</a></code>(3). </p>
<p> The <code>opendir</code>() function sets the close-on-exec flag for the file descriptor underlying the <i>DIR *</i>. The <code>fdopendir</code>() function leaves the setting of the close-on-exec flag unchanged for the file descriptor, <i>fd</i>. POSIX.1-200x leaves it unspecified whether a successful call to <code>fdopendir</code>() will set the close-on-exec flag for the file descriptor, <i>fd</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-dirfd/">dirfd</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
