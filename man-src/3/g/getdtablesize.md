---
title: "getdtablesize(3)"
name: "getdtablesize"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdtablesize/"
description: "getdtablesize – get file descriptor table size"
---

<h2 class="name">NAME</h2>
<p> getdtablesize &#8211; get file descriptor table size </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getdtablesize(void);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getdtablesize</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre><code>
/* Glibc since 2.19: */ _DEFAULT_SOURCE
|| /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE || !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L)
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>getdtablesize</code>() returns the maximum number of files a process can have open, one more than the largest possible value for a file descriptor.</p>
<h2>RETURN VALUE</h2>
<p> The current limit on the number of open files per process.</p>
<h2>ERRORS</h2>
<p> On Linux, <code>getdtablesize</code>() can return any of the errors described for <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2); see NOTES below.</p>
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
<td> <code>getdtablesize</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.4BSD (the <code>getdtablesize</code>() function first appeared in 4.2BSD). It is not specified in POSIX.1; portable applications should employ <i>sysconf(_SC_OPEN_MAX)</i> instead of this call.</p>
<h2>NOTES</h2>
<p> The glibc version of <code>getdtablesize</code>() calls <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) and returns the current <code>RLIMIT_NOFILE</code> limit, or <code>OPEN_MAX</code> when that fails.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
