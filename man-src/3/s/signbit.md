---
title: "signbit(3)"
name: "signbit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-signbit/"
description: "signbit – test sign of a real floating-point number"
---

<p>signbit &#8211; test sign of a real floating-point number</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;math.h&gt;
int signbit(x);</code></pre>
<p> Link with <i>-lm</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>signbit</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p><code>signbit</code>() is a generic macro which can work on all real floating-point types. It returns a nonzero value if the value of <i>x</i> has its sign bit set. </p>
<p> This is not the same as <i>x &lt; 0.0</i>, because IEEE 754 floating point allows zero to be signed. The comparison <i>-0.0 &lt; 0.0</i> is false, but <i>signbit(-0.0)</i> will return a nonzero value. </p>
<p> NaNs and infinities have a sign bit.</p>
<h2>Return Value</h2>
<p>The <code>signbit</code>() macro returns nonzero if the sign of <i>x</i> is negative; otherwise it returns zero.</p>
<h2>Errors</h2>
<p>No errors occur.</p>
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
<td> <code>signbit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99. This function is defined in IEC 559 (and the appendix with recommended functions in IEEE 754/IEEE 854).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-copysign/">copysign</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
