---
title: "wcpncpy(3)"
name: "wcpncpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcpncpy/"
description: "wcpncpy – copy a fixed-size string of wide characters, returning a pointer to its end"
---

<p>wcpncpy &#8211; copy a fixed-size string of wide characters, returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
wchar_t *wcpncpy(wchar_t *dest, const wchar_t *src, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcpncpy</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>wcpncpy</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3) function. It copies at most <i>n</i> wide characters from the wide-character string pointed to by <i>src</i>, including the terminating null wide (L&#8217;\0&#8217;), to the array pointed to by <i>dest</i>. Exactly <i>n</i> wide characters are written at <i>dest</i>. If the length <i>wcslen(src)</i> is smaller than <i>n</i>, the remaining wide characters in the array pointed to by <i>dest</i> are filled with L&#8217;\0&#8217; characters. If the length <i>wcslen(src)</i> is greater than or equal to <i>n</i>, the string pointed to by <i>dest</i> will not be L&#8217;\0&#8217; terminated. </p>
<p> The strings may not overlap. </p>
<p> The programmer must ensure that there is room for at least <i>n</i> wide characters at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> <code>wcpncpy</code>() returns a pointer to the last wide character written, that is, <i>dest</i>+<i>n</i>-1.  </p>
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
<td> <code>wcpncpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3), <code><a href="/docs/linux/man/3-wcsncpy/">wcsncpy</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
