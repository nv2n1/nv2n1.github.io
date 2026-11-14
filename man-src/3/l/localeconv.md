---
title: "localeconv(3)"
name: "localeconv"
section: "3"
letter: "l"
url: "/docs/linux/man/3-localeconv/"
description: "localeconv – get numeric formatting information"
---

<h2 class="name">NAME</h2>
<p> localeconv &#8211; get numeric formatting information </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;locale.h&gt;
struct lconv *localeconv(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>localeconv</code>() function returns a pointer to a <i>struct lconv</i> for the current locale. This structure is shown in <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), and contains all values associated with the locale categories <code>LC_NUMERIC</code> and <code>LC_MONETARY</code>. Programs may also use the functions <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) and <code><a href="/docs/linux/man/3-strfmon/">strfmon</a></code>(3), which behave according to the actual locale in use.</p>
<h2>RETURN VALUE</h2>
<p> The <code>localeconv</code>() function returns a pointer to a filled in <i>struct lconv</i>. This structure may be (in glibc, <i>is</i>) statically allocated, and may be overwritten by subsequent calls. According to POSIX, the caller should not modify the contents of this structure. The <code>localeconv</code>() function always succeeds.</p>
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
<td> <code>localeconv</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:localeconv locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C89, C99.</p>
<h2>BUGS</h2>
<p> The <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions may or may not honor the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/3-isalpha/">isalpha</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
