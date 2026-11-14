---
title: "signal(7)"
name: "signal"
section: "7"
letter: "s"
url: "/docs/linux/man/7-signal/"
description: "signal – overview of signals"
---

<p>signal &#8211; overview of signals</p>
<h2>Description</h2>
<p>Linux supports both POSIX reliable signals (hereinafter &quot;standard signals&quot;) and POSIX real-time signals.</p>
<h3>Signal dispositions</h3>
<p>Each signal has a current <i>disposition</i>, which determines how the process behaves when it is delivered the signal. </p>
<p> The entries in the &quot;Action&quot; column of the table below specify the default disposition for each signal, as follows:</p>
<dl>
<dt>Term</p>
<dd>Default action is to terminate the process.</p>
<dt>Ign</p>
<dd>Default action is to ignore the signal.</p>
<dt>Core</p>
<dd>Default action is to terminate the process and dump core (see <code><a href="/docs/linux/man/5-core/">core</a></code>(5)).</p>
<dt>Stop</p>
<dd>Default action is to stop the process.</p>
<dt>Cont</p>
<dd>Default action is to continue the process if it is currently stopped.</dl>
<p> A process can change the disposition of a signal using <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) or <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2). (The latter is less portable when establishing a signal handler; see <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) for details.) Using these system calls, a process can elect one of the following behaviors to occur on delivery of the signal: perform the default action; ignore the signal; or catch the signal with a <i>signal handler</i>, a programmer-defined function that is automatically invoked when the signal is delivered. </p>
<p> By default, a signal handler is invoked on the normal process stack. It is possible to arrange that the signal handler uses an alternate stack; see <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2) for a discussion of how to do this and when it might be useful. </p>
<p> The signal disposition is a per-process attribute: in a multithreaded application, the disposition of a particular signal is the same for all threads. </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits a copy of its parent&#8217;s signal dispositions. During an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the dispositions of handled signals are reset to the default; the dispositions of ignored signals are left unchanged.</p>
<h3>Sending a signal</h3>
<p>The following system calls and library functions allow the caller to send a signal:</p>
<dl>
<dt><code><a href="/docs/linux/man/3-raise/">raise</a></code>(3)</p>
<dd>Sends a signal to the calling thread.</p>
<dt><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)</p>
<dd>Sends a signal to a specified process, to all members of a specified process group, or to all processes on the system.</p>
<dt><code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2)</p>
<dd>Sends a signal to a process identified by a PID file descriptor.</p>
<dt><code><a href="/docs/linux/man/3-killpg/">killpg</a></code>(3)</p>
<dd>Sends a signal to all of the members of a specified process group.</p>
<dt><code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3)</p>
<dd>Sends a signal to a specified POSIX thread in the same process as the caller.</p>
<dt><code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2)</p>
<dd>Sends a signal to a specified thread within a specific process. (This is the system call used to implement <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3).)</p>
<dt><code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3)</p>
<dd>Sends a real-time signal with accompanying data to a specified process.</dl>
<h3>Waiting for a signal to be caught</h3>
<p>The following system calls suspend execution of the calling thread until a signal is caught (or an unhandled signal terminates the process):</p>
<dl>
<dt><code><a href="/docs/linux/man/2-pause/">pause</a></code>(2)</p>
<dd>Suspends execution until any signal is caught.</p>
<dt><code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</p>
<dd>Temporarily changes the signal mask (see below) and suspends execution until one of the unmasked signals is caught.</dl>
<h3>Synchronously accepting a signal</h3>
<p>Rather than asynchronously catching a signal via a signal handler, it is possible to synchronously accept the signal, that is, to block execution until the signal is delivered, at which point the kernel returns information about the signal to the caller. There are two general ways to do this:</p>
<dl>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2), and <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3) suspend execution until one of the signals in a specified set is delivered. Each of these calls returns information about the delivered signal.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2) returns a file descriptor that can be used to read information about signals that are delivered to the caller. Each <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from this file descriptor blocks until one of the signals in the set specified in the <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2) call is delivered to the caller. The buffer returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) contains a structure describing the signal.</dl>
<h3>Signal mask and pending signals</h3>
<p>A signal may be <i>blocked</i>, which means that it will not be delivered until it is later unblocked. Between the time when it is generated and when it is delivered a signal is said to be <i>pending</i>. </p>
<p> Each thread in a process has an independent <i>signal mask</i>, which indicates the set of signals that the thread is currently blocking. A thread can manipulate its signal mask using <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3). In a traditional single-threaded application, <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) can be used to manipulate the signal mask. </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits a copy of its parent&#8217;s signal mask; the signal mask is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> A signal may be process-directed or thread-directed. A process-directed signal is one that is targeted at (and thus pending for) the process as a whole. A signal may be process-directed because it was generated by the kernel for reasons other than a hardware exception, or because it was sent using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) or <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3). A thread-directed signal is one that is targeted at a specific thread. A signal may be thread-directed because it was generated as a consequence of executing a specific machine-language instruction that triggered a hardware exception (e.g., <code>SIGSEGV</code> for an invalid memory access, or <code>SIGFPE</code> for a math error), or because it was targeted at a specific thread using interfaces such as <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2) or <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3). </p>
<p> A process-directed signal may be delivered to any one of the threads that does not currently have the signal blocked. If more than one of the threads has the signal unblocked, then the kernel chooses an arbitrary thread to which to deliver the signal. </p>
<p> A thread can obtain the set of signals that it currently has pending using <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2). This set will consist of the union of the set of pending process-directed signals and the set of signals pending for the calling thread. </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) initially has an empty pending signal set; the pending signal set is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h3>Execution of signal handlers</h3>
<p>Whenever there is a transition from kernel-mode to user-mode execution (e.g., on return from a system call or scheduling of a thread onto the CPU), the kernel checks whether there is a pending unblocked signal for which the process has established a signal handler. If there is such a pending signal, the following steps occur:</p>
<dl>
<dt>1.</p>
<dd>The kernel performs the necessary preparatory steps for execution of the signal handler:</p>
<dl>
<dd>
<dl>
<dt>a)</p>
<dd>The signal is removed from the set of pending signals.</p>
<dt>b)</p>
<dd>If the signal handler was installed by a call to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) that specified the <code>SA_ONSTACK</code> flag and the thread has defined an alternate signal stack (using <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)), then that stack is installed.</p>
<dt>c)</p>
<dd>Various pieces of signal-related context are saved into a special frame that is created on the stack. The saved information includes:</p>
<dl>
<dd>
<dl>
<dt>+</p>
<dd>the program counter register (i.e., the address of the next instruction in the main program that should be executed when the signal handler returns);</p>
<dt>+</p>
<dd>architecture-specific register state required for resuming the interrupted program;</p>
<dt>+</p>
<dd>the thread&#8217;s current signal mask;</p>
<dt>+</p>
<dd>the thread&#8217;s alternate signal stack settings.</dl>
</dl>
<dd>(If the signal handler was installed using the <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) <code>SA_SIGINFO</code> flag, then the above information is accessible via the <i>ucontext_t</i> object that is pointed to by the third argument of the signal handler.)</p>
<dt>d)</p>
<dd>Any signals specified in <i>act-&gt;sa_mask</i> when registering the handler with <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) are added to the thread&#8217;s signal mask. The signal being delivered is also added to the signal mask, unless <code>SA_NODEFER</code> was specified when registering the handler. These signals are thus blocked while the handler executes.</dl>
</dl>
<dt>2.</p>
<dd>The kernel constructs a frame for the signal handler on the stack. The kernel sets the program counter for the thread to point to the first instruction of the signal handler function, and configures the return address for that function to point to a piece of user-space code known as the signal trampoline (described in <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2)).</p>
<dt>3.</p>
<dd>The kernel passes control back to user-space, where execution commences at the start of the signal handler function.</p>
<dt>4.</p>
<dd>When the signal handler returns, control passes to the signal trampoline code.</p>
<dt>5.</p>
<dd>The signal trampoline calls <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2), a system call that uses the information in the stack frame created in step 1 to restore the thread to its state before the signal handler was called. The thread&#8217;s signal mask and alternate signal stack settings are restored as part of this procedure. Upon completion of the call to <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2), the kernel transfers control back to user space, and the thread recommences execution at the point where it was interrupted by the signal handler.</dl>
<p> Note that if the signal handler does not return (e.g., control is transferred out of the handler using <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3), or the handler executes a new program with <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)), then the final step is not performed. In particular, in such scenarios it is the programmer&#8217;s responsibility to restore the state of the signal mask (using <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)), if it is desired to unblock the signals that were blocked on entry to the signal handler. (Note that <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3) may or may not restore the signal mask, depending on the <i>savesigs</i> value that was specified in the corresponding call to <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3).) </p>
<p> From the kernel&#8217;s point of view, execution of the signal handler code is exactly the same as the execution of any other user-space code. That is to say, the kernel does not record any special state information indicating that the thread is currently excuting inside a signal handler. All necessary state information is maintained in user-space registers and the user-space stack. The depth to which nested signal handlers may be invoked is thus limited only by the user-space stack (and sensible software design!).</p>
<h3>Standard signals</h3>
<p>Linux supports the standard signals listed below. The second column of the table indicates which standard (if any) specified the signal: &quot;P1990&quot; indicates that the signal is described in the original POSIX.1-1990 standard; &quot;P2001&quot; indicates that the signal was added in SUSv2 and POSIX.1-2001. </p>
<table>
<tr VALIGN=top>
<td>Signal</td>
<td ALIGN=center>Standard</td>
<td ALIGN=center>Action</td>
<td>Comment
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGALRM</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Timer signal from <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGBUS</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Core</td>
<td>Bus error (bad memory access)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCHLD</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Ign</td>
<td>Child stopped or terminated
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCLD</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Ign</td>
<td>A synonym for <code>SIGCHLD</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCONT</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Cont</td>
<td>Continue if stopped
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGEMT</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Term</td>
<td>Emulator trap
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGFPE</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Core</td>
<td>Floating-point exception
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGHUP</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Hangup detected on controlling terminal
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>or death of controlling process
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGILL</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Core</td>
<td>Illegal Instruction
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGINFO</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center></td>
<td>A synonym for <code>SIGPWR</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGINT</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Interrupt from keyboard
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGIO</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Term</td>
<td>I/O now possible (4.2BSD)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGIOT</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Core</td>
<td>IOT trap. A synonym for <code>SIGABRT</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGKILL</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Kill signal
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGLOST</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Term</td>
<td>File lock lost (unused)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPIPE</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Broken pipe: write to pipe with no
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>readers; see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPOLL</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Term</td>
<td>Pollable event (Sys V);
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>synonym for <code>SIGIO</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPROF</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Term</td>
<td>Profiling timer expired
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPWR</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Term</td>
<td>Power failure (System V)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGQUIT</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Core</td>
<td>Quit from keyboard
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSEGV</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Core</td>
<td>Invalid memory reference
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSTKFLT</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Term</td>
<td>Stack fault on coprocessor (unused)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSTOP</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Stop</td>
<td>Stop process
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTSTP</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Stop</td>
<td>Stop typed at terminal
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSYS</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Core</td>
<td>Bad system call (SVr4);
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>see also <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTERM</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>Termination signal
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTRAP</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Core</td>
<td>Trace/breakpoint trap
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTTIN</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Stop</td>
<td>Terminal input for background process
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTTOU</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Stop</td>
<td>Terminal output for background process
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUNUSED</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Core</td>
<td>Synonymous with <code>SIGSYS</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGURG</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Ign</td>
<td>Urgent condition on socket (4.2BSD)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUSR1</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>User-defined signal 1
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUSR2</code></td>
<td ALIGN=center>P1990</td>
<td ALIGN=center>Term</td>
<td>User-defined signal 2
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGVTALRM</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Term</td>
<td>Virtual alarm clock (4.2BSD)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGXCPU</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Core</td>
<td>CPU time limit exceeded (4.2BSD);
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGXFSZ</code></td>
<td ALIGN=center>P2001</td>
<td ALIGN=center>Core</td>
<td>File size limit exceeded (4.2BSD);
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGWINCH</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>Ign</td>
<td>Window resize signal (4.3BSD, Sun)
</td>
</tr>
</table>
<p> The signals <code>SIGKILL</code> and <code>SIGSTOP</code> cannot be caught, blocked, or ignored. </p>
<p> Up to and including Linux 2.2, the default behavior for <code>SIGSYS</code>, <code>SIGXCPU</code>, <code>SIGXFSZ</code>, and (on architectures other than SPARC and MIPS) <code>SIGBUS</code> was to terminate the process (without a core dump). (On some other UNIX systems the default action for <code>SIGXCPU</code> and <code>SIGXFSZ</code> is to terminate the process without a core dump.) Linux 2.4 conforms to the POSIX.1-2001 requirements for these signals, terminating the process with a core dump. </p>
<p> <code>SIGEMT</code> is not specified in POSIX.1-2001, but nevertheless appears on most other UNIX systems, where its default action is typically to terminate the process with a core dump. </p>
<p> <code>SIGPWR</code> (which is not specified in POSIX.1-2001) is typically ignored by default on those other UNIX systems where it appears. </p>
<p> <code>SIGIO</code> (which is not specified in POSIX.1-2001) is ignored by default on several other UNIX systems.</p>
<h3>Queueing and delivery semantics for standard signals</h3>
<p>If multiple standard signals are pending for a process, the order in which the signals are delivered is unspecified. </p>
<p> Standard signals do not queue. If multiple instances of a standard signal are generated while that signal is blocked, then only one instance of the signal is marked as pending (and the signal will be delivered just once when it is unblocked). In the case where a standard signal is already pending, the <i>siginfo_t</i> structure (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) associated with that signal is not overwritten on arrival of subsequent instances of the same signal. Thus, the process will receive the information associated with the first instance of the signal.</p>
<h3>Signal numbering for standard signals</h3>
<p>The numeric value for each signal is given in the table below. As shown in the table, many signals have different numeric values on different architectures. The first numeric value in each table row shows the signal number on x86, ARM, and most other architectures; the second value is for Alpha and SPARC; the third is for MIPS; and the last is for PARISC. A dash (-) denotes that a signal is absent on the corresponding architecture. </p>
<table>
<tr VALIGN=top>
<td>Signal</td>
<td ALIGN=center>x86/ARM</td>
<td ALIGN=center>Alpha/</td>
<td ALIGN=center>MIPS</td>
<td ALIGN=center>PARISC</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center>most others</td>
<td ALIGN=center>SPARC</td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGINT</code></td>
<td ALIGN=center>&nbsp;2</td>
<td ALIGN=center>&nbsp;2</td>
<td ALIGN=center>&nbsp;2</td>
<td ALIGN=center>&nbsp;2</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGQUIT</code></td>
<td ALIGN=center>&nbsp;3</td>
<td ALIGN=center>&nbsp;3</td>
<td ALIGN=center>&nbsp;3</td>
<td ALIGN=center>&nbsp;3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGILL</code></td>
<td ALIGN=center>&nbsp;4</td>
<td ALIGN=center>&nbsp;4</td>
<td ALIGN=center>&nbsp;4</td>
<td ALIGN=center>&nbsp;4</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTRAP</code></td>
<td ALIGN=center>&nbsp;5</td>
<td ALIGN=center>&nbsp;5</td>
<td ALIGN=center>&nbsp;5</td>
<td ALIGN=center>&nbsp;5</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGABRT</code></td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGIOT</code></td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td ALIGN=center>&nbsp;6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGBUS</code></td>
<td ALIGN=center>&nbsp;7</td>
<td ALIGN=center>10</td>
<td ALIGN=center>10</td>
<td ALIGN=center>10</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGEMT</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&nbsp;7</td>
<td ALIGN=center>&nbsp;7</td>
<td ALIGN=center>&#8211;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGFPE</code></td>
<td ALIGN=center>&nbsp;8</td>
<td ALIGN=center>&nbsp;8</td>
<td ALIGN=center>&nbsp;8</td>
<td ALIGN=center>&nbsp;8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGKILL</code></td>
<td ALIGN=center>&nbsp;9</td>
<td ALIGN=center>&nbsp;9</td>
<td ALIGN=center>&nbsp;9</td>
<td ALIGN=center>&nbsp;9</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUSR1</code></td>
<td ALIGN=center>10</td>
<td ALIGN=center>30</td>
<td ALIGN=center>16</td>
<td ALIGN=center>16</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSEGV</code></td>
<td ALIGN=center>11</td>
<td ALIGN=center>11</td>
<td ALIGN=center>11</td>
<td ALIGN=center>11</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUSR2</code></td>
<td ALIGN=center>12</td>
<td ALIGN=center>31</td>
<td ALIGN=center>17</td>
<td ALIGN=center>17</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPIPE</code></td>
<td ALIGN=center>13</td>
<td ALIGN=center>13</td>
<td ALIGN=center>13</td>
<td ALIGN=center>13</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGALRM</code></td>
<td ALIGN=center>14</td>
<td ALIGN=center>14</td>
<td ALIGN=center>14</td>
<td ALIGN=center>14</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTERM</code></td>
<td ALIGN=center>15</td>
<td ALIGN=center>15</td>
<td ALIGN=center>15</td>
<td ALIGN=center>15</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSTKFLT</code></td>
<td ALIGN=center>16</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&nbsp;7</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCHLD</code></td>
<td ALIGN=center>17</td>
<td ALIGN=center>20</td>
<td ALIGN=center>18</td>
<td ALIGN=center>18</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCLD</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>18</td>
<td ALIGN=center>&#8211;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGCONT</code></td>
<td ALIGN=center>18</td>
<td ALIGN=center>19</td>
<td ALIGN=center>25</td>
<td ALIGN=center>26</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSTOP</code></td>
<td ALIGN=center>19</td>
<td ALIGN=center>17</td>
<td ALIGN=center>23</td>
<td ALIGN=center>24</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTSTP</code></td>
<td ALIGN=center>20</td>
<td ALIGN=center>18</td>
<td ALIGN=center>24</td>
<td ALIGN=center>25</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTTIN</code></td>
<td ALIGN=center>21</td>
<td ALIGN=center>21</td>
<td ALIGN=center>26</td>
<td ALIGN=center>27</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGTTOU</code></td>
<td ALIGN=center>22</td>
<td ALIGN=center>22</td>
<td ALIGN=center>27</td>
<td ALIGN=center>28</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGURG</code></td>
<td ALIGN=center>23</td>
<td ALIGN=center>16</td>
<td ALIGN=center>21</td>
<td ALIGN=center>29</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGXCPU</code></td>
<td ALIGN=center>24</td>
<td ALIGN=center>24</td>
<td ALIGN=center>30</td>
<td ALIGN=center>12</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGXFSZ</code></td>
<td ALIGN=center>25</td>
<td ALIGN=center>25</td>
<td ALIGN=center>31</td>
<td ALIGN=center>30</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGVTALRM</code></td>
<td ALIGN=center>26</td>
<td ALIGN=center>26</td>
<td ALIGN=center>28</td>
<td ALIGN=center>20</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPROF</code></td>
<td ALIGN=center>27</td>
<td ALIGN=center>27</td>
<td ALIGN=center>29</td>
<td ALIGN=center>21</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGWINCH</code></td>
<td ALIGN=center>28</td>
<td ALIGN=center>28</td>
<td ALIGN=center>20</td>
<td ALIGN=center>23</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGIO</code></td>
<td ALIGN=center>29</td>
<td ALIGN=center>23</td>
<td ALIGN=center>22</td>
<td ALIGN=center>22</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPOLL</code></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td ALIGN=center></td>
<td>Same as SIGIO
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGPWR</code></td>
<td ALIGN=center>30</td>
<td ALIGN=center>29/-</td>
<td ALIGN=center>19</td>
<td ALIGN=center>19</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGINFO</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>29/-</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&#8211;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGLOST</code></td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>-/29</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&#8211;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGSYS</code></td>
<td ALIGN=center>31</td>
<td ALIGN=center>12</td>
<td ALIGN=center>12</td>
<td ALIGN=center>31</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>SIGUNUSED</code></td>
<td ALIGN=center>31</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>&#8211;</td>
<td ALIGN=center>31</td>
<td>
</td>
</tr>
</table>
<p> Note the following:</p>
<dl>
<dt>*</p>
<dd>Where defined, <code>SIGUNUSED</code> is synonymous with <code>SIGSYS</code>. Since glibc 2.26, <code>SIGUNUSED</code> is no longer defined on any architecture.</p>
<dt>*</p>
<dd>Signal 29 is <code>SIGINFO</code>/<code>SIGPWR</code> (synonyms for the same value) on Alpha but <code>SIGLOST</code> on SPARC.</dl>
<h3>Real-time signals</h3>
<p>Starting with version 2.2, Linux supports real-time signals as originally defined in the POSIX.1b real-time extensions (and now included in POSIX.1-2001). The range of supported real-time signals is defined by the macros <code>SIGRTMIN</code> and <code>SIGRTMAX</code>. POSIX.1-2001 requires that an implementation support at least <code>_POSIX_RTSIG_MAX</code> (8) real-time signals. </p>
<p> The Linux kernel supports a range of 33 different real-time signals, numbered 32 to 64. However, the glibc POSIX threads implementation internally uses two (for NPTL) or three (for LinuxThreads) real-time signals (see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)), and adjusts the value of <code>SIGRTMIN</code> suitably (to 34 or 35). Because the range of available real-time signals varies according to the glibc threading implementation (and this variation can occur at run time according to the available kernel and glibc), and indeed the range of real-time signals varies across UNIX systems, programs should <i>never refer to real-time signals using hard-coded numbers</i>, but instead should always refer to real-time signals using the notation <code>SIGRTMIN</code>+n, and include suitable (run-time) checks that <code>SIGRTMIN</code>+n does not exceed <code>SIGRTMAX</code>. </p>
<p> Unlike standard signals, real-time signals have no predefined meanings: the entire set of real-time signals can be used for application-defined purposes. </p>
<p> The default action for an unhandled real-time signal is to terminate the receiving process. </p>
<p> Real-time signals are distinguished by the following:</p>
<dl>
<dt>1.</p>
<dd>Multiple instances of real-time signals can be queued. By contrast, if multiple instances of a standard signal are delivered while that signal is currently blocked, then only one instance is queued.</p>
<dt>2.</p>
<dd>If the signal is sent using <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), an accompanying value (either an integer or a pointer) can be sent with the signal. If the receiving process establishes a handler for this signal using the <code>SA_SIGINFO</code> flag to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), then it can obtain this data via the <i>si_value</i> field of the <i>siginfo_t</i> structure passed as the second argument to the handler. Furthermore, the <i>si_pid</i> and <i>si_uid</i> fields of this structure can be used to obtain the PID and real user ID of the process sending the signal.</p>
<dt>3.</p>
<dd>Real-time signals are delivered in a guaranteed order. Multiple real-time signals of the same type are delivered in the order they were sent. If different real-time signals are sent to a process, they are delivered starting with the lowest-numbered signal. (I.e., low-numbered signals have highest priority.) By contrast, if multiple standard signals are pending for a process, the order in which they are delivered is unspecified.</dl>
<p> If both standard and real-time signals are pending for a process, POSIX leaves it unspecified which is delivered first. Linux, like many other implementations, gives priority to standard signals in this case. </p>
<p> According to POSIX, an implementation should permit at least <code>_POSIX_SIGQUEUE_MAX</code> (32) real-time signals to be queued to a process. However, Linux does things differently. In kernels up to and including 2.6.7, Linux imposes a system-wide limit on the number of queued real-time signals for all processes. This limit can be viewed and (with privilege) changed via the <i>/proc/sys/kernel/rtsig-max</i> file. A related file, <i>/proc/sys/kernel/rtsig-nr</i>, can be used to find out how many real-time signals are currently queued. In Linux 2.6.8, these <i>/proc</i> interfaces were replaced by the <code>RLIMIT_SIGPENDING</code> resource limit, which specifies a per-user limit for queued signals; see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) for further details. </p>
<p> The addition of real-time signals required the widening of the signal set structure (<i>sigset_t</i>) from 32 to 64 bits. Consequently, various system calls were superseded by new system calls that supported the larger signal sets. The old and new system calls are as follows: </p>
<table>
<tr VALIGN=top>
<td><code>Linux 2.0 and earlier</code></td>
<td><code>Linux 2.2 and later</code>
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigaction/">rt_sigaction</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigpending/">rt_sigpending</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigprocmask/">rt_sigprocmask</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigreturn/">rt_sigreturn</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigsuspend/">rt_sigsuspend</a></code>(2)
</td>
</tr>
<tr VALIGN=top>
<td><code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2)</td>
<td><code><a href="/docs/linux/man/2-rt_sigtimedwait/">rt_sigtimedwait</a></code>(2)
</td>
</tr>
</table>
<h3>Interruption of system calls and library functions by signal handlers</h3>
<p>If a signal handler is invoked while a system call or library function call is blocked, then either:</p>
<dl>
<dt>*</p>
<dd>the call is automatically restarted after the signal handler returns; or</p>
<dt>*</p>
<dd>the call fails with the error <code>EINTR</code>.</dl>
<p> Which of these two behaviors occurs depends on the interface and whether or not the signal handler was established using the <code>SA_RESTART</code> flag (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)). The details vary across UNIX systems; below, the details for Linux. </p>
<p> If a blocked call to one of the following interfaces is interrupted by a signal handler, then the call is automatically restarted after the signal handler returns if the <code>SA_RESTART</code> flag was used; otherwise the call fails with the error <code>EINTR</code>:</p>
<dl>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2), and <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls on &quot;slow&quot; devices. A &quot;slow&quot; device is one where the I/O call may block for an indefinite time, for example, a terminal, pipe, or socket. If an I/O call on a slow device has already transferred some data by the time it is interrupted by a signal handler, then the call will return a success status (normally, the number of bytes transferred). Note that a (local) disk is not a slow device according to this definition; I/O operations on disk devices are not interrupted by signals.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-open/">open</a></code>(2), if it can block (e.g., when opening a FIFO; see <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7)).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/2-wait3/">wait3</a></code>(2), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2), and <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2).</p>
<dt>*</p>
<dd>Socket interfaces: <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), and <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), unless a timeout has been set on the socket (see below).</p>
<dt>*</p>
<dd>File locking interfaces: <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) and the <code>F_SETLKW</code> and <code>F_OFD_SETLKW</code> operations of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)</p>
<dt>*</p>
<dd>POSIX message queue interfaces: <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_timedreceive/">mq_timedreceive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), and <code><a href="/docs/linux/man/3-mq_timedsend/">mq_timedsend</a></code>(3).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) <code>FUTEX_WAIT</code> (since Linux 2.6.22; beforehand, always failed with <code>EINTR</code>).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cond_wait/">pthread_cond_wait</a></code>(3), and related APIs.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) <code>FUTEX_WAIT_BITSET</code>.</p>
<dt>*</p>
<dd>POSIX semaphore interfaces: <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3) and <code><a href="/docs/linux/man/3-sem_timedwait/">sem_timedwait</a></code>(3) (since Linux 2.6.22; beforehand, always failed with <code>EINTR</code>).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-read/">read</a></code>(2) from an <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) file descriptor (since Linux 3.8; beforehand, always failed with <code>EINTR</code>).</dl>
<p> The following interfaces are never restarted after being interrupted by a signal handler, regardless of the use of <code>SA_RESTART</code>; they always fail with the error <code>EINTR</code> when interrupted by a signal handler:</p>
<dl>
<dt>*</p>
<dd>&quot;Input&quot; socket interfaces, when a timeout (<code>SO_RCVTIMEO</code>) has been set on the socket using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2): <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2) (also with a non-NULL <i>timeout</i> argument), and <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2).</p>
<dt>*</p>
<dd>&quot;Output&quot; socket interfaces, when a timeout (<code>SO_RCVTIMEO</code>) has been set on the socket using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2): <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), and <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2).</p>
<dt>*</p>
<dd>Interfaces used to wait for signals: <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2), and <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2).</p>
<dt>*</p>
<dd>File descriptor multiplexing interfaces: <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/2-epoll_pwait/">epoll_pwait</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), and <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2).</p>
<dt>*</p>
<dd>System V IPC interfaces: <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), and <code><a href="/docs/linux/man/2-semtimedop/">semtimedop</a></code>(2).</p>
<dt>*</p>
<dd>Sleep interfaces: <code><a href="/docs/linux/man/2-clock_nanosleep/">clock_nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), and <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2).</dl>
<p> The <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3) function is also never restarted if interrupted by a handler, but gives a success return: the number of seconds remaining to sleep.</p>
<h3>Interruption of system calls and library functions by stop signals</h3>
<p>On Linux, even in the absence of signal handlers, certain blocking interfaces can fail with the error <code>EINTR</code> after the process is stopped by one of the stop signals and then resumed via <code>SIGCONT</code>. This behavior is not sanctioned by POSIX.1, and doesn&#8217;t occur on other systems. </p>
<p> The Linux interfaces that display this behavior are:</p>
<dl>
<dt>*</p>
<dd>&quot;Input&quot; socket interfaces, when a timeout (<code>SO_RCVTIMEO</code>) has been set on the socket using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2): <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2) (also with a non-NULL <i>timeout</i> argument), and <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2).</p>
<dt>*</p>
<dd>&quot;Output&quot; socket interfaces, when a timeout (<code>SO_RCVTIMEO</code>) has been set on the socket using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2): <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), and <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), if a send timeout (<code>SO_SNDTIMEO</code>) has been set.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/2-epoll_pwait/">epoll_pwait</a></code>(2).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-semtimedop/">semtimedop</a></code>(2).</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2).</p>
<dt>*</p>
<dd>Linux 3.7 and earlier: <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from an <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) file descriptor</p>
<dt>*</p>
<dd>Linux 2.6.21 and earlier: <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) <code>FUTEX_WAIT</code>, <code><a href="/docs/linux/man/3-sem_timedwait/">sem_timedwait</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3).</p>
<dt>*</p>
<dd>Linux 2.6.8 and earlier: <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2).</p>
<dt>*</p>
<dd>Linux 2.4 and earlier: <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2).</dl>
<h2>Conforming To</h2>
<p>POSIX.1, except as noted.</p>
<h2>Notes</h2>
<p>For a discussion of async-signal-safe functions, see <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7). </p>
<p> The <i>/proc/[pid]/task/[tid]/status</i> file contains various fields that show the signals that a thread is blocking (<i>SigBlk</i>), catching (<i>SigCgt</i>), or ignoring (<i>SigIgn</i>). (The set of signals that are caught or ignored will be the same across all threads in a process.) Other fields show the set of pending signals that are directed to the thread (<i>SigPnd</i>) as well as the set of pending signals that are directed to the process as a whole (<i>ShdPnd</i>). The corresponding fields in <i>/proc/[pid]/status</i> show the information for the main thread. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details.</p>
<h2>Bugs</h2>
<p>There are six signals that can be delivered as a consequence of a hardware exception: <code>SIGBUS</code>, <code>SIGEMT</code>, <code>SIGFPE</code>, <code>SIGILL</code>, <code>SIGSEGV</code>, and <code>SIGTRAP</code>. Which of these signals is delivered, for any given hardware exception, is not documented and does not always make sense. </p>
<p> For example, an invalid memory access that causes delivery of <code>SIGSEGV</code> on one CPU architecture may cause delivery of <code>SIGBUS</code> on another architecture, or vice versa. </p>
<p> For another example, using the x86 <i>int</i> instruction with a forbidden argument (any number other than 3 or 128) causes delivery of <code>SIGSEGV</code>, even though <code>SIGILL</code> would make more sense, because of how the CPU reports the forbidden operation to the kernel.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-sgetmask/">sgetmask</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3), <code><a href="/docs/linux/man/3-bsd_signal/">bsd_signal</a></code>(3), <code><a href="/docs/linux/man/3-killpg/">killpg</a></code>(3), <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3), <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigset/">sigset</a></code>(3), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/3-sigvec/">sigvec</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/3-strsignal/">strsignal</a></code>(3), <code><a href="/docs/linux/man/3-swapcontext/">swapcontext</a></code>(3), <code><a href="/docs/linux/man/3-sysv_signal/">sysv_signal</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
