---
title: "powf(3)"
name: "powf"
section: "3"
letter: "p"
url: "/docs/linux/man/3-powf/"
description: "pow, powf, powl – power functions"
---

<p>pow, powf, powl &#8211; power functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double pow(double x, double y);
float powf(float x, float y);
long double powl(long double x, long double y);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>powf</code>(), <code>powl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions return the value of <i>x</i> raised to the power of <i>y</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return the value of <i>x</i> to the power of <i>y</i>. </p>
<p> If <i>x</i> is a finite value less than 0, and <i>y</i> is a finite noninteger, a domain error occurs, and a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the mathematically correct sign. </p>
<p> If result underflows, and is not representable, a range error occurs, and 0.0 is returned. </p>
<p> Except as specified below, if <i>x</i> or <i>y</i> is a NaN, the result is a NaN. </p>
<p> If <i>x</i> is +1, the result is 1.0 (even if <i>y</i> is a NaN). </p>
<p> If <i>y</i> is 0, the result is 1.0 (even if <i>x</i> is a NaN). </p>
<p> If <i>x</i> is +0 (-0), and <i>y</i> is an odd integer greater than 0, the result is +0 (-0). </p>
<p> If <i>x</i> is 0, and <i>y</i> greater than 0 and not an odd integer, the result is +0. </p>
<p> If <i>x</i> is -1, and <i>y</i> is positive infinity or negative infinity, the result is 1.0. </p>
<p> If the absolute value of <i>x</i> is less than 1, and <i>y</i> is negative infinity, the result is positive infinity. </p>
<p> If the absolute value of <i>x</i> is greater than 1, and <i>y</i> is negative infinity, the result is +0. </p>
<p> If the absolute value of <i>x</i> is less than 1, and <i>y</i> is positive infinity, the result is +0. </p>
<p> If the absolute value of <i>x</i> is greater than 1, and <i>y</i> is positive infinity, the result is positive infinity. </p>
<p> If <i>x</i> is negative infinity, and <i>y</i> is an odd integer less than 0, the result is -0. </p>
<p> If <i>x</i> is negative infinity, and <i>y</i> less than 0 and not an odd integer, the result is +0. </p>
<p> If <i>x</i> is negative infinity, and <i>y</i> is an odd integer greater than 0, the result is negative infinity. </p>
<p> If <i>x</i> is negative infinity, and <i>y</i> greater than 0 and not an odd integer, the result is positive infinity. </p>
<p> If <i>x</i> is positive infinity, and <i>y</i> less than 0, the result is +0. </p>
<p> If <i>x</i> is positive infinity, and <i>y</i> greater than 0, the result is positive infinity. </p>
<p> If <i>x</i> is +0 or -0, and <i>y</i> is an odd integer less than 0, a pole error occurs and <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, is returned, with the same sign as <i>x</i>. </p>
<p> If <i>x</i> is +0 or -0, and <i>y</i> is less than 0 and not an odd integer, a pole error occurs and +<code>HUGE_VAL</code>, +<code>HUGE_VALF</code>, or +<code>HUGE_VALL</code>, is returned.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is negative, and <i>y</i> is a finite noninteger</p>
<dd><i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Pole error: <i>x</i> is zero, and <i>y</i> is negative</p>
<dd><i>errno</i> is set to <code>ERANGE</code> (but see BUGS). A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</p>
<dt>Range error: the result overflows</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</p>
<dt>Range error: the result underflows</p>
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
<td> <code>pow</code>(), <code>powf</code>(), <code>powl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>Bugs</h2>
<h3>Historical bugs (now fixed)</h3>
<p>Before glibc 2.28, on some architectures (e.g., x86-64) <code>pow</code>() may be more than 10,000 times slower for some inputs than for other nearby inputs. This affects only <code>pow</code>(), and not <code>powf</code>() nor <code>powl</code>(). This problem was fixed in glibc 2.28. </p>
<p> A number of bugs in the glibc implementation of <code>pow</code>() were fixed in glibc version 2.16. </p>
<p> In glibc 2.9 and earlier, when a pole error occurs, <i>errno</i> is set to <code>EDOM</code> instead of the POSIX-mandated <code>ERANGE</code>. Since version 2.10, glibc does the right thing. </p>
<p> In version 2.3.2 and earlier, when an overflow or underflow error occurs, glibc&#8217;s <code>pow</code>() generates a bogus invalid floating-point exception (<code>FE_INVALID</code>) in addition to the overflow or underflow exception.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cbrt/">cbrt</a></code>(3), <code><a href="/docs/linux/man/3-cpow/">cpow</a></code>(3), <code><a href="/docs/linux/man/3-sqrt/">sqrt</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
