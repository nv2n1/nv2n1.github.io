---
title: "getw(3)"
name: "getw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getw/"
description: "getw, putw – input and output of words (ints)"
---

<h2 class="name">NAME</h2>
<p> getw, putw &#8211; input and output of words (ints) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
int getw(FILE *stream);
int putw(int w, FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getw</code>(), <code>putw</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.3.3:</p>
<dd> _XOPEN_SOURCE &amp;&amp; ! (_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<dt>Before glibc 2.3.3:</p>
<dd> _SVID_SOURCE || _BSD_SOURCE || _XOPEN_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>getw</code>() reads a word (that is, an <i>int</i>) from <i>stream</i>. It&#8217;s provided for compatibility with SVr4. We recommend you use <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3) instead. </p>
<p> <code>putw</code>() writes the word <i>w</i> (that is, an <i>int</i>) to <i>stream</i>. It is provided for compatibility with SVr4, but we recommend you use <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3) instead.</p>
<h2>RETURN VALUE</h2>
<p> Normally, <code>getw</code>() returns the word read, and <code>putw</code>() returns 0. On error, they return <code>EOF</code>.</p>
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
<td> <code>getw</code>(), <code>putw</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4, SUSv2. Not present in POSIX.1.</p>
<h2>BUGS</h2>
<p> The value returned on error is also a legitimate data value. <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3) can be used to distinguish between the two cases.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3), <code><a href="/docs/linux/man/3-getc/">getc</a></code>(3), <code><a href="/docs/linux/man/3-putc/">putc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
