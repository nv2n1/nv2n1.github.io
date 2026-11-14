---
title: "ecvt_r(3)"
name: "ecvt_r"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecvt_r/"
description: "ecvt_r, fcvt_r, qecvt_r, qfcvt_r – convert a floating-point number to a string"
---

<h2 class="name">NAME</h2>
<p> ecvt_r, fcvt_r, qecvt_r, qfcvt_r &#8211; convert a floating-point number to a string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int ecvt_r(double number, int ndigits, int *decpt,
           int *sign, char *buf, size_t len);
int fcvt_r(double number, int ndigits, int *decpt,
           int *sign, char *buf, size_t len);
int qecvt_r(long double number, int ndigits, int *decpt,
            int *sign, char *buf, size_t len);
int qfcvt_r(long double number, int ndigits, int *decpt,
            int *sign, char *buf, size_t len);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ecvt_r</code>(), <code>fcvt_r</code>(), <code>qecvt_r</code>(), <code>qfcvt_r</code>():</p>
<dl>
<dt>
<dd> /* Glibc since 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The functions <code>ecvt_r</code>(), <code>fcvt_r</code>(), <code>qecvt_r</code>(), and <code>qfcvt_r</code>() are identical to <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3), <code><a href="/docs/linux/man/3-fcvt/">fcvt</a></code>(3), <code><a href="/docs/linux/man/3-qecvt/">qecvt</a></code>(3), and <code><a href="/docs/linux/man/3-qfcvt/">qfcvt</a></code>(3), respectively, except that they do not return their result in a static buffer, but instead use the supplied <i>buf</i> of size <i>len</i>. See <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3) and <code><a href="/docs/linux/man/3-qecvt/">qecvt</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> These functions return 0 on success, and -1 otherwise.</p>
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
<td> <code>ecvt_r</code>(), <code>fcvt_r</code>(),<br />
 <code>qecvt_r</code>(), <code>qfcvt_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> These functions are obsolete. Instead, <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) is recommended.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ecvt/">ecvt</a></code>(3), <code><a href="/docs/linux/man/3-qecvt/">qecvt</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
