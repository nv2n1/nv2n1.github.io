---
title: "wmemmove(3)"
name: "wmemmove"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmemmove/"
description: "wmemmove – copy an array of wide-characters"
---

<p>wmemmove &#8211; copy an array of wide-characters</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wmemmove(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wmemmove</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3) function. It copies <i>n</i> wide characters from the array starting at <i>src</i> to the array starting at <i>dest</i>. The arrays may overlap. </p>
<p> The programmer must ensure that there is room for at least <i>n</i> wide characters at <i>dest</i>.</p>
<h2>Return Value</h2>
<p><code>wmemmove</code>() returns <i>dest</i>.</p>
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
<td> <code>wmemmove</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
