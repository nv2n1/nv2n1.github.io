---
title: "stpncpy(3)"
name: "stpncpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stpncpy/"
description: "stpncpy – copy a fixed-size string, returning a pointer to its end"
---

<p>stpncpy &#8211; copy a fixed-size string, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *stpncpy(char *dest, const char *src, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>stpncpy</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>stpncpy</code>() function copies at most <i>n</i> characters from the string pointed to by <i>src</i>, including the terminating null byte (&#8216;\0&#8217;), to the array pointed to by <i>dest</i>. Exactly <i>n</i> characters are written at <i>dest</i>. If the length <i>strlen(src)</i> is smaller than <i>n</i>, the remaining characters in the array pointed to by <i>dest</i> are filled with null bytes (&#8216;\0&#8217;), If the length <i>strlen(src)</i> is greater than or equal to <i>n</i>, the string pointed to by <i>dest</i> will not be null-terminated. </p>
<p> The strings may not overlap. </p>
<p> The programmer must ensure that there is room for at least <i>n</i> characters at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> <code>stpncpy</code>() returns a pointer to the terminating null byte in <i>dest</i>, or, if <i>dest</i> is not null-terminated, <i>dest</i>+<i>n</i>.  </p>
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
<td> <code>stpncpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function was added to POSIX.1-2008. Before that, it was a GNU extension. It first appeared in version 1.07 of the GNU C library in 1993.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-wcpncpy/">wcpncpy</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
