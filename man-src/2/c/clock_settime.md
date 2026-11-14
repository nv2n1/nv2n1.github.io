---
title: "clock_settime(2)"
name: "clock_settime"
section: "2"
letter: "c"
url: "/docs/linux/man/2-clock_settime/"
description: "clock_getres, clock_gettime, clock_settime – clock and time functions"
---

<h2 class="name">NAME</h2>
<p> clock_getres, clock_gettime, clock_settime &#8211; clock and time functions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int clock_getres(clockid_t </code><i>clockid</i><code>, struct timespec *</code><i>res</i><code>);</code> </p>
<p> <code>int clock_gettime(clockid_t </code><i>clockid</i><code>, struct timespec *</code><i>tp</i><code>);</code> </p>
<p> <code>int clock_settime(clockid_t </code><i>clockid</i><code>, const struct timespec *</code><i>tp</i><code>);</code> </p>
<p> Link with <i>-lrt</i> (only for glibc versions before 2.17). </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>clock_getres</code>(), <code>clock_gettime</code>(), <code>clock_settime</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>clock_getres</code>() finds the resolution (precision) of the specified clock <i>clockid</i>, and, if <i>res</i> is non-NULL, stores it in the <i>struct timespec</i> pointed to by <i>res</i>. The resolution of clocks depends on the implementation and cannot be configured by a particular process. If the time value pointed to by the argument <i>tp</i> of <code>clock_settime</code>() is not a multiple of <i>res</i>, then it is truncated to a multiple of <i>res</i>. </p>
<p> The functions <code>clock_gettime</code>() and <code>clock_settime</code>() retrieve and set the time of the specified clock <i>clockid</i>. </p>
<p> The <i>res</i> and <i>tp</i> arguments are <i>timespec</i> structures, as specified in <i>&lt;time.h&gt;</i>: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> The <i>clockid</i> argument is the identifier of the particular clock on which to act. A clock may be system-wide and hence visible for all processes, or per-process if it measures time only within a single process. </p>
<p> All implementations support the system-wide real-time clock, which is identified by <code>CLOCK_REALTIME</code>. Its time represents seconds and nanoseconds since the Epoch. When its time is changed, timers for a relative interval are unaffected, but timers for an absolute point in time are affected. </p>
<p> More clocks may be implemented. The interpretation of the corresponding time values and the effect on timers is unspecified. </p>
<p> Sufficiently recent versions of glibc and the Linux kernel support the following clocks:</p>
<dl>
<dt><code>CLOCK_REALTIME</code></p>
<dd> A settable system-wide clock that measures real (i.e., wall-clock) time. Setting this clock requires appropriate privileges. This clock is affected by discontinuous jumps in the system time (e.g., if the system administrator manually changes the clock), and by the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3) and NTP.</p>
<dt><code>CLOCK_REALTIME_ALARM</code> (since Linux 3.0; Linux-specific)</p>
<dd> Like <code>CLOCK_REALTIME</code>, but not settable. See <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2) for further details.</p>
<dt><code>CLOCK_REALTIME_COARSE</code> (since Linux 2.6.32; Linux-specific)</p>
<dd> A faster but less precise version of <code>CLOCK_REALTIME</code>. This clock is not settable. Use when you need very fast, but not fine-grained timestamps. Requires per-architecture support, and probably also architecture support for this flag in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<dt><code>CLOCK_TAI</code> (since Linux 3.10; Linux-specific)</p>
<dd> A nonsettable system-wide clock derived from wall-clock time but ignoring leap seconds. This clock does not experience discontinuities and backwards jumps caused by NTP inserting leap seconds as <code>CLOCK_REALTIME</code> does.</p>
<dt>
<dd> The acronym TAI refers to International Atomic Time.</p>
<dt><code>CLOCK_MONOTONIC</code></p>
<dd> A nonsettable system-wide clock that represents monotonic time since&#8212;as described by POSIX&#8212;&quot;some unspecified point in the past&quot;. On Linux, that point corresponds to the number of seconds that the system has been running since it was booted.</p>
<dt>
<dd> The <code>CLOCK_MONOTONIC</code> clock is not affected by discontinuous jumps in the system time (e.g., if the system administrator manually changes the clock), but is affected by the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3) and NTP. This clock does not count time that the system is suspended. All <code>CLOCK_MONOTONIC</code> variants guarantee that the time returned by consecutive calls will not go backwards, but successive calls may&#8212;depending on the architecture&#8212;return identical (not-increased) time values.</p>
<dt><code>CLOCK_MONOTONIC_COARSE</code> (since Linux 2.6.32; Linux-specific)</p>
<dd> A faster but less precise version of <code>CLOCK_MONOTONIC</code>. Use when you need very fast, but not fine-grained timestamps. Requires per-architecture support, and probably also architecture support for this flag in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<dt><code>CLOCK_MONOTONIC_RAW</code> (since Linux 2.6.28; Linux-specific)</p>
<dd> Similar to <code>CLOCK_MONOTONIC</code>, but provides access to a raw hardware-based time that is not subject to NTP adjustments or the incremental adjustments performed by <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3). This clock does not count time that the system is suspended.</p>
<dt><code>CLOCK_BOOTTIME</code> (since Linux 2.6.39; Linux-specific)</p>
<dd> A nonsettable system-wide clock that is identical to <code>CLOCK_MONOTONIC</code>, except that it also includes any time that the system is suspended. This allows applications to get a suspend-aware monotonic clock without having to deal with the complications of <code>CLOCK_REALTIME</code>, which may have discontinuities if the time is changed using <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2) or similar.</p>
<dt><code>CLOCK_BOOTTIME_ALARM</code> (since Linux 3.0; Linux-specific)</p>
<dd> Like <code>CLOCK_BOOTTIME</code>. See <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2) for further details.</p>
<dt><code>CLOCK_PROCESS_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> This is a clock that measures CPU time consumed by this process (i.e., CPU time consumed by all threads in the process). On Linux, this clock is not settable.</p>
<dt><code>CLOCK_THREAD_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> This is a clock that measures CPU time consumed by this thread. On Linux, this clock is not settable.</dl>
<p> Linux also implements dynamic clock instances as described below.</p>
<h3>Dynamic clocks</h3>
<p> In addition to the hard-coded System-V style clock IDs described above, Linux also supports POSIX clock operations on certain character devices. Such devices are called &quot;dynamic&quot; clocks, and are supported since Linux 2.6.39. </p>
<p> Using the appropriate macros, open file descriptors may be converted into clock IDs and passed to <code>clock_gettime</code>(), <code>clock_settime</code>(), and <code><a href="/docs/linux/man/2-clock_adjtime/">clock_adjtime</a></code>(2). The following example shows how to convert a file descriptor into a dynamic clock ID. </p>
<p> #define CLOCKFD 3 #define FD_TO_CLOCKID(fd) ((~(clockid_t) (fd) &lt;&lt; 3) | CLOCKFD) #define CLOCKID_TO_FD(clk) ((unsigned int) ~((clk) &gt;&gt; 3)) </p>
<p> struct timespec ts; clockid_t clkid; int fd; </p>
<p> fd = open(&quot;/dev/ptp0&quot;, O_RDWR); clkid = FD_TO_CLOCKID(fd); clock_gettime(clkid, &amp;ts);</p>
<h2>RETURN VALUE</h2>
<p> <code>clock_gettime</code>(), <code>clock_settime</code>(), and <code>clock_getres</code>() return 0 for success, or -1 for failure (in which case <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <code>clock_settime</code>() does not have write permission for the dynamic POSIX clock device indicated.</p>
<dt><code>EFAULT</code></p>
<dd> <i>tp</i> points outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>clockid</i> specified is invalid for one of two reasons. Either the System-V style hard coded positive value is out of range, or the dynamic clock ID does not refer to a valid instance of a clock object.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>clock_settime</code>()): <i>tp.tv_sec</i> is negative or <i>tp.tv_nsec</i> is outside the range [0..999,999,999].</p>
<dt><code>EINVAL</code></p>
<dd> The <i>clockid</i> specified in a call to <code>clock_settime</code>() is not a settable clock.</p>
<dt><code>EINVAL</code> (since Linux 4.3)</p>
<dd> A call to <code>clock_settime</code>() with a <i>clockid</i> of <code>CLOCK_REALTIME</code> attempted to set the time to a value less than the current value of the <code>CLOCK_MONOTONIC</code> clock.</p>
<dt><code>ENODEV</code></p>
<dd> The hot-pluggable device (like USB for example) represented by a dynamic <i>clk_id</i> has disappeared after its character device was opened.</p>
<dt><code>ENOTSUP</code></p>
<dd> The operation is not supported by the dynamic POSIX clock device specified.</p>
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
<p> POSIX.1-2001, POSIX.1-2008, SUSv2. </p>
<p> On POSIX systems on which these functions are available, the symbol <code>_POSIX_TIMERS</code> is defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. The symbols <code>_POSIX_MONOTONIC_CLOCK</code>, <code>_POSIX_CPUTIME</code>, <code>_POSIX_THREAD_CPUTIME</code> indicate that <code>CLOCK_MONOTONIC</code>, <code>CLOCK_PROCESS_CPUTIME_ID</code>, <code>CLOCK_THREAD_CPUTIME_ID</code> are available. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>NOTES</h2>
<p> POSIX.1 specifies the following:</p>
<dl>
<dt>
<dd>
<p> Setting the value of the <code>CLOCK_REALTIME</code> clock via <code>clock_settime</code>() shall have no effect on threads that are blocked waiting for a relative time service based upon this clock, including the <code>nanosleep</code>() function; nor on the expiration of relative timers based upon this clock. Consequently, these time services shall expire when the requested relative interval elapses, independently of the new or old value of the clock.</dl>
<p> According to POSIX.1-2001, a process with &quot;appropriate privileges&quot; may set the <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code> clocks using <code>clock_settime</code>(). On Linux, these clocks are not settable (i.e., no process has &quot;appropriate privileges&quot;).</p>
<h3>C library/kernel differences</h3>
<p> On some architectures, an implementation of <code>clock_gettime</code>() is provided in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<h3>Historical note for SMP systems</h3>
<p> Before Linux added kernel support for <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code>, glibc implemented these clocks on many platforms using timer registers from the CPUs (TSC on i386, AR.ITC on Itanium). These registers may differ between CPUs and as a consequence these clocks may return <code>bogus results</code> if a process is migrated to another CPU. </p>
<p> If the CPUs in an SMP system have different clock sources, then there is no way to maintain a correlation between the timer registers since each CPU will run at a slightly different frequency. If that is the case, then <i>clock_getcpuclockid(0)</i> will return <code>ENOENT</code> to signify this condition. The two clocks will then be useful only if it can be ensured that a process stays on a certain CPU. </p>
<p> The processors in an SMP system do not start all at exactly the same time and therefore the timer registers are typically running at an offset. Some architectures include code that attempts to limit these offsets on bootup. However, the code cannot guarantee to accurately tune the offsets. Glibc contains no provisions to deal with these offsets (unlike the Linux Kernel). Typically these offsets are small and therefore the effects may be negligible in most cases. </p>
<p> Since glibc 2.4, the wrapper functions for the system calls described in this page avoid the abovementioned problems by employing the kernel implementation of <code>CLOCK_PROCESS_CPUTIME_ID</code> and <code>CLOCK_THREAD_CPUTIME_ID</code>, on systems that provide such an implementation (i.e., Linux 2.6.12 and later).</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>clock_gettime</code>() and <code>clock_getres</code>() with various clocks. This is an example of what we might see when running the program: </p>
<p> $ <code>./clock_times x</code> CLOCK_REALTIME : 1585985459.446 (18356 days + 7h 30m 59s)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resolution:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000001 CLOCK_TAI : 1585985496.447 (18356 days + 7h 31m 36s)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resolution:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000001 CLOCK_MONOTONIC: 52395.722 (14h 33m 15s)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resolution:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000001 CLOCK_BOOTTIME : 72691.019 (20h 11m 31s)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resolution:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.000000001</p>
<h3>Program source</h3>
<p> /* clock_times.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later. */ #define _XOPEN_SOURCE 600 #include &lt;time.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdbool.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define SECS_IN_DAY (24 * 60 * 60) </p>
<p> static void displayClock(clockid_t clock, const char *name, bool showRes) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec ts; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_gettime(clock,&nbsp;&amp;ts)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;clock_gettime&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%-15s:&nbsp;%10jd.%03ld&nbsp;(&quot;, name,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;ts.tv_sec, ts.tv_nsec&nbsp;/&nbsp;1000000); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long days&nbsp;=&nbsp;ts.tv_sec&nbsp;/&nbsp;SECS_IN_DAY;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(days&nbsp;&gt;&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%ld days&nbsp;+&nbsp;&quot;, days); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%2dh&nbsp;%2dm&nbsp;%2ds&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(int)&nbsp;(ts.tv_sec&nbsp;%&nbsp;SECS_IN_DAY)&nbsp;/&nbsp;3600,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(int)&nbsp;(ts.tv_sec&nbsp;%&nbsp;3600)&nbsp;/&nbsp;60,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(int)&nbsp;ts.tv_sec&nbsp;%&nbsp;60);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;)
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_getres(clock,&nbsp;&amp;ts)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;clock_getres&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(showRes)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;resolution:&nbsp;%10jd.%09ld
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;ts.tv_sec, ts.tv_nsec); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool showRes&nbsp;=&nbsp;argc&nbsp;&gt;&nbsp;1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displayClock(CLOCK_REALTIME,&nbsp;&quot;CLOCK_REALTIME&quot;, showRes); #ifdef CLOCK_TAI<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displayClock(CLOCK_TAI,&nbsp;&quot;CLOCK_TAI&quot;, showRes); #endif<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displayClock(CLOCK_MONOTONIC,&nbsp;&quot;CLOCK_MONOTONIC&quot;, showRes); #ifdef CLOCK_BOOTTIME<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displayClock(CLOCK_BOOTTIME,&nbsp;&quot;CLOCK_BOOTTIME&quot;, showRes); #endif<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-adjtime/">adjtime</a></code>(3), <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/7-time_namespaces/">time_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
