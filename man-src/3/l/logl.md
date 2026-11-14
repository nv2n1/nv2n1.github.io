---
title: "logl(3)"
name: "logl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logl/"
description: "log, logf, logl – natural logarithmic function"
---

<h2 class="name">NAME</h2>
<p> log, logf, logl &#8211; natural logarithmic function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double log(double x);
float logf(float x);
long double logl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>logf</code>(), <code>logl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the natural logarithm of <i>x</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the natural logarithm of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is 1, the result is +0. </p>
<p> If <i>x</i> is positive infinity, positive infinity is returned. </p>
<p> If <i>x</i> is zero, then a pole error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. </p>
<p> If <i>x</i> is negative (including negative infinity), then a domain error occurs, and a NaN (not a number) is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is negative</p>
<dd> <i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Pole error: <i>x</i> is zero</p>
<dd> <i>errno</i> is set to <code>ERANGE</code>. A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</dl>
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
<td> <code>log</code>(), <code>logf</code>(), <code>logl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>BUGS</h2>
<p> In glibc 2.5 and earlier, taking the <code>log</code>() of a NaN produces a bogus invalid floating-point (<code>FE_INVALID</code>) exception.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cbrt/">cbrt</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/3-log10/">log10</a></code>(3), <code><a href="/docs/linux/man/3-log1p/">log1p</a></code>(3), <code><a href="/docs/linux/man/3-log2/">log2</a></code>(3), <code><a href="/docs/linux/man/3-sqrt/">sqrt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
