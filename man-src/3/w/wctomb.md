---
title: "wctomb(3)"
name: "wctomb"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wctomb/"
description: "wctomb – convert a wide character to a multibyte sequence"
---

<p>wctomb &#8211; convert a wide character to a multibyte sequence</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int wctomb(char *s, wchar_t wc);</code></pre>
<h2>Description</h2>
<p>If <i>s</i> is not NULL, the <code>wctomb</code>() function converts the wide character <i>wc</i> to its multibyte representation and stores it at the beginning of the character array pointed to by <i>s</i>. It updates the shift state, which is stored in a static anonymous variable known only to the <code>wctomb</code>() function, and returns the length of said multibyte representation, that is, the number of bytes written at <i>s</i>. </p>
<p> The programmer must ensure that there is room for at least <code>MB_CUR_MAX</code> bytes at <i>s</i>. </p>
<p> If <i>s</i> is NULL, the <code>wctomb</code>() function resets the shift state, known only to this function, to the initial state, and returns nonzero if the encoding has nontrivial shift state, or zero if the encoding is stateless.</p>
<h2>Return Value</h2>
<p>If <i>s</i> is not NULL, the <code>wctomb</code>() function returns the number of bytes that have been written to the byte array at <i>s</i>. If <i>wc</i> can not be represented as a multibyte sequence (according to the current locale), -1 is returned. </p>
<p> If <i>s</i> is NULL, the <code>wctomb</code>() function returns nonzero if the encoding has nontrivial shift state, or zero if the encoding is stateless.</p>
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
<td> <code>wctomb</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>wctomb</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> The function <code><a href="/docs/linux/man/3-wcrtomb/">wcrtomb</a></code>(3) provides a better interface to the same functionality.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mb_cur_max/">MB_CUR_MAX</a></code>(3), <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3), <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3), <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3), <code><a href="/docs/linux/man/3-wcrtomb/">wcrtomb</a></code>(3), <code><a href="/docs/linux/man/3-wcstombs/">wcstombs</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
