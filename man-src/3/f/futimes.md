---
title: "futimes(3)"
name: "futimes"
section: "3"
letter: "f"
url: "/docs/linux/man/3-futimes/"
description: "futimes, lutimes – change file timestamps"
---

<h2 class="name">NAME</h2>
<p> futimes, lutimes &#8211; change file timestamps </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/time.h&gt;
int futimes(int fd, const struct timeval tv[2]);
int lutimes(const char *filename, const struct timeval tv[2]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>futimes</code>(), <code>lutimes</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>futimes</code>() changes the access and modification times of a file in the same way as <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), with the difference that the file whose timestamps are to be changed is specified via a file descriptor, <i>fd</i>, rather than via a pathname. </p>
<p> <code>lutimes</code>() changes the access and modification times of a file in the same way as <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), with the difference that if <i>filename</i> refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link are changed.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Errors are as for <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), with the following additions for <code>futimes</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>ENOSYS</code></p>
<dd> The <i>/proc</i> filesystem could not be accessed.</dl>
<p> The following additional error may occur for <code>lutimes</code>():</p>
<dl>
<dt><code>ENOSYS</code></p>
<dd> The kernel does not support this call; Linux 2.6.22 or later is required.</dl>
<h2>VERSIONS</h2>
<p> <code>futimes</code>() is available since glibc 2.3. <code>lutimes</code>() is available since glibc 2.6, and is implemented using the <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2) system call, which is supported since kernel 2.6.22.</p>
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
<td> <code>futimes</code>(), <code>lutimes</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are not specified in any standard. Other than Linux, they are available only on the BSDs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
