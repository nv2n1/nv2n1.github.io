---
title: "sigwaitinfo(2)"
name: "sigwaitinfo"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sigwaitinfo/"
description: "sigwaitinfo, sigtimedwait, rt_sigtimedwait – synchronously wait for queued signals"
---

<h2 class="name">NAME</h2>
<p> sigwaitinfo, sigtimedwait, rt_sigtimedwait &#8211; synchronously wait for queued signals </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;signal.h&gt;
int sigwaitinfo(const sigset_t *set, siginfo_t *info);
int sigtimedwait(const sigset_t *set, siginfo_t *info,
                 const struct timespec *timeout);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sigwaitinfo</code>(), <code>sigtimedwait</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>DESCRIPTION</h2>
<p> <code>sigwaitinfo</code>() suspends execution of the calling thread until one of the signals in <i>set</i> is pending (If one of the signals in <i>set</i> is already pending for the calling thread, <code>sigwaitinfo</code>() will return immediately.) </p>
<p> <code>sigwaitinfo</code>() removes the signal from the set of pending signals and returns the signal number as its function result. If the <i>info</i> argument is not NULL, then the buffer that it points to is used to return a structure of type <i>siginfo_t</i> (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) containing information about the signal. </p>
<p> If multiple signals in <i>set</i> are pending for the caller, the signal that is retrieved by <code>sigwaitinfo</code>() is determined according to the usual ordering rules; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for further details. </p>
<p> <code>sigtimedwait</code>() operates in exactly the same way as <code>sigwaitinfo</code>() except that it has an additional argument, <i>timeout</i>, which specifies the interval for which the thread is suspended waiting for a signal. (This interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the interval may overrun by a small amount.) This argument is of the following type: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ } </p>
<p> If both fields of this structure are specified as 0, a poll is performed: <code>sigtimedwait</code>() returns immediately, either with information about a signal that was pending for the caller, or with an error if none of the signals in <i>set</i> was pending.</p>
<h2>RETURN VALUE</h2>
<p> On success, both <code>sigwaitinfo</code>() and <code>sigtimedwait</code>() return a signal number (i.e., a value greater than zero). On failure both calls return -1, with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> No signal in <i>set</i> was became pending within the <i>timeout</i> period specified to <code>sigtimedwait</code>().</p>
<dt><code>EINTR</code></p>
<dd> The wait was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). (This handler was for a signal other than one of those in <i>set</i>.)</p>
<dt><code>EINVAL</code></p>
<dd> <i>timeout</i> was invalid.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> In normal usage, the calling program blocks the signals in <i>set</i> via a prior call to <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) (so that the default disposition for these signals does not occur if they become pending between successive calls to <code>sigwaitinfo</code>() or <code>sigtimedwait</code>()) and does not establish handlers for these signals. In a multithreaded program, the signal should be blocked in all threads, in order to prevent the signal being treated according to its default disposition in a thread other than the one calling <code>sigwaitinfo</code>() or <code>sigtimedwait</code>()). </p>
<p> The set of signals that is pending for a given thread is the union of the set of signals that is pending specifically for that thread and the set of signals that is pending for the process as a whole (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). </p>
<p> Attempts to wait for <code>SIGKILL</code> and <code>SIGSTOP</code> are silently ignored. </p>
<p> If multiple threads of a process are blocked waiting for the same signal(s) in <code>sigwaitinfo</code>() or <code>sigtimedwait</code>(), then exactly one of the threads will actually receive the signal if it becomes pending for the process as a whole; which of the threads receives the signal is indeterminate. </p>
<p> <code>sigwaitinfo</code>() or <code>sigtimedwait</code>(), can&#8217;t be used to receive signals that are synchronously generated, such as the <code>SIGSEGV</code> signal that results from accessing an invalid memory address or the <code>SIGFPE</code> signal that results from an arithmetic error. Such signals can be caught only via signal handler. </p>
<p> POSIX leaves the meaning of a NULL value for the <i>timeout</i> argument of <code>sigtimedwait</code>() unspecified, permitting the possibility that this has the same meaning as a call to <code>sigwaitinfo</code>(), and indeed this is what is done on Linux.</p>
<h3>C library/kernel differences</h3>
<p> On Linux, <code>sigwaitinfo</code>() is a library function implemented on top of <code>sigtimedwait</code>(). </p>
<p> The glibc wrapper functions for <code>sigwaitinfo</code>() and <code>sigtimedwait</code>() silently ignore attempts to wait for the two real-time signals that are used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details. </p>
<p> The original Linux system call was named <code>sigtimedwait</code>(). However, with the addition of real-time signals in Linux 2.2, the fixed-size, 32-bit <i>sigset_t</i> type supported by that system call was no longer fit for purpose. Consequently, a new system call, <code>rt_sigtimedwait</code>(), was added to support an enlarged <i>sigset_t</i> type. The new system call takes a fourth argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the signal set in <i>set</i>. This argument is currently required to have the value <i>sizeof(sigset_t)</i> (or the error <code>EINVAL</code> results). The glibc <code>sigtimedwait</code>() wrapper function hides these details from us, transparently calling <code>rt_sigtimedwait</code>() when the kernel provides it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
