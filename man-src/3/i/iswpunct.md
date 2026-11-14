---
title: "iswpunct(3)"
name: "iswpunct"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswpunct/"
description: "iswpunct – test for punctuation or symbolic wide character"
---

<h2 class="name">NAME</h2>
<p> iswpunct &#8211; test for punctuation or symbolic wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wctype.h&gt;
int iswpunct(wint_t wc);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iswpunct</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-ispunct/">ispunct</a></code>(3) function. It tests whether <i>wc</i> is a wide character belonging to the wide-character class &quot;punct&quot;. </p>
<p> The wide-character class &quot;punct&quot; is a subclass of the wide-character class &quot;graph&quot;, and therefore also a subclass of the wide-character class &quot;print&quot;. </p>
<p> The wide-character class &quot;punct&quot; is disjoint from the wide-character class &quot;alnum&quot; and therefore also disjoint from its subclasses &quot;alpha&quot;, &quot;upper&quot;, &quot;lower&quot;, &quot;digit&quot;, &quot;xdigit&quot;. </p>
<p> Being a subclass of the wide-character class &quot;print&quot;, the wide-character class &quot;punct&quot; is disjoint from the wide-character class &quot;cntrl&quot;. </p>
<p> Being a subclass of the wide-character class &quot;graph&quot;, the wide-character class &quot;punct&quot; is disjoint from the wide-character class &quot;space&quot; and its subclass &quot;blank&quot;.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswpunct</code>() function returns nonzero if <i>wc</i> is a wide-character belonging to the wide-character class &quot;punct&quot;. Otherwise, it returns zero.</p>
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
<td> <code>iswpunct</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswpunct</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> This function&#8217;s name is a misnomer when dealing with Unicode characters, because the wide-character class &quot;punct&quot; contains both punctuation characters and symbol (math, currency, etc.) characters.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ispunct/">ispunct</a></code>(3), <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
