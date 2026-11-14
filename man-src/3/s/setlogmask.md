---
title: "setlogmask(3)"
name: "setlogmask"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setlogmask/"
description: "setlogmask – set log priority mask"
---

<p>setlogmask &#8211; set log priority mask</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;syslog.h&gt;

int setlogmask(int mask);</code></pre>
<h2>Description</h2>
<p>A process has a log priority mask that determines which calls to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) may be logged. All other calls will be ignored. Logging is enabled for the priorities that have the corresponding bit set in <i>mask</i>. The initial mask is such that logging is enabled for all priorities. </p>
<p> The <code>setlogmask</code>() function sets this logmask for the calling process, and returns the previous mask. If the mask argument is 0, the current logmask is not modified. </p>
<p> The eight priorities are <code>LOG_EMERG</code>, <code>LOG_ALERT</code>, <code>LOG_CRIT</code>, <code>LOG_ERR</code>, <code>LOG_WARNING</code>, <code>LOG_NOTICE</code>, <code>LOG_INFO</code>, and <code>LOG_DEBUG</code>. The bit corresponding to a priority <i>p</i> is <i>LOG_MASK(p)</i>. Some systems also provide a macro <i>LOG_UPTO(p)</i> for the mask of all priorities in the above list up to and including <i>p</i>.</p>
<h2>Return Value</h2>
<p>This function returns the previous log priority mask.</p>
<h2>Errors</h2>
<p>None.</p>
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
<td> <code>setlogmask</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:LogMask
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>LOG_UPTO</code>() will be included in the next release of the POSIX specification (Issue 8).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-closelog/">closelog</a></code>(3), <code><a href="/docs/linux/man/3-openlog/">openlog</a></code>(3), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
