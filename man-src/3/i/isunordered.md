---
title: "isunordered(3)"
name: "isunordered"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isunordered/"
description: "isgreater, isgreaterequal, isless, islessequal, islessgreater, isunordered – floating-point relational tests without exception for NaN"
---

<h2 class="name">NAME</h2>
<p> isgreater, isgreaterequal, isless, islessequal, islessgreater, isunordered &#8211; floating-point relational tests without exception for NaN </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
int isgreater(x, y);
int isgreaterequal(x, y);
int isless(x, y);
int islessequal(x, y);
int islessgreater(x, y);
int isunordered(x, y);
</code></pre>
<p> Link with <i>-lm</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> All functions described here:</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> The normal relational operations (like <code>&lt;</code>, &quot;less than&quot;) fail if one of the operands is NaN. This will cause an exception. To avoid this, C99 defines the macros listed below. </p>
<p> These macros are guaranteed to evaluate their arguments only once. The arguments must be of real floating-point type (note: do not pass integer values as arguments to these macros, since the arguments will <i>not</i> be promoted to real-floating types).</p>
<dl>
<dt><code>isgreater</code>()</p>
<dd> determines <i>(x)&nbsp;&gt;&nbsp;(y)</i> without an exception if <i>x</i> or <i>y</i> is NaN.</p>
<dt><code>isgreaterequal</code>()</p>
<dd> determines <i>(x)&nbsp;&gt;=&nbsp;(y)</i> without an exception if <i>x</i> or <i>y</i> is NaN.</p>
<dt><code>isless</code>()</p>
<dd> determines <i>(x)&nbsp;&lt;&nbsp;(y)</i> without an exception if <i>x</i> or <i>y</i> is NaN.</p>
<dt><code>islessequal</code>()</p>
<dd> determines <i>(x)&nbsp;&lt;=&nbsp;(y)</i> without an exception if <i>x</i> or <i>y</i> is NaN.</p>
<dt><code>islessgreater</code>()</p>
<dd> determines <i>(x)&nbsp;&lt; (y) || (x) &gt;&nbsp;(y)</i> without an exception if <i>x</i> or <i>y</i> is NaN. This macro is not equivalent to <i>x&nbsp;!=&nbsp;y</i> because that expression is true if <i>x</i> or <i>y</i> is NaN.</p>
<dt><code>isunordered</code>()</p>
<dd> determines whether its arguments are unordered, that is, whether at least one of the arguments is a NaN.</dl>
<h2>RETURN VALUE</h2>
<p> The macros other than <code>isunordered</code>() return the result of the relational comparison; these macros return 0 if either argument is a NaN. </p>
<p> <code>isunordered</code>() returns 1 if <i>x</i> or <i>y</i> is NaN and 0 otherwise.</p>
<h2>ERRORS</h2>
<p> No errors occur.</p>
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
<td> <code>isgreater</code>(), <code>isgreaterequal</code>(), <code>isless</code>(), <code>islessequal</code>(), <code>islessgreater</code>(), <code>isunordered</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> Not all hardware supports these functions, and where hardware support isn&#8217;t provided, they will be emulated by macros. This will result in a performance penalty. Don&#8217;t use these functions if NaN is of no concern for you.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fpclassify/">fpclassify</a></code>(3), <code><a href="/docs/linux/man/3-isnan/">isnan</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
