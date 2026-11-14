---
title: "lldiv(3)"
name: "lldiv"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lldiv/"
description: "div, ldiv, lldiv, imaxdiv – compute quotient and remainder of an integer division"
---

<h2 class="name">NAME</h2>
<p> div, ldiv, lldiv, imaxdiv &#8211; compute quotient and remainder of an integer division </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
div_t div(int numerator, int denominator);
ldiv_t ldiv(long numerator, long denominator);
lldiv_t lldiv(long long numerator, long long denominator);
#include &lt;inttypes.h&gt;
imaxdiv_t imaxdiv(intmax_t numerator, intmax_t denominator);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>lldiv</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> The <code>div</code>() function computes the value <i>numerator</i>/<i>denominator</i> and returns the quotient and remainder in a structure named <i>div_t</i> that contains two integer members (in unspecified order) named <i>quot</i> and <i>rem</i>. The quotient is rounded toward zero. The result satisfies <i>quot</i>*<i>denominator</i>+<i>rem</i> = <i>numerator</i>. </p>
<p> The <code>ldiv</code>(), <code>lldiv</code>(), and <code>imaxdiv</code>() functions do the same, dividing numbers of the indicated type and returning the result in a structure of the indicated name, in all cases with fields <i>quot</i> and <i>rem</i> of the same type as the function arguments.</p>
<h2>RETURN VALUE</h2>
<p> The <i>div_t</i> (etc.) structure.</p>
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
<td> <code>div</code>(), <code>ldiv</code>(), <code>lldiv</code>(), <code>imaxdiv</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD. The functions <code>lldiv</code>() and <code>imaxdiv</code>() were added in C99.</p>
<h2>EXAMPLES</h2>
<p> After </p>
<p> div_t q = div(-5, 3); </p>
<p> the values <i>q.quot</i> and <i>q.rem</i> are -1 and -2, respectively.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-abs/">abs</a></code>(3), <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
