---
title: "toascii(3)"
name: "toascii"
section: "3"
letter: "t"
url: "/docs/linux/man/3-toascii/"
description: "toascii – convert character to ASCII"
---

<p>toascii &#8211; convert character to ASCII</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ctype.h&gt;

int toascii(int c);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>toascii</code>(): _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p><code>toascii</code>() converts <i>c</i> to a 7-bit <i>unsigned char</i> value that fits into the ASCII character set, by clearing the high-order bits.</p>
<h2>Return Value</h2>
<p>The value returned is that of the converted character.</p>
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
<td> <code>toascii</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4, BSD, POSIX.1-2001. POSIX.1-2008 marks <code>toascii</code>() as obsolete, noting that it cannot be used portably in a localized application.</p>
<h2>Bugs</h2>
<p>Many people will be unhappy if you use this function. This function will convert accented letters into random characters.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-isascii/">isascii</a></code>(3), <code><a href="/docs/linux/man/3-tolower/">tolower</a></code>(3), <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
