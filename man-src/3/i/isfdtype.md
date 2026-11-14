---
title: "isfdtype(3)"
name: "isfdtype"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isfdtype/"
description: "isfdtype – test file type of a file descriptor"
---

<h2 class="name">NAME</h2>
<p> isfdtype &#8211; test file type of a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/stat.h&gt;
int isfdtype(int fd, int fdtype);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>isfdtype</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.20:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Before glibc 2.20:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>isfdtype</code>() function tests whether the file descriptor <i>fd</i> refers to a file of type <i>fdtype</i>. The <i>fdtype</i> argument specifies one of the <code>S_IF*</code> constants defined in <i>&lt;sys/stat.h&gt;</i> and documented in <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) (e.g., <code>S_IFREG</code>).</p>
<h2>RETURN VALUE</h2>
<p> The <code>isfdtype</code>() function returns 1 if the file descriptor <i>fd</i> is of type <i>fdtype</i> and 0 if it is not. On error, -1 is returned and <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<p> The <code>isfdtype</code>() function can fail with any of the same errors as <code><a href="/docs/linux/man/3-fstat/">fstat</a></code>(3).</p>
<h2>CONFORMING TO</h2>
<p> The <code>isfdtype</code>() function is not specified in any standard, but did appear in the draft POSIX.1g standard. It is present on OpenBSD and Tru64 UNIX (where the required header file in both cases is just <i>&lt;sys/stat.h&gt;</i>, as shown in the POSIX.1g draft), and possibly other systems.</p>
<h2>NOTES</h2>
<p> Portable applications should use <code><a href="/docs/linux/man/3-fstat/">fstat</a></code>(3) instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fstat/">fstat</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
