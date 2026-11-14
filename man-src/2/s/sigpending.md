---
title: "sigpending(2)"
name: "sigpending"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sigpending/"
description: "sigpending, rt_sigpending – examine pending signals"
---

<h2 class="name">NAME</h2>
<p> sigpending, rt_sigpending &#8211; examine pending signals </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;signal.h&gt;</code> </p>
<p> <code>int sigpending(sigset_t *</code><i>set</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sigpending</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>sigpending</code>() returns the set of signals that are pending for delivery to the calling thread (i.e., the signals which have been raised while blocked). The mask of pending signals is returned in <i>set</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>sigpending</code>() returns 0 on success and -1 on error. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>set</i> points to memory which is not a valid part of the process address space.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> See <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3) for details on manipulating signal sets. </p>
<p> If a signal is both blocked and has a disposition of &quot;ignored&quot;, it is <i>not</i> added to the mask of pending signals when generated. </p>
<p> The set of signals that is pending for a thread is the union of the set of signals that is pending for that thread and the set of signals that is pending for the process as a whole; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) initially has an empty pending signal set; the pending signal set is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h3>C library/kernel differences</h3>
<p> The original Linux system call was named <code>sigpending</code>(). However, with the addition of real-time signals in Linux 2.2, the fixed-size, 32-bit <i>sigset_t</i> argument supported by that system call was no longer fit for purpose. Consequently, a new system call, <code>rt_sigpending</code>(), was added to support an enlarged <i>sigset_t</i> type. The new system call takes a second argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the signal set in <i>set</i>. The glibc <code>sigpending</code>() wrapper function hides these details from us, transparently calling <code>rt_sigpending</code>() when the kernel provides it.</p>
<h2>BUGS</h2>
<p> In versions of glibc up to and including 2.2.1, there is a bug in the wrapper function for <code>sigpending</code>() which means that information about pending real-time signals is not correctly returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
