---

title: "mbtowc(3)"
name: "mbtowc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbtowc/"
description: "mbtowc – convert a multibyte sequence to a wide character"
---

<p> mbtowc &#8211; convert a multibyte sequence to a wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int mbtowc(wchar_t *pwc, const char *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The main case for this function is when <i>s</i> is not NULL and <i>pwc</i> is not NULL. In this case, the <code>mbtowc</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i>, extracts the next complete multibyte character, converts it to a wide character and stores it at <i>*pwc</i>. It updates an internal shift state known only to the <code>mbtowc</code>() function. If <i>s</i> does not point to a null byte (&#8216;\0&#8217;), it returns the number of bytes that were consumed from <i>s</i>, otherwise it returns 0. </p>
<p> If the <i>n</i> bytes starting at <i>s</i> do not contain a complete multibyte character, or if they contain an invalid multibyte sequence, <code>mbtowc</code>() returns -1. This can happen even if <i>n</i> &gt;= <i>MB_CUR_MAX</i>, if the multibyte string contains redundant shift sequences. </p>
<p> A different case is when <i>s</i> is not NULL but <i>pwc</i> is NULL. In this case, the <code>mbtowc</code>() function behaves as above, except that it does not store the converted wide character in memory. </p>
<p> A third case is when <i>s</i> is NULL. In this case, <i>pwc</i> and <i>n</i> are ignored. The <code>mbtowc</code>() function resets the shift state, only known to this function, to the initial state, and returns nonzero if the encoding has nontrivial shift state, or zero if the encoding is stateless.  </p>
<h2>RETURN VALUE</h2>
<p> If <i>s</i> is not NULL, the <code>mbtowc</code>() function returns the number of consumed bytes starting at <i>s</i>, or 0 if <i>s</i> points to a null byte, or -1 upon failure. </p>
<p> If <i>s</i> is NULL, the <code>mbtowc</code>() function returns nonzero if the encoding has nontrivial shift state, or zero if the encoding is stateless.  </p>
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
<td> <code>mbtowc</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>mbtowc</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> This function is not multithread safe. The function <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3) provides a better interface to the same functionality.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-MB_CUR_MAX/">MB_CUR_MAX</a></code>(3), <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3), <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3), <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3), <code><a href="/docs/linux/man/3-wcstombs/">wcstombs</a></code>(3), <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
