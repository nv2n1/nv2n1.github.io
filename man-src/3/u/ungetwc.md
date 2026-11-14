---
title: "ungetwc(3)"
name: "ungetwc"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ungetwc/"
description: "ungetwc – push back a wide character onto a FILE stream"
---

<p>ungetwc &#8211; push back a wide character onto a FILE stream</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

wint_t ungetwc(wint_t wc, FILE *stream);</code></pre>
<h2>Description</h2>
<p>The <code>ungetwc</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-ungetc/">ungetc</a></code>(3) function. It pushes back a wide character onto <i>stream</i> and returns it. </p>
<p> If <i>wc</i> is <code>WEOF</code>, it returns <code>WEOF</code>. If <i>wc</i> is an invalid wide character, it sets <i>errno</i> to <code>EILSEQ</code> and returns <code>WEOF</code>. </p>
<p> If <i>wc</i> is a valid wide character, it is pushed back onto the stream and thus becomes available for future wide-character read operations. The file-position indicator is decremented by one or more. The end-of-file indicator is cleared. The backing storage of the file is not affected. </p>
<p> Note: <i>wc</i> need not be the last wide-character read from the stream; it can be any other valid wide character. </p>
<p> If the implementation supports multiple push-back operations in a row, the pushed-back wide characters will be read in reverse order; however, only one level of push-back is guaranteed.</p>
<h2>Return Value</h2>
<p>The <code>ungetwc</code>() function returns <i>wc</i> when successful, or <code>WEOF</code> upon failure.</p>
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
<td> <code>ungetwc</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>ungetwc</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
