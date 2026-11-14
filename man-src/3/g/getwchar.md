---
title: "getwchar(3)"
name: "getwchar"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getwchar/"
description: "getwchar – read a wide character from standard input"
---

<h2 class="name">NAME</h2>
<p> getwchar &#8211; read a wide character from standard input </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
wint_t getwchar(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getwchar</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-getchar/">getchar</a></code>(3) function. It reads a wide character from <i>stdin</i> and returns it. If the end of stream is reached, or if <i>ferror(stdin)</i> becomes true, it returns <code>WEOF</code>. If a wide-character conversion error occurs, it sets <i>errno</i> to <code>EILSEQ</code> and returns <code>WEOF</code>. </p>
<p> For a nonlocking counterpart, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> The <code>getwchar</code>() function returns the next wide-character from standard input, or <code>WEOF</code>.</p>
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
<td> <code>getwchar</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>getwchar</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> It is reasonable to expect that <code>getwchar</code>() will actually read a multibyte sequence from standard input and then convert it to a wide character.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
