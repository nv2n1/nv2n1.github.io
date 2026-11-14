---
title: "chdir(2)"
name: "chdir"
section: "2"
letter: "c"
url: "/docs/linux/man/2-chdir/"
description: "chdir, fchdir – change working directory"
---

<h2 class="name">NAME</h2>
<p> chdir, fchdir &#8211; change working directory </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int chdir(const char *</code><i>path</i><code>);</code><br />
 <code>int fchdir(int </code><i>fd</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fchdir</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc up to and including 2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>chdir</code>() changes the current working directory of the calling process to the directory specified in <i>path</i>. </p>
<p> <code>fchdir</code>() is identical to <code>chdir</code>(); the only difference is that the directory is given as an open file descriptor.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Depending on the filesystem, other errors can be returned. The more general errors for <code>chdir</code>() are listed below:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied for one of the components of <i>path</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EFAULT</code></p>
<dd> <i>path</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>path</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>path</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> The directory specified in <i>path</i> does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of <i>path</i> is not a directory.</dl>
<p> The general errors for <code>fchdir</code>() are listed below:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission was denied on the directory open on <i>fd</i>.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>fd</i> does not refer to a directory.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD.</p>
<h2>NOTES</h2>
<p> The current working directory is the starting point for interpreting relative pathnames (those not starting with &#8216;/&#8217;). </p>
<p> A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s current working directory. The current working directory is left unchanged by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/3-getcwd/">getcwd</a></code>(3), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
