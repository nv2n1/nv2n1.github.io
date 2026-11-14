---
title: "wctob(3)"
name: "wctob"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wctob/"
description: "wctob – try to represent a wide character as a single byte"
---

<p>wctob &#8211; try to represent a wide character as a single byte</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

int wctob(wint_t c);</code></pre>
<h2>Description</h2>
<p>The <code>wctob</code>() function tests whether the multibyte representation of the wide character <i>c</i>, starting in the initial state, consists of a single byte. If so, it is returned as an <i>unsigned char</i>. </p>
<p> Never use this function. It cannot help you in writing internationalized programs. Internationalized programs must never distinguish single-byte and multibyte characters.</p>
<h2>Return Value</h2>
<p>The <code>wctob</code>() function returns the single-byte representation of <i>c</i>, if it exists, or <code>EOF</code> otherwise.</p>
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
<td> <code>wctob</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>wctob</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> This function should never be used. Internationalized programs must never distinguish single-byte and multibyte characters. Use either <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3) or the thread-safe <code><a href="/docs/linux/man/3-wcrtomb/">wcrtomb</a></code>(3) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-btowc/">btowc</a></code>(3), <code><a href="/docs/linux/man/3-wcrtomb/">wcrtomb</a></code>(3), <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
