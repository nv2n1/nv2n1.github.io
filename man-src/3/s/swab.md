---
title: "swab(3)"
name: "swab"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swab/"
description: "swab – swap adjacent bytes"
---

<p>swab &#8211; swap adjacent bytes</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;unistd.h&gt;

void swab(const void *from, void *to, ssize_t n);</code></pre>
<h2>Description</h2>
<p>The <code>swab</code>() function copies <i>n</i> bytes from the array pointed to by <i>from</i> to the array pointed to by <i>to</i>, exchanging adjacent even and odd bytes. This function is used to exchange data between machines that have different low/high byte ordering. </p>
<p> This function does nothing when <i>n</i> is negative. When <i>n</i> is positive and odd, it handles <i>n-1</i> bytes as above, and does something unspecified with the last byte. (In other words, <i>n</i> should be even.)</p>
<h2>Return Value</h2>
<p>The <code>swab</code>() function returns no value.</p>
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
<td> <code>swab</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
