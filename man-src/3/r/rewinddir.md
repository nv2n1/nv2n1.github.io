---
title: "rewinddir(3)"
name: "rewinddir"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rewinddir/"
description: "rewinddir – reset directory stream"
---

<p>rewinddir &#8211; reset directory stream</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/types.h&gt;

#include &lt;dirent.h&gt;

void rewinddir(DIR *dirp);</code></pre>
<h2>Description</h2>
<p>The <code>rewinddir</code>() function resets the position of the directory stream <i>dirp</i> to the beginning of the directory.</p>
<h2>Return Value</h2>
<p>The <code>rewinddir</code>() function returns no value.</p>
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
<td> <code>rewinddir</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
