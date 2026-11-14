---
title: "fputwc(3)"
name: "fputwc"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fputwc/"
description: "fputwc, putwc – write a wide character to a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fputwc, putwc &#8211; write a wide character to a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
#include &lt;wchar.h&gt;
wint_t fputwc(wchar_t wc, FILE *stream);
wint_t putwc(wchar_t wc, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fputwc</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fputc/">fputc</a></code>(3) function. It writes the wide character <i>wc</i> to <i>stream</i>. If <i>ferror(stream)</i> becomes true, it returns <code>WEOF</code>. If a wide-character conversion error occurs, it sets <i>errno</i> to <code>EILSEQ</code> and returns <code>WEOF</code>. Otherwise, it returns <i>wc</i>. </p>
<p> The <code>putwc</code>() function or macro functions identically to <code>fputwc</code>(). It may be implemented as a macro, and may evaluate its argument more than once. There is no reason ever to use it. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> The <code>fputwc</code>() function returns <i>wc</i> if no error occurred, or <code>WEOF</code> to indicate an error. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<p> Apart from the usual ones, there is</p>
<dl>
<dt><code>EILSEQ</code></p>
<dd> Conversion of <i>wc</i> to the stream&#8217;s encoding fails.</dl>
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
<td> <code>fputwc</code>(), <code>putwc</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>fputwc</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> In the absence of additional information passed to the <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) call, it is reasonable to expect that <code>fputwc</code>() will actually write the multibyte sequence corresponding to the wide character <i>wc</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3), <code><a href="/docs/linux/man/3-fputws/">fputws</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
