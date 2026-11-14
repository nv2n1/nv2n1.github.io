---
title: "tgammal(3)"
name: "tgammal"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tgammal/"
description: "tgamma, tgammaf, tgammal – true gamma function"
---

<p>tgamma, tgammaf, tgammal &#8211; true gamma function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
double tgamma(double x);


float tgammaf(float x);


long double tgammal(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>tgamma</code>(), <code>tgammaf</code>(), <code>tgammal</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>These functions calculate the Gamma function of <i>x</i>. </p>
<p> The Gamma function is defined by </p>
<dl>
<dd>Gamma(x) = integral from 0 to infinity of t^(x-1) e^-t dt</dl>
<p> It is defined for every real number except for nonpositive integers. For nonnegative integral <i>m</i> one has </p>
<dl>
<dd>Gamma(m+1) = m!</dl>
<p> and, more generally, for all <i>x</i>: </p>
<dl>
<dd>Gamma(x+1) = x * Gamma(x)</dl>
<p> Furthermore, the following is valid for all values of <i>x</i> outside the poles: </p>
<dl>
<dd>Gamma(x) * Gamma(1 &#8211; x) = PI / sin(PI * x)</dl>
<h2>Return Value</h2>
<p>On success, these functions return Gamma(x). </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is positive infinity, positive infinity is returned. </p>
<p> If <i>x</i> is a negative integer, or is negative infinity, a domain error occurs, and a NaN is returned. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the correct mathematical sign. </p>
<p> If the result underflows, a range error occurs, and the functions return 0, with the correct mathematical sign. </p>
<p> If <i>x</i> is -0 or +0, a pole error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the same sign as the 0.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is a negative integer, or negative infinity</p>
<dd><i>errno</i> is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised (but see BUGS).</p>
<dt>Pole error: <i>x</i> is +0 or -0</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</p>
<dt>Range error: result overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
<p> glibc also gives the following error which is not specified in C99 or POSIX.1-2001.</p>
<dl>
<dt>Range error: result underflow</p>
<dd>An underflow floating-point exception (<code>FE_UNDERFLOW</code>) is raised, and <i>errno</i> is set to <code>ERANGE</code>.</dl>
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
<td> <code>tgamma</code>(), <code>tgammaf</code>(), <code>tgammal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>This function had to be called &quot;true gamma function&quot; since there is already a function <code><a href="/docs/linux/man/3-gamma/">gamma</a></code>(3) that returns something else (see <code><a href="/docs/linux/man/3-gamma/">gamma</a></code>(3) for details).</p>
<h2>Bugs</h2>
<p>Before version 2.18, the glibc implementation of these functions did not set <i>errno</i> to <code>EDOM</code> when <i>x</i> is negative infinity. </p>
<p> Before glibc 2.19, the glibc implementation of these functions did not set <i>errno</i> to <code>ERANGE</code> on an underflow range error. <i>x</i> </p>
<p> In glibc versions 2.3.3 and earlier, an argument of +0 or -0 incorrectly produced a domain error (<i>errno</i> set to <code>EDOM</code> and an <code>FE_INVALID</code> exception raised), rather than a pole error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gamma/">gamma</a></code>(3), <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
