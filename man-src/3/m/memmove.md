---
title: "memmove(3)"
name: "memmove"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memmove/"
description: "memmove – copy memory area"
---

<h2 class="name">NAME</h2>
<p> memmove &#8211; copy memory area </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
void *memmove(void *dest, const void *src, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memmove</code>() function copies <i>n</i> bytes from memory area <i>src</i> to memory area <i>dest</i>. The memory areas may overlap: copying takes place as though the bytes in <i>src</i> are first copied into a temporary array that does not overlap <i>src</i> or <i>dest</i>, and the bytes are then copied from the temporary array to <i>dest</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memmove</code>() function returns a pointer to <i>dest</i>.</p>
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
<td> <code>memmove</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcopy/">bcopy</a></code>(3), <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-wmemmove/">wmemmove</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
