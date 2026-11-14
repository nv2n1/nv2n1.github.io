---
title: "fcvt(3)"
name: "fcvt"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcvt/"
description: "ecvt, fcvt – convert a floating-point number to a string"
---

<h2 class="name">NAME</h2>
<p> ecvt, fcvt &#8211; convert a floating-point number to a string </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdlib.h&gt;</code> </p>
<p> <code>char *ecvt(double </code><i>number</i><code>, int </code><i>ndigits</i><code>, int *</code><i>decpt</i><code>,</code> <code>int *</code><i>sign</i><code>);</code> </p>
<p> <code>char *fcvt(double </code><i>number</i><code>, int </code><i>ndigits</i><code>, int *</code><i>decpt</i><code>,</code> <code>int *</code><i>sign</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ecvt</code>(), <code>fcvt</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre><code>
(_XOPEN_SOURCE &amp;nbsp; &gt;= &amp;nbsp; 500) !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L) || /* Glibc since 2.19: */ _DEFAULT_SOURCE
    || /* Glibc versions &lt;= 2.19: */ _SVID_SOURCE
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _SVID_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ecvt</code>() function converts <i>number</i> to a null-terminated string of <i>ndigits</i> digits (where <i>ndigits</i> is reduced to a system-specific limit determined by the precision of a <i>double</i>), and returns a pointer to the string. The high-order digit is nonzero, unless <i>number</i> is zero. The low order digit is rounded. The string itself does not contain a decimal point; however, the position of the decimal point relative to the start of the string is stored in <i>*decpt</i>. A negative value for <i>*decpt</i> means that the decimal point is to the left of the start of the string. If the sign of <i>number</i> is negative, <i>*sign</i> is set to a nonzero value, otherwise it is set to 0. If <i>number</i> is zero, it is unspecified whether <i>*decpt</i> is 0 or 1. </p>
<p> The <code>fcvt</code>() function is identical to <code>ecvt</code>(), except that <i>ndigits</i> specifies the number of digits after the decimal point.</p>
<h2>RETURN VALUE</h2>
<p> Both the <code>ecvt</code>() and <code>fcvt</code>() functions return a pointer to a static string containing the ASCII representation of <i>number</i>. The static string is overwritten by each call to <code>ecvt</code>() or <code>fcvt</code>().</p>
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
<td> <code>ecvt</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ecvt
</td>
</tr>
<tr VALIGN=top>
<td> <code>fcvt</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fcvt
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr2; marked as LEGACY in POSIX.1-2001. POSIX.1-2008 removes the specifications of <code>ecvt</code>() and <code>fcvt</code>(), recommending the use of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) instead (though <code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3) may be preferable).</p>
<h2>NOTES</h2>
<p> Not all locales use a point as the radix character (&quot;decimal point&quot;).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ecvt_r/">ecvt_r</a></code>(3), <code><a href="/docs/linux/man/3-gcvt/">gcvt</a></code>(3), <code><a href="/docs/linux/man/3-qecvt/">qecvt</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
