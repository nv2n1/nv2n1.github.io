---
title: "nanosleep(2)"
name: "nanosleep"
section: "2"
letter: "n"
url: "/docs/linux/man/2-nanosleep/"
description: "nanosleep – high-resolution sleep"
---

<h2 class="name">NAME</h2>
<p> nanosleep &#8211; high-resolution sleep </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int nanosleep(const struct timespec *</code><i>req</i><code>, struct timespec *</code><i>rem</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>nanosleep</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>DESCRIPTION</h2>
<p> <code>nanosleep</code>() suspends the execution of the calling thread until either at least the time specified in <i>*req</i> has elapsed, or the delivery of a signal that triggers the invocation of a handler in the calling thread or that terminates the process. </p>
<p> If the call is interrupted by a signal handler, <code>nanosleep</code>() returns -1, sets <i>errno</i> to <code>EINTR</code>, and writes the remaining time into the structure pointed to by <i>rem</i> unless <i>rem</i> is NULL. The value of <i>*rem</i> can then be used to call <code>nanosleep</code>() again and complete the specified pause (but see NOTES). </p>
<p> The structure <i>timespec</i> is used to specify intervals of time with nanosecond precision. It is defined as follows: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> The value of the nanoseconds field must be in the range 0 to 999999999. </p>
<p> Compared to <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3) and <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3), <code>nanosleep</code>() has the following advantages: it provides a higher resolution for specifying the sleep interval; POSIX.1 explicitly specifies that it does not interact with signals; and it makes the task of resuming a sleep that has been interrupted by a signal handler easier.</p>
<h2>RETURN VALUE</h2>
<p> On successfully sleeping for the requested interval, <code>nanosleep</code>() returns 0. If the call is interrupted by a signal handler or encounters an error, then it returns -1, with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Problem with copying information from user space.</p>
<dt><code>EINTR</code></p>
<dd> The pause has been interrupted by a signal that was delivered to the thread (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). The remaining sleep time has been written into <i>*rem</i> so that the thread can easily call <code>nanosleep</code>() again and continue with the pause.</p>
<dt><code>EINVAL</code></p>
<dd> The value in the <i>tv_nsec</i> field was not in the range 0 to 999999999 or <i>tv_sec</i> was negative.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> If the interval specified in <i>req</i> is not an exact multiple of the granularity underlying clock (see <code><a href="/docs/linux/man/7-time/">time</a></code>(7)), then the interval will be rounded up to the next multiple. Furthermore, after the sleep completes, there may still be a delay before the CPU becomes free to once again execute the calling thread. </p>
<p> The fact that <code>nanosleep</code>() sleeps for a relative interval can be problematic if the call is repeatedly restarted after being interrupted by signals, since the time between the interruptions and restarts of the call will lead to drift in the time when the sleep finally completes. This problem can be avoided by using <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2) with an absolute time value. </p>
<p> POSIX.1 specifies that <code>nanosleep</code>() should measure time against the <code>CLOCK_REALTIME</code> clock. However, Linux measures the time using the <code>CLOCK_MONOTONIC</code> clock. This probably does not matter, since the POSIX.1 specification for <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2) says that discontinuous changes in <code>CLOCK_REALTIME</code> should not affect <code>nanosleep</code>():</p>
<dl>
<dt>
<dd>
<p> Setting the value of the <code>CLOCK_REALTIME</code> clock via <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2) shall have no effect on threads that are blocked waiting for a relative time service based upon this clock, including the <code>nanosleep</code>() function; &#8230; Consequently, these time services shall expire when the requested relative interval elapses, independently of the new or old value of the clock.</dl>
<h3>Old behavior</h3>
<p> In order to support applications requiring much more precise pauses (e.g., in order to control some time-critical hardware), <code>nanosleep</code>() would handle pauses of up to 2 milliseconds by busy waiting with microsecond precision when called from a thread scheduled under a real-time policy like <code>SCHED_FIFO</code> or <code>SCHED_RR</code>. This special extension was removed in kernel 2.5.39, and is thus not available in Linux 2.6.0 and later kernels.</p>
<h2>BUGS</h2>
<p> If a program that catches signals and uses <code>nanosleep</code>() receives signals at a very high rate, then scheduling delays and rounding errors in the kernel&#8217;s calculation of the sleep interval and the returned <i>remain</i> value mean that the <i>remain</i> value may steadily <i>increase</i> on successive restarts of the <code>nanosleep</code>() call. To avoid such problems, use <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2) with the <code>TIMER_ABSTIME</code> flag to sleep to an absolute deadline. </p>
<p> In Linux 2.4, if <code>nanosleep</code>() is stopped by a signal (e.g., <code>SIGTSTP</code>), then the call fails with the error <code>EINTR</code> after the thread is resumed by a <code>SIGCONT</code> signal. If the system call is subsequently restarted, then the time that the thread spent in the stopped state is <i>not</i> counted against the sleep interval. This problem is fixed in Linux 2.6.0 and later kernels.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
