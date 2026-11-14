---
title: "fmodl(3)"
name: "fmodl"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmodl/"
description: "fmod, fmodf, fmodl – floating-point remainder function"
---

<h2 class="name">NAME</h2>
<p> fmod, fmodf, fmodl &#8211; floating-point remainder function </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double fmod(double x, double y);
float fmodf(float x, float y);
long double fmodl(long double x, long double y);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fmodf</code>(), <code>fmodl</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions compute the floating-point remainder of dividing <i>x</i> by <i>y</i>. The return value is <i>x</i> &#8211; <i>n</i> * <i>y</i>, where <i>n</i> is the quotient of <i>x</i> / <i>y</i>, rounded toward zero to an integer.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the value <i>x</i>&nbsp;&#8211;&nbsp;<i>n</i>*<i>y</i>, for some integer <i>n</i>, such that the returned value has the same sign as <i>x</i> and a magnitude less than the magnitude of <i>y</i>. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is an infinity, a domain error occurs, and a NaN is returned. </p>
<p> If <i>y</i> is zero, a domain error occurs, and a NaN is returned. </p>
<p> If <i>x</i> is +0 (-0), and <i>y</i> is not zero, +0 (-0) is returned.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is an infinity</p>
<dd> <i>errno</i> is set to <code>EDOM</code> (but see BUGS). An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dt>Domain error: <i>y</i> is zero</p>
<dd> <i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
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
<td> <code>fmod</code>(), <code>fmodf</code>(), <code>fmodl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> The variant returning <i>double</i> also conforms to SVr4, 4.3BSD, C89.</p>
<h2>BUGS</h2>
<p> Before version 2.10, the glibc implementation did not set <i>errno</i> to <code>EDOM</code> when a domain error occurred for an infinite <i>x</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remainder/">remainder</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
