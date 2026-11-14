---
title: "memmem(3)"
name: "memmem"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memmem/"
description: "memmem – locate a substring"
---

<h2 class="name">NAME</h2>
<p> memmem &#8211; locate a substring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;
void *memmem(const void *haystack, size_t haystacklen,
             const void *needle, size_t needlelen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memmem</code>() function finds the start of the first occurrence of the substring <i>needle</i> of length <i>needlelen</i> in the memory area <i>haystack</i> of length <i>haystacklen</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memmem</code>() function returns a pointer to the beginning of the substring, or NULL if the substring is not found.</p>
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
<td> <code>memmem</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is not specified in POSIX.1, but is present on a number of other systems.</p>
<h2>BUGS</h2>
<p> In glibc 2.0, if <i>needle</i> is empty, <code>memmem</code>() returns a pointer to the last byte of <i>haystack</i>. This is fixed in glibc 2.1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
