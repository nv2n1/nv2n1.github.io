---
title: "wcswidth(3)"
name: "wcswidth"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcswidth/"
description: "wcswidth – determine columns needed for a fixed-size wide-character string"
---

<p>wcswidth &#8211; determine columns needed for a fixed-size wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;wchar.h&gt;

int wcswidth(const wchar_t *s, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>wcswidth</code>() function returns the number of columns needed to represent the wide-character string pointed to by <i>s</i>, but at most <i>n</i> wide characters. If a nonprintable wide character occurs among these characters, -1 is returned.</p>
<h2>Return Value</h2>
<p>The <code>wcswidth</code>() function returns the number of column positions for the wide-character string <i>s</i>, truncated to at most length <i>n</i>.</p>
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
<td> <code>wcswidth</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The behavior of <code>wcswidth</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-iswprint/">iswprint</a></code>(3), <code><a href="/docs/linux/man/3-wcwidth/">wcwidth</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
