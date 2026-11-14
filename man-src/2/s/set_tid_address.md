---
title: "set_tid_address(2)"
name: "set_tid_address"
section: "2"
letter: "s"
url: "/docs/linux/man/2-set_tid_address/"
description: "set_tid_address – set pointer to thread ID"
---

<h2 class="name">NAME</h2>
<p> set_tid_address &#8211; set pointer to thread ID </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/unistd.h&gt;
pid_t set_tid_address(int *tidptr);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> For each thread, the kernel maintains two attributes (addresses) called <i>set_child_tid</i> and <i>clear_child_tid</i>. These two attributes contain the value NULL by default.</p>
<dl>
<dt><i>set_child_tid</i></p>
<dd> If a thread is started using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_CHILD_SETTID</code> flag, <i>set_child_tid</i> is set to the value passed in the <i>ctid</i> argument of that system call.</p>
<dt>
<dd> When <i>set_child_tid</i> is set, the very first thing the new thread does is to write its thread ID at this address.</p>
<dt><i>clear_child_tid</i></p>
<dd> If a thread is started using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_CHILD_CLEARTID</code> flag, <i>clear_child_tid</i> is set to the value passed in the <i>ctid</i> argument of that system call.</dl>
<p> The system call <code>set_tid_address</code>() sets the <i>clear_child_tid</i> value for the calling thread to <i>tidptr</i>. </p>
<p> When a thread whose <i>clear_child_tid</i> is not NULL terminates, then, if the thread is sharing memory with other threads, then 0 is written at the address specified in <i>clear_child_tid</i> and the kernel performs the following operation: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;futex(clear_child_tid, FUTEX_WAKE, 1, NULL, NULL, 0); </p>
<p> The effect of this operation is to wake a single thread that is performing a futex wait on the memory location. Errors from the futex wake operation are ignored.</p>
<h2>RETURN VALUE</h2>
<p> <code>set_tid_address</code>() always returns the caller&#8217;s thread ID.</p>
<h2>ERRORS</h2>
<p> <code>set_tid_address</code>() always succeeds.</p>
<h2>VERSIONS</h2>
<p> This call is present since Linux 2.5.48. Details as given here are valid since Linux 2.5.49.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
