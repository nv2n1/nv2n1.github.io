---
title: "btowc(3)"
name: "btowc"
section: "3"
letter: "b"
url: "/docs/linux/man/3-btowc/"
description: "btowc – convert single byte to wide character"
---

<h2 class="name">NAME</h2>
<p> btowc &#8211; convert single byte to wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
wint_t btowc(int c);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>btowc</code>() function converts <i>c</i>, interpreted as a multibyte sequence of length 1, starting in the initial shift state, to a wide character and returns it. If <i>c</i> is <code>EOF</code> or not a valid multibyte sequence of length 1, the <code>btowc</code>() function returns <code>WEOF</code>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>btowc</code>() function returns the wide character converted from the single byte <i>c</i>. If <i>c</i> is <code>EOF</code> or not a valid multibyte sequence of length 1, it returns <code>WEOF</code>.</p>
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
<td> <code>btowc</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>btowc</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> This function should never be used. It does not work for encodings which have state, and unnecessarily treats single bytes differently from multibyte sequences. Use either <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3) or the thread-safe <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3) instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3), <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3), <code><a href="/docs/linux/man/3-wctob/">wctob</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
