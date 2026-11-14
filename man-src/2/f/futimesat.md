---
title: "futimesat(2)"
name: "futimesat"
section: "2"
letter: "f"
url: "/docs/linux/man/2-futimesat/"
description: "futimesat – change timestamps of a file relative to a directory file descriptor"
---

<h2 class="name">NAME</h2>
<p> futimesat &#8211; change timestamps of a file relative to a directory file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/time.h&gt;
int futimesat(int dirfd, const char *pathname,
              const struct timeval times[2]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>futimesat</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> This system call is obsolete. Use <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2) instead. </p>
<p> The <code>futimesat</code>() system call operates in exactly the same way as <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), except for the differences described in this manual page. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2) for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2)). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>futimesat</code>() returns a 0. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> The same errors that occur for <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2) can also occur for <code>futimesat</code>(). The following additional errors can occur for <code>futimesat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>futimesat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> This system call is nonstandard. It was implemented from a specification that was proposed for POSIX.1, but that specification was replaced by the one for <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2). </p>
<p> A similar system call exists on Solaris.</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> If <i>pathname</i> is NULL, then the glibc <code>futimesat</code>() wrapper function updates the times for the file referred to by <i>dirfd</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-utimensat/">utimensat</a></code>(2), <code><a href="/docs/linux/man/2-utimes/">utimes</a></code>(2), <code><a href="/docs/linux/man/3-futimes/">futimes</a></code>(3), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
