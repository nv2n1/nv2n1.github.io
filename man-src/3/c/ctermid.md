---
title: "ctermid(3)"
name: "ctermid"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctermid/"
description: "ctermid – get controlling terminal name"
---

<h2 class="name">NAME</h2>
<p> ctermid &#8211; get controlling terminal name </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
char *ctermid(char *s);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>ctermid</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>ctermid</code>() returns a string which is the pathname for the current controlling terminal for this process. If <i>s</i> is NULL, a static buffer is used, otherwise <i>s</i> points to a buffer used to hold the terminal pathname. The symbolic constant <code>L_ctermid</code> is the maximum number of characters in the returned pathname.</p>
<h2>RETURN VALUE</h2>
<p> The pointer to the pathname.</p>
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
<td> <code>ctermid</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, Svr4.</p>
<h2>BUGS</h2>
<p> The returned pathname may not uniquely identify the controlling terminal; it may, for example, be <i>/dev/tty</i>. </p>
<p> It is not assured that the program can open the terminal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
