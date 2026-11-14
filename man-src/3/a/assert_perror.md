---
title: "assert_perror(3)"
name: "assert_perror"
section: "3"
letter: "a"
url: "/docs/linux/man/3-assert_perror/"
description: "assert_perror – test errnum and abort"
---

<h2 class="name">NAME</h2>
<p> assert_perror &#8211; test errnum and abort </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;assert.h&gt;
void assert_perror(int errnum);
</code></pre>
<h2>DESCRIPTION</h2>
<p> If the macro <code>NDEBUG</code> was defined at the moment <i>&lt;assert.h&gt;</i> was last included, the macro <code>assert_perror</code>() generates no code, and hence does nothing at all. Otherwise, the macro <code>assert_perror</code>() prints an error message to standard error and terminates the program by calling <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3) if <i>errnum</i> is nonzero. The message contains the filename, function name and line number of the macro call, and the output of <i>strerror(errnum)</i>.</p>
<h2>RETURN VALUE</h2>
<p> No value is returned.</p>
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
<td> <code>assert_perror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This is a GNU extension.</p>
<h2>BUGS</h2>
<p> The purpose of the assert macros is to help programmers find bugs in their programs, things that cannot happen unless there was a coding mistake. However, with system or library calls the situation is rather different, and error returns can happen, and will happen, and should be tested for. Not by an assert, where the test goes away when <code>NDEBUG</code> is defined, but by proper error handling code. Never use this macro.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3), <code><a href="/docs/linux/man/3-assert/">assert</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
