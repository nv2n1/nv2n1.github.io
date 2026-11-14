---
title: "iswcntrl(3)"
name: "iswcntrl"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswcntrl/"
description: "iswcntrl – test for control wide character"
---

<h2 class="name">NAME</h2>
<p> iswcntrl &#8211; test for control wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wctype.h&gt;
int iswcntrl(wint_t wc);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iswcntrl</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-iscntrl/">iscntrl</a></code>(3) function. It tests whether <i>wc</i> is a wide character belonging to the wide-character class &quot;cntrl&quot;. </p>
<p> The wide-character class &quot;cntrl&quot; is disjoint from the wide-character class &quot;print&quot; and therefore also disjoint from its subclasses &quot;graph&quot;, &quot;alpha&quot;, &quot;upper&quot;, &quot;lower&quot;, &quot;digit&quot;, &quot;xdigit&quot;, &quot;punct&quot;. </p>
<p> For an unsigned char <i>c</i>, <i>iscntrl(c)</i> implies <i>iswcntrl(btowc(c))</i>, but not vice versa.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswcntrl</code>() function returns nonzero if <i>wc</i> is a wide character belonging to the wide-character class &quot;cntrl&quot;. Otherwise, it returns zero.</p>
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
<td> <code>iswcntrl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswcntrl</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iscntrl/">iscntrl</a></code>(3), <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
