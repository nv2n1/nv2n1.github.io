---
title: "ssetmask(2)"
name: "ssetmask"
section: "2"
letter: "s"
url: "/docs/linux/man/2-ssetmask/"
description: "sgetmask, ssetmask – manipulation of signal mask (obsolete)"
---

<h2 class="name">NAME</h2>
<p> sgetmask, ssetmask &#8211; manipulation of signal mask (obsolete) </p>
<h2>SYNOPSIS</h2>
<p> <code>long sgetmask(void);</code> </p>
<p> <code>long ssetmask(long </code><i>newmask</i><code>);</code> </p>
<p> <i>Note</i>: There are no glibc wrappers for these system calls; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> These system calls are obsolete. <i>Do not use them</i>; use <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) instead. </p>
<p> <code>sgetmask</code>() returns the signal mask of the calling process. </p>
<p> <code>ssetmask</code>() sets the signal mask of the calling process to the value given in <i>newmask</i>. The previous signal mask is returned. </p>
<p> The signal masks dealt with by these two system calls are plain bit masks (unlike the <i>sigset_t</i> used by <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)); use <code><a href="/docs/linux/man/3-sigmask/">sigmask</a></code>(3) to create and inspect these masks.</p>
<h2>RETURN VALUE</h2>
<p> <code>sgetmask</code>() always successfully returns the signal mask. <code>ssetmask</code>() always succeeds, and returns the previous signal mask.</p>
<h2>ERRORS</h2>
<p> These system calls always succeed.</p>
<h2>VERSIONS</h2>
<p> Since Linux 3.16, support for these system calls is optional, depending on whether the kernel was built with the <code>CONFIG_SGETMASK_SYSCALL</code> option.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> Glibc does not provide wrappers for these obsolete system calls; in the unlikely event that you want to call them, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> These system calls are unaware of signal numbers greater than 31 (i.e., real-time signals). </p>
<p> These system calls do not exist on x86-64. </p>
<p> It is not possible to block <code>SIGSTOP</code> or <code>SIGKILL</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
