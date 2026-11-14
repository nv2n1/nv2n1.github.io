---
title: "putwchar(3)"
name: "putwchar"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putwchar/"
description: "putwchar – write a wide character to standard output"
---

<p>putwchar &#8211; write a wide character to standard output</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wint_t putwchar(wchar_t wc);</code></pre>
<h2>Description</h2>
<p>The <code>putwchar</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-putchar/">putchar</a></code>(3) function. It writes the wide character <i>wc</i> to <i>stdout</i>. If <i>ferror(stdout)</i> becomes true, it returns <code>WEOF</code>. If a wide character conversion error occurs, it sets <i>errno</i> to <code>EILSEQ</code> and returns <code>WEOF</code>. Otherwise, it returns <i>wc</i>. </p>
<p> For a nonlocking counterpart, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>Return Value</h2>
<p>The <code>putwchar</code>() function returns <i>wc</i> if no error occurred, or <code>WEOF</code> to indicate an error.</p>
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
<td> <code>putwchar</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>putwchar</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> It is reasonable to expect that <code>putwchar</code>() will actually write the multibyte sequence corresponding to the wide character <i>wc</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fputwc/">fputwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
