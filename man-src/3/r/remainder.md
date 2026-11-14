---
title: "remainder(3)"
name: "remainder"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remainder/"
description: "drem, dremf, dreml, remainder, remainderf, remainderl – floating-point remainder function"
---

<p>drem, dremf, dreml, remainder, remainderf, remainderl &#8211; floating-point remainder function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

/* The C99 versions */
double remainder(double x, double y);
float remainderf(float x, float y);
long double remainderl(long double x, long double y);

/* Obsolete synonyms */
double drem(double x, double y);
float dremf(float x, float y);
long double dreml(long double x, long double y);


Link with -lm.</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>remainder</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>remainderf</code>(), <code>remainderl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>drem</code>(), <code>dremf</code>(), <code>dreml</code>():</p>
<dl>
<dd>/* Since glibc 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>These functions compute the remainder of dividing <i>x</i> by <i>y</i>. The return value is <i>x</i>&#8211;<i>n</i>*<i>y</i>, where <i>n</i> is the value <i>x&nbsp;/&nbsp;y</i>, rounded to the nearest integer. If the absolute value of <i>x</i>&#8211;<i>n</i>*<i>y</i> is 0.5, <i>n</i> is chosen to be even. </p>
<p> These functions are unaffected by the current rounding mode (see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)). </p>
<p> The <code>drem</code>() function does precisely the same thing.</p>
<h2>Return Value</h2>
<p>On success, these functions return the floating-point remainder, <i>x</i>&#8211;<i>n</i>*<i>y</i>. If the return value is 0, it has the sign of <i>x</i>. </p>
<p> If <i>x</i> or <i>y</i> is a NaN, a NaN is returned. </p>
<p> If <i>x</i> is an infinity, and <i>y</i> is not a NaN, a domain error occurs, and a NaN is returned. </p>
<p> If <i>y</i> is zero, and <i>x</i> is not a NaN, a domain error occurs, and a NaN is returned.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7) for information on how to determine whether an error has occurred when calling these functions. </p>
<p> The following errors can occur:</p>
<dl>
<dt>Domain error: <i>x</i> is an infinity and <i>y</i> is not a NaN</p>
<dd><i>errno</i> is set to <code>EDOM</code> (but see BUGS). An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</p>
<dd>These functions do not set <i>errno</i> for this case.</p>
<dt>Domain error: <i>y</i> is zero<i>errno</i></p>
<dd>is set to <code>EDOM</code>. An invalid floating-point exception (<code>FE_INVALID</code>) is raised.</dl>
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
<td> <code>drem</code>(), <code>dremf</code>(), <code>dreml</code>(),<br />
 <code>remainder</code>(), <code>remainderf</code>(),<br />
 <code>remainderl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The functions <code>remainder</code>(), <code>remainderf</code>(), and <code>remainderl</code>() are specified in C99, POSIX.1-2001, and POSIX.1-2008. </p>
<p> The function <code>drem</code>() is from 4.3BSD. The <i>float</i> and <i>long double</i> variants <code>dremf</code>() and <code>dreml</code>() exist on some systems, such as Tru64 and glibc2. Avoid the use of these functions in favor of <code>remainder</code>() etc.</p>
<h2>Bugs</h2>
<p>Before glibc 2.15, the call </p>
<pre><code>remainder(nan(&quot;&quot;), 0);</code></pre>
<p> returned a NaN, as expected, but wrongly caused a domain error. Since glibc 2.15, a silent NaN (i.e., no domain error) is returned. Before glibc 2.15, <i>errno</i> was not set to <code>EDOM</code> for the domain error that occurs when <i>x</i> is an infinity and <i>y</i> is not a NaN.</p>
<h2>Examples</h2>
<p>The call &quot;remainder(29.0, 3.0)&quot; returns -1.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-div/">div</a></code>(3), <code><a href="/docs/linux/man/3-fmod/">fmod</a></code>(3), <code><a href="/docs/linux/man/3-remquo/">remquo</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
