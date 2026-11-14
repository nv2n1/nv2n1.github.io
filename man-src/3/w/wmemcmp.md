---
title: "wmemcmp(3)"
name: "wmemcmp"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmemcmp/"
description: "wmemcmp – compare two arrays of wide-characters"
---

<p>wmemcmp &#8211; compare two arrays of wide-characters</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

int wmemcmp(const wchar_t *s1, const wchar_t *s2, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wmemcmp</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3) function. It compares the <i>n</i> wide-characters starting at <i>s1</i> and the <i>n</i> wide-characters starting at <i>s2</i>.</p>
<h2>Return Value</h2>
<p>The <code>wmemcmp</code>() function returns zero if the wide-character arrays of size <i>n</i> at <i>s1</i> and <i>s2</i> are equal. It returns an integer greater than zero if at the first differing position <i>i</i> (<i>i</i> &lt; <i>n</i>), the corresponding wide-character <i>s1[i]</i> is greater than <i>s2[i]</i>. It returns an integer less than zero if at the first differing position <i>i</i> (<i>i</i> &lt; <i>n</i>), the corresponding wide-character <i>s1[i]</i> is less than <i>s2[i]</i>.</p>
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
<td> <code>wmemcmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-wcscmp/">wcscmp</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
