---
title: "wmempcpy(3)"
name: "wmempcpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wmempcpy/"
description: "mempcpy, wmempcpy – copy memory area"
---

<p>mempcpy, wmempcpy &#8211; copy memory area</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;

void *mempcpy(void *dest, const void *src, size_t n);

#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;wchar.h&gt;

wchar_t *wmempcpy(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>mempcpy</code>() function is nearly identical to the <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3) function. It copies <i>n</i> bytes from the object beginning at <i>src</i> into the object pointed to by <i>dest</i>. But instead of returning the value of <i>dest</i> it returns a pointer to the byte following the last written byte. </p>
<p> This function is useful in situations where a number of objects shall be copied to consecutive memory positions. </p>
<p> The <code>wmempcpy</code>() function is identical but takes <i>wchar_t</i> type arguments and copies <i>n</i> wide characters.</p>
<h2>Return Value</h2>
<p><i>dest</i> + <i>n</i>.</p>
<h2>Versions</h2>
<p><code>mempcpy</code>() first appeared in glibc in version 2.1.</p>
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
<td> <code>mempcpy</code>(), <code>wmempcpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a GNU extension.</p>
<h2>Examples</h2>
<pre><code>void *
combine(void *o1, size_t s1, void *o2, size_t s2)
{
    void *result = malloc(s1 + s2);
    if (result != NULL)
        mempcpy(mempcpy(result, o1, s1), o2, s2);
    return result;
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
