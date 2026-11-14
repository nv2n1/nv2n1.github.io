---
title: "rt_sigreturn(2)"
name: "rt_sigreturn"
section: "2"
letter: "r"
url: "/docs/linux/man/2-rt_sigreturn/"
description: "sigreturn, rt_sigreturn – return from signal handler and cleanup stack frame"
---

<h2 class="name">NAME</h2>
<p> sigreturn, rt_sigreturn &#8211; return from signal handler and cleanup stack frame </p>
<h2>SYNOPSIS</h2>
<p> <code>int sigreturn(&#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> If the Linux kernel determines that an unblocked signal is pending for a process, then, at the next transition back to user mode in that process (e.g., upon return from a system call or when the process is rescheduled onto the CPU), it creates a new frame on the user-space stack where it saves various pieces of process context (processor status word, registers, signal mask, and signal stack settings). </p>
<p> The kernel also arranges that, during the transition back to user mode, the signal handler is called, and that, upon return from the handler, control passes to a piece of user-space code commonly called the &quot;signal trampoline&quot;. The signal trampoline code in turn calls <code>sigreturn</code>(). </p>
<p> This <code>sigreturn</code>() call undoes everything that was done&#8212;changing the process&#8217;s signal mask, switching signal stacks (see <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2))&#8212;in order to invoke the signal handler. Using the information that was earlier saved on the user-space stack <code>sigreturn</code>() restores the process&#8217;s signal mask, switches stacks, and restores the process&#8217;s context (processor flags and registers, including the stack pointer and instruction pointer), so that the process resumes execution at the point where it was interrupted by the signal.</p>
<h2>RETURN VALUE</h2>
<p> <code>sigreturn</code>() never returns.</p>
<h2>CONFORMING TO</h2>
<p> Many UNIX-type systems have a <code>sigreturn</code>() system call or near equivalent. However, this call is not specified in POSIX, and details of its behavior vary across systems.</p>
<h2>NOTES</h2>
<p> <code>sigreturn</code>() exists only to allow the implementation of signal handlers. It should <code>never</code> be called directly. (Indeed, a simple <code>sigreturn</code>() wrapper in the GNU C library simply returns -1, with <i>errno</i> set to <code>ENOSYS</code>.) Details of the arguments (if any) passed to <code>sigreturn</code>() vary depending on the architecture. (On some architectures, such as x86-64, <code>sigreturn</code>() takes no arguments, since all of the information that it requires is available in the stack frame that was previously created by the kernel on the user-space stack.) </p>
<p> Once upon a time, UNIX systems placed the signal trampoline code onto the user stack. Nowadays, pages of the user stack are protected so as to disallow code execution. Thus, on contemporary Linux systems, depending on the architecture, the signal trampoline code lives either in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7) or in the C library. In the latter case, the C library&#8217;s <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) wrapper function informs the kernel of the location of the trampoline code by placing its address in the <i>sa_restorer</i> field of the <i>sigaction</i> structure, and sets the <code>SA_RESTORER</code> flag in the <i>sa_flags</i> field. </p>
<p> The saved process context information is placed in a <i>ucontext_t</i> structure (see <i>&lt;sys/ucontext.h&gt;</i>). That structure is visible within the signal handler as the third argument of a handler established via <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) with the <code>SA_SIGINFO</code> flag. </p>
<p> On some other UNIX systems, the operation of the signal trampoline differs a little. In particular, on some systems, upon transitioning back to user mode, the kernel passes control to the trampoline (rather than the signal handler), and the trampoline code calls the signal handler (and then calls <code>sigreturn</code>() once the handler returns).</p>
<h3>C library/kernel differences</h3>
<p> The original Linux system call was named <code>sigreturn</code>(). However, with the addition of real-time signals in Linux 2.2, a new system call, <code>rt_sigreturn</code>() was added to support an enlarged <i>sigset_t</i> type. The GNU C library hides these details from us, transparently employing <code>rt_sigreturn</code>() when the kernel provides it.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
