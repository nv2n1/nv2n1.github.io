---
title: "gcvt(3)"
name: "gcvt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gcvt/"
description: "gcvt – convert a floating-point number to a string"
---

<h2 class="name">NAME</h2>
<p> gcvt &#8211; convert a floating-point number to a string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
char *gcvt(double number, int ndigit, char *buf);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>gcvt</code>():</p>
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
<p> The <code>gcvt</code>() function converts <i>number</i> to a minimal length null-terminated ASCII string and stores the result in <i>buf</i>. It produces <i>ndigit</i> significant digits in either <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) F format or E format.</p>
<h2>RETURN VALUE</h2>
<p> The <code>gcvt</code>() function returns <i>buf</i>.</p>
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
<td> <code>gcvt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Marked as LEGACY in POSIX.1-2001. POSIX.1-2008 removes the specification of <code>gcvt</code>(), recommending the use of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) instead (though <code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3) may be preferable).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3), <code><a href="/docs/linux/man/3-fcvt/">fcvt</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
