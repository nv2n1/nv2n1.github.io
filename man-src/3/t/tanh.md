---
title: "tanh(3)"
name: "tanh"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tanh/"
description: "tanh, tanhf, tanhl – hyperbolic tangent function"
---

<p>tanh, tanhf, tanhl &#8211; hyperbolic tangent function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double tanh(double x);
float tanhf(float x);
long double tanhl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>tanhf</code>(), <code>tanhl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions return the hyperbolic tangent of <i>x</i>, which is defined mathematically as: </p>
<pre> tanh(x) = sinh(x) / cosh(x)</pre>
<h2>Return Value</h2>
<p>On success, these functions return the hyperbolic tangent of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), +0 (-0) is returned. </p>
<p> If <i>x</i> is positive infinity (negative infinity), +1 (-1) is returned.</p>
<h2>Errors</h2>
<p>No errors occur.</p>
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
<td> <code>tanh</code>(), <code>tanhf</code>(), <code>tanhl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-acosh/">acosh</a></code>(3), <code><a href="/docs/linux/man/3-asinh/">asinh</a></code>(3), <code><a href="/docs/linux/man/3-atanh/">atanh</a></code>(3), <code><a href="/docs/linux/man/3-cosh/">cosh</a></code>(3), <code><a href="/docs/linux/man/3-ctanh/">ctanh</a></code>(3), <code><a href="/docs/linux/man/3-sinh/">sinh</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
