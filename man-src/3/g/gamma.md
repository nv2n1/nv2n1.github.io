---
title: "gamma(3)"
name: "gamma"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gamma/"
description: "gamma, gammaf, gammal – (logarithm of the) gamma function"
---

<h2 class="name">NAME</h2>
<p> gamma, gammaf, gammal &#8211; (logarithm of the) gamma function </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;math.h&gt;</code> </p>
<p> <code>double gamma(double </code><i>x</i><code>);</code><br />
 <code>float gammaf(float </code><i>x</i><code>);</code><br />
 <code>long double gammal(long double </code><i>x</i><code>);</code> </p>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>gamma</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<p> <code>gammaf</code>(), <code>gammal</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE &gt;= 600 || (_XOPEN_SOURCE &amp;&amp; _ISOC99_SOURCE)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> These functions are deprecated: instead, use either the <code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3) or the <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3) functions, as appropriate. </p>
<p> For the definition of the Gamma function, see <code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3).</p>
<h3>*BSD version</h3>
<p> The libm in 4.4BSD and some versions of FreeBSD had a <code>gamma</code>() function that computes the Gamma function, as one would expect.</p>
<h3>glibc version</h3>
<p> Glibc has a <code>gamma</code>() function that is equivalent to <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3) and computes the natural logarithm of the Gamma function.</p>
<h2>RETURN VALUE</h2>
<p> See <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3).</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3).</p>
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
<td> <code>gamma</code>(), <code>gammaf</code>(), <code>gammal</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:signgam
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Because of historical variations in behavior across systems, this function is not specified in any recent standard. It was documented in SVID 2.</p>
<h2>NOTES</h2>
<h3>History</h3>
<p> 4.2BSD had a <code>gamma</code>() that computed ln(|Gamma(|<i>x</i>|)|), leaving the sign of Gamma(|<i>x</i>|) in the external integer <i>signgam</i>. In 4.3BSD the name was changed to <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3), and the man page promises </p>
<p> &quot;At some time in the future the name gamma will be rehabilitated and used for the Gamma function&quot; </p>
<p> This did indeed happen in 4.4BSD, where <code>gamma</code>() computes the Gamma function (with no effect on <i>signgam</i>). However, this came too late, and we now have <code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3), the &quot;true gamma&quot; function.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lgamma/">lgamma</a></code>(3), <code><a href="/docs/linux/man/3-signgam/">signgam</a></code>(3), <code><a href="/docs/linux/man/3-tgamma/">tgamma</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
