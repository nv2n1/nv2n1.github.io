---
title: "siginterrupt(3)"
name: "siginterrupt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-siginterrupt/"
description: "siginterrupt – allow signals to interrupt system calls"
---

<p>siginterrupt &#8211; allow signals to interrupt system calls</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int siginterrupt(int sig, int flag);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>siginterrupt</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p>The <code>siginterrupt</code>() function changes the restart behavior when a system call is interrupted by the signal <i>sig</i>. If the <i>flag</i> argument is false (0), then system calls will be restarted if interrupted by the specified signal <i>sig</i>. This is the default behavior in Linux. </p>
<p> If the <i>flag</i> argument is true (1) and no data has been transferred, then a system call interrupted by the signal <i>sig</i> will return -1 and <i>errno</i> will be set to <code>EINTR</code>. </p>
<p> If the <i>flag</i> argument is true (1) and data transfer has started, then the system call will be interrupted and will return the actual amount of data transferred.</p>
<h2>Return Value</h2>
<p>The <code>siginterrupt</code>() function returns 0 on success. It returns -1 if the signal number <i>sig</i> is invalid, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>The specified signal number is invalid.</dl>
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
<td> <code>siginterrupt</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:sigintr
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.3BSD, POSIX.1-2001. POSIX.1-2008 marks <code>siginterrupt</code>() as obsolete, recommending the use of <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) with the <code>SA_RESTART</code> flag instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-signal/">signal</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
