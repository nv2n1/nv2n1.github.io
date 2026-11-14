---
title: "timer_create(2)"
name: "timer_create"
section: "2"
letter: "t"
url: "/docs/linux/man/2-timer_create/"
description: "timer_create – create a POSIX per-process timer"
---

<h2 class="name">NAME</h2>
<p> timer_create &#8211; create a POSIX per-process timer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;signal.h&gt;
#include &lt;time.h&gt;
int timer_create(clockid_t clockid, struct sigevent *sevp,
                 timer_t *timerid);
</code></pre>
<p> Link with <i>-lrt</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>timer_create</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>DESCRIPTION</h2>
<p> <code>timer_create</code>() creates a new per-process interval timer. The ID of the new timer is returned in the buffer pointed to by <i>timerid</i>, which must be a non-null pointer. This ID is unique within the process, until the timer is deleted. The new timer is initially disarmed. </p>
<p> The <i>clockid</i> argument specifies the clock that the new timer uses to measure time. It can be specified as one of the following values:</p>
<dl>
<dt><code>CLOCK_REALTIME</code></p>
<dd> A settable system-wide real-time clock.</p>
<dt><code>CLOCK_MONOTONIC</code></p>
<dd> A nonsettable monotonically increasing clock that measures time from some unspecified point in the past that does not change after system startup.</p>
<dt><code>CLOCK_PROCESS_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> A clock that measures (user and system) CPU time consumed by (all of the threads in) the calling process.</p>
<dt><code>CLOCK_THREAD_CPUTIME_ID</code> (since Linux 2.6.12)</p>
<dd> A clock that measures (user and system) CPU time consumed by the calling thread.</p>
<dt><code>CLOCK_BOOTTIME</code> (Since Linux 2.6.39)</p>
<dd> Like <code>CLOCK_MONOTONIC</code>, this is a monotonically increasing clock. However, whereas the <code>CLOCK_MONOTONIC</code> clock does not measure the time while a system is suspended, the <code>CLOCK_BOOTTIME</code> clock does include the time during which the system is suspended. This is useful for applications that need to be suspend-aware. <code>CLOCK_REALTIME</code> is not suitable for such applications, since that clock is affected by discontinuous changes to the system clock.</p>
<dt><code>CLOCK_REALTIME_ALARM</code> (since Linux 3.0)</p>
<dd> This clock is like <code>CLOCK_REALTIME</code>, but will wake the system if it is suspended. The caller must have the <code>CAP_WAKE_ALARM</code> capability in order to set a timer against this clock.</p>
<dt><code>CLOCK_BOOTTIME_ALARM</code> (since Linux 3.0)</p>
<dd> This clock is like <code>CLOCK_BOOTTIME</code>, but will wake the system if it is suspended. The caller must have the <code>CAP_WAKE_ALARM</code> capability in order to set a timer against this clock.</p>
<dt><code>CLOCK_TAI</code> (since Linux 3.10)</p>
<dd> A system-wide clock derived from wall-clock time but ignoring leap seconds.</dl>
<p> See <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2) for some further details on the above clocks. </p>
<p> As well as the above values, <i>clockid</i> can be specified as the <i>clockid</i> returned by a call to <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3) or <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3). </p>
<p> The <i>sevp</i> argument points to a <i>sigevent</i> structure that specifies how the caller should be notified when the timer expires. For the definition and general details of this structure, see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7). </p>
<p> The <i>sevp.sigev_notify</i> field can have the following values:</p>
<dl>
<dt><code>SIGEV_NONE</code></p>
<dd> Don&#8217;t asynchronously notify when the timer expires. Progress of the timer can be monitored using <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2).</p>
<dt><code>SIGEV_SIGNAL</code></p>
<dd> Upon timer expiration, generate the signal <i>sigev_signo</i> for the process. See <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for general details. The <i>si_code</i> field of the <i>siginfo_t</i> structure will be set to <code>SI_TIMER</code>. At any point in time, at most one signal is queued to the process for a given timer; see <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2) for more details.</p>
<dt><code>SIGEV_THREAD</code></p>
<dd> Upon timer expiration, invoke <i>sigev_notify_function</i> as if it were the start function of a new thread. See <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for details.</p>
<dt><code>SIGEV_THREAD_ID</code> (Linux-specific)</p>
<dd> As for <code>SIGEV_SIGNAL</code>, but the signal is targeted at the thread whose ID is given in <i>sigev_notify_thread_id</i>, which must be a thread in the same process as the caller. The <i>sigev_notify_thread_id</i> field specifies a kernel thread ID, that is, the value returned by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2). This flag is intended only for use by threading libraries.</dl>
<p> Specifying <i>sevp</i> as NULL is equivalent to specifying a pointer to a <i>sigevent</i> structure in which <i>sigev_notify</i> is <code>SIGEV_SIGNAL</code>, <i>sigev_signo</i> is <code>SIGALRM</code>, and <i>sigev_value.sival_int</i> is the timer ID.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>timer_create</code>() returns 0, and the ID of the new timer is placed in <i>*timerid</i>. On failure, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Temporary error during kernel allocation of timer structures.</p>
<dt><code>EINVAL</code></p>
<dd> Clock ID, <i>sigev_notify</i>, <i>sigev_signo</i>, or <i>sigev_notify_thread_id</i> is invalid.</p>
<dt><code>ENOMEM</code></p>
<dd> Could not allocate memory.</p>
<dt><code>ENOTSUP</code></p>
<dd> The kernel does not support creating a timer against this <i>clockid</i>.</p>
<dt><code>EPERM</code></p>
<dd> <i>clockid</i> was <code>CLOCK_REALTIME_ALARM</code> or <code>CLOCK_BOOTTIME_ALARM</code> but the caller did not have the <code>CAP_WAKE_ALARM</code> capability.</dl>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> A program may create multiple interval timers using <code>timer_create</code>(). </p>
<p> Timers are not inherited by the child of a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), and are disarmed and deleted during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The kernel preallocates a &quot;queued real-time signal&quot; for each timer created using <code>timer_create</code>(). Consequently, the number of timers is limited by the <code>RLIMIT_SIGPENDING</code> resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)). </p>
<p> The timers created by <code>timer_create</code>() are commonly known as &quot;POSIX (interval) timers&quot;. The POSIX timers API consists of the following interfaces:</p>
<dl>
<dt>*</p>
<dd> <code>timer_create</code>(): Create a timer.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2): Arm (start) or disarm (stop) a timer.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-timer_gettime/">timer_gettime</a></code>(2): Fetch the time remaining until the next expiration of a timer, along with the interval setting of the timer.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2): Return the overrun count for the last timer expiration.</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2): Disarm and delete a timer.</dl>
<p> Since Linux 3.10, the <i>/proc/[pid]/timers</i> file can be used to list the POSIX timers for the process with PID <i>pid</i>. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further information. </p>
<p> Since Linux 4.10, support for POSIX timers is a configurable option that is enabled by default. Kernel support can be disabled via the <code>CONFIG_POSIX_TIMERS</code> option.</p>
<h3>C library/kernel differences</h3>
<p> Part of the implementation of the POSIX timers API is provided by glibc. In particular:</p>
<dl>
<dt>*</p>
<dd> Much of the functionality for <code>SIGEV_THREAD</code> is implemented within glibc, rather than the kernel. (This is necessarily so, since the thread involved in handling the notification is one that must be managed by the C library POSIX threads implementation.) Although the notification delivered to the process is via a thread, internally the NPTL implementation uses a <i>sigev_notify</i> value of <code>SIGEV_THREAD_ID</code> along with a real-time signal that is reserved by the implementation (see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7)).</p>
<dt>*</p>
<dd> The implementation of the default case where <i>evp</i> is NULL is handled inside glibc, which invokes the underlying system call with a suitably populated <i>sigevent</i> structure.</p>
<dt>*</p>
<dd> The timer IDs presented at user level are maintained by glibc, which maps these IDs to the timer IDs employed by the kernel.</dl>
<p> The POSIX timers system calls first appeared in Linux 2.6. Prior to this, glibc provided an incomplete user-space implementation (<code>CLOCK_REALTIME</code> timers only) using POSIX threads, and in glibc versions before 2.17, the implementation falls back to this technique on systems running pre-2.6 Linux kernels.</p>
<h2>EXAMPLES</h2>
<p> The program below takes two arguments: a sleep period in seconds, and a timer frequency in nanoseconds. The program establishes a handler for the signal it uses for the timer, blocks that signal, creates and arms a timer that expires with the given frequency, sleeps for the specified number of seconds, and then unblocks the timer signal. Assuming that the timer expired at least once while the program slept, the signal handler will be invoked, and the handler displays some information about the timer notification. The program terminates after one invocation of the signal handler. </p>
<p> In the following example run, the program sleeps for 1 second, after creating a timer that has a frequency of 100 nanoseconds. By the time the signal is unblocked and delivered, there have been around ten million overruns. </p>
<p> $ <code>./a.out 1 100</code> Establishing handler for signal 34 Blocking signal 34 timer ID is 0x804c008 Sleeping for 1 seconds Unblocking signal 34 Caught signal 34<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sival_ptr&nbsp;=&nbsp;0xbfb174f4;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*sival_ptr&nbsp;=&nbsp;0x804c008<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overrun count&nbsp;=&nbsp;10004886</p>
<h3>Program source</h3>
<p> #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; #include &lt;signal.h&gt; #include &lt;time.h&gt; </p>
<p> #define CLOCKID CLOCK_REALTIME #define SIG SIGRTMIN </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void print_siginfo(siginfo_t *si) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timer_t&nbsp;*tidp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int or; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tidp&nbsp;=&nbsp;si-&gt;si_value.sival_ptr; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sival_ptr&nbsp;=&nbsp;%p;&nbsp;&quot;, si-&gt;si_value.sival_ptr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*sival_ptr&nbsp;=&nbsp;%#jx
&quot;,&nbsp;(uintmax_t)&nbsp;*tidp); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;or&nbsp;=&nbsp;timer_getoverrun(*tidp);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(or&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;timer_getoverrun&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overrun count&nbsp;=&nbsp;%d
&quot;, or); } </p>
<p> static void handler(int sig, siginfo_t *si, void *uc) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Note: calling printf()&nbsp;from a signal handler is not safe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(and should not be done in production programs), since<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf()&nbsp;is not async-signal-safe;&nbsp;see&nbsp;<a href="/docs/linux/man/7-signal-safety/">signal-safety</a>(7).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Nevertheless, we use printf()&nbsp;here as a simple way of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;showing that the handler was called.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Caught signal&nbsp;%d
&quot;, sig);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;print_siginfo(si);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;signal(sig, SIG_IGN); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timer_t timerid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigevent sev;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct itimerspec its;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long long freq_nanosecs;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigset_t mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigaction sa; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;sleep-secs&gt;&nbsp;&lt;freq-nanosecs&gt;
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Establish handler for timer signal&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Establishing handler for signal&nbsp;%d
&quot;, SIG);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa.sa_flags&nbsp;=&nbsp;SA_SIGINFO;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa.sa_sigaction&nbsp;=&nbsp;handler;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigemptyset(&amp;sa.sa_mask);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sigaction(SIG,&nbsp;&amp;sa, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sigaction&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Block timer signal temporarily&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Blocking signal&nbsp;%d
&quot;, SIG);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigemptyset(&amp;mask);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigaddset(&amp;mask, SIG);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sigprocmask(SIG_SETMASK,&nbsp;&amp;mask, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sigprocmask&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create the timer&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_notify&nbsp;=&nbsp;SIGEV_SIGNAL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_signo&nbsp;=&nbsp;SIG;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_value.sival_ptr&nbsp;=&nbsp;&amp;timerid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(timer_create(CLOCKID,&nbsp;&amp;sev,&nbsp;&amp;timerid)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;timer_create&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;timer ID is&nbsp;%#jx
&quot;,&nbsp;(uintmax_t)&nbsp;timerid); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Start the timer&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freq_nanosecs&nbsp;=&nbsp;atoll(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;its.it_value.tv_sec&nbsp;=&nbsp;freq_nanosecs&nbsp;/&nbsp;1000000000;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;its.it_value.tv_nsec&nbsp;=&nbsp;freq_nanosecs&nbsp;%&nbsp;1000000000;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;its.it_interval.tv_sec&nbsp;=&nbsp;its.it_value.tv_sec;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;its.it_interval.tv_nsec&nbsp;=&nbsp;its.it_value.tv_nsec; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(timer_settime(timerid, 0,&nbsp;&amp;its, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;timer_settime&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sleep for a while;&nbsp;meanwhile, the timer may expire<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multiple times&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Sleeping for&nbsp;%d seconds
&quot;, atoi(argv[1]));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sleep(atoi(argv[1])); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unlock the timer signal, so that timer notification<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;can be delivered&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Unblocking signal&nbsp;%d
&quot;, SIG);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sigprocmask(SIG_UNBLOCK,&nbsp;&amp;mask, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sigprocmask&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-timer_delete/">timer_delete</a></code>(2), <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2), <code><a href="/docs/linux/man/2-timer_settime/">timer_settime</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
