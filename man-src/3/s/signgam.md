---
title: "signgam(3)"
name: "signgam"
section: "3"
letter: "s"
url: "/docs/linux/man/3-signgam/"
description: "lgamma, lgammaf, lgammal, lgamma_r, lgammaf_r, lgammal_r, signgam – log gamma function"
---

<p>lgamma, lgammaf, lgammal, lgamma_r, lgammaf_r, lgammal_r, signgam &#8211; log gamma function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double lgamma(double x);
float lgammaf(float x);
long double lgammal(long double x);

double lgamma_r(double x, int *signp);
float lgammaf_r(float x, int *signp);
long double lgammal_r(long double x, int *signp);

extern int signgam;</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>lgamma</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L || _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>lgammaf</code>(), <code>lgammal</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>lgamma_r</code>(), <code>lgammaf_r</code>(), <code>lgammal_r</code>():</p>
<dl>
<dd>/* Since glibc 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <i>signgam</i>:</p>
<dl>
<dd>_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>For the definition of the Gamma function, see <code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3). </p>
<p> The <code>lgamma</code>(), <code>lgammaf</code>(), and <code>lgammal</code>() functions return the natural logarithm of the absolute value of the Gamma function. The sign of the Gamma function is returned in the external integer <i>signgam</i> declared in <i>&lt;math.h&gt;</i>. It is 1 when the Gamma function is positive or zero, -1 when it is negative. </p>
<p> Since using a constant location <i>signgam</i> is not thread-safe, the functions <code>lgamma_r</code>(), <code>lgammaf_r</code>(), and <code>lgammal_r</code>() have been introduced; they return the sign via the argument <i>signp</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return the natural logarithm of Gamma(x). </p>
<p> If <i>x</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is 1 or 2, +0 is returned. </p>
<p> If <i>x</i> is positive infinity or negative infinity, positive infinity is returned. </p>
<p> If <i>x</i> is a nonpositive integer, a pole error occurs, and the functions return +<code>HUGE_VAL</code>, +<code>HUGE_VALF</code>, or +<code>HUGE_VALL</code>, respectively. </p>
<p> If the result overflows, a range error occurs, and the functions return <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code>, respectively, with the correct mathematical sign.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Pole error: <i>x</i> is a nonpositive integer</p>
<dd><i>errno</i> is set to <code>ERANGE</code> (but see BUGS). A divide-by-zero floating-point exception (<code>FE_DIVBYZERO</code>) is raised.</p>
<dt>Range error: result overflow</p>
<dd><i>errno</i> is set to <code>ERANGE</code>. An overflow floating-point exception (<code>FE_OVERFLOW</code>) is raised.</dl>
<h2>Conforming To</h2>
<p>The <code>lgamma</code>() functions are specified in C99, POSIX.1-2001, and POSIX.1-2008. <i>signgam</i> is specified in POSIX.1-2001 and POSIX.1-2008, but not in C99. The <code>lgamma_r</code>() functions are nonstandard, but present on several other systems.</p>
<h2>Bugs</h2>
<p>In glibc 2.9 and earlier, when a pole error occurs, <i>errno</i> is set to <code>EDOM</code>; instead of the POSIX-mandated <code>ERANGE</code>. Since version 2.10, glibc does the right thing.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
