---
title: "isatty(3)"
name: "isatty"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isatty/"
description: "isatty – test whether a file descriptor refers to a terminal"
---

<h2 class="name">NAME</h2>
<p> isatty &#8211; test whether a file descriptor refers to a terminal </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int isatty(int fd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>isatty</code>() function tests whether <i>fd</i> is an open file descriptor referring to a terminal.</p>
<h2>RETURN VALUE</h2>
<p> <code>isatty</code>() returns 1 if <i>fd</i> is an open file descriptor referring to a terminal; otherwise 0 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>ENOTTY</code></p>
<dd> <i>fd</i> refers to a file other than a terminal. On some older kernels, some types of files resulted in the error <code>EINVAL</code> in this case (which is a violation of POSIX, which specifies the error <code>ENOTTY</code>).</dl>
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
<td> <code>isatty</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
