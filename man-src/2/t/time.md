---
title: "time(2)"
name: "time"
section: "2"
letter: "t"
url: "/docs/linux/man/2-time/"
description: "time – get time in seconds"
---

<h2 class="name">NAME</h2>
<p> time &#8211; get time in seconds </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>time_t time(time_t *</code><i>tloc</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>time</code>() returns the time as the number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). </p>
<p> If <i>tloc</i> is non-NULL, the return value is also stored in the memory pointed to by <i>tloc</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, the value of time in seconds since the Epoch is returned. On error, <i>((time_t)&nbsp;-1)</i> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>tloc</i> points outside your accessible address space (but see BUGS).</p>
<dt>
<dd> On systems where the C library <code>time</code>() wrapper function invokes an implementation provided by the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7) (so that there is no trap into the kernel), an invalid address may instead trigger a <code>SIGSEGV</code> signal.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD, C89, C99, POSIX.1-2001. POSIX does not specify any error conditions.</p>
<h2>NOTES</h2>
<p> POSIX.1 defines <i>seconds since the Epoch</i> using a formula that approximates the number of seconds between a specified time and the Epoch. This formula takes account of the facts that all years that are evenly divisible by 4 are leap years, but years that are evenly divisible by 100 are not leap years unless they are also evenly divisible by 400, in which case they are leap years. This value is not the same as the actual number of seconds between the time and the Epoch, because of leap seconds and because system clocks are not required to be synchronized to a standard reference. The intention is that the interpretation of seconds since the Epoch values be consistent; see POSIX.1-2008 Rationale A.4.15 for further rationale. </p>
<p> On Linux, a call to <code>time</code>() with <i>tloc</i> specified as NULL cannot fail with the error <code>EOVERFLOW</code>, even on ABIs where <i>time_t</i> is a signed 32-bit integer and the clock ticks past the time 2**31 (2038-01-19 03:14:08 UTC, ignoring leap seconds). (POSIX.1 permits, but does not require, the <code>EOVERFLOW</code> error in the case where the seconds since the Epoch will not fit in <i>time_t</i>.) Instead, the behavior on Linux is undefined when the system time is out of the <i>time_t</i> range. Applications intended to run after 2038 should use ABIs with <i>time_t</i> wider than 32 bits.</p>
<h2>BUGS</h2>
<p> Error returns from this system call are indistinguishable from successful reports that the time is a few seconds <i>before</i> the Epoch, so the C library wrapper function never sets <i>errno</i> as a result of this call. </p>
<p> The <i>tloc</i> argument is obsolescent and should always be NULL in new code. When <i>tloc</i> is NULL, the call cannot fail.</p>
<h3>C library/kernel differences</h3>
<p> On some architectures, an implementation of <code>time</code>() is provided in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-ftime/">ftime</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
