---
title: "assert(3)"
name: "assert"
section: "3"
letter: "a"
url: "/docs/linux/man/3-assert/"
description: "assert – abort the program if assertion is false"
---

<h2 class="name">NAME</h2>
<p> assert &#8211; abort the program if assertion is false </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;assert.h&gt;
void assert(scalar expression);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This macro can help programmers find bugs in their programs, or handle exceptional cases via a crash that will produce limited debugging output. </p>
<p> If <i>expression</i> is false (i.e., compares equal to zero), <code>assert</code>() prints an error message to standard error and terminates the program by calling <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3). The error message includes the name of the file and function containing the <code>assert</code>() call, the source code line number of the call, and the text of the argument; something like: </p>
<p> prog: some_file.c:16: some_func: Assertion `val == 0&#8242; failed. </p>
<p> If the macro <code>NDEBUG</code> is defined at the moment <i>&lt;assert.h&gt;</i> was last included, the macro <code>assert</code>() generates no code, and hence does nothing at all. It is not recommended to define <code>NDEBUG</code> if using <code>assert</code>() to detect error conditions since the software may behave non-deterministically.</p>
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
<td> <code>assert</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99. In C89, <i>expression</i> is required to be of type <i>int</i> and undefined behavior results if it is not, but in C99 it may have any scalar type.</p>
<h2>BUGS</h2>
<p> <code>assert</code>() is implemented as a macro; if the expression tested has side-effects, program behavior will be different depending on whether <code>NDEBUG</code> is defined. This may create Heisenbugs which go away when debugging is turned on.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3), <code><a href="/docs/linux/man/3-assert_perror/">assert_perror</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
