---
title: "log1pf(3)"
name: "log1pf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log1pf/"
description: "log1p, log1pf, log1pl – logarithm of 1 plus argument"
---

<h2 class="name">NAME</h2>
<p> log1p, log1pf, log1pl &#8211; logarithm of 1 plus argument </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double log1p(double x);
float log1pf(float x);
long double log1pl(long double x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>log1p</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>log1pf</code>(), <code>log1pl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return a value equivalent to </p>
<pre>
    log (1 + <i>x</i>)
</pre>
<p> The result is computed in a way that is accurate even if the value of <i>x</i> is near zero.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the natural logarithm of <i>(1&nbsp;+&nbsp;x)</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity, positive infinity is returned. </p>
<p> If <i>x</i> is -1, a pole error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. </p>
<p> If <i>x</i> is less than -1 (including negative infinity), a domain error occurs, and a NaN (not a number) is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is less than -1</p>
<dd> <i>errno</i> is set to <code>EDOM</code> (but see BUGS). An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Pole error: <i>x</i> is -1</p>
<dd> <i>errno</i> is set to <code>ERANGE</code> (but see BUGS). A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</dl>
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
<td> <code>log1p</code>(), <code>log1pf</code>(), <code>log1pl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>BUGS</h2>
<p> Before version 2.22, the glibc implementation did not set <i>errno</i> to <code>EDOM</code> when a domain error occurred. </p>
<p> Before version 2.22, the glibc implementation did not set <i>errno</i> to <code>ERANGE</code> when a range error occurred.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exp/">exp</a></code>(3), <code><a href="/docs/linux/man/3-expm1/">expm1</a></code>(3), <code><a href="/docs/linux/man/3-log/">log</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
