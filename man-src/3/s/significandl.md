---
title: "significandl(3)"
name: "significandl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-significandl/"
description: "significand, significandf, significandl – get mantissa of floating-point number"
---

<p>significand, significandf, significandl &#8211; get mantissa of floating-point number</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
double significand(double x);


float significandf(float x);


long double significandl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>significand</code>(), <code>significandf</code>(), <code>significandl</code>():</p>
<dl>
<dd>/* Since glibc 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions return the mantissa of <i>x</i> scaled to the range [1,2). They are equivalent to </p>
<p> scalb(x, (double) -ilogb(x)) </p>
<p> This function exists mainly for use in certain standardized tests for IEEE 754 conformance.</p>
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
<td> <code>significand</code>(),<br />
 <code>significandf</code>(),<br />
 <code>significandl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard; the <i>double</i> version is available on a number of other systems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ilogb/">ilogb</a></code>(3), <code><a href="/docs/linux/man/3-scalb/">scalb</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
