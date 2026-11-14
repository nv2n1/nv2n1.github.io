---
title: "wcspbrk(3)"
name: "wcspbrk"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcspbrk/"
description: "wcspbrk – search a wide-character string for any of a set of wide characters"
---

<p>wcspbrk &#8211; search a wide-character string for any of a set of wide characters</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wcspbrk(const wchar_t *wcs, const wchar_t *accept);</code></pre>
<h2>Description</h2>
<p>The <code>wcspbrk</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3) function. It searches for the first occurrence in the wide-character string pointed to by <i>wcs</i> of any of the characters in the wide-character string pointed to by <i>accept</i>.</p>
<h2>Return Value</h2>
<p>The <code>wcspbrk</code>() function returns a pointer to the first occurrence in <i>wcs</i> of any of the characters listed in <i>accept</i>. If <i>wcs</i> contains none of these characters, NULL is returned.</p>
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
<td> <code>wcspbrk</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3), <code><a href="/docs/linux/man/3-wcscspn/">wcscspn</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
