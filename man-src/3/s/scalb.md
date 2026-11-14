---
title: "scalb(3)"
name: "scalb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scalb/"
description: "scalb, scalbf, scalbl – multiply floating-point number by integral power of radix (OBSOLETE)"
---

<p>scalb, scalbf, scalbl &#8211; multiply floating-point number by integral power of radix (OBSOLETE)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
double scalb(double x, double exp);


float scalbf(float x, float exp);


long double scalbl(long double x, long double exp);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>scalb</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>scalbf</code>(), <code>scalbl</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;600<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions multiply their first argument <i>x</i> by <code>FLT_RADIX</code> (probably 2) to the power of <i>exp</i>, that is: </p>
<pre> x * FLT_RADIX ** exp</pre>
<p>The definition of <code>FLT_RADIX</code> can be obtained by including <i>&lt;float.h&gt;</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return <i>x</i> * <code>FLT_RADIX</code> ** <i>exp</i>. </p>
<p> If <i>x</i> or <i>exp</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), and <i>exp</i> is not negative infinity, positive infinity (negative infinity) is returned. </p>
<p> If <i>x</i> is +0 (-0), and <i>exp</i> is not positive infinity, +0 (-0) is returned. </p>
<p> If <i>x</i> is zero, and <i>exp</i> is positive infinity, a domain error occurs, and a NaN is returned. </p>
<p> If <i>x</i> is an infinity, and <i>exp</i> is negative infinity, a domain error occurs, and a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with a sign the same as <i>x</i>. </p>
<p> If the result underflows, a range error occurs, and the functions return zero, with a sign the same as <i>x</i>.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is 0, and <i>exp</i> is positive infinity, or <i>x</i> is positive infinity and <i>exp</i> is negative infinity and the other argument is not a NaN</p>
<dd><i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Range error, overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error, underflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</dl>
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
<td> <code>scalb</code>(), <code>scalbf</code>(), <code>scalbl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>scalb</code>() is specified in POSIX.1-2001, but marked obsolescent. POSIX.1-2008 removes the specification of <code>scalb</code>(), recommending the use of <code><a href="/docs/linux/man/3-scalbln/">scalbln</a></code>(3), <code><a href="/docs/linux/man/3-scalblnf/">scalblnf</a></code>(3), or <code><a href="/docs/linux/man/3-scalblnl/">scalblnl</a></code>(3) instead. The <code>scalb</code>() function is from 4.3BSD. </p>
<p> <code>scalbf</code>() and <code>scalbl</code>() are unstandardized; <code>scalbf</code>() is nevertheless present on several other systems</p>
<h2>Bugs</h2>
<p>Before glibc 2.20, these functions did not set <i>errno</i> for domain and range errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldexp/">ldexp</a></code>(3), <code><a href="/docs/linux/man/3-scalbln/">scalbln</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
