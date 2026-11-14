---
title: "qfcvt(3)"
name: "qfcvt"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qfcvt/"
description: "qecvt, qfcvt, qgcvt – convert a floating-point number to a string"
---

<p>qecvt, qfcvt, qgcvt &#8211; convert a floating-point number to a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;
char *qecvt(long double number, int ndigits, int *decpt,

            int *sign);
char *qfcvt(long double number, int ndigits, int *decpt,

            int *sign);
char *qgcvt(long double number, int ndigit, char *buf);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>qecvt</code>(), <code>qfcvt</code>(), <code>qgcvt</code>(): _SVID_SOURCE</p>
<h2>Description</h2>
<p>The functions <code>qecvt</code>(), <code>qfcvt</code>(), and <code>qgcvt</code>() are identical to <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3), <code><a href="/docs/linux/man/3-fcvt/">fcvt</a></code>(3), and <code><a href="/docs/linux/man/3-gcvt/">gcvt</a></code>(3) respectively, except that they use a <i>long double</i> argument <i>number</i>. See <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3) and <code><a href="/docs/linux/man/3-gcvt/">gcvt</a></code>(3).</p>
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
<td> <code>qecvt</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:qecvt
</td>
</tr>
<tr VALIGN=top>
<td> <code>qfcvt</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:qfcvt
</td>
</tr>
<tr VALIGN=top>
<td> <code>qgcvt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4. Not seen in most common UNIX implementations, but occurs in SunOS. Supported by glibc.</p>
<h2>Notes</h2>
<p>These functions are obsolete. Instead, <code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3) is recommended.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3), <code><a href="/docs/linux/man/3-ecvt_r/">ecvt_r</a></code>(3), <code><a href="/docs/linux/man/3-gcvt/">gcvt</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
