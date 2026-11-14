---
title: "wmemchr(3)"
name: "wmemchr"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmemchr/"
description: "wmemchr – search a wide character in a wide-character array"
---

<p>wmemchr &#8211; search a wide character in a wide-character array</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wmemchr(const wchar_t *s, wchar_t c, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wmemchr</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3) function. It searches the <i>n</i> wide characters starting at <i>s</i> for the first occurrence of the wide character <i>c</i>.</p>
<h2>Return Value</h2>
<p>The <code>wmemchr</code>() function returns a pointer to the first occurrence of <i>c</i> among the <i>n</i> wide characters starting at <i>s</i>, or NULL if <i>c</i> does not occur among these.</p>
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
<td> <code>wmemchr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
