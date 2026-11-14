---
title: "restart_syscall(2)"
name: "restart_syscall"
section: "2"
letter: "r"
url: "/docs/linux/man/2-restart_syscall/"
description: "restart_syscall – restart a system call after interruption by a stop signal"
---

<h2 class="name">NAME</h2>
<p> restart_syscall &#8211; restart a system call after interruption by a stop signal </p>
<h2>SYNOPSIS</h2>
<p> <code>long restart_syscall(void);</code> </p>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>restart_syscall</code>() system call is used to restart certain system calls after a process that was stopped by a signal (e.g., <code>SIGSTOP</code> or <code>SIGTSTP</code>) is later resumed after receiving a <code>SIGCONT</code> signal. This system call is designed only for internal use by the kernel. </p>
<p> <code>restart_syscall</code>() is used for restarting only those system calls that, when restarted, should adjust their time-related parameters&#8212;namely <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) (since Linux 2.6.24), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2) (since Linux 2.6), <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2) (since Linux 2.6), and <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), when employed with the <code>FUTEX_WAIT</code> (since Linux 2.6.22) and <code>FUTEX_WAIT_BITSET</code> (since Linux 2.6.31) operations. <code>restart_syscall</code>() restarts the interrupted system call with a time argument that is suitably adjusted to account for the time that has already elapsed (including the time where the process was stopped by a signal). Without the <code>restart_syscall</code>() mechanism, restarting these system calls would not correctly deduct the already elapsed time when the process continued execution.</p>
<h2>RETURN VALUE</h2>
<p> The return value of <code>restart_syscall</code>() is the return value of whatever system call is being restarted.</p>
<h2>ERRORS</h2>
<p> <i>errno</i> is set as per the errors for whatever system call is being restarted by <code>restart_syscall</code>().</p>
<h2>VERSIONS</h2>
<p> The <code>restart_syscall</code>() system call is present since Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> There is no glibc wrapper for this system call, because it is intended for use only by the kernel and should never be called by applications. </p>
<p> The kernel uses <code>restart_syscall</code>() to ensure that when a system call is restarted after a process has been stopped by a signal and then resumed by <code>SIGCONT</code>, then the time that the process spent in the stopped state is counted against the timeout interval specified in the original system call. In the case of system calls that take a timeout argument and automatically restart after a stop signal plus <code>SIGCONT</code>, but which do not have the <code>restart_syscall</code>() mechanism built in, then, after the process resumes execution, the time that the process spent in the stop state is <i>not</i> counted against the timeout value. Notable examples of system calls that suffer this problem are <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), and <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2). </p>
<p> From user space, the operation of <code>restart_syscall</code>() is largely invisible: to the process that made the system call that is restarted, it appears as though that system call executed and returned in the usual fashion.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
