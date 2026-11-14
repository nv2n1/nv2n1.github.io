---
title: "ynf(3)"
name: "ynf"
section: "3"
letter: "y"
url: "/docs/linux/man/3-ynf/"
description: "y0, y0f, y0l, y1, y1f, y1l, yn, ynf, ynl – Bessel functions of the second kind"
---

<p>y0, y0f, y0l, y1, y1f, y1l, yn, ynf, ynl &#8211; Bessel functions of the second kind</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double y0(double x);
double y1(double x);
double yn(int n, double x);

float y0f(float x);
float y1f(float x);
float ynf(int n, float x);

long double y0l(long double x);
long double y1l(long double x);
long double ynl(int n, long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>y0</code>(), <code>y1</code>(), <code>yn</code>():</p>
<dl>
<dd>_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<p> <code>y0f</code>(), <code>y0l</code>(), <code>y1f</code>(), <code>y1l</code>(), <code>ynf</code>(), <code>ynl</code>():</p>
<dl>
<dd>_XOPEN_SOURCE &nbsp;&gt;=&nbsp;600<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;(_ISOC99_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p>The <code>y0</code>() and <code>y1</code>() functions return Bessel functions of <i>x</i> of the second kind of orders 0 and 1, respectively. The <code>yn</code>() function returns the Bessel function of <i>x</i> of the second kind of order <i>n</i>. </p>
<p> The value of <i>x</i> must be positive. </p>
<p> The <code>y0f</code>(), <code>y1f</code>(), and <code>ynf</code>() functions are versions that take and return <i>float</i> values. The <code>y0l</code>(), <code>y1l</code>(), and <code>ynl</code>() functions are versions that take and return <i>long double</i> values.</p>
<h2>Return Value</h2>
<p>On success, these functions return the appropriate Bessel value of the second kind for <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is negative, a domain error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. (POSIX.1-2001 also allows a NaN return for this case.) </p>
<p> If <i>x</i> is 0.0, a pole error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. </p>
<p> If the result underflows, a range error occurs, and the functions return 0.0 </p>
<p> If the result overflows, a range error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. (POSIX.1-2001 also allows a 0.0 return for this case.)</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is negative</p>
<dd><i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Pole error: <i>x</i> is 0.0</p>
<dd><i>errno</i> is set to <code>ERANGE</code> and an <code>FE_DIVBYZERO</code> exception is raised (but see BUGS).</p>
<dt>Range error: result underflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. No <code>FE_UNDERFLOW</code> exception is returned by <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3) for this case.</p>
<dt>Range error: result overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code> (but see BUGS). An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
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
<td> <code>y0</code>(), <code>y0f</code>(), <code>y0l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>y1</code>(), <code>y1f</code>(), <code>y1l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>yn</code>(), <code>ynf</code>(), <code>ynl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The functions returning <i>double</i> conform to SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. The others are nonstandard functions that also exist on the BSDs.</p>
<h2>Bugs</h2>
<p>Before glibc 2.19, these functions misdiagnosed pole errors: <i>errno</i> was set to <code>EDOM</code>, instead of <code>ERANGE</code> and no <code>FE_DIVBYZERO</code> exception was raised. </p>
<p> Before glibc 2.17, did not set <i>errno</i> for &quot;range error: result underflow&quot;. </p>
<p> In glibc version 2.3.2 and earlier, these functions do not raise an invalid floating-point exception (<code>FE_INVALID</code>) when a domain error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-j0/">j0</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
