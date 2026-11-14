---
title: "scalbnl(3)"
name: "scalbnl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scalbnl/"
description: "scalbn, scalbnf, scalbnl, scalbln, scalblnf, scalblnl – multiply floating-point number by integral power of radix"
---

<p>scalbn, scalbnf, scalbnl, scalbln, scalblnf, scalblnl &#8211; multiply floating-point number by integral power of radix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
double scalbln(double x, long exp);

float scalblnf(float x, long exp);

long double scalblnl(long double x, long exp);
double scalbn(double x, int exp);

float scalbnf(float x, int exp);

long double scalbnl(long double x, int exp);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>scalbln</code>(), <code>scalblnf</code>(), <code>scalblnl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE</dl>
<p> <code>scalbn</code>(), <code>scalbnf</code>(), <code>scalbnl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions multiply their first argument <i>x</i> by <code>FLT_RADIX</code> (probably 2) to the power of <i>exp</i>, that is: </p>
<pre> x * FLT_RADIX ** exp</pre>
<p>The definition of <code>FLT_RADIX</code> can be obtained by including <i>&lt;float.h&gt;</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return <i>x</i> * <code>FLT_RADIX</code> ** <i>exp</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), positive infinity (negative infinity) is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with a sign the same as <i>x</i>. </p>
<p> If the result underflows, a range error occurs, and the functions return zero, with a sign the same as <i>x</i>.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error, overflow</p>
<dd>An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error, underflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised.</dl>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>scalbn</code>(), <code>scalbnf</code>(), <code>scalbnl</code>(),<br />
 <code>scalbln</code>(), <code>scalblnf</code>(), <code>scalblnl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>These functions differ from the obsolete functions described in <code><a href="/docs/linux/man/3-scalb/">scalb</a></code>(3) in the type of their second argument. The functions described on this page have a second argument of an integral type, while those in <code><a href="/docs/linux/man/3-scalb/">scalb</a></code>(3) have a second argument of type <i>double</i>. </p>
<p> If <code>FLT_RADIX</code> equals 2 (which is usual), then <code>scalbn</code>() is equivalent to <code><a href="/docs/linux/man/3-ldexp/">ldexp</a></code>(3).</p>
<h2>Bugs</h2>
<p>Before glibc 2.20, these functions did not set <i>errno</i> for range errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldexp/">ldexp</a></code>(3), <code><a href="/docs/linux/man/3-scalb/">scalb</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
