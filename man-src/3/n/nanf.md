---
title: "nanf(3)"
name: "nanf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nanf/"
description: "nan, nanf, nanl – return ‘Not a Number’"
---

<p>nan, nanf, nanl &#8211; return &#8216;Not a Number&#8217; </p>
<h2>Synopsis</h2>
<p><code>#include &lt;math.h&gt;</code> </p>
<p> <code>double nan(const char *</code><i>tagp</i><code>);</code><br />
 <code>float nanf(const char *</code><i>tagp</i><code>);</code><br />
 <code>long double nanl(const char *</code><i>tagp</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>nan</code>(), <code>nanf</code>(), <code>nanl</code>():</p>
<dl COMPACT>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>These functions return a representation (determined by <i>tagp</i>) of a quiet NaN. If the implementation does not support quiet NaNs, these functions return zero. </p>
<p> The call <i>nan(char-sequence)</i> is equivalent to: </p>
<p> strtod(&quot;NAN(char-sequence)&quot;, NULL); </p>
<p> Similarly, calls to <code>nanf</code>() and <code>nanl</code>() are equivalent to analogous calls to <code><a href="/docs/linux/man/3-strtof/">strtof</a></code>(3) and <code><a href="/docs/linux/man/3-strtold/">strtold</a></code>(3). </p>
<p> The argument <i>tagp</i> is used in an unspecified manner. On IEEE 754 systems, there are many representations of NaN, and <i>tagp</i> selects one. On other systems it may do nothing.</p>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>nan</code>(), <code>nanf</code>(), <code>nanl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>C99, POSIX.1-2001, POSIX.1-2008. See also IEC 559 and the appendix with recommended functions in IEEE 754/IEEE 854.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-isnan/">isnan</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3), <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
