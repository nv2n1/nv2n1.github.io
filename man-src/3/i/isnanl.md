---
title: "isnanl(3)"
name: "isnanl"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isnanl/"
description: "finite, finitef, finitel, isinf, isinff, isinfl, isnan, isnanf, isnanl – BSD floating-point classification functions"
---

<h2 class="name">NAME</h2>
<p> finite, finitef, finitel, isinf, isinff, isinfl, isnan, isnanf, isnanl &#8211; BSD floating-point classification functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
int finite(double x);
int finitef(float x);
int finitel(long double x);
int isinf(double x);
int isinff(float x);
int isinfl(long double x);
int isnan(double x);
int isnanf(float x);
int isnanl(long double x);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>finite</code>(), <code>finitef</code>(), <code>finitel</code>():</p>
<dl>
<dt>
<dd> /* Glibc since 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>isinf</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;600 || _ISOC99_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>isinff</code>(), <code>isinfl</code>():</p>
<dl>
<dt>
<dd> /* Glibc since 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>isnan</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE || _ISOC99_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>isnanf</code>(), <code>isnanl</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;600<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>finite</code>(), <code>finitef</code>(), and <code>finitel</code>() functions return a nonzero value if <i>x</i> is neither infinite nor a &quot;not-a-number&quot; (NaN) value, and 0 otherwise. </p>
<p> The <code>isnan</code>(), <code>isnanf</code>(), and <code>isnanl</code>() functions return a nonzero value if <i>x</i> is a NaN value, and 0 otherwise. </p>
<p> The <code>isinf</code>(), <code>isinff</code>(), and <code>isinfl</code>() functions return 1 if <i>x</i> is positive infinity, -1 if <i>x</i> is negative infinity, and 0 otherwise.</p>
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
<td> <code>finite</code>(), <code>finitef</code>(), <code>finitel</code>(),<br />
 <code>isinf</code>(), <code>isinff</code>(), <code>isinfl</code>(),<br />
 <code>isnan</code>(), <code>isnanf</code>(), <code>isnanl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>NOTES</h2>
<p> Note that these functions are obsolete. C99 defines macros <code>isfinite</code>(), <code>isinf</code>(), and <code>isnan</code>() (for all types) replacing them. Further note that the C99 <code>isinf</code>() has weaker guarantees on the return value. See <code><a href="/docs/linux/man/3-fpclassify/">fpclassify</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fpclassify/">fpclassify</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
