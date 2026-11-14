---
title: "strcasecmp(3)"
name: "strcasecmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strcasecmp/"
description: "strcasecmp, strncasecmp – compare two strings ignoring case"
---

<p>strcasecmp, strncasecmp &#8211; compare two strings ignoring case</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;strings.h&gt;

int strcasecmp(const char *s1, const char *s2);

int strncasecmp(const char *s1, const char *s2, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strcasecmp</code>() function performs a byte-by-byte comparison of the strings <i>s1</i> and <i>s2</i>, ignoring the case of the characters. It returns an integer less than, equal to, or greater than zero if <i>s1</i> is found, respectively, to be less than, to match, or be greater than <i>s2</i>. </p>
<p> The <code>strncasecmp</code>() function is similar, except that it compares no more than <i>n</i> bytes of <i>s1</i> and <i>s2</i>.</p>
<h2>Return Value</h2>
<p>The <code>strcasecmp</code>() and <code>strncasecmp</code>() functions return an integer less than, equal to, or greater than zero if <i>s1</i> is, after ignoring case, found to be less than, to match, or be greater than <i>s2</i>, respectively.</p>
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
<td> <code>strcasecmp</code>(), <code>strncasecmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.4BSD, POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The <code>strcasecmp</code>() and <code>strncasecmp</code>() functions first appeared in 4.4BSD, where they were declared in <i>&lt;string.h&gt;</i>. Thus, for reasons of historical compatibility, the glibc <i>&lt;string.h&gt;</i> header file also declares these functions, if the <code>_DEFAULT_SOURCE</code> (or, in glibc 2.19 and earlier, <code>_BSD_SOURCE</code>) feature test macro is defined. </p>
<p> The POSIX.1-2008 standard says of these functions: </p>
<dl>
<dd>When the <code>LC_CTYPE</code> category of the locale being used is from the POSIX locale, these functions shall behave as if the strings had been converted to lowercase and then a byte comparison performed. Otherwise, the results are unspecified.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bcmp/">bcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3), <code><a href="/docs/linux/man/3-wcscasecmp/">wcscasecmp</a></code>(3), <code><a href="/docs/linux/man/3-wcsncasecmp/">wcsncasecmp</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
