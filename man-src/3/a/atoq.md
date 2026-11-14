---
title: "atoq(3)"
name: "atoq"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atoq/"
description: "atoi, atol, atoll – convert a string to an integer"
---

<h2 class="name">NAME</h2>
<p> atoi, atol, atoll &#8211; convert a string to an integer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int atoi(const char *nptr);
long atol(const char *nptr);
long long atoll(const char *nptr);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>atoll</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>atoi</code>() function converts the initial portion of the string pointed to by <i>nptr</i> to <i>int</i>. The behavior is the same as </p>
<p> strtol(nptr, NULL, 10); </p>
<p> except that <code>atoi</code>() does not detect errors. </p>
<p> The <code>atol</code>() and <code>atoll</code>() functions behave the same as <code>atoi</code>(), except that they convert the initial portion of the string to their return type of <i>long</i> or <i>long long</i>.</p>
<h2>RETURN VALUE</h2>
<p> The converted value or 0 on error.</p>
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
<td> <code>atoi</code>(), <code>atol</code>(), <code>atoll</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99, SVr4, 4.3BSD. C89 and POSIX.1-1996 include the functions <code>atoi</code>() and <code>atol</code>() only.</p>
<h2>NOTES</h2>
<p> POSIX.1 leaves the return value of <code>atoi</code>() on error unspecified. On glibc, musl libc, and uClibc, 0 is returned on error.</p>
<h2>BUGS</h2>
<p> <i>errno</i> is not set on error so there is no way to distinguish between 0 as an error and as the converted value. No checks for overflow or underflow are done. Only base-10 input can be converted. It is recommended to instead use the <code>strtol</code>() and <code>strtoul</code>() family of functions in new programs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atof/">atof</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3), <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
