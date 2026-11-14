---
title: "towctrans(3)"
name: "towctrans"
section: "3"
letter: "t"
url: "/docs/linux/man/3-towctrans/"
description: "towctrans – wide-character transliteration"
---

<p>towctrans &#8211; wide-character transliteration</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wctype.h&gt;

wint_t towctrans(wint_t wc, wctrans_t desc);</code></pre>
<h2>Description</h2>
<p>If <i>wc</i> is a wide character, the <code>towctrans</code>() function translates it according to the transliteration descriptor <i>desc</i>. If <i>wc</i> is <code>WEOF</code>, <code>WEOF</code> is returned. </p>
<p> <i>desc</i> must be a transliteration descriptor returned by the <code><a href="/docs/linux/man/3-wctrans/">wctrans</a></code>(3) function.</p>
<h2>Return Value</h2>
<p>The <code>towctrans</code>() function returns the translated wide character, or <code>WEOF</code> if <i>wc</i> is <code>WEOF</code>.</p>
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
<td> <code>towctrans</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>towctrans</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-towlower/">towlower</a></code>(3), <code><a href="/docs/linux/man/3-towupper/">towupper</a></code>(3), <code><a href="/docs/linux/man/3-wctrans/">wctrans</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
