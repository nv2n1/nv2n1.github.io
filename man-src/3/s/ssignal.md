---
title: "ssignal(3)"
name: "ssignal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssignal/"
description: "gsignal, ssignal – software signal facility"
---

<p>gsignal, ssignal &#8211; software signal facility</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

typedef void (*sighandler_t)(int);

int gsignal(int signum);

sighandler_t ssignal(int signum, sighandler_t action);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>gsignal</code>(), <code>ssignal</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>Don&#8217;t use these functions under Linux. Due to a historical mistake, under Linux these functions are aliases for <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3) and <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), respectively. </p>
<p> Elsewhere, on System V-like systems, these functions implement software signaling, entirely independent of the classical <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) and <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) functions. The function <code>ssignal</code>() defines the action to take when the software signal with number <i>signum</i> is raised using the function <code>gsignal</code>(), and returns the previous such action or <code>SIG_DFL</code>. The function <code>gsignal</code>() does the following: if no action (or the action <code>SIG_DFL</code>) was specified for <i>signum</i>, then it does nothing and returns 0. If the action <code>SIG_IGN</code> was specified for <i>signum</i>, then it does nothing and returns 1. Otherwise, it resets the action to <code>SIG_DFL</code> and calls the action function with argument <i>signum</i>, and returns the value returned by that function. The range of possible values <i>signum</i> varies (often 1-15 or 1-17).</p>
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
<td> <code>gsignal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>ssignal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe sigintr
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are available under AIX, DG/UX, HP-UX, SCO, Solaris, Tru64. They are called obsolete under most of these systems, and are broken under glibc. Some systems also have <code>gsignal_r</code>() and <code>ssignal_r</code>().</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
