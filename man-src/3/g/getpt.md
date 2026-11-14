---
title: "getpt(3)"
name: "getpt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpt/"
description: "getpt – open a new pseudoterminal master"
---

<h2 class="name">NAME</h2>
<p> getpt &#8211; open a new pseudoterminal master </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;stdlib.h&gt;
int getpt(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>getpt</code>() opens a new pseudoterminal device and returns a file descriptor that refers to that device. It is equivalent to opening the pseudoterminal multiplexor device </p>
<p> open(&quot;/dev/ptmx&quot;, O_RDWR); </p>
<p> on Linux systems, though the pseudoterminal multiplexor device is located elsewhere on some systems that use the GNU C library.</p>
<h2>RETURN VALUE</h2>
<p> <code>getpt</code>() returns an open file descriptor upon successful completion. Otherwise, it returns -1 and sets <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<p> <code>getpt</code>() can fail with various errors described in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> <code>getpt</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>getpt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>getpt</code>() is glibc-specific; use <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3) instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3), <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3), <code><a href="/docs/linux/man/4-ptmx/">ptmx</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
