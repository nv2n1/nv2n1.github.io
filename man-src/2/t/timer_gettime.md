---
title: "timer_gettime(2)"
name: "timer_gettime"
section: "2"
letter: "t"
url: "/docs/linux/man/2-timer_gettime/"
description: "timer_settime, timer_gettime – arm/disarm and fetch state of POSIX per-process timer"
---

<h2 class="name">NAME</h2>
<p> timer_settime, timer_gettime &#8211; arm/disarm and fetch state of POSIX per-process timer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;time.h&gt;
int timer_settime(timer_t timerid, int flags,
                  const struct itimerspec *new_value,
                  struct itimerspec *old_value);
int timer_gettime(timer_t timerid, struct itimerspec *curr_value);
</code></pre>
<p> Link with <i>-lrt</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>timer_settime</code>(), <code>timer_gettime</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>DESCRIPTION</h2>
<p> <code>timer_settime</code>() arms or disarms the timer identified by <i>timerid</i>. The <i>new_value</i> argument is pointer to an <i>itimerspec</i> structure that specifies the new initial value and the new interval for the timer. The <i>itimerspec</i> structure is defined as follows: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Nanoseconds&nbsp;*/ }; </p>
<p> struct itimerspec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec it_interval;&nbsp;<wbr>&nbsp;/*&nbsp;Timer interval&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec it_value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initial expiration&nbsp;*/ }; </p>
<p> Each of the substructures of the <i>itimerspec</i> structure is a <i>timespec</i> structure that allows a time value to be specified in seconds and nanoseconds. These time values are measured according to the clock that was specified when the timer was created by <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2). </p>
<p> If <i>new_value-&gt;it_value</i> specifies a nonzero value (i.e., either subfield is nonzero), then <code>timer_settime</code>() arms (starts) the timer, setting it to initially expire at the given time. (If the timer was already armed, then the previous settings are overwritten.) If <i>new_value-&gt;it_value</i> specifies a zero value (i.e., both subfields are zero), then the timer is disarmed. </p>
<p> The <i>new_value-&gt;it_interval</i> field specifies the period of the timer, in seconds and nanoseconds. If this field is nonzero, then each time that an armed timer expires, the timer is reloaded from the value specified in <i>new_value-&gt;it_interval</i>. If <i>new_value-&gt;it_interval</i> specifies a zero value, then the timer expires just once, at the time specified by <i>it_value</i>. </p>
<p> By default, the initial expiration time specified in <i>new_value-&gt;it_value</i> is interpreted relative to the current time on the timer&#8217;s clock at the time of the call. This can be modified by specifying <code>TIMER_ABSTIME</code> in <i>flags</i>, in which case <i>new_value-&gt;it_value</i> is interpreted as an absolute value as measured on the timer&#8217;s clock; that is, the timer will expire when the clock value reaches the value specified by <i>new_value-&gt;it_value</i>. If the specified absolute time has already passed, then the timer expires immediately, and the overrun count (see <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2)) will be set correctly. </p>
<p> If the value of the <code>CLOCK_REALTIME</code> clock is adjusted while an absolute timer based on that clock is armed, then the expiration of the timer will be appropriately adjusted. Adjustments to the <code>CLOCK_REALTIME</code> clock have no effect on relative timers based on that clock. </p>
<p> If <i>old_value</i> is not NULL, then it points to a buffer that is used to return the previous interval of the timer (in <i>old_value-&gt;it_interval</i>) and the amount of time until the timer would previously have next expired (in <i>old_value-&gt;it_value</i>). </p>
<p> <code>timer_gettime</code>() returns the time until next expiration, and the interval, for the timer specified by <i>timerid</i>, in the buffer pointed to by <i>curr_value</i>. The time remaining until the next timer expiration is returned in <i>curr_value-&gt;it_value</i>; this is always a relative value, regardless of whether the <code>TIMER_ABSTIME</code> flag was used when arming the timer. If the value returned in <i>curr_value-&gt;it_value</i> is zero, then the timer is currently disarmed. The timer interval is returned in <i>curr_value-&gt;it_interval</i>. If the value returned in <i>curr_value-&gt;it_interval</i> is zero, then this is a &quot;one-shot&quot; timer.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>timer_settime</code>() and <code>timer_gettime</code>() return 0. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> These functions may fail with the following errors:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>new_value</i>, <i>old_value</i>, or <i>curr_value</i> is not a valid pointer.</p>
<dt><code>EINVAL</code></p>
<dd> <i>timerid</i> is invalid.</dl>
<p> <code>timer_settime</code>() may fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>new_value.it_value</i> is negative; or <i>new_value.it_value.tv_nsec</i> is negative or greater than 999,999,999.</dl>
<h2>VERSIONS</h2>
<p> These system calls are available since Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
