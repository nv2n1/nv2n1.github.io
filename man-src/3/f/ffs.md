---
title: "ffs(3)"
name: "ffs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffs/"
description: "ffs, ffsl, ffsll – find first bit set in a word"
---

<h2 class="name">NAME</h2>
<p> ffs, ffsl, ffsll &#8211; find first bit set in a word </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;strings.h&gt;
int ffs(int i);
#include &lt;string.h&gt;
int ffsl(long i);
int ffsll(long long i);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ffs</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;700<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;!&nbsp;(_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<dt>Before glibc 2.12:</p>
<dd> none</dl>
</dl>
<p> <code>ffsl</code>(), <code>ffsll</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.27:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE</p>
<dt>Before glibc 2.27:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ffs</code>() function returns the position of the first (least significant) bit set in the word <i>i</i>. The least significant bit is position 1 and the most significant position is, for example, 32 or 64. The functions <code>ffsll</code>() and <code>ffsl</code>() do the same but take arguments of possibly different size.</p>
<h2>RETURN VALUE</h2>
<p> These functions return the position of the first bit set, or 0 if no bits are set in <i>i</i>.</p>
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
<td> <code>ffs</code>(), <code>ffsl</code>(), <code>ffsll</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>ffs</code>(): POSIX.1-2001, POSIX.1-2008, 4.3BSD. </p>
<p> The <code>ffsl</code>() and <code>ffsll</code>() functions are glibc extensions.</p>
<h2>NOTES</h2>
<p> BSD systems have a prototype in <i>&lt;string.h&gt;</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
