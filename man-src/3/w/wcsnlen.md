---
title: "wcsnlen(3)"
name: "wcsnlen"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsnlen/"
description: "wcsnlen – determine the length of a fixed-size wide-character string"
---

<p>wcsnlen &#8211; determine the length of a fixed-size wide-character string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
size_t wcsnlen(const wchar_t *s, size_t maxlen);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>wcsnlen</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>wcsnlen</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-strnlen/">strnlen</a></code>(3) function. It returns the number of wide-characters in the string pointed to by <i>s</i>, not including the terminating null wide character (L&#8217;\0&#8217;), but at most <i>maxlen</i> wide characters (note: this parameter is not a byte count). In doing this, <code>wcsnlen</code>() looks at only the first <i>maxlen</i> wide characters at <i>s</i> and never beyond <i>s+maxlen</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcsnlen</code>() function returns <i>wcslen(s)</i>, if that is less than <i>maxlen</i>, or <i>maxlen</i> if there is no null wide character among the first <i>maxlen</i> wide characters pointed to by <i>s</i>.  </p>
<h2>VERSIONS</h2>
<p> The <code>wcsnlen</code>() function is provided in glibc since version 2.1.  </p>
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
<td> <code>wcsnlen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strnlen/">strnlen</a></code>(3), <code><a href="/docs/linux/man/3-wcslen/">wcslen</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
