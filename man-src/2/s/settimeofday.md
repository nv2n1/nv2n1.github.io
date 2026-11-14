---
title: "settimeofday(2)"
name: "settimeofday"
section: "2"
letter: "s"
url: "/docs/linux/man/2-settimeofday/"
description: "gettimeofday, settimeofday – get / set time"
---

<h2 class="name">NAME</h2>
<p> gettimeofday, settimeofday &#8211; get / set time </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/time.h&gt;
int gettimeofday(struct timeval *tv, struct timezone *tz);
int settimeofday(const struct timeval *tv, const struct timezone *tz);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>settimeofday</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The functions <code>gettimeofday</code>() and <code>settimeofday</code>() can get and set the time as well as a timezone. </p>
<p> The <i>tv</i> argument is a <i>struct timeval</i> (as specified in <i>&lt;sys/time.h&gt;</i>): </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;microseconds&nbsp;*/ }; </p>
<p> and gives the number of seconds and microseconds since the Epoch (see <code><a href="/docs/linux/man/2-time/">time</a></code>(2)). </p>
<p> The <i>tz</i> argument is a <i>struct timezone</i>: </p>
<p> struct timezone {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tz_minuteswest;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;minutes west of Greenwich&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tz_dsttime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;type of DST correction&nbsp;*/ }; </p>
<p> If either <i>tv</i> or <i>tz</i> is NULL, the corresponding structure is not set or returned. (However, compilation warnings will result if <i>tv</i> is NULL.) </p>
<p> The use of the <i>timezone</i> structure is obsolete; the <i>tz</i> argument should normally be specified as NULL. (See NOTES below.) </p>
<p> Under Linux, there are some peculiar &quot;warp clock&quot; semantics associated with the <code>settimeofday</code>() system call if on the very first call (after booting) that has a non-NULL <i>tz</i> argument, the <i>tv</i> argument is NULL and the <i>tz_minuteswest</i> field is nonzero. (The <i>tz_dsttime</i> field should be zero for this case.) In such a case it is assumed that the CMOS clock is on local time, and that it has to be incremented by this amount to get UTC system time. No doubt it is a bad idea to use this feature.</p>
<h2>RETURN VALUE</h2>
<p> <code>gettimeofday</code>() and <code>settimeofday</code>() return 0 for success, or -1 for failure (in which case <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> One of <i>tv</i> or <i>tz</i> pointed outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>settimeofday</code>()): <i>timezone</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>settimeofday</code>()): <i>tv.tv_sec</i> is negative or <i>tv.tv_usec</i> is outside the range [0..999,999].</p>
<dt><code>EINVAL</code> (since Linux 4.3)</p>
<dd> (<code>settimeofday</code>()): An attempt was made to set the time to a value less than the current value of the <code>CLOCK_MONOTONIC</code> clock (see <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)).</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege to call <code>settimeofday</code>(); under Linux the <code>CAP_SYS_TIME</code> capability is required.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD. POSIX.1-2001 describes <code>gettimeofday</code>() but not <code>settimeofday</code>(). POSIX.1-2008 marks <code>gettimeofday</code>() as obsolete, recommending the use of <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) instead.</p>
<h2>NOTES</h2>
<p> The time returned by <code>gettimeofday</code>() <i>is</i> affected by discontinuous jumps in the system time (e.g., if the system administrator manually changes the system time). If you need a monotonically increasing clock, see <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2). </p>
<p> Macros for operating on <i>timeval</i> structures are described in <code><a href="/docs/linux/man/3-timeradd/">timeradd</a></code>(3). </p>
<p> Traditionally, the fields of <i>struct timeval</i> were of type <i>long</i>.</p>
<h3>C library/kernel differences</h3>
<p> On some architectures, an implementation of <code>gettimeofday</code>() is provided in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<h3>The tz_dsttime field</h3>
<p> On a non-Linux kernel, with glibc, the <i>tz_dsttime</i> field of <i>struct timezone</i> will be set to a nonzero value by <code>gettimeofday</code>() if the current timezone has ever had or will have a daylight saving rule applied. In this sense it exactly mirrors the meaning of <code><a href="/docs/linux/man/3-daylight/">daylight</a></code>(3) for the current zone. On Linux, with glibc, the setting of the <i>tz_dsttime</i> field of <i>struct timezone</i> has never been used by <code>settimeofday</code>() or <code>gettimeofday</code>(). Thus, the following is purely of historical interest. </p>
<p> On old systems, the field <i>tz_dsttime</i> contains a symbolic constant (values are given below) that indicates in which part of the year Daylight Saving Time is in force. (Note: this value is constant throughout the year: it does not indicate that DST is in force, it just selects an algorithm.) The daylight saving time algorithms defined are as follows: </p>
<p> <code>DST_NONE</code> /* not on DST */ <code>DST_USA</code> /* USA style DST */ <code>DST_AUST</code> /* Australian style DST */ <code>DST_WET</code> /* Western European DST */ <code>DST_MET</code> /* Middle European DST */ <code>DST_EET</code> /* Eastern European DST */ <code>DST_CAN</code> /* Canada */ <code>DST_GB</code> /* Great Britain and Eire */ <code>DST_RUM</code> /* Romania */ <code>DST_TUR</code> /* Turkey */ <code>DST_AUSTALT</code> /* Australian style with shift in 1986 */ </p>
<p> Of course it turned out that the period in which Daylight Saving Time is in force cannot be given by a simple algorithm, one per country; indeed, this period is determined by unpredictable political decisions. So this method of representing timezones has been abandoned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/3-timeradd/">timeradd</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
