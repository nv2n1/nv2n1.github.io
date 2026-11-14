---
title: "mbrlen(3)"
name: "mbrlen"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbrlen/"
description: "mbrlen – determine number of bytes in next multibyte character"
---

<h2 class="name">NAME</h2>
<p> mbrlen &#8211; determine number of bytes in next multibyte character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
size_t mbrlen(const char *s, size_t n, mbstate_t *ps);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>mbrlen</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i> and extracts the next complete multibyte character. It updates the shift state <i>*ps</i>. If the multibyte character is not the null wide character, it returns the number of bytes that were consumed from <i>s</i>. If the multibyte character is the null wide character, it resets the shift state <i>*ps</i> to the initial state and returns 0. </p>
<p> If the <i>n</i> bytes starting at <i>s</i> do not contain a complete multibyte character, <code>mbrlen</code>() returns <i>(size_t)&nbsp;-2</i>. This can happen even if <i>n</i> &gt;= <i>MB_CUR_MAX</i>, if the multibyte string contains redundant shift sequences. </p>
<p> If the multibyte string starting at <i>s</i> contains an invalid multibyte sequence before the next complete character, <code>mbrlen</code>() returns <i>(size_t)&nbsp;-1</i> and sets <i>errno</i> to <code>EILSEQ</code>. In this case, the effects on <i>*ps</i> are undefined. </p>
<p> If <i>ps</i> is NULL, a static anonymous state known only to the <code>mbrlen</code>() function is used instead.</p>
<h2>RETURN VALUE</h2>
<p> The <code>mbrlen</code>() function returns the number of bytes parsed from the multibyte sequence starting at <i>s</i>, if a non-null wide character was recognized. It returns 0, if a null wide character was recognized. It returns <i>(size_t)&nbsp;-1</i> and sets <i>errno</i> to <code>EILSEQ</code>, if an invalid multibyte sequence was encountered. It returns <i>(size_t)&nbsp;-2</i> if it couldn&#8217;t parse a complete multibyte character, meaning that <i>n</i> should be increased.</p>
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
<td> <code>mbrlen</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:mbrlen/!ps
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>mbrlen</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
