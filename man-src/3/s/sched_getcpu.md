---
title: "sched_getcpu(3)"
name: "sched_getcpu"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sched_getcpu/"
description: "sched_getcpu – determine CPU on which the calling thread is running"
---

<p>sched_getcpu &#8211; determine CPU on which the calling thread is running</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sched.h&gt;

int sched_getcpu(void);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sched_getcpu</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.14:</p>
<dd>_GNU_SOURCE</p>
<dt>Before glibc 2.14:</p>
<dd>_BSD_SOURCE || _SVID_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;_GNU_SOURCE also suffices&nbsp;*/</dl>
</dl>
<h2>Description</h2>
<p><code>sched_getcpu</code>() returns the number of the CPU on which the calling thread is currently executing.</p>
<h2>Return Value</h2>
<p>On success, <code>sched_getcpu</code>() returns a nonnegative CPU number. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOSYS</code></p>
<dd>This kernel does not implement <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2).</dl>
<h2>Versions</h2>
<p>This function is available since glibc 2.6.</p>
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
<td> <code>sched_getcpu</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>sched_getcpu</code>() is glibc-specific.</p>
<h2>Notes</h2>
<p>The call int c, s;<br />
s = getcpu(&amp;c, NULL, NULL);<br />
cpu = (s == -1) ? s : c; is equivalent to the following <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2) call: </p>
<pre><code>int c, s;
s = getcpu(&amp;c, NULL, NULL);
cpu = (s == -1) ? s : c;</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
