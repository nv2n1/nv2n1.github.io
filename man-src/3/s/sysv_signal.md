---
title: "sysv_signal(3)"
name: "sysv_signal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sysv_signal/"
description: "sysv_signal – signal handling with System V semantics"
---

<p>sysv_signal &#8211; signal handling with System V semantics</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE         /* See feature_test_macros(7) */


#include &lt;signal.h&gt;</code></pre>
<p> <code>typedef void (*sighandler_t)(int);</code> <code>sighandler_t sysv_signal(int </code><i>signum</i><code>, sighandler_t </code><i>handler</i><code>);</code></p>
<h2>Description</h2>
<p>The <code>sysv_signal</code>() function takes the same arguments, and performs the same task, as <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2). </p>
<p> However <code>sysv_signal</code>() provides the System V unreliable signal semantics, that is: a) the disposition of the signal is reset to the default when the handler is invoked; b) delivery of further instances of the signal is not blocked while the signal handler is executing; and c) if the handler interrupts (certain) blocking system calls, then the system call is not automatically restarted.</p>
<h2>Return Value</h2>
<p>The <code>sysv_signal</code>() function returns the previous value of the signal handler, or <code>SIG_ERR</code> on error.</p>
<h2>Errors</h2>
<p>As for <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2).</p>
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
<td> <code>sysv_signal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is nonstandard.</p>
<h2>Notes</h2>
<p>Use of <code>sysv_signal</code>() should be avoided; use <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) instead. </p>
<p> On older Linux systems, <code>sysv_signal</code>() and <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) were equivalent. But on newer systems, <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) provides reliable signal semantics; see <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) for details. </p>
<p> The use of <i>sighandler_t</i> is a GNU extension; this type is defined only if the <code>_GNU_SOURCE</code> feature test macro is defined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-bsd_signal/">bsd_signal</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
