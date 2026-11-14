---
title: "iswgraph(3)"
name: "iswgraph"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswgraph/"
description: "iswgraph – test for graphic wide character"
---

<h2 class="name">NAME</h2>
<p> iswgraph &#8211; test for graphic wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wctype.h&gt;
int iswgraph(wint_t wc);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iswgraph</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-isgraph/">isgraph</a></code>(3) function. It tests whether <i>wc</i> is a wide character belonging to the wide-character class &quot;graph&quot;. </p>
<p> The wide-character class &quot;graph&quot; is a subclass of the wide-character class &quot;print&quot;. </p>
<p> Being a subclass of the wide-character class &quot;print&quot;, the wide-character class &quot;graph&quot; is disjoint from the wide-character class &quot;cntrl&quot;. </p>
<p> The wide-character class &quot;graph&quot; is disjoint from the wide-character class &quot;space&quot; and therefore also disjoint from its subclass &quot;blank&quot;. </p>
<p> The wide-character class &quot;graph&quot; contains all the wide characters from the wide-character class &quot;print&quot; except the space character. It therefore contains the wide-character classes &quot;alnum&quot; and &quot;punct&quot;.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswgraph</code>() function returns nonzero if <i>wc</i> is a wide character belonging to the wide-character class &quot;graph&quot;. Otherwise, it returns zero.</p>
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
<td> <code>iswgraph</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswgraph</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-isgraph/">isgraph</a></code>(3), <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
