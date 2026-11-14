---
title: "re_comp(3)"
name: "re_comp"
section: "3"
letter: "r"
url: "/docs/linux/man/3-re_comp/"
description: "re_comp, re_exec – BSD regex functions"
---

<p>re_comp, re_exec &#8211; BSD regex functions</p>
<h2>Synopsis</h2>
<pre><code>#define _REGEX_RE_COMP

#include &lt;sys/types.h&gt;

#include &lt;regex.h&gt;
char *re_comp(const char *regex);
int re_exec(const char *string);</code></pre>
<h2>Description</h2>
<p><code>re_comp</code>() is used to compile the null-terminated regular expression pointed to by <i>regex</i>. The compiled pattern occupies a static area, the pattern buffer, which is overwritten by subsequent use of <code>re_comp</code>(). If <i>regex</i> is NULL, no operation is performed and the pattern buffer&#8217;s contents are not altered. </p>
<p> <code>re_exec</code>() is used to assess whether the null-terminated string pointed to by <i>string</i> matches the previously compiled <i>regex</i>.</p>
<h2>Return Value</h2>
<p><code>re_comp</code>() returns NULL on successful compilation of <i>regex</i> otherwise it returns a pointer to an appropriate error message. </p>
<p> <code>re_exec</code>() returns 1 for a successful match, zero for failure.</p>
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
<td> <code>re_comp</code>(), <code>re_exec</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.3BSD.</p>
<h2>Notes</h2>
<p>These functions are obsolete; the functions documented in <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3) should be used instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), GNU regex manual</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
