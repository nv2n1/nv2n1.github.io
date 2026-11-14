---
title: "clock_settime(3)"
name: "clock_settime"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clock_settime/"
description: "clock_getres, clock_gettime, clock_settime – clock and time functions"
---

<h2 class="name">NAME</h2>
<p> clock_getres, clock_gettime, clock_settime &#8211; clock and time functions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int clock_getres(clockid_t </code><i>clk_id</i><code>, struct timespec *</code><i>res</i><code>);</code> </p>
<p> <code>int clock_gettime(clockid_t </code><i>clk_id</i><code>, struct timespec *</code><i>tp</i><code>);</code> </p>
<p> <code>int clock_settime(clockid_t </code><i>clk_id</i><code>, const struct timespec *</code><i>tp</i><code>);</code> </p>
<p> Link with <i>-lrt</i> (only for glibc versions before 2.17). </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>clock_getres</code>(), <code>clock_gettime</code>(), <code>clock_settime</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>clock_getres</code>() finds the resolution (precision) of the specified clock <i>clk_id</i>, and, if <i>res</i> is non-NULL, stores it in the <i>struct timespec</i> pointed to by <i>res</i>. The resolution of clocks depends on the implementation and cannot be configured by a particular process. If the time value pointed to by the argument <i>tp</i> of <code>clock_settime</code>() is not a multiple of <i>res</i>, then it is truncated to a multiple of <i>res</i>. </p>
<p> The functions <code>clock_gettime</code>() and <code>clock_settime</code>() retrieve and set the time of the specified clock <i>clk_id</i>. </p>
<p> The <i>res</i> and <i>tp</i> arguments are <i>timespec</i> structures, as specified in <i>&lt;time.h&gt;</i>: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> The <i>clk_id</i> argument is the identifier of the particular clock on which to act. A clock may be system-wide and hence visible for all processes, or per-process if it measures time only within a single process. </p>
<p> All implementations support the system-wide real-time clock, which is identified by <code>CLOCK_REALTIME</code>. Its time represents seconds and nanoseconds since the Epoch. When its time is changed, timers for a relative interval are unaffected, but timers for an absolute point in time are affected. </p>
<p> More clocks may be implemented. The interpretation of the corresponding time values and the effect on timers is unspecified. </p>
<p> Sufficiently recent versions of glibc and the Linux kernel support the following clocks:</p>
<dl>
<dt><code>CLOCK_REALTIME</code></p>
<dd> System-wide clock that measures real (i.e., wall-clock) time. Setting this clock requires appropriate privileges. This clock is affected by discontinuous jumps in the system time (e.g., if the system administrator manually changes the clock), and by the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3) and NTP.</p>
<dt><code>CLOCK_REALTIME_COARSE</code> (since Linux 2.6.32; Linux-specific)</p>
<dd> A faster but less precise version of <code>CLOCK_REALTIME</code>. Use when you need very fast, but not fine-grained timestamps. Requires per-architecture support, and probably also architecture support for this flag in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<dt><code>CLOCK_MONOTONIC</code></p>
<dd> Clock that cannot be set and represents monotonic time since&#8212;as described by POSIX&#8212;&quot;some unspecified point in the past&quot;. On Linux, that point corresponds to the number of seconds that the system has been running since it was booted.</p>
<dt>
<dd> The <code>CLOCK_MONOTONIC</code> clock is not affected by discontinuous jumps in the system time (e.g., if the system administrator manually changes the clock), but is affected by the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3) and NTP. This clock does not count time that the system is suspended.</p>
<dt><code>CLOCK_MONOTONIC_COARSE</code> (since Linux 2.6.32; Linux-specific)</p>
<dd> A faster but less precise version of <code>CLOCK_MONOTONIC</code>. Use when you need very fast, but not fine-grained timestamps. Requires per-architecture support, and probably also architecture support for this flag in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<dt><code>CLOCK_MONOTONIC_RAW</code> (since Linux 2.6.28; Linux-specific)</p>
<dd> Similar to <code>CLOCK_MONOTONIC</code>, but provides access to a raw hardware-based time that is not subject to NTP adjustments or the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3). This clock does not count time that the system is suspended.</p>
<dt><code>CLOCK_BOOTTIME</code> (since Linux 2.6.39; Linux-specific)</p>
<dd> Identical to <code>CLOCK_MONOTONIC</code>, except it also includes any time that the system is suspended. This allows applications to get a suspend-aware monotonic clock without having to deal with the complications of <code>CLOCK_REALTIME</code>, which may have discontinuities if the time is changed using <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2) or similar.</p>
<dt><code>CLOCK_PROCESS_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> Per-process CPU-time clock (measures CPU time consumed by all threads in the process).</p>
<dt><code>CLOCK_THREAD_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> Thread-specific CPU-time clock.</dl>
<h2>RETURN VALUE</h2>
<p> <code>clock_gettime</code>(), <code>clock_settime</code>(), and <code>clock_getres</code>() return 0 for success, or -1 for failure (in which case <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>tp</i> points outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>clk_id</i> specified is not supported on this system.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>clock_settime</code>()): <i>tp.tv_sec</i> is negative or <i>tp.tv_nsec</i> is outside the range [0..999,999,999].</p>
<dt><code>EINVAL</code> (since Linux 4.3)</p>
<dd> A call to <code>clock_settime</code>() with a <i>clk_id</i> of <code>CLOCK_REALTIME</code> attempted to set the time to a value less than the current value of the <code>CLOCK_MONOTONIC</code> clock.</p>
<dt><code>EPERM</code></p>
<dd> <code>clock_settime</code>() does not have permission to set the clock indicated.</dl>
<h2>VERSIONS</h2>
<p> These system calls first appeared in Linux 2.6.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>clock_getres</code>(), <code>clock_gettime</code>(), <code>clock_settime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SUSv2.</p>
<h2>AVAILABILITY</h2>
<p> On POSIX systems on which these functions are available, the symbol <code>_POSIX_TIMERS</code> is defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. The symbols <code>_POSIX_MONOTONIC_CLOCK</code>, <code>_POSIX_CPUTIME</code>, <code>_POSIX_THREAD_CPUTIME</code> indicate that <code>CLOCK_MONOTONIC</code>, <code>CLOCK_PROCESS_CPUTIME_ID</code>, <code>CLOCK_THREAD_CPUTIME_ID</code> are available. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>NOTES</h2>
<p> POSIX.1 specifies the following:</p>
<dl>
<dt>
<dd>
<p> Setting the value of the <code>CLOCK_REALTIME</code> clock via <code>clock_settime</code>() shall have no effect on threads that are blocked waiting for a relative time service based upon this clock, including the <code>nanosleep</code>() function; nor on the expiration of relative timers based upon this clock. Consequently, these time services shall expire when the requested relative interval elapses, independently of the new or old value of the clock.</dl>
<h3>C library/kernel differences</h3>
<p> On some architectures, an implementation of <code>clock_gettime</code>() is provided in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<h3>Historical note for SMP systems</h3>
<p> Before Linux added kernel support for <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code>, glibc implemented these clocks on many platforms using timer registers from the CPUs (TSC on i386, AR.ITC on Itanium). These registers may differ between CPUs and as a consequence these clocks may return <code>bogus results</code> if a process is migrated to another CPU. </p>
<p> If the CPUs in an SMP system have different clock sources, then there is no way to maintain a correlation between the timer registers since each CPU will run at a slightly different frequency. If that is the case, then <i>clock_getcpuclockid(0)</i> will return <code>ENOENT</code> to signify this condition. The two clocks will then be useful only if it can be ensured that a process stays on a certain CPU. </p>
<p> The processors in an SMP system do not start all at exactly the same time and therefore the timer registers are typically running at an offset. Some architectures include code that attempts to limit these offsets on bootup. However, the code cannot guarantee to accurately tune the offsets. Glibc contains no provisions to deal with these offsets (unlike the Linux Kernel). Typically these offsets are small and therefore the effects may be negligible in most cases. </p>
<p> Since glibc 2.4, the wrapper functions for the system calls described in this page avoid the abovementioned problems by employing the kernel implementation of <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code>, on systems that provide such an implementation (i.e., Linux 2.6.12 and later).</p>
<h2>BUGS</h2>
<p> According to POSIX.1-2001, a process with &quot;appropriate privileges&quot; may set the <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code> clocks using <code>clock_settime</code>(). On Linux, these clocks are not settable (i.e., no process has &quot;appropriate privileges&quot;).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3), <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.05 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
