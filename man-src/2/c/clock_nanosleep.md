---
title: "clock_nanosleep(2)"
name: "clock_nanosleep"
section: "2"
letter: "c"
url: "/docs/linux/man/2-clock_nanosleep/"
description: "clock_nanosleep – high-resolution sleep with specifiable clock"
---

<h2 class="name">NAME</h2>
<p> clock_nanosleep &#8211; high-resolution sleep with specifiable clock </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<pre><code>
int clock_nanosleep(clockid_t clockid, int flags,
                    const struct timespec *request,
                    struct timespec *remain);
</code></pre>
<p> Link with <i>-lrt</i> (only for glibc versions before 2.17). </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>clock_nanosleep</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> Like <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code>clock_nanosleep</code>() allows the calling thread to sleep for an interval specified with nanosecond precision. It differs in allowing the caller to select the clock against which the sleep interval is to be measured, and in allowing the sleep interval to be specified as either an absolute or a relative value. </p>
<p> The time values passed to and returned by this call are specified using <i>timespec</i> structures, defined as follows: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;[0 .. 999999999]&nbsp;*/ }; </p>
<p> The <i>clockid</i> argument specifies the clock against which the sleep interval is to be measured. This argument can have one of the following values:</p>
<dl>
<dt><code>CLOCK_REALTIME</code></p>
<dd> A settable system-wide real-time clock.</p>
<dt><code>CLOCK_TAI</code> (since Linux 3.10)</p>
<dd> A system-wide clock derived from wall-clock time but ignoring leap seconds.</p>
<dt><code>CLOCK_MONOTONIC</code></p>
<dd> A nonsettable, monotonically increasing clock that measures time since some unspecified point in the past that does not change after system startup.</p>
<dt><code>CLOCK_BOOTIME</code> (since Linux 2.6.39)</p>
<dd> Identical to <code>CLOCK_MONOTONIC</code>, except that it also includes any time that the system is suspended.</p>
<dt><code>CLOCK_PROCESS_CPUTIME_ID</code></p>
<dd> A settable per-process clock that measures CPU time consumed by all threads in the process.</dl>
<p> See <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2) for further details on these clocks. In addition, the CPU clock IDs returned by <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3) can also be passed in <i>clockid</i>. </p>
<p> If <i>flags</i> is 0, then the value specified in <i>request</i> is interpreted as an interval relative to the current value of the clock specified by <i>clockid</i>. </p>
<p> If <i>flags</i> is <code>TIMER_ABSTIME</code>, then <i>request</i> is interpreted as an absolute time as measured by the clock, <i>clockid</i>. If <i>request</i> is less than or equal to the current value of the clock, then <code>clock_nanosleep</code>() returns immediately without suspending the calling thread. </p>
<p> <code>clock_nanosleep</code>() suspends the execution of the calling thread until either at least the time specified by <i>request</i> has elapsed, or a signal is delivered that causes a signal handler to be called or that terminates the process. </p>
<p> If the call is interrupted by a signal handler, <code>clock_nanosleep</code>() fails with the error <code>EINTR</code>. In addition, if <i>remain</i> is not NULL, and <i>flags</i> was not <code>TIMER_ABSTIME</code>, it returns the remaining unslept time in <i>remain</i>. This value can then be used to call <code>clock_nanosleep</code>() again and complete a (relative) sleep.</p>
<h2>RETURN VALUE</h2>
<p> On successfully sleeping for the requested interval, <code>clock_nanosleep</code>() returns 0. If the call is interrupted by a signal handler or encounters an error, then it returns one of the positive error number listed in ERRORS.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>request</i> or <i>remain</i> specified an invalid address.</p>
<dt><code>EINTR</code></p>
<dd> The sleep was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The value in the <i>tv_nsec</i> field was not in the range 0 to 999999999 or <i>tv_sec</i> was negative.</p>
<dt><code>EINVAL</code></p>
<dd> <i>clockid</i> was invalid. (<code>CLOCK_THREAD_CPUTIME_ID</code> is not a permitted value for <i>clockid</i>.)</p>
<dt><code>ENOTSUP</code></p>
<dd> The kernel does not support sleeping against this <i>clockid</i>.</dl>
<h2>VERSIONS</h2>
<p> The <code>clock_nanosleep</code>() system call first appeared in Linux 2.6. Support is available in glibc since version 2.1.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> If the interval specified in <i>request</i> is not an exact multiple of the granularity underlying clock (see <code><a href="/docs/linux/man/7-time/">time</a></code>(7)), then the interval will be rounded up to the next multiple. Furthermore, after the sleep completes, there may still be a delay before the CPU becomes free to once again execute the calling thread. </p>
<p> Using an absolute timer is useful for preventing timer drift problems of the type described in <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2). (Such problems are exacerbated in programs that try to restart a relative sleep that is repeatedly interrupted by signals.) To perform a relative sleep that avoids these problems, call <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) for the desired clock, add the desired interval to the returned time value, and then call <code>clock_nanosleep</code>() with the <code>TIMER_ABSTIME</code> flag. </p>
<p> <code>clock_nanosleep</code>() is never restarted after being interrupted by a signal handler, regardless of the use of the <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) <code>SA_RESTART</code> flag. </p>
<p> The <i>remain</i> argument is unused, and unnecessary, when <i>flags</i> is <code>TIMER_ABSTIME</code>. (An absolute sleep can be restarted using the same <i>request</i> argument.) </p>
<p> POSIX.1 specifies that <code>clock_nanosleep</code>() has no effect on signals dispositions or the signal mask. </p>
<p> POSIX.1 specifies that after changing the value of the <code>CLOCK_REALTIME</code> clock via <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2), the new clock value shall be used to determine the time at which a thread blocked on an absolute <code>clock_nanosleep</code>() will wake up; if the new clock value falls past the end of the sleep interval, then the <code>clock_nanosleep</code>() call will return immediately. </p>
<p> POSIX.1 specifies that changing the value of the <code>CLOCK_REALTIME</code> clock via <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2) shall have no effect on a thread that is blocked on a relative <code>clock_nanosleep</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
