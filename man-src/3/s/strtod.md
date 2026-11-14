---
title: "strtod(3)"
name: "strtod"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtod/"
description: "strtod, strtof, strtold – convert ASCII string to floating-point number"
---

<p>strtod, strtof, strtold &#8211; convert ASCII string to floating-point number</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;
double strtod(const char *nptr, char **endptr);

float strtof(const char *nptr, char **endptr);

long double strtold(const char *nptr, char **endptr);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strtof</code>(), <code>strtold</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>strtod</code>(), <code>strtof</code>(), and <code>strtold</code>() functions convert the initial portion of the string pointed to by <i>nptr</i> to <i>double</i>, <i>float</i>, and <i>long double</i> representation, respectively. </p>
<p> The expected form of the (initial portion of the) string is optional leading white space as recognized by <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3), an optional plus (&#8216;+&#8217;) or minus sign (&#8216;-&#8216;) and then either (i) a decimal number, or (ii) a hexadecimal number, or (iii) an infinity, or (iv) a NAN (not-a-number). </p>
<p> A <i>decimal number</i> consists of a nonempty sequence of decimal digits possibly containing a radix character (decimal point, locale-dependent, usually &#8216;.&#8217;), optionally followed by a decimal exponent. A decimal exponent consists of an &#8216;E&#8217; or &#8216;e&#8217;, followed by an optional plus or minus sign, followed by a nonempty sequence of decimal digits, and indicates multiplication by a power of 10. </p>
<p> A <i>hexadecimal number</i> consists of a &quot;0x&quot; or &quot;0X&quot; followed by a nonempty sequence of hexadecimal digits possibly containing a radix character, optionally followed by a binary exponent. A binary exponent consists of a &#8216;P&#8217; or &#8216;p&#8217;, followed by an optional plus or minus sign, followed by a nonempty sequence of decimal digits, and indicates multiplication by a power of 2. At least one of radix character and binary exponent must be present. </p>
<p> An <i>infinity</i> is either &quot;INF&quot; or &quot;INFINITY&quot;, disregarding case. </p>
<p> A <i>NAN</i> is &quot;NAN&quot; (disregarding case) optionally followed by a string, <i>(n-char-sequence)</i>, where <i>n-char-sequence</i> specifies in an implementation-dependent way the type of NAN (see NOTES).</p>
<h2>Return Value</h2>
<p>These functions return the converted value, if any. </p>
<p> If <i>endptr</i> is not NULL, a pointer to the character after the last character used in the conversion is stored in the location referenced by <i>endptr</i>. </p>
<p> If no conversion is performed, zero is returned and (unless <i>endptr</i> is null) the value of <i>nptr</i> is stored in the location referenced by <i>endptr</i>. </p>
<p> If the correct value would cause overflow, plus or minus <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, or <code>HUGE_VALL</code> is returned (according to the return type and sign of the value), and <code>ERANGE</code> is stored in <i>errno</i>. </p>
<p> If the correct value would cause underflow, a value with magnitude no larger than <code>DBL_MIN</code>, <code>FLT_MIN</code>, or <code>LDBL_MIN</code> is returned and <code>ERANGE</code> is stored in <i>errno</i>.</p>
<h2>Errors</h2>
<dl>
<dt><code>ERANGE</code></p>
<dd>Overflow or underflow occurred.</dl>
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
<td> <code>strtod</code>(), <code>strtof</code>(), <code>strtold</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99. </p>
<p> <code>strtod</code>() was also described in C89.</p>
<h2>Notes</h2>
<p>Since 0 can legitimately be returned on both success and failure, the calling program should set <i>errno</i> to 0 before the call, and then determine if an error occurred by checking whether <i>errno</i> has a nonzero value after the call. </p>
<p> In the glibc implementation, the <i>n-char-sequence</i> that optionally follows &quot;NAN&quot; is interpreted as an integer number (with an optional &#8216;0&#8217; or &#8216;0x&#8217; prefix to select base 8 or 16) that is to be placed in the mantissa component of the returned value.</p>
<h2>Examples</h2>
<p>See the example on the <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3) manual page; the use of the functions described in this manual page is similar.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-atof/">atof</a></code>(3), <code><a href="/docs/linux/man/3-atoi/">atoi</a></code>(3), <code><a href="/docs/linux/man/3-atol/">atol</a></code>(3), <code><a href="/docs/linux/man/3-nan/">nan</a></code>(3), <code><a href="/docs/linux/man/3-nanf/">nanf</a></code>(3), <code><a href="/docs/linux/man/3-nanl/">nanl</a></code>(3), <code><a href="/docs/linux/man/3-strfromd/">strfromd</a></code>(3), <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
