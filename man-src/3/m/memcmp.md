---
title: "memcmp(3)"
name: "memcmp"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcmp/"
description: "memcmp – compare memory areas"
---

<h2 class="name">NAME</h2>
<p> memcmp &#8211; compare memory areas </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
int memcmp(const void *s1, const void *s2, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memcmp</code>() function compares the first <i>n</i> bytes (each interpreted as <i>unsigned char</i>) of the memory areas <i>s1</i> and <i>s2</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memcmp</code>() function returns an integer less than, equal to, or greater than zero if the first <i>n</i> bytes of <i>s1</i> is found, respectively, to be less than, to match, or be greater than the first <i>n</i> bytes of <i>s2</i>. </p>
<p> For a nonzero return value, the sign is determined by the sign of the difference between the first pair of bytes (interpreted as <i>unsigned char</i>) that differ in <i>s1</i> and <i>s2</i>. </p>
<p> If <i>n</i> is zero, the return value is zero.</p>
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
<td> <code>memcmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Do not use <code>memcmp</code>() to compare security critical data, such as cryptographic secrets, because the required CPU time depends on the number of equal bytes. Instead, a function that performs comparisons in constant time is required. Some operating systems provide such a function (e.g., NetBSD&#8217;s <code>consttime_memequal</code>()), but no such function is specified in POSIX. On Linux, it may be necessary to implement such a function oneself.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcmp/">bcmp</a></code>(3), <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3), <code><a href="/docs/linux/man/3-wmemcmp/">wmemcmp</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
