---
title: "modff(3)"
name: "modff"
section: "3"
letter: "m"
url: "/docs/linux/man/3-modff/"
description: "modf, modff, modfl – extract signed integral and fractional values from floating-point number"
---

<p>modf, modff, modfl &#8211; extract signed integral and fractional values from floating-point number </p>
<h2>Synopsis</h2>
<pre>
<code>#include &lt;math.h&gt;</code>
<code>double modf(double </code><i>x</i><code>, double *</code><i>iptr</i><code>);</code>
<code>float modff(float </code><i>x</i><code>, float *</code><i>iptr</i><code>);</code>
<code>long double modfl(long double </code><i>x</i><code>, long double *</code><i>iptr</i><code>);</code>
</pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>modff</code>(), <code>modfl</code>():</p>
<dl COMPACT>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p> These functions break the argument <i>x</i> into an integral part and a fractional part, each of which has the same sign as <i>x</i>. The integral part is stored in the location pointed to by <i>iptr</i>.</p>
<h2>Return Value</h2>
<p> These functions return the fractional part of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned, and <i>*iptr</i> is set to a NaN. </p>
<p> If <i>x</i> is positive infinity (negative infinity), +0 (-0) is returned, and <i>*iptr</i> is set to positive infinity (negative infinity).</p>
<h2>Errors</h2>
<p> No errors occur.</p>
<h2>Attributes</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>modf</code>(), <code>modff</code>(), <code>modfl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-frexp/">frexp</a></code>(3), <code><a href="/docs/linux/man/3-ldexp/">ldexp</a></code>(3)</p>
<h2>Colophon</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
