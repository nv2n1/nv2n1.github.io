---
title: "strchr(3)"
name: "strchr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strchr/"
description: "strchr, strrchr, strchrnul – locate character in string"
---

<p>strchr, strrchr, strchrnul &#8211; locate character in string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strchr(const char *s, int c);
char *strrchr(const char *s, int c);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;
char *strchrnul(const char *s, int c);</code></pre>
<h2>Description</h2>
<p>The <code>strchr</code>() function returns a pointer to the first occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>strrchr</code>() function returns a pointer to the last occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>strchrnul</code>() function is like <code>strchr</code>() except that if <i>c</i> is not found in <i>s</i>, then it returns a pointer to the null byte at the end of <i>s</i>, rather than NULL. </p>
<p> Here &quot;character&quot; means &quot;byte&quot;; these functions do not work with wide or multibyte characters.</p>
<h2>Return Value</h2>
<p>The <code>strchr</code>() and <code>strrchr</code>() functions return a pointer to the matched character or NULL if the character is not found. The terminating null byte is considered part of the string, so that if <i>c</i> is specified as &#8216;\0&#8217;, these functions return a pointer to the terminator. </p>
<p> The <code>strchrnul</code>() function returns a pointer to the matched character, or a pointer to the null byte at the end of <i>s</i> (i.e., <i>s+strlen(s)</i>) if the character is not found.  </p>
<h2>VERSIONS</h2>
<p> <code>strchrnul</code>() first appeared in glibc in version 2.1.1.  </p>
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
<td> <code>strchr</code>(), <code>strrchr</code>(), <code>strchrnul</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>strchr</code>(), <code>strrchr</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD. </p>
<p> <code>strchrnul</code>() is a GNU extension.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), <code><a href="/docs/linux/man/3-wcschr/">wcschr</a></code>(3), <code><a href="/docs/linux/man/3-wcsrchr/">wcsrchr</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
