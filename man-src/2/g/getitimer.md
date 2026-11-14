---
title: "getitimer(2)"
name: "getitimer"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getitimer/"
description: "getitimer, setitimer – get or set value of an interval timer"
---

<h2 class="name">NAME</h2>
<p> getitimer, setitimer &#8211; get or set value of an interval timer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/time.h&gt;
int getitimer(int which, struct itimerval *curr_value);
int setitimer(int which, const struct itimerval *new_value,
              struct itimerval *old_value);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These system calls provide access to interval timers, that is, timers that initially expire at some point in the future, and (optionally) at regular intervals after that. When a timer expires, a signal is generated for the calling process, and the timer is reset to the specified interval (if the interval is nonzero). </p>
<p> Three types of timers&#8212;specified via the <i>which</i> argument&#8212;are provided, each of which counts against a different clock and generates a different signal on timer expiration:</p>
<dl>
<dt><code>ITIMER_REAL</code></p>
<dd> This timer counts down in real (i.e., wall clock) time. At each expiration, a <code>SIGALRM</code> signal is generated.</p>
<dt><code>ITIMER_VIRTUAL</code></p>
<dd> This timer counts down against the user-mode CPU time consumed by the process. (The measurement includes CPU time consumed by all threads in the process.) At each expiration, a <code>SIGVTALRM</code> signal is generated.</p>
<dt><code>ITIMER_PROF</code></p>
<dd> This timer counts down against the total (i.e., both user and system) CPU time consumed by the process. (The measurement includes CPU time consumed by all threads in the process.) At each expiration, a <code>SIGPROF</code> signal is generated.</p>
<dt>
<dd> In conjunction with <code>ITIMER_VIRTUAL</code>, this timer can be used to profile user and system CPU time consumed by the process.</dl>
<p> A process has only one of each of the three types of timers. </p>
<p> Timer values are defined by the following structures: </p>
<p> struct itimerval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timeval it_interval;&nbsp;/*&nbsp;Interval for periodic timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timeval it_value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Time until next expiration&nbsp;*/ }; </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;microseconds&nbsp;*/ };</p>
<h3>getitimer()</h3>
<p> The function <code>getitimer</code>() places the current value of the timer specified by <i>which</i> in the buffer pointed to by <i>curr_value</i>. </p>
<p> The <i>it_value</i> substructure is populated with the amount of time remaining until the next expiration of the specified timer. This value changes as the timer counts down, and will be reset to <i>it_interval</i> when the timer expires. If both fields of <i>it_value</i> are zero, then this timer is currently disarmed (inactive). </p>
<p> The <i>it_interval</i> substructure is populated with the timer interval. If both fields of <i>it_interval</i> are zero, then this is a single-shot timer (i.e., it expires just once).</p>
<h3>setitimer()</h3>
<p> The function <code>setitimer</code>() arms or disarms the timer specified by <i>which</i>, by setting the timer to the value specified by <i>new_value</i>. If <i>old_value</i> is non-NULL, the buffer it points to is used to return the previous value of the timer (i.e., the same information that is returned by <code>getitimer</code>()). </p>
<p> If either field in <i>new_value.it_value</i> is nonzero, then the timer is armed to initially expire at the specified time. If both fields in <i>new_value.it_value</i> are zero, then the timer is disarmed. </p>
<p> The <i>new_value.it_interval</i> field specifies the new interval for the timer; if both of its subfields are zero, the timer is single-shot.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>new_value</i>, <i>old_value</i>, or <i>curr_value</i> is not valid a pointer.</p>
<dt><code>EINVAL</code></p>
<dd> <i>which</i> is not one of <code>ITIMER_REAL</code>, <code>ITIMER_VIRTUAL</code>, or <code>ITIMER_PROF</code>; or (since Linux 2.6.22) one of the <i>tv_usec</i> fields in the structure pointed to by <i>new_value</i> contains a value outside the range 0 to 999999.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, SVr4, 4.4BSD (this call first appeared in 4.2BSD). POSIX.1-2008 marks <code>getitimer</code>() and <code>setitimer</code>() obsolete, recommending the use of the POSIX timers API (<code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), etc.) instead.</p>
<h2>NOTES</h2>
<p> Timers will never expire before the requested time, but may expire some (short) time afterward, which depends on the system timer resolution and on the system load; see <code><a href="/docs/linux/man/7-time/">time</a></code>(7). (But see BUGS below.) If the timer expires while the process is active (always true for <code>ITIMER_VIRTUAL</code>), the signal will be delivered immediately when generated. </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) does not inherit its parent&#8217;s interval timers. Interval timers are preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> POSIX.1 leaves the interaction between <code>setitimer</code>() and the three interfaces <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), and <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3) unspecified. </p>
<p> The standards are silent on the meaning of the call: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setitimer(which, NULL,&nbsp;&amp;old_value); </p>
<p> Many systems (Solaris, the BSDs, and perhaps others) treat this as equivalent to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getitimer(which,&nbsp;&amp;old_value); </p>
<p> In Linux, this is treated as being equivalent to a call in which the <i>new_value</i> fields are zero; that is, the timer is disabled. <i>Don&#8217;t use this Linux misfeature</i>: it is nonportable and unnecessary.</p>
<h2>BUGS</h2>
<p> The generation and delivery of a signal are distinct, and only one instance of each of the signals listed above may be pending for a process. Under very heavy loading, an <code>ITIMER_REAL</code> timer may expire before the signal from a previous expiration has been delivered. The second signal in such an event will be lost. </p>
<p> On Linux kernels before 2.6.16, timer values are represented in jiffies. If a request is made set a timer with a value whose jiffies representation exceeds <code>MAX_SEC_IN_JIFFIES</code> (defined in <i>include/linux/jiffies.h</i>), then the timer is silently truncated to this ceiling value. On Linux/i386 (where, since Linux 2.6.13, the default jiffy is 0.004 seconds), this means that the ceiling value for a timer is approximately 99.42 days. Since Linux 2.6.16, the kernel uses a different internal representation for times, and this ceiling is removed. </p>
<p> On certain systems (including i386), Linux kernels before version 2.6.12 have a bug which will produce premature timer expirations of up to one jiffy under some circumstances. This bug is fixed in kernel 2.6.12. </p>
<p> POSIX.1-2001 says that <code>setitimer</code>() should fail if a <i>tv_usec</i> value is specified that is outside of the range 0 to 999999. However, in kernels up to and including 2.6.21, Linux does not give an error, but instead silently adjusts the corresponding seconds value for the timer. From kernel 2.6.22 onward, this nonconformance has been repaired: an improper <i>tv_usec</i> value results in an <code>EINVAL</code> error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
