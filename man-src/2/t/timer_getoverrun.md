---
title: "timer_getoverrun(2)"
name: "timer_getoverrun"
section: "2"
letter: "t"
url: "/docs/linux/man/2-timer_getoverrun/"
description: "timer_getoverrun – get overrun count for a POSIX per-process timer"
---

<h2 class="name">NAME</h2>
<p> timer_getoverrun &#8211; get overrun count for a POSIX per-process timer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;time.h&gt;
int timer_getoverrun(timer_t timerid);
</code></pre>
<p> Link with <i>-lrt</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>timer_getoverrun</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>DESCRIPTION</h2>
<p> <code>timer_getoverrun</code>() returns the &quot;overrun count&quot; for the timer referred to by <i>timerid</i>. An application can use the overrun count to accurately calculate the number of timer expirations that would have occurred over a given time interval. Timer overruns can occur both when receiving expiration notifications via signals (<code>SIGEV_SIGNAL</code>), and via threads (<code>SIGEV_THREAD</code>). </p>
<p> When expiration notifications are delivered via a signal, overruns can occur as follows. Regardless of whether or not a real-time signal is used for timer notifications, the system queues at most one signal per timer. (This is the behavior specified by POSIX.1. The alternative, queuing one signal for each timer expiration, could easily result in overflowing the allowed limits for queued signals on the system.) Because of system scheduling delays, or because the signal may be temporarily blocked, there can be a delay between the time when the notification signal is generated and the time when it is delivered (e.g., caught by a signal handler) or accepted (e.g., using <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2)). In this interval, further timer expirations may occur. The timer overrun count is the number of additional timer expirations that occurred between the time when the signal was generated and when it was delivered or accepted. </p>
<p> Timer overruns can also occur when expiration notifications are delivered via invocation of a thread, since there may be an arbitrary delay between an expiration of the timer and the invocation of the notification thread, and in that delay interval, additional timer expirations may occur.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>timer_getoverrun</code>() returns the overrun count of the specified timer; this count may be 0 if no overruns have occurred. On failure, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>timerid</i> is not a valid timer ID.</dl>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> When timer notifications are delivered via signals (<code>SIGEV_SIGNAL</code>), on Linux it is also possible to obtain the overrun count via the <i>si_overrun</i> field of the <i>siginfo_t</i> structure (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)). This allows an application to avoid the overhead of making a system call to obtain the overrun count, but is a nonportable extension to POSIX.1. </p>
<p> POSIX.1 discusses timer overruns only in the context of timer notifications using signals.</p>
<h2>BUGS</h2>
<p> POSIX.1 specifies that if the timer overrun count is equal to or greater than an implementation-defined maximum, <code>DELAYTIMER_MAX</code>, then <code>timer_getoverrun</code>() should return <code>DELAYTIMER_MAX</code>. However, before Linux 4.19, if the timer overrun value exceeds the maximum representable integer, the counter cycles, starting once more from low values. Since Linux 4.19, <code>timer_getoverrun</code>() returns <code>DELAYTIMER_MAX</code> (defined as <code>INT_MAX</code> in <i>&lt;limits.h&gt;</i>) in this case (and the overrun value is reset to 0).</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
