---
title: "mblen(3)"
name: "mblen"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mblen/"
description: "mblen – determine number of bytes in next multibyte character"
---

<h2 class="name">NAME</h2>
<p> mblen &#8211; determine number of bytes in next multibyte character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int mblen(const char *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>s</i> is not NULL, the <code>mblen</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i> and extracts the next complete multibyte character. It uses a static anonymous shift state known only to the <code>mblen</code>() function. If the multibyte character is not the null wide character, it returns the number of bytes that were consumed from <i>s</i>. If the multibyte character is the null wide character, it returns 0. </p>
<p> If the <i>n</i> bytes starting at <i>s</i> do not contain a complete multibyte character, <code>mblen</code>() returns -1. This can happen even if <i>n</i> is greater than or equal to <i>MB_CUR_MAX</i>, if the multibyte string contains redundant shift sequences. </p>
<p> If the multibyte string starting at <i>s</i> contains an invalid multibyte sequence before the next complete character, <code>mblen</code>() also returns -1. </p>
<p> If <i>s</i> is NULL, the <code>mblen</code>() function resets the shift state, known to only this function, to the initial state, and returns nonzero if the encoding has nontrivial shift state, or zero if the encoding is stateless.</p>
<h2>RETURN VALUE</h2>
<p> The <code>mblen</code>() function returns the number of bytes parsed from the multibyte sequence starting at <i>s</i>, if a non-null wide character was recognized. It returns 0, if a null wide character was recognized. It returns -1, if an invalid multibyte sequence was encountered or if it couldn&#8217;t parse a complete multibyte character.</p>
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
<td> <code>mblen</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>mblen</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> The function <code><a href="/docs/linux/man/3-mbrlen/">mbrlen</a></code>(3) provides a better interface to the same functionality.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbrlen/">mbrlen</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
