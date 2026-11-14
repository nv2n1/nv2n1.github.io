---
title: "iswxdigit(3)"
name: "iswxdigit"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswxdigit/"
description: "iswxdigit – test for hexadecimal digit wide character"
---

<h2 class="name">NAME</h2>
<p> iswxdigit &#8211; test for hexadecimal digit wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wctype.h&gt;
int iswxdigit(wint_t wc);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iswxdigit</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-isxdigit/">isxdigit</a></code>(3) function. It tests whether <i>wc</i> is a wide character belonging to the wide-character class &quot;xdigit&quot;. </p>
<p> The wide-character class &quot;xdigit&quot; is a subclass of the wide-character class &quot;alnum&quot;, and therefore also a subclass of the wide-character class &quot;graph&quot; and of the wide-character class &quot;print&quot;. </p>
<p> Being a subclass of the wide-character class &quot;print&quot;, the wide-character class &quot;xdigit&quot; is disjoint from the wide-character class &quot;cntrl&quot;. </p>
<p> Being a subclass of the wide-character class &quot;graph&quot;, the wide-character class &quot;xdigit&quot; is disjoint from the wide-character class &quot;space&quot; and its subclass &quot;blank&quot;. </p>
<p> Being a subclass of the wide-character class &quot;alnum&quot;, the wide-character class &quot;xdigit&quot; is disjoint from the wide-character class &quot;punct&quot;. </p>
<p> The wide-character class &quot;xdigit&quot; always contains at least the letters &#8216;A&#8217; to &#8216;F&#8217;, &#8216;a&#8217; to &#8216;f&#8217; and the digits &#8216;0&#8217; to &#8216;9&#8217;.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswxdigit</code>() function returns nonzero if <i>wc</i> is a wide character belonging to the wide-character class &quot;xdigit&quot;. Otherwise, it returns zero.</p>
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
<td> <code>iswxdigit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswxdigit</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3), <code><a href="/docs/linux/man/3-isxdigit/">isxdigit</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
