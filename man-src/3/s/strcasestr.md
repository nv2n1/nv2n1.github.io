---
title: "strcasestr(3)"
name: "strcasestr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strcasestr/"
description: "strstr, strcasestr – locate a substring"
---

<p>strstr, strcasestr &#8211; locate a substring</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strstr(const char *haystack, const char *needle);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;
char *strcasestr(const char *haystack, const char *needle);</code></pre>
<h2>Description</h2>
<p>The <code>strstr</code>() function finds the first occurrence of the substring <i>needle</i> in the string <i>haystack</i>. The terminating null bytes (&#8216;\0&#8217;) are not compared. </p>
<p> The <code>strcasestr</code>() function is like <code>strstr</code>(), but ignores the case of both arguments.  </p>
<h2>RETURN VALUE</h2>
<p> These functions return a pointer to the beginning of the located substring, or NULL if the substring is not found.  </p>
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
<td> <code>strstr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>strcasestr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>strstr</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> The <code>strcasestr</code>() function is a nonstandard extension.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-memmem/">memmem</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), <code><a href="/docs/linux/man/3-wcsstr/">wcsstr</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
