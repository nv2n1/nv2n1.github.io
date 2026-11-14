---
title: "scalblnl(3)"
name: "scalblnl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scalblnl/"
---

scalbn, scalbnf, scalbnl, scalbln, scalblnf, scalblnl - multiply floating-point number by integral power of radix

<h2>Synopsis</h2>

<pre><code>#include &lt;math.h&gt;
double scalbln(double x, long exp);

float scalblnf(float x, long exp);

long double scalblnl(long double x, long exp);
double scalbn(double x, int exp);

float scalbnf(float x, int exp);

long double scalbnl(long double x, int exp);</code></pre> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <b><a HREF="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></b>(7)): <b>scalbln</b>(), <b>scalblnf</b>(), <b>scalblnl</b>():
<dl><dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE</dl>
 
 <b>scalbn</b>(), <b>scalbnf</b>(), <b>scalbnl</b>():
<dl><dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>

<h2>Description</h2>

These functions multiply their first argument <i>x</i> by <b>FLT_RADIX</b> (probably 2) to the power of <i>exp</i>, that is: 

 <pre> x * FLT_RADIX ** exp</pre>The definition of <b>FLT_RADIX</b> can be obtained by including <i>&lt;float.h&gt;</i>.

<h2>Return Value</h2>

On success, these functions return <i>x</i> * <b>FLT_RADIX</b> ** <i>exp</i>. 

 If <i>x</i> is a NaN, a NaN is returned. 

 If <i>x</i> is positive infinity (negative infinity), positive infinity (negative infinity) is returned. 

 If <i>x</i> is +0 (-0), +0 (-0) is returned. 

 If the result overflows, a range error occurs, and the functions return <b>HUGE_VAL</b>, <b>HUGE_VALF</b>, or <b>HUGE_VALL</b>, respectively, with a sign the same as <i>x</i>. 

 If the result underflows, a range error occurs, and the functions return zero, with a sign the same as <i>x</i>.

<h2>Errors</h2>

See <b><a HREF="/docs/linux/man/7-math_error/">math_error</a></b>(7) for information on how to determine whether an error has occurred when calling these functions. 

 The following errors can occur:
<dl><dt>Range error, overflow
<dd>An overflow floating-point exception (<b>FE_OVERFLOW</b>) is raised.
<dt>Range error, underflow
<dd><i>errno</i> is set to <b>ERANGE</b>. An underflow floating-point exception (<b>FE_UNDERFLOW</b>) is raised.</dl>

<h2>Versions</h2>

These functions first appeared in glibc in version 2.1.

<h2>Attributes</h2>

For an explanation of the terms used in this section, see <b><a HREF="/docs/linux/man/7-attributes/">attributes</a></b>(7). <table BORDER> <tr VALIGN=top><td><b>Interface</b></td><td><b>Attribute</b></td><td><b>Value</b>
</td></tr><tr VALIGN=top><td> <b>scalbn</b>(), <b>scalbnf</b>(), <b>scalbnl</b>(), 
 <b>scalbln</b>(), <b>scalblnf</b>(), <b>scalblnl</b>() </td><td>Thread safety</td><td>MT-Safe
</td></tr> </table>

<h2>Conforming To</h2>

C99, POSIX.1-2001, POSIX.1-2008.

<h2>Notes</h2>

These functions differ from the obsolete functions described in <b><a HREF="/docs/linux/man/3-scalb/">scalb</a></b>(3) in the type of their second argument. The functions described on this page have a second argument of an integral type, while those in <b><a HREF="/docs/linux/man/3-scalb/">scalb</a></b>(3) have a second argument of type <i>double</i>. 

 If <b>FLT_RADIX</b> equals 2 (which is usual), then <b>scalbn</b>() is equivalent to <b><a HREF="/docs/linux/man/3-ldexp/">ldexp</a></b>(3).

<h2>Bugs</h2>

Before glibc 2.20, these functions did not set <i>errno</i> for range errors.

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/3-ldexp/">ldexp</a></b>(3), <b><a HREF="/docs/linux/man/3-scalb/">scalb</a></b>(3)

<h2>Colophon</h2>

This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 
