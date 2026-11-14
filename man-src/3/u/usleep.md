---
title: "usleep(3)"
name: "usleep"
section: "3"
letter: "u"
url: "/docs/linux/man/3-usleep/"
description: "usleep – suspend execution for microsecond intervals"
---

<p>usleep &#8211; suspend execution for microsecond intervals</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

int usleep(useconds_t usec);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>usleep</code>():</p>
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
<p>The <code>usleep</code>() function suspends execution of the calling thread for (at least) <i>usec</i> microseconds. The sleep may be lengthened slightly by any system activity or by the time spent processing the call or by the granularity of system timers.</p>
<h2>Return Value</h2>
<p>The <code>usleep</code>() function returns 0 on success. On error, -1 is returned, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINTR</code></p>
<dd>Interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd><i>usec</i> is greater than or equal to 1000000. (On systems where that is considered an error.)</dl>
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
<td> <code>usleep</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>4.3BSD, POSIX.1-2001. POSIX.1-2001 declares this function obsolete; use <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2) instead. POSIX.1-2008 removes the specification of <code>usleep</code>(). </p>
<p> On the original BSD implementation, and in glibc before version 2.2.2, the return type of this function is <i>void</i>. The POSIX version returns <i>int</i>, and this is also the prototype used since glibc 2.2.2. </p>
<p> Only the <code>EINVAL</code> error return is documented by SUSv2 and POSIX.1-2001.</p>
<h2>Notes</h2>
<p>The type <i>useconds_t</i> is an unsigned integer type capable of holding integers in the range [0,1000000]. Programs will be more portable if they never mention this type explicitly. Use </p>
<pre><code>#include &lt;unistd.h&gt;
... unsigned int usecs;
... usleep(usecs);</code></pre>
<p> The interaction of this function with the <code>SIGALRM</code> signal, and with other timer functions such as <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2), <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/3-ualarm/">ualarm</a></code>(3) is unspecified.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-getitimer/">getitimer</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/3-ualarm/">ualarm</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
