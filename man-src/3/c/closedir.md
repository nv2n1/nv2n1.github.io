---
title: "closedir(3)"
name: "closedir"
section: "3"
letter: "c"
url: "/docs/linux/man/3-closedir/"
description: "closedir – close a directory"
---

<h2 class="name">NAME</h2>
<p> closedir &#8211; close a directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;dirent.h&gt;
#include &lt;sys/types.h&gt;
int closedir(DIR *dirp);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>closedir</code>() function closes the directory stream associated with <i>dirp</i>. A successful call to <code>closedir</code>() also closes the underlying file descriptor associated with <i>dirp</i>. The directory stream descriptor <i>dirp</i> is not available after this call.</p>
<h2>RETURN VALUE</h2>
<p> The <code>closedir</code>() function returns 0 on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> Invalid directory stream descriptor <i>dirp</i>.</dl>
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
<td> <code>closedir</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
