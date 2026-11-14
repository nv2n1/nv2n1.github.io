---
title: "ilogbf(3)"
name: "ilogbf"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilogbf/"
description: "ilogb, ilogbf, ilogbl – get integer exponent of a floating-point value"
---

<h2 class="name">NAME</h2>
<p> ilogb, ilogbf, ilogbl &#8211; get integer exponent of a floating-point value </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;math.h&gt;</code> </p>
<p> <code>int ilogb(double </code><i>x</i><code>);</code><br />
 <code>int ilogbf(float </code><i>x</i><code>);</code><br />
 <code>int ilogbl(long double </code><i>x</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ilogb</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>ilogbf</code>(), <code>ilogbl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions return the exponent part of their argument as a signed integer. When no error occurs, these functions are equivalent to the corresponding <code><a href="/docs/linux/man/3-logb/">logb</a></code>(3) functions, cast to <i>int</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the exponent of <i>x</i>, as a signed integer. </p>
<p> If <i>x</i> is zero, then a domain error occurs, and the functions return <code>FP_ILOGB0</code>. </p>
<p> If <i>x</i> is a NaN, then a domain error occurs, and the functions return <code>FP_ILOGBNAN</code>. </p>
<p> If <i>x</i> is negative infinity or positive infinity, then a domain error occurs, and the functions return <code>INT_MAX</code>.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is 0 or a NaN</p>
<dd> An invalid floating-point exception (<code>FE_INVALID</code>) is raised, and <i>errno</i> is set to <code>EDOM</code> (but see BUGS).</p>
<dt>Domain error: <i>x</i> is an infinity</p>
<dd> An invalid floating-point exception (<code>FE_INVALID</code>) is raised, and <i>errno</i> is set to <code>EDOM</code> (but see BUGS).</dl>
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
<td> <code>ilogb</code>(), <code>ilogbf</code>(), <code>ilogbl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>BUGS</h2>
<p> Before version 2.16, the following bugs existed in the glibc implementation of these functions:</p>
<dl>
<dt>*</p>
<dd> The domain error case where <i>x</i> is 0 or a NaN did not cause <i>errno</i> to be set or (on some architectures) raise a floating-point exception.</p>
<dt>*</p>
<dd> The domain error case where <i>x</i> is an infinity did not cause <i>errno</i> to be set or raise a floating-point exception.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-log/">log</a></code>(3), <code><a href="/docs/linux/man/3-logb/">logb</a></code>(3), <code><a href="/docs/linux/man/3-significand/">significand</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
