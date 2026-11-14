---
title: "wmemset(3)"
name: "wmemset"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmemset/"
description: "wmemset – fill an array of wide-characters with a constant wide character"
---

<p>wmemset &#8211; fill an array of wide-characters with a constant wide character</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wchar_t *wmemset(wchar_t *wcs, wchar_t wc, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wmemset</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3) function. It fills the array of <i>n</i> wide-characters starting at <i>wcs</i> with <i>n</i> copies of the wide character <i>wc</i>.</p>
<h2>Return Value</h2>
<p><code>wmemset</code>() returns <i>wcs</i>.</p>
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
<td> <code>wmemset</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memset/">memset</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
