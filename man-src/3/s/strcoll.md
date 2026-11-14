---
title: "strcoll(3)"
name: "strcoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strcoll/"
description: "strcoll – compare two strings using the current locale"
---

<p>strcoll &#8211; compare two strings using the current locale</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

int strcoll(const char *s1, const char *s2);</code></pre>
<h2>Description</h2>
<p>The <code>strcoll</code>() function compares the two strings <i>s1</i> and <i>s2</i>. It returns an integer less than, equal to, or greater than zero if <i>s1</i> is found, respectively, to be less than, to match, or be greater than <i>s2</i>. The comparison is based on strings interpreted as appropriate for the program&#8217;s current locale for category <code>LC_COLLATE</code>. (See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3).)</p>
<h2>Return Value</h2>
<p>The <code>strcoll</code>() function returns an integer less than, equal to, or greater than zero if <i>s1</i> is found, respectively, to be less than, to match, or be greater than <i>s2</i>, when both are interpreted as appropriate for the current locale.</p>
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
<td> <code>strcoll</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>In the <i>POSIX</i> or <i>C</i> locales <code>strcoll</code>() is equivalent to <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bcmp/">bcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
