---
title: "ualarm(3)"
name: "ualarm"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ualarm/"
description: "ualarm – schedule signal after given number of microseconds"
---

<p>ualarm &#8211; schedule signal after given number of microseconds</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

useconds_t ualarm(useconds_t usecs, useconds_t interval);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>ualarm</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre>(_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500) &amp;&amp; ! (_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L)
 || /* Glibc since 2.19: */ _DEFAULT_SOURCE
 || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE</pre>
<dt>Before glibc 2.12:</p>
<dd>_BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>Description</h2>
<p>The <code>ualarm</code>() function causes the signal <code>SIGALRM</code> to be sent to the invoking process after (not less than) <i>usecs</i> microseconds. The delay may be lengthened slightly by any system activity or by the time spent processing the call or by the granularity of system timers. </p>
<p> Unless caught or ignored, the <code>SIGALRM</code> signal will terminate the process. </p>
<p> If the <i>interval</i> argument is nonzero, further <code>SIGALRM</code> signals will be sent every <i>interval</i> microseconds after the first.</p>
<h2>Return Value</h2>
<p>This function returns the number of microseconds remaining for any alarm that was previously set, or 0 if no alarm was pending.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINTR</code></p>
<dd>Interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd><i>usecs</i> or <i>interval</i> is not smaller than 1000000. (On systems where that is considered an error.)</dl>
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
<td> <code>ualarm</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.3BSD, POSIX.1-2001. POSIX.1-2001 marks <code>ualarm</code>() as obsolete. POSIX.1-2008 removes the specification of <code>ualarm</code>(). 4.3BSD, SUSv2, and POSIX do not define any errors.</p>
<h2>Notes</h2>
<p>POSIX.1-2001 does not specify what happens if the <i>usecs</i> argument is 0. On Linux (and probably most other systems), the effect is to cancel any pending alarm. </p>
<p> The type <i>useconds_t</i> is an unsigned integer type capable of holding integers in the range [0,1000000]. On the original BSD implementation, and in glibc before version 2.1, the arguments to <code>ualarm</code>() were instead typed as <i>unsigned int</i>. Programs will be more portable if they never mention <i>useconds_t</i> explicitly. </p>
<p> The interaction of this function with other timer functions such as <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2), <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3) is unspecified. </p>
<p> This function is obsolete. Use <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) or POSIX interval timers (<code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), etc.) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-getitimer/">getitimer</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
