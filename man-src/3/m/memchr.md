---
title: "memchr(3)"
name: "memchr"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memchr/"
description: "memchr, memrchr, rawmemchr – scan memory for a character"
---

<h2 class="name">NAME</h2>
<p> memchr, memrchr, rawmemchr &#8211; scan memory for a character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
void *memchr(const void *s, int c, size_t n);
void *memrchr(const void *s, int c, size_t n);
void *rawmemchr(const void *s, int c);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>memrchr</code>(), <code>rawmemchr</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>memchr</code>() function scans the initial <i>n</i> bytes of the memory area pointed to by <i>s</i> for the first instance of <i>c</i>. Both <i>c</i> and the bytes of the memory area pointed to by <i>s</i> are interpreted as <i>unsigned char</i>. </p>
<p> The <code>memrchr</code>() function is like the <code>memchr</code>() function, except that it searches backward from the end of the <i>n</i> bytes pointed to by <i>s</i> instead of forward from the beginning. </p>
<p> The <code>rawmemchr</code>() function is similar to <code>memchr</code>(): it assumes (i.e., the programmer knows for certain) that an instance of <i>c</i> lies somewhere in the memory area starting at the location pointed to by <i>s</i>, and so performs an optimized search for <i>c</i> (i.e., no use of a count argument to limit the range of the search). If an instance of <i>c</i> is not found, the results are unpredictable. The following call is a fast means of locating a string&#8217;s terminating null byte: </p>
<p> char *p = rawmemchr(s,&nbsp;&#8216;\0&#8217;);  </p>
<h2>RETURN VALUE</h2>
<p> The <code>memchr</code>() and <code>memrchr</code>() functions return a pointer to the matching byte or NULL if the character does not occur in the given memory area. </p>
<p> The <code>rawmemchr</code>() function returns a pointer to the matching byte, if one is found. If no matching byte is found, the result is unspecified.  </p>
<h2>VERSIONS</h2>
<p> <code>rawmemchr</code>() first appeared in glibc in version 2.1. </p>
<p> <code>memrchr</code>() first appeared in glibc in version 2.2.  </p>
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
<td> <code>memchr</code>(), <code>memrchr</code>(), <code>rawmemchr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>memchr</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD. </p>
<p> The <code>memrchr</code>() function is a GNU extension, available since glibc 2.1.91. </p>
<p> The <code>rawmemchr</code>() function is a GNU extension, available since glibc 2.1.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-ffs/">ffs</a></code>(3), <code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memmem/">memmem</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-wmemchr/">wmemchr</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
