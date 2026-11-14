---
title: "dirfd(3)"
name: "dirfd"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfd/"
description: "dirfd – get directory stream file descriptor"
---

<h2 class="name">NAME</h2>
<p> dirfd &#8211; get directory stream file descriptor </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;dirent.h&gt;</code> </p>
<p> <code>int dirfd(DIR *</code><i>dirp</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>dirfd</code>(): </p>
<dl>
<dt>
<dd> /* Since glibc 2.10: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>dirfd</code>() returns the file descriptor associated with the directory stream <i>dirp</i>. </p>
<p> This file descriptor is the one used internally by the directory stream. As a result, it is useful only for functions which do not depend on or alter the file position, such as <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2) and <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2). It will be automatically closed when <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3) is called.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfd</code>() returns a file descriptor (a nonnegative integer). On error, -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> POSIX.1-2008 specifies two errors, neither of which is returned by the current implementation.</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>dirp</i> does not refer to a valid directory stream.</p>
<dt><code>ENOTSUP</code></p>
<dd> The implementation does not support the association of a file descriptor with a directory.</dl>
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
<td> <code>dirfd</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008. This function was a BSD extension, present in 4.3BSD-Reno, not in 4.2BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
