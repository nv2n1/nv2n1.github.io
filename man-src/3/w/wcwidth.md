---
title: "wcwidth(3)"
name: "wcwidth"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcwidth/"
description: "wcwidth – determine columns needed for a wide character"
---

<p>wcwidth &#8211; determine columns needed for a wide character</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE /* See feature_test_macros(7) */
#include &lt;wchar.h&gt;
int wcwidth(wchar_t c);</code></pre>
<h2>Description</h2>
<p>The <code>wcwidth</code>() function returns the number of columns needed to represent the wide character <i>c</i>. If <i>c</i> is a printable wide character, the value is at least 0. If <i>c</i> is null wide character (L&#8217;\0&#8217;), the value is 0. Otherwise, -1 is returned.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcwidth</code>() function returns the number of column positions for <i>c</i>.  </p>
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
<td> <code>wcwidth</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> Note that glibc before 2.2.5 used the prototype </p>
<pre><code>
 int wcwidth(wint_t  c  ); 
</code></pre>
<h2>NOTES</h2>
<p> The behavior of <code>wcwidth</code>() depends on the <code>LC_CTYPE</code> category of the current locale.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iswprint/">iswprint</a></code>(3), <code><a href="/docs/linux/man/3-wcswidth/">wcswidth</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
