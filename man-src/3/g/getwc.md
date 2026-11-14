---
title: "getwc(3)"
name: "getwc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getwc/"
description: "fgetwc, getwc – read a wide character from a FILE stream"
---

<h2 class="name">NAME</h2>
<p> fgetwc, getwc &#8211; read a wide character from a FILE stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
#include &lt;wchar.h&gt;
wint_t fgetwc(FILE *stream);
wint_t getwc(FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fgetwc</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-fgetc/">fgetc</a></code>(3) function. It reads a wide character from <i>stream</i> and returns it. If the end of stream is reached, or if <i>ferror(stream)</i> becomes true, it returns <code>WEOF</code>. If a wide-character conversion error occurs, it sets <i>errno</i> to <code>EILSEQ</code> and returns <code>WEOF</code>. </p>
<p> The <code>getwc</code>() function or macro functions identically to <code>fgetwc</code>(). It may be implemented as a macro, and may evaluate its argument more than once. There is no reason ever to use it. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> The <code>fgetwc</code>() function returns the next wide-character from the stream, or <code>WEOF</code>. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<p> Apart from the usual ones, there is</p>
<dl>
<dt><code>EILSEQ</code></p>
<dd> The data obtained from the input stream does not form a valid character.</dl>
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
<td> <code>fgetwc</code>(), <code>getwc</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>fgetwc</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> In the absence of additional information passed to the <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3) call, it is reasonable to expect that <code>fgetwc</code>() will actually read a multibyte sequence from the stream and then convert it to a wide character.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fgetws/">fgetws</a></code>(3), <code><a href="/docs/linux/man/3-fputwc/">fputwc</a></code>(3), <code><a href="/docs/linux/man/3-ungetwc/">ungetwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
