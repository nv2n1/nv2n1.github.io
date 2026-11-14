---
title: "memcpy(3)"
name: "memcpy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcpy/"
description: "memcpy – copy memory area"
---

<h2 class="name">NAME</h2>
<p> memcpy &#8211; copy memory area </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
void *memcpy(void *dest, const void *src, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memcpy</code>() function copies <i>n</i> bytes from memory area <i>src</i> to memory area <i>dest</i>. The memory areas must not overlap. Use <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3) if the memory areas do overlap.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memcpy</code>() function returns a pointer to <i>dest</i>.</p>
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
<td> <code>memcpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Failure to observe the requirement that the memory areas do not overlap has been the source of significant bugs. (POSIX and the C standards are explicit that employing <code>memcpy</code>() with overlapping areas produces undefined behavior.) Most notably, in glibc 2.13 a performance optimization of <code>memcpy</code>() on some platforms (including x86-64) included changing the order in which bytes were copied from <i>src</i> to <i>dest</i>. </p>
<p> This change revealed breakages in a number of applications that performed copying with overlapping areas. Under the previous implementation, the order in which the bytes were copied had fortuitously hidden the bug, which was revealed when the copying order was reversed. In glibc 2.14, a versioned symbol was added so that old binaries (i.e., those linked against glibc versions earlier than 2.14) employed a <code>memcpy</code>() implementation that safely handles the overlapping buffers case (by providing an &quot;older&quot; <code>memcpy</code>() implementation that was aliased to <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3)).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcopy/">bcopy</a></code>(3), <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-mempcpy/">mempcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
