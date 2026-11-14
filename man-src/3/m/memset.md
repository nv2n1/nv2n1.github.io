---
title: "memset(3)"
name: "memset"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memset/"
description: "memset – fill memory with a constant byte"
---

<h2 class="name">NAME</h2>
<p> memset &#8211; fill memory with a constant byte </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
void *memset(void *s, int c, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memset</code>() function fills the first <i>n</i> bytes of the memory area pointed to by <i>s</i> with the constant byte <i>c</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memset</code>() function returns a pointer to the memory area <i>s</i>.</p>
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
<td> <code>memset</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-bzero/">bzero</a></code>(3), <code><a href="/docs/linux/man/3-swab/">swab</a></code>(3), <code><a href="/docs/linux/man/3-wmemset/">wmemset</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
