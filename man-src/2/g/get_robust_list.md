---
title: "get_robust_list(2)"
name: "get_robust_list"
section: "2"
letter: "g"
url: "/docs/linux/man/2-get_robust_list/"
description: "get_robust_list, set_robust_list – get/set list of robust futexes"
---

<h2 class="name">NAME</h2>
<p> get_robust_list, set_robust_list &#8211; get/set list of robust futexes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/futex.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;syscall.h&gt;
long get_robust_list(int pid, struct robust_list_head **head_ptr,
                     size_t *len_ptr);
long set_robust_list(struct robust_list_head *head, size_t len);
</code></pre>
<p> <i>Note</i>: There are no glibc wrappers for these system calls; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> These system calls deal with per-thread robust futex lists. These lists are managed in user space: the kernel knows only about the location of the head of the list. A thread can inform the kernel of the location of its robust futex list using <code>set_robust_list</code>(). The address of a thread&#8217;s robust futex list can be obtained using <code>get_robust_list</code>(). </p>
<p> The purpose of the robust futex list is to ensure that if a thread accidentally fails to unlock a futex before terminating or calling <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), another thread that is waiting on that futex is notified that the former owner of the futex has died. This notification consists of two pieces: the <code>FUTEX_OWNER_DIED</code> bit is set in the futex word, and the kernel performs a <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) <code>FUTEX_WAKE</code> operation on one of the threads waiting on the futex. </p>
<p> The <code>get_robust_list</code>() system call returns the head of the robust futex list of the thread whose thread ID is specified in <i>pid</i>. If <i>pid</i> is 0, the head of the list for the calling thread is returned. The list head is stored in the location pointed to by <i>head_ptr</i>. The size of the object pointed to by <i>**head_ptr</i> is stored in <i>len_ptr</i>. </p>
<p> Permission to employ <code>get_robust_list</code>() is governed by a ptrace access mode <code>PTRACE_MODE_READ_REALCREDS</code> check; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2). </p>
<p> The <code>set_robust_list</code>() system call requests the kernel to record the head of the list of robust futexes owned by the calling thread. The <i>head</i> argument is the list head to record. The <i>len</i> argument should be <i>sizeof(*head)</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>set_robust_list</code>() and <code>get_robust_list</code>() system calls return zero when the operation is successful, an error code otherwise.</p>
<h2>ERRORS</h2>
<p> The <code>set_robust_list</code>() system call can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>len</i> does not equal <i>sizeof(struct robust_list_head)</i>.</dl>
<p> The <code>get_robust_list</code>() system call can fail with the following errors:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> The head of the robust futex list can&#8217;t be stored at the location <i>head</i>.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have permission to see the robust futex list of the thread with the thread ID <i>pid</i>, and does not have the <code>CAP_SYS_PTRACE</code> capability.</p>
<dt><code>ESRCH</code></p>
<dd> No thread with the thread ID <i>pid</i> could be found.</dl>
<h2>VERSIONS</h2>
<p> These system calls were added in Linux 2.6.17.</p>
<h2>NOTES</h2>
<p> These system calls are not needed by normal applications. No support for them is provided in glibc. In the unlikely event that you want to call them directly, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> A thread can have only one robust futex list; therefore applications that wish to use this functionality should use the robust mutexes provided by glibc. </p>
<p> In the initial implementation, a thread waiting on a futex was notified that the owner had died only if the owner terminated. Starting with Linux 2.6.28, notification was extended to include the case where the owner performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The thread IDs mentioned in the main text are <i>kernel</i> thread IDs of the kind returned by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/3-pthread_mutexattr_setrobust/">pthread_mutexattr_setrobust</a></code>(3) </p>
<p> <i>Documentation/robust-futexes.txt</i> and <i>Documentation/robust-futex-ABI.txt</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
