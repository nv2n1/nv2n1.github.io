---
title: "sigsuspend(2)"
name: "sigsuspend"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sigsuspend/"
description: "sigsuspend, rt_sigsuspend – wait for a signal"
---

<h2 class="name">NAME</h2>
<p> sigsuspend, rt_sigsuspend &#8211; wait for a signal </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;signal.h&gt;</code> </p>
<p> <code>int sigsuspend(const sigset_t *</code><i>mask</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sigsuspend</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>sigsuspend</code>() temporarily replaces the signal mask of the calling thread with the mask given by <i>mask</i> and then suspends the thread until delivery of a signal whose action is to invoke a signal handler or to terminate a process. </p>
<p> If the signal terminates the process, then <code>sigsuspend</code>() does not return. If the signal is caught, then <code>sigsuspend</code>() returns after the signal handler returns, and the signal mask is restored to the state before the call to <code>sigsuspend</code>(). </p>
<p> It is not possible to block <code>SIGKILL</code> or <code>SIGSTOP</code>; specifying these signals in <i>mask</i>, has no effect on the thread&#8217;s signal mask.</p>
<h2>RETURN VALUE</h2>
<p> <code>sigsuspend</code>() always returns -1, with <i>errno</i> set to indicate the error (normally, <code>EINTR</code>).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>mask</i> points to memory which is not a valid part of the process address space.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal; <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Normally, <code>sigsuspend</code>() is used in conjunction with <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) in order to prevent delivery of a signal during the execution of a critical code section. The caller first blocks the signals with <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2). When the critical code has completed, the caller then waits for the signals by calling <code>sigsuspend</code>() with the signal mask that was returned by <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) (in the <i>oldset</i> argument). </p>
<p> See <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3) for details on manipulating signal sets.</p>
<h3>C library/kernel differences</h3>
<p> The original Linux system call was named <code>sigsuspend</code>(). However, with the addition of real-time signals in Linux 2.2, the fixed-size, 32-bit <i>sigset_t</i> type supported by that system call was no longer fit for purpose. Consequently, a new system call, <code>rt_sigsuspend</code>(), was added to support an enlarged <i>sigset_t</i> type. The new system call takes a second argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the signal set in <i>mask</i>. This argument is currently required to have the value <i>sizeof(sigset_t)</i> (or the error <code>EINVAL</code> results). The glibc <code>sigsuspend</code>() wrapper function hides these details from us, transparently calling <code>rt_sigsuspend</code>() when the kernel provides it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
