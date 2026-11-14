---
title: "sinhl(3)"
name: "sinhl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sinhl/"
description: "sinh, sinhf, sinhl – hyperbolic sine function"
---

<p>sinh, sinhf, sinhl &#8211; hyperbolic sine function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double sinh(double x);
float sinhf(float x);
long double sinhl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sinhf</code>(), <code>sinhl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions return the hyperbolic sine of <i>x</i>, which is defined mathematically as: </p>
<pre> sinh(x) = (exp(x) - exp(-x)) / 2</pre>
<h2>Return Value</h2>
<p>On success, these functions return the hyperbolic sine of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), positive infinity (negative infinity) is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the same sign as <i>x</i>.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
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
<td> <code>sinh</code>(), <code>sinhf</code>(), <code>sinhl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-acosh/">acosh</a></code>(3), <code><a href="/docs/linux/man/3-asinh/">asinh</a></code>(3), <code><a href="/docs/linux/man/3-atanh/">atanh</a></code>(3), <code><a href="/docs/linux/man/3-cosh/">cosh</a></code>(3), <code><a href="/docs/linux/man/3-csinh/">csinh</a></code>(3), <code><a href="/docs/linux/man/3-tanh/">tanh</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
