---
title: "wcsncasecmp(3)"
name: "wcsncasecmp"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsncasecmp/"
description: "wcsncasecmp – compare two fixed-size wide-character strings, ignoring case"
---

<p>wcsncasecmp &#8211; compare two fixed-size wide-character strings, ignoring case</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;

int wcsncasecmp(const wchar_t *s1, const wchar_t *s2, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcsncasecmp</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>wcsncasecmp</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3) function. It compares the wide-character string pointed to by <i>s1</i> and the wide-character string pointed to by <i>s2</i>, but at most <i>n</i> wide characters from each string, ignoring case differences (<code><a href="/docs/linux/man/3-towupper/">towupper</a></code>(3), <code><a href="/docs/linux/man/3-towlower/">towlower</a></code>(3)).</p>
<h2>Return Value</h2>
<p>The <code>wcsncasecmp</code>() function returns zero if the wide-character strings at <i>s1</i> and <i>s2</i>, truncated to at most length <i>n</i>, are equal except for case distinctions. It returns a positive integer if truncated <i>s1</i> is greater than truncated <i>s2</i>, ignoring case. It returns a negative integer if truncated <i>s1</i> is smaller than truncated <i>s2</i>, ignoring case.</p>
<h2>Versions</h2>
<p>The <code>wcsncasecmp</code>() function is provided in glibc since version 2.1.</p>
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
<td> <code>wcsncasecmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2008. This function is not specified in POSIX.1-2001, and is not widely available on other systems.</p>
<h2>Notes</h2>
<p>The behavior of <code>wcsncasecmp</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3), <code><a href="/docs/linux/man/3-wcsncmp/">wcsncmp</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
