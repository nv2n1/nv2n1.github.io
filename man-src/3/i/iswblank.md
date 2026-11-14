---
title: "iswblank(3)"
name: "iswblank"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswblank/"
description: "iswblank – test for whitespace wide character"
---

<h2 class="name">NAME</h2>
<p> iswblank &#8211; test for whitespace wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wctype.h&gt;
int iswblank(wint_t wc);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>iswblank</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> The <code>iswblank</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-isblank/">isblank</a></code>(3) function. It tests whether <i>wc</i> is a wide character belonging to the wide-character class &quot;blank&quot;. </p>
<p> The wide-character class &quot;blank&quot; is a subclass of the wide-character class &quot;space&quot;. </p>
<p> Being a subclass of the wide-character class &quot;space&quot;, the wide-character class &quot;blank&quot; is disjoint from the wide-character class &quot;graph&quot; and therefore also disjoint from its subclasses &quot;alnum&quot;, &quot;alpha&quot;, &quot;upper&quot;, &quot;lower&quot;, &quot;digit&quot;, &quot;xdigit&quot;, &quot;punct&quot;. </p>
<p> The wide-character class &quot;blank&quot; always contains at least the space character and the control character &#8216;	&#8217;.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswblank</code>() function returns nonzero if <i>wc</i> is a wide character belonging to the wide-character class &quot;blank&quot;. Otherwise, it returns zero.</p>
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
<td> <code>iswblank</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswblank</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-isblank/">isblank</a></code>(3), <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
