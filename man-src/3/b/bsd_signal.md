---
title: "bsd_signal(3)"
name: "bsd_signal"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bsd_signal/"
description: "bsd_signal – signal handling with BSD semantics"
---

<h2 class="name">NAME</h2>
<p> bsd_signal &#8211; signal handling with BSD semantics </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;signal.h&gt;</code> </p>
<p> <code>typedef void (*sighandler_t)(int);</code> </p>
<p> <code>sighandler_t bsd_signal(int </code><i>signum</i><code>, sighandler_t </code><i>handler</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>bsd_signal</code>():</p>
<dl>
<dt>
<dd> Since glibc 2.26:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;&amp;&nbsp;!&nbsp;(_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L)<br />
 Glibc 2.25 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>bsd_signal</code>() function takes the same arguments, and performs the same task, as <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2). </p>
<p> The difference between the two is that <code>bsd_signal</code>() is guaranteed to provide reliable signal semantics, that is: a) the disposition of the signal is not reset to the default when the handler is invoked; b) delivery of further instances of the signal is blocked while the signal handler is executing; and c) if the handler interrupts a blocking system call, then the system call is automatically restarted. A portable application cannot rely on <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) to provide these guarantees.</p>
<h2>RETURN VALUE</h2>
<p> The <code>bsd_signal</code>() function returns the previous value of the signal handler, or <code>SIG_ERR</code> on error.</p>
<h2>ERRORS</h2>
<p> As for <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2).</p>
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
<td> <code>bsd_signal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.2BSD, POSIX.1-2001. POSIX.1-2008 removes the specification of <code>bsd_signal</code>(), recommending the use of <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) instead.</p>
<h2>NOTES</h2>
<p> Use of <code>bsd_signal</code>() should be avoided; use <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) instead. </p>
<p> On modern Linux systems, <code>bsd_signal</code>() and <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) are equivalent. But on older systems, <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) provided unreliable signal semantics; see <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) for details. </p>
<p> The use of <i>sighandler_t</i> is a GNU extension; this type is defined only if the <code>_GNU_SOURCE</code> feature test macro is defined.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-sysv_signal/">sysv_signal</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
