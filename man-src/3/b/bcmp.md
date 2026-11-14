---
title: "bcmp(3)"
name: "bcmp"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bcmp/"
description: "bcmp – compare byte sequences"
---

<h2 class="name">NAME</h2>
<p> bcmp &#8211; compare byte sequences </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
int bcmp(const void *s1, const void *s2, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bcmp</code>() function compares the two byte sequences <i>s1</i> and <i>s2</i> of length <i>n</i> each. If they are equal, and in particular if <i>n</i> is zero, <code>bcmp</code>() returns 0. Otherwise, it returns a nonzero result.</p>
<h2>RETURN VALUE</h2>
<p> The <code>bcmp</code>() function returns 0 if the byte sequences are equal, otherwise a nonzero result is returned.</p>
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
<td> <code>bcmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD. This function is deprecated (marked as LEGACY in POSIX.1-2001): use <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3) in new programs. POSIX.1-2008 removes the specification of <code>bcmp</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
