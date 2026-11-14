---
title: "wcstoimax(3)"
name: "wcstoimax"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcstoimax/"
description: "wcstoimax, wcstoumax – convert wide-character string to integer"
---

<p>wcstoimax, wcstoumax &#8211; convert wide-character string to integer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;inttypes.h&gt;
#include &lt;stddef.h&gt;

intmax_t wcstoimax(const wchar_t *nptr, wchar_t **endptr, int base);
uintmax_t wcstoumax(const wchar_t *nptr, wchar_t **endptr, int base);</code></pre>
<h2>Description</h2>
<p>These functions are just like <code><a href="/docs/linux/man/3-wcstol/">wcstol</a></code>(3) and <code><a href="/docs/linux/man/3-wcstoul/">wcstoul</a></code>(3), except that they return a value of type <i>intmax_t</i> and <i>uintmax_t</i>, respectively.</p>
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
<td> <code>wcstoimax</code>(), <code>wcstoumax</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-imaxabs/">imaxabs</a></code>(3), <code><a href="/docs/linux/man/3-imaxdiv/">imaxdiv</a></code>(3), <code><a href="/docs/linux/man/3-strtoimax/">strtoimax</a></code>(3), <code><a href="/docs/linux/man/3-strtoumax/">strtoumax</a></code>(3), <code><a href="/docs/linux/man/3-wcstol/">wcstol</a></code>(3), <code><a href="/docs/linux/man/3-wcstoul/">wcstoul</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
