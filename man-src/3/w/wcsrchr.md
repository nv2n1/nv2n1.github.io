---
title: "wcsrchr(3)"
name: "wcsrchr"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsrchr/"
description: "wcsrchr – search a wide character in a wide-character string"
---

<p>wcsrchr &#8211; search a wide character in a wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcsrchr(const wchar_t *wcs, wchar_t wc);</code></pre>
<h2>Description</h2>
<p>The <code>wcsrchr</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3) function. It searches the last occurrence of <i>wc</i> in the wide-character string pointed to by <i>wcs</i>.</p>
<h2>Return Value</h2>
<p>The <code>wcsrchr</code>() function returns a pointer to the last occurrence of <i>wc</i> in the wide-character string pointed to by <i>wcs</i>, or NULL if <i>wc</i> does not occur in the string.</p>
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
<td> <code>wcsrchr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
