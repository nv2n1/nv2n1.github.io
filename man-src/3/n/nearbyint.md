---
title: "nearbyint(3)"
name: "nearbyint"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nearbyint/"
description: "nearbyint, nearbyintf, nearbyintl, rint, rintf, rintl – round to nearest integer"
---

<p>nearbyint, nearbyintf, nearbyintl, rint, rintf, rintl &#8211; round to nearest integer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;

double nearbyint(double x);
float nearbyintf(float x);
long double nearbyintl(long double x);

double rint(double x);
float rintf(float x);
long double rintl(long double x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>nearbyint</code>(), <code>nearbyintf</code>(), <code>nearbyintl</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L || _ISOC99_SOURCE</dl>
<p> <code>rint</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>rintf</code>(), <code>rintl</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>The <code>nearbyint</code>(), <code>nearbyintf</code>(), and <code>nearbyintl</code>() functions round their argument to an integer value in floating-point format, using the current rounding direction (see <code><a href="/docs/linux/man/3-fesetround/">fesetround</a></code>(3)) and without raising the <i>inexact</i> exception. When the current rounding direction is to nearest, these functions round halfway cases to the even integer in accordance with IEEE-754. </p>
<p> The <code>rint</code>(), <code>rintf</code>(), and <code>rintl</code>() functions do the same, but will raise the <i>inexact</i> exception (<code>FE_INEXACT</code>, checkable via <code><a href="/docs/linux/man/3-fetestexcept/">fetestexcept</a></code>(3)) when the result differs in value from the argument.</p>
<h2>Return Value</h2>
<p>These functions return the rounded integer value. </p>
<p> If <i>x</i> is integral, +0, -0, NaN, or infinite, <i>x</i> itself is returned.</p>
<h2>Errors</h2>
<p>No errors occur. POSIX.1-2001 documents a range error for overflows, but see NOTES.</p>
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
<td> <code>nearbyint</code>(), <code>nearbyintf</code>(),<br />
 <code>nearbyintl</code>(), <code>rint</code>(),<br />
 <code>rintf</code>(), <code>rintl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>SUSv2 and POSIX.1-2001 contain text about overflow (which might set <i>errno</i> to <code>ERANGE</code>, or raise an <code>FE_OVERFLOW</code> exception). In practice, the result cannot overflow on any current machine, so this error-handling stuff is just nonsense. (More precisely, overflow can happen only when the maximum value of the exponent is smaller than the number of mantissa bits. For the IEEE-754 standard 32-bit and 64-bit floating-point numbers the maximum value of the exponent is 128 (respectively, 1024), and the number of mantissa bits is 24 (respectively, 53).) </p>
<p> If you want to store the rounded value in an integer type, you probably want to use one of the functions described in <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ceil/">ceil</a></code>(3), <code><a href="/docs/linux/man/3-floor/">floor</a></code>(3), <code><a href="/docs/linux/man/3-lrint/">lrint</a></code>(3), <code><a href="/docs/linux/man/3-round/">round</a></code>(3), <code><a href="/docs/linux/man/3-trunc/">trunc</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
