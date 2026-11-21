---
title: "strnlen(3)"
name: "strnlen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strnlen/"
description: "strnlen – determine the length of a fixed-size string"
---

<p>strnlen &#8211; determine the length of a fixed-size string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
size_t strnlen(const char *s, size_t maxlen);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strnlen</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>strnlen</code>() function returns the number of bytes in the string pointed to by <i>s</i>, excluding the terminating null byte (&#8216;\0&#8217;), but at most <i>maxlen</i>. In doing this, <code>strnlen</code>() looks only at the first <i>maxlen</i> characters in the string pointed to by <i>s</i> and never beyond <i>s[maxlen-1]</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strnlen</code>() function returns <i>strlen(s)</i>, if that is less than <i>maxlen</i>, or <i>maxlen</i> if there is no null terminating (&#8216;\0&#8217;) among the first <i>maxlen</i> characters pointed to by <i>s</i>.  </p>
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
<td> <code>strnlen</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
