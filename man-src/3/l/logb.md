---
title: "logb(3)"
name: "logb"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logb/"
description: "logb, logbf, logbl – get exponent of a floating-point value"
---

<h2 class="name">NAME</h2>
<p> logb, logbf, logbl &#8211; get exponent of a floating-point value </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;math.h&gt;</code> </p>
<p> <code>double logb(double </code><i>x</i><code>);</code><br />
 <code>float logbf(float </code><i>x</i><code>);</code><br />
 <code>long double logbl(long double </code><i>x</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>logb</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>logbf</code>(), <code>logbl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions extract the exponent from the internal floating-point representation of <i>x</i> and return it as a floating-point value. The integer constant <code>FLT_RADIX</code>, defined in <i>&lt;float.h&gt;</i>, indicates the radix used for the system&#8217;s floating-point representation. If <code>FLT_RADIX</code> is 2, <code>logb(</code><i>x</i><code>)</code> is equal to <code>floor(log2(</code><i>x</i><code>))</code>, except that it is probably faster. </p>
<p> If <i>x</i> is subnormal, <code>logb</code>() returns the exponent <i>x</i> would have if it were normalized.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the exponent of <i>x</i>. </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is zero, then a pole error occurs, and the functions return &#8211;<code>HUGE_VAL</code>, &#8211;<code>HUGE_VALF</code>, or &#8211;<code>HUGE_VALL</code>, respectively. </p>
<p> If <i>x</i> is negative infinity or positive infinity, then positive infinity is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Pole error: <i>x</i> is 0</p>
<dd> A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</dl>
<p> These functions do not set <i>errno</i>.</p>
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
<td> <code>logb</code>(), <code>logbf</code>(), <code>logbl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ilogb/">ilogb</a></code>(3), <code><a href="/docs/linux/man/3-log/">log</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
