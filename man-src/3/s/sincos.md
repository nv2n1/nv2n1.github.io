---
title: "sincos(3)"
name: "sincos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sincos/"
description: "sincos, sincosf, sincosl – calculate sin and cos simultaneously"
---

<p>sincos, sincosf, sincosl &#8211; calculate sin and cos simultaneously</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;math.h&gt;

void sincos(double x, double *sin, double *cos);
void sincosf(float x, float *sin, float *cos);
void sincosl(long double x, long double *sin, long double *cos);</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>Description</h2>
<p>Several applications need sine and cosine of the same angle <i>x</i>. These functions compute both at the same time, and store the results in <i>*sin</i> and <i>*cos</i>. Using this function can be more efficient than two separate calls to <code><a href="/docs/linux/man/3-sin/">sin</a></code>(3) and <code><a href="/docs/linux/man/3-cos/">cos</a></code>(3). </p>
<p> If <i>x</i> is a NaN, a NaN is returned in <i>*sin</i> and <i>*cos</i>. </p>
<p> If <i>x</i> is positive infinity or negative infinity, a domain error occurs, and a NaN is returned in <i>*sin</i> and <i>*cos</i>.</p>
<h2>Return Value</h2>
<p>These functions return <i>void</i>.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is an infinity</p>
<dd><i>errno</i> is set to <code>EDOM</code> (but see BUGS). An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>sincos</code>(), <code>sincosf</code>(), <code>sincosl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are GNU extensions.</p>
<h2>Notes</h2>
<p>To see the performance advantage of <code>sincos</code>(), it may be necessary to disable <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) built-in optimizations, using flags such as: </p>
<p> cc -O -lm -fno-builtin prog.c</p>
<h2>Bugs</h2>
<p>Before version 2.22, the glibc implementation did not set <i>errno</i> to <code>EDOM</code> when a domain error occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cos/">cos</a></code>(3), <code><a href="/docs/linux/man/3-sin/">sin</a></code>(3), <code><a href="/docs/linux/man/3-tan/">tan</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
