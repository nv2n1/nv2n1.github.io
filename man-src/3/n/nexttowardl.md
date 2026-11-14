---
title: "nexttowardl(3)"
name: "nexttowardl"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nexttowardl/"
description: "nextafter, nextafterf, nextafterl, nexttoward, nexttowardf, nexttowardl – floating-point number manipulation"
---

<p>nextafter, nextafterf, nextafterl, nexttoward, nexttowardf, nexttowardl &#8211; floating-point number manipulation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
double nextafter(double x, double y);


float nextafterf(float x, float y);


long double nextafterl(long double x, long double y);
double nexttoward(double x, long double y);


float nexttowardf(float x, long double y);


long double nexttowardl(long double x, long double y);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>nextafter</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>nextafterf</code>(), <code>nextafterl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>nexttoward</code>(), <code>nexttowardf</code>(), <code>nexttowardl</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;600 || _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>nextafter</code>(), <code>nextafterf</code>(), and <code>nextafterl</code>() functions return the next representable floating-point value following <i>x</i> in the direction of <i>y</i>. If <i>y</i> is less than <i>x</i>, these functions will return the largest representable number less than <i>x</i>. </p>
<p> If <i>x</i> equals <i>y</i>, the functions return <i>y</i>. </p>
<p> The <code>nexttoward</code>(), <code>nexttowardf</code>(), and <code>nexttowardl</code>() functions do the same as the corresponding <code>nextafter</code>() functions, except that they have a <i>long double</i> second argument.</p>
<h2>Return Value</h2>
<p>On success, these functions return the next representable floating-point value after <i>x</i> in the direction of <i>y</i>. </p>
<p> If <i>x</i> equals <i>y</i>, then <i>y</i> (cast to the same type as <i>x</i>) is returned. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is finite, and the result would overflow, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the correct mathematical sign. </p>
<p> If <i>x</i> is not equal to <i>y</i>, and the correct function result would be subnormal, zero, or underflow, a range error occurs, and either the correct value (if it can be represented), or 0.0, is returned.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Range error: result overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error: result is subnormal or underflows</p>
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
<td> <code>nextafter</code>(), <code>nextafterf</code>(),<br />
 <code>nextafterl</code>(), <code>nexttoward</code>(),<br />
 <code>nexttowardf</code>(), <code>nexttowardl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. This function is defined in IEC 559 (and the appendix with recommended functions in IEEE 754/IEEE 854).</p>
<h2>Bugs</h2>
<p>In glibc version 2.5 and earlier, these functions do not raise an underflow floating-point (<code>FE_UNDERFLOW</code>) exception when an underflow occurs. </p>
<p> Before glibc version 2.23 these functions did not set <i>errno</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nearbyint/">nearbyint</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
