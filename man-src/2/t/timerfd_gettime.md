---
title: "timerfd_gettime(2)"
name: "timerfd_gettime"
section: "2"
letter: "t"
url: "/docs/linux/man/2-timerfd_gettime/"
description: "timerfd_create, timerfd_settime, timerfd_gettime – timers that notify via file descriptors"
---

<h2 class="name">NAME</h2>
<p> timerfd_create, timerfd_settime, timerfd_gettime &#8211; timers that notify via file descriptors </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/timerfd.h&gt;
int timerfd_create(int clockid, int flags);
int timerfd_settime(int fd, int flags,
                    const struct itimerspec *new_value,
                    struct itimerspec *old_value);
int timerfd_gettime(int fd, struct itimerspec *curr_value);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These system calls create and operate on a timer that delivers timer expiration notifications via a file descriptor. They provide an alternative to the use of <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) or <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), with the advantage that the file descriptor may be monitored by <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). </p>
<p> The use of these three system calls is analogous to the use of <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), and <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2). (There is no analog of <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), since that functionality is provided by <code><a href="/docs/linux/man/2-read/">read</a></code>(2), as described below.)</p>
<h3>timerfd_create()</h3>
<p> <code>timerfd_create</code>() creates a new timer object, and returns a file descriptor that refers to that timer. The <i>clockid</i> argument specifies the clock that is used to mark the progress of the timer, and must be one of the following:</p>
<dl>
<dt><code>CLOCK_REALTIME</code></p>
<dd> A settable system-wide real-time clock.</p>
<dt><code>CLOCK_MONOTONIC</code></p>
<dd> A nonsettable monotonically increasing clock that measures time from some unspecified point in the past that does not change after system startup.</p>
<dt><code>CLOCK_BOOTTIME</code> (Since Linux 3.15)</p>
<dd> Like <code>CLOCK_MONOTONIC</code>, this is a monotonically increasing clock. However, whereas the <code>CLOCK_MONOTONIC</code> clock does not measure the time while a system is suspended, the <code>CLOCK_BOOTTIME</code> clock does include the time during which the system is suspended. This is useful for applications that need to be suspend-aware. <code>CLOCK_REALTIME</code> is not suitable for such applications, since that clock is affected by discontinuous changes to the system clock.</p>
<dt><code>CLOCK_REALTIME_ALARM</code> (since Linux 3.11)</p>
<dd> This clock is like <code>CLOCK_REALTIME</code>, but will wake the system if it is suspended. The caller must have the <code>CAP_WAKE_ALARM</code> capability in order to set a timer against this clock.</p>
<dt><code>CLOCK_BOOTTIME_ALARM</code> (since Linux 3.11)</p>
<dd> This clock is like <code>CLOCK_BOOTTIME</code>, but will wake the system if it is suspended. The caller must have the <code>CAP_WAKE_ALARM</code> capability in order to set a timer against this clock.</dl>
<p> See <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2) for some further details on the above clocks. </p>
<p> The current value of each of these clocks can be retrieved using <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2). </p>
<p> Starting with Linux 2.6.27, the following values may be bitwise ORed in <i>flags</i> to change the behavior of <code>timerfd_create</code>():</p>
<dl>
<dt><code>TFD_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>TFD_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<p> In Linux versions up to and including 2.6.26, <i>flags</i> must be specified as zero.</p>
<h3>timerfd_settime()</h3>
<p> <code>timerfd_settime</code>() arms (starts) or disarms (stops) the timer referred to by the file descriptor <i>fd</i>. </p>
<p> The <i>new_value</i> argument specifies the initial expiration and interval for the timer. The <i>itimerspec</i> structure used for this argument contains two fields, each of which is in turn a structure of type <i>timespec</i>: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Nanoseconds&nbsp;*/ }; </p>
<p> struct itimerspec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec it_interval;&nbsp;<wbr>&nbsp;/*&nbsp;Interval for periodic timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec it_value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initial expiration&nbsp;*/ }; </p>
<p> <i>new_value.it_value</i> specifies the initial expiration of the timer, in seconds and nanoseconds. Setting either field of <i>new_value.it_value</i> to a nonzero value arms the timer. Setting both fields of <i>new_value.it_value</i> to zero disarms the timer. </p>
<p> Setting one or both fields of <i>new_value.it_interval</i> to nonzero values specifies the period, in seconds and nanoseconds, for repeated timer expirations after the initial expiration. If both fields of <i>new_value.it_interval</i> are zero, the timer expires just once, at the time specified by <i>new_value.it_value</i>. </p>
<p> By default, the initial expiration time specified in <i>new_value</i> is interpreted relative to the current time on the timer&#8217;s clock at the time of the call (i.e., <i>new_value.it_value</i> specifies a time relative to the current value of the clock specified by <i>clockid</i>). An absolute timeout can be selected via the <i>flags</i> argument. </p>
<p> The <i>flags</i> argument is a bit mask that can include the following values:</p>
<dl>
<dt><code>TFD_TIMER_ABSTIME</code></p>
<dd> Interpret <i>new_value.it_value</i> as an absolute value on the timer&#8217;s clock. The timer will expire when the value of the timer&#8217;s clock reaches the value specified in <i>new_value.it_value</i>.</p>
<dt><code>TFD_TIMER_CANCEL_ON_SET</code></p>
<dd> If this flag is specified along with <code>TFD_TIMER_ABSTIME</code> and the clock for this timer is <code>CLOCK_REALTIME</code> or <code>CLOCK_REALTIME_ALARM</code>, then mark this timer as cancelable if the real-time clock undergoes a discontinuous change (<code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2), or similar). When such changes occur, a current or future <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the file descriptor will fail with the error <code>ECANCELED</code>.</dl>
<p> If the <i>old_value</i> argument is not NULL, then the <i>itimerspec</i> structure that it points to is used to return the setting of the timer that was current at the time of the call; see the description of <code>timerfd_gettime</code>() following.</p>
<h3>timerfd_gettime()</h3>
<p> <code>timerfd_gettime</code>() returns, in <i>curr_value</i>, an <i>itimerspec</i> structure that contains the current setting of the timer referred to by the file descriptor <i>fd</i>. </p>
<p> The <i>it_value</i> field returns the amount of time until the timer will next expire. If both fields of this structure are zero, then the timer is currently disarmed. This field always contains a relative value, regardless of whether the <code>TFD_TIMER_ABSTIME</code> flag was specified when setting the timer. </p>
<p> The <i>it_interval</i> field returns the interval of the timer. If both fields of this structure are zero, then the timer is set to expire just once, at the time specified by <i>curr_value.it_value</i>.</p>
<h3>Operating on a timer file descriptor</h3>
<p> The file descriptor returned by <code>timerfd_create</code>() supports the following additional operations:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If the timer has already expired one or more times since its settings were last modified using <code>timerfd_settime</code>(), or since the last successful <code><a href="/docs/linux/man/2-read/">read</a></code>(2), then the buffer given to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns an unsigned 8-byte integer (<i>uint64_t</i>) containing the number of expirations that have occurred. (The returned value is in host byte order&#8212;that is, the native byte order for integers on the host machine.)</p>
<dt>
<dd> If no timer expirations have occurred at the time of the <code><a href="/docs/linux/man/2-read/">read</a></code>(2), then the call either blocks until the next timer expiration, or fails with the error <code>EAGAIN</code> if the file descriptor has been made nonblocking (via the use of the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFL</code> operation to set the <code>O_NONBLOCK</code> flag).</p>
<dt>
<dd> A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>EINVAL</code> if the size of the supplied buffer is less than 8 bytes.</p>
<dt>
<dd> If the associated clock is either <code>CLOCK_REALTIME</code> or <code>CLOCK_REALTIME_ALARM</code>, the timer is absolute (<code>TFD_TIMER_ABSTIME</code>), and the flag <code>TFD_TIMER_CANCEL_ON_SET</code> was specified when calling <code>timerfd_settime</code>(), then <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>ECANCELED</code> if the real-time clock undergoes a discontinuous change. (This allows the reading application to discover such discontinuous changes to the clock.)</p>
<dt>
<dd> If the associated clock is either <code>CLOCK_REALTIME</code> or <code>CLOCK_REALTIME_ALARM</code>, the timer is absolute (<code>TFD_TIMER_ABSTIME</code>), and the flag <code>TFD_TIMER_CANCEL_ON_SET</code> was <i>not</i> specified when calling <code>timerfd_settime</code>(), then a discontinuous negative change to the clock (e.g., <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2)) may cause <code><a href="/docs/linux/man/2-read/">read</a></code>(2) to unblock, but return a value of 0 (i.e., no bytes read), if the clock change occurs after the time expired, but before the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) on the file descriptor.</p>
<dt><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2) (and similar)</p>
<dd> The file descriptor is readable (the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) <i>readfds</i> argument; the <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) <code>POLLIN</code> flag) if one or more timer expirations have occurred.</p>
<dt>
<dd> The file descriptor also supports the other file-descriptor multiplexing APIs: <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).</p>
<dt><code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<dd> The following timerfd-specific command is supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>TFD_IOC_SET_TICKS</code> (since Linux 3.17)</p>
<dd> Adjust the number of timer expirations that have occurred. The argument is a pointer to a nonzero 8-byte integer (<i>uint64_t</i>*) containing the new number of expirations. Once the number is set, any waiter on the timer is woken up. The only purpose of this command is to restore the expirations for the purpose of checkpoint/restore. This operation is available only if the kernel was configured with the <code>CONFIG_CHECKPOINT_RESTORE</code> option.</dl>
</dl>
<dt><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</p>
<dd> When the file descriptor is no longer required it should be closed. When all file descriptors associated with the same timer object have been closed, the timer is disarmed and its resources are freed by the kernel.</dl>
<h3><a href="/docs/linux/man/2-fork/">fork</a>(2) semantics</h3>
<p> After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child inherits a copy of the file descriptor created by <code>timerfd_create</code>(). The file descriptor refers to the same underlying timer object as the corresponding file descriptor in the parent, and <code><a href="/docs/linux/man/2-read/">read</a></code>(2)s in the child will return information about expirations of the timer.</p>
<h3><a href="/docs/linux/man/2-execve/">execve</a>(2) semantics</h3>
<p> A file descriptor created by <code>timerfd_create</code>() is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and continues to generate timer expirations if the timer was armed.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>timerfd_create</code>() returns a new file descriptor. On error, -1 is returned and <i>errno</i> is set to indicate the error. </p>
<p> <code>timerfd_settime</code>() and <code>timerfd_gettime</code>() return 0 on success; on error they return -1, and set <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<p> <code>timerfd_create</code>() can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>clockid</i> is not valid.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is invalid; or, in Linux 2.6.26 or earlier, <i>flags</i> is nonzero.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> Could not mount (internal) anonymous inode device.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient kernel memory to create the timer.</p>
<dt><code>EPERM</code></p>
<dd> <i>clockid</i> was <code>CLOCK_REALTIME_ALARM</code> or <code>CLOCK_BOOTTIME_ALARM</code> but the caller did not have the <code>CAP_WAKE_ALARM</code> capability.</dl>
<p> <code>timerfd_settime</code>() and <code>timerfd_gettime</code>() can fail with the following errors:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>new_value</i>, <i>old_value</i>, or <i>curr_value</i> is not valid a pointer.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is not a valid timerfd file descriptor.</dl>
<p> <code>timerfd_settime</code>() can also fail with the following errors:</p>
<dl>
<dt><code>ECANCELED</code></p>
<dd> See NOTES.</p>
<dt><code>EINVAL</code></p>
<dd> <i>new_value</i> is not properly initialized (one of the <i>tv_nsec</i> falls outside the range zero to 999,999,999).</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is invalid.</dl>
<h2>VERSIONS</h2>
<p> These system calls are available on Linux since kernel 2.6.25. Library support is provided by glibc since version 2.8.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> Suppose the following scenario for <code>CLOCK_REALTIME</code> or <code>CLOCK_REALTIME_ALARM</code> timer that was created with <code>timerfd_create</code>():</p>
<dl>
<dt>(a)</p>
<dd> The timer has been started (<code>timerfd_settime</code>()) with the <code>TFD_TIMER_ABSTIME</code> and <code>TFD_TIMER_CANCEL_ON_SET</code> flags;</p>
<dt>(b)</p>
<dd> A discontinuous change (e.g., <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2)) is subsequently made to the <code>CLOCK_REALTIME</code> clock; and</p>
<dt>(c)</p>
<dd> the caller once more calls <code>timerfd_settime</code>() to rearm the timer (without first doing a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) on the file descriptor).</dl>
<p> In this case the following occurs:</p>
<dl>
<dt>&bull;</p>
<dd> The <code>timerfd_settime</code>() returns -1 with <i>errno</i> set to <code>ECANCELED</code>. (This enables the caller to know that the previous timer was affected by a discontinuous change to the clock.)</p>
<dt>&bull;</p>
<dd> The timer <i>is successfully rearmed</i> with the settings provided in the second <code>timerfd_settime</code>() call. (This was probably an implementation accident, but won&#8217;t be fixed now, in case there are applications that depend on this behaviour.)</dl>
<h2>BUGS</h2>
<p> Currently, <code>timerfd_create</code>() supports fewer types of clock IDs than <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2).</p>
<h2>EXAMPLES</h2>
<p> The following program creates a timer and then monitors its progress. The program accepts up to three command-line arguments. The first argument specifies the number of seconds for the initial expiration of the timer. The second argument specifies the interval for the timer, in seconds. The third argument specifies the number of times the program should allow the timer to expire before terminating. The second and third command-line arguments are optional. </p>
<p> The following shell session demonstrates the use of the program: </p>
<p> $<code> a.out 3 1 100</code> 0.000: timer started 3.000: read: 1; total=1 4.000: read: 1; total=2 <code>haZ </code> # type control-Z to suspend the program [1]+ Stopped ./timerfd3_demo 3 1 100 $ <code>fg</code> # Resume execution after a few seconds a.out 3 1 100 9.660: read: 5; total=7 10.000: read: 1; total=8 11.000: read: 1; total=9 <code>haC </code> # type control-C to suspend the program</p>
<h3>Program source</h3>
<p> #include &lt;sys/timerfd.h&gt; #include &lt;time.h&gt; #include &lt;unistd.h&gt; #include &lt;inttypes.h&gt; /* Definition of PRIu64 */ #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;stdint.h&gt; /* Definition of uint64_t */ </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void print_elapsed_time(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static struct timespec start;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec curr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static int first_call&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int secs, nsecs; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(first_call)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first_call&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_gettime(CLOCK_MONOTONIC,&nbsp;&amp;start)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;clock_gettime&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_gettime(CLOCK_MONOTONIC,&nbsp;&amp;curr)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;clock_gettime&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;secs&nbsp;=&nbsp;curr.tv_sec &#8211; start.tv_sec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsecs&nbsp;=&nbsp;curr.tv_nsec &#8211; start.tv_nsec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nsecs&nbsp;&lt;&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;secs&#8211;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsecs&nbsp;+=&nbsp;1000000000;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d.%03d:&nbsp;&quot;, secs,&nbsp;(nsecs&nbsp;+&nbsp;500000)&nbsp;/&nbsp;1000000); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct itimerspec new_value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int max_exp, fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec now;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t exp, tot_exp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;((argc&nbsp;!=&nbsp;2)&nbsp;&amp;&amp;&nbsp;(argc&nbsp;!=&nbsp;4))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s init-secs&nbsp;[interval-secs max-exp]
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_gettime(CLOCK_REALTIME,&nbsp;&amp;now)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;clock_gettime&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a CLOCK_REALTIME absolute timer with initial<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expiration and interval as specified in command line&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_value.it_value.tv_sec&nbsp;=&nbsp;now.tv_sec&nbsp;+&nbsp;atoi(argv[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_value.it_value.tv_nsec&nbsp;=&nbsp;now.tv_nsec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;==&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_value.it_interval.tv_sec&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_exp&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_value.it_interval.tv_sec&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;max_exp&nbsp;=&nbsp;atoi(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_value.it_interval.tv_nsec&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;timerfd_create(CLOCK_REALTIME, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;timerfd_create&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(timerfd_settime(fd, TFD_TIMER_ABSTIME,&nbsp;&amp;new_value, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;timerfd_settime&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print_elapsed_time();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;timer started
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(tot_exp&nbsp;=&nbsp;0;&nbsp;tot_exp&nbsp;&lt;&nbsp;max_exp;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;read(fd,&nbsp;&amp;exp, sizeof(uint64_t));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;sizeof(uint64_t))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;read&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tot_exp&nbsp;+=&nbsp;exp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print_elapsed_time();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;read:&nbsp;%&quot;&nbsp;PRIu64&nbsp;&quot;;&nbsp;total=%&quot;&nbsp;PRIu64&nbsp;&quot;
&quot;, exp, tot_exp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
