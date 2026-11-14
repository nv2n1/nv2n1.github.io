---
title: "isfinite(3)"
name: "isfinite"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isfinite/"
description: "fpclassify, isfinite, isnormal, isnan, isinf – floating-point classification macros"
---

<h2 class="name">NAME</h2>
<p> fpclassify, isfinite, isnormal, isnan, isinf &#8211; floating-point classification macros </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
int fpclassify(x);
int isfinite(x);
int isnormal(x);
int isnan(x);
int isinf(x);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fpclassify</code>(), <code>isfinite</code>(), <code>isnormal</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<p> <code>isnan</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>isinf</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> Floating point numbers can have special values, such as infinite or NaN. With the macro <code>fpclassify(</code><i>x</i><code>)</code> you can find out what type <i>x</i> is. The macro takes any floating-point expression as argument. The result is one of the following values:</p>
<dl>
<dt><code>FP_NAN</code></p>
<dd> <i>x</i> is &quot;Not a Number&quot;.</p>
<dt><code>FP_INFINITE</code></p>
<dd> <i>x</i> is either positive infinity or negative infinity.</p>
<dt><code>FP_ZERO</code></p>
<dd> <i>x</i> is zero.</p>
<dt><code>FP_SUBNORMAL</code></p>
<dd> <i>x</i> is too small to be represented in normalized format.</p>
<dt><code>FP_NORMAL</code></p>
<dd> if nothing of the above is correct then it must be a normal floating-point number.</dl>
<p> The other macros provide a short answer to some standard questions.</p>
<dl>
<dt><code>isfinite(</code><i>x</i><code>)</code></p>
<dd> returns a nonzero value if<br />
 (fpclassify(x) != FP_NAN &amp;&amp; fpclassify(x) != FP_INFINITE)</p>
<dt><code>isnormal(</code><i>x</i><code>)</code></p>
<dd> returns a nonzero value if (fpclassify(x) == FP_NORMAL)</p>
<dt><code>isnan(</code><i>x</i><code>)</code></p>
<dd> returns a nonzero value if (fpclassify(x) == FP_NAN)</p>
<dt><code>isinf(</code><i>x</i><code>)</code></p>
<dd> returns 1 if <i>x</i> is positive infinity, and -1 if <i>x</i> is negative infinity.</dl>
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
<td> <code>fpclassify</code>(), <code>isfinite</code>(), <code>isnormal</code>(), <code>isnan</code>(), <code>isinf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99. </p>
<p> For <code>isinf</code>(), the standards merely say that the return value is nonzero if and only if the argument has an infinite value.</p>
<h2>NOTES</h2>
<p> In glibc 2.01 and earlier, <code>isinf</code>() returns a nonzero value (actually: 1) if <i>x</i> is positive infinity or negative infinity. (This is all that C99 requires.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-finite/">finite</a></code>(3), <code><a href="/docs/linux/man/3-infinity/">INFINITY</a></code>(3), <code><a href="/docs/linux/man/3-isgreater/">isgreater</a></code>(3), <code><a href="/docs/linux/man/3-signbit/">signbit</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
