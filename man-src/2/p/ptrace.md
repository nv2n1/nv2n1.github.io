---
title: "ptrace(2)"
name: "ptrace"
section: "2"
letter: "p"
url: "/docs/linux/man/2-ptrace/"
description: "ptrace – process trace"
---

<h2 class="name">NAME</h2>
<p> ptrace &#8211; process trace </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ptrace.h&gt;
long ptrace(enum __ptrace_request request, pid_t pid,
            void *addr, void *data);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ptrace</code>() system call provides a means by which one process (the &quot;tracer&quot;) may observe and control the execution of another process (the &quot;tracee&quot;), and examine and change the tracee&#8217;s memory and registers. It is primarily used to implement breakpoint debugging and system call tracing. </p>
<p> A tracee first needs to be attached to the tracer. Attachment and subsequent commands are per thread: in a multithreaded process, every thread can be individually attached to a (potentially different) tracer, or left not attached and thus not debugged. Therefore, &quot;tracee&quot; always means &quot;(one) thread&quot;, never &quot;a (possibly multithreaded) process&quot;. Ptrace commands are always sent to a specific tracee using a call of the form </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_foo, pid, &#8230;) </p>
<p> where <i>pid</i> is the thread ID of the corresponding Linux thread. </p>
<p> (Note that in this page, a &quot;multithreaded process&quot; means a thread group consisting of threads created using the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_THREAD</code> flag.) </p>
<p> A process can initiate a trace by calling <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and having the resulting child do a <code>PTRACE_TRACEME</code>, followed (typically) by an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Alternatively, one process may commence tracing another process using <code>PTRACE_ATTACH</code> or <code>PTRACE_SEIZE</code>. </p>
<p> While being traced, the tracee will stop each time a signal is delivered, even if the signal is being ignored. (An exception is <code>SIGKILL</code>, which has its usual effect.) The tracer will be notified at its next call to <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) (or one of the related &quot;wait&quot; system calls); that call will return a <i>status</i> value containing information that indicates the cause of the stop in the tracee. While the tracee is stopped, the tracer can use various ptrace requests to inspect and modify the tracee. The tracer then causes the tracee to continue, optionally ignoring the delivered signal (or even delivering a different signal instead). </p>
<p> If the <code>PTRACE_O_TRACEEXEC</code> option is not in effect, all successful calls to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) by the traced process will cause it to be sent a <code>SIGTRAP</code> signal, giving the parent a chance to gain control before the new program begins execution. </p>
<p> When the tracer is finished tracing, it can cause the tracee to continue executing in a normal, untraced mode via <code>PTRACE_DETACH</code>. </p>
<p> The value of <i>request</i> determines the action to be performed:</p>
<dl>
<dt><code>PTRACE_TRACEME</code></p>
<dd> Indicate that this process is to be traced by its parent. A process probably shouldn&#8217;t make this request if its parent isn&#8217;t expecting to trace it. (<i>pid</i>, <i>addr</i>, and <i>data</i> are ignored.)</p>
<dt>
<dd> The <code>PTRACE_TRACEME</code> request is used only by the tracee; the remaining requests are used only by the tracer. In the following requests, <i>pid</i> specifies the thread ID of the tracee to be acted on. For requests other than <code>PTRACE_ATTACH</code>, <code>PTRACE_SEIZE</code>, <code>PTRACE_INTERRUPT</code>, and <code>PTRACE_KILL</code>, the tracee must be stopped.</p>
<dt><code>PTRACE_PEEKTEXT</code>, <code>PTRACE_PEEKDATA</code></p>
<dd> Read a word at the address <i>addr</i> in the tracee&#8217;s memory, returning the word as the result of the <code>ptrace</code>() call. Linux does not have separate text and data address spaces, so these two requests are currently equivalent. (<i>data</i> is ignored; but see NOTES.)</p>
<dt><code>PTRACE_PEEKUSER</code></p>
<dd> Read a word at offset <i>addr</i> in the tracee&#8217;s USER area, which holds the registers and other information about the process (see <i>&lt;sys/user.h&gt;</i>). The word is returned as the result of the <code>ptrace</code>() call. Typically, the offset must be word-aligned, though this might vary by architecture. See NOTES. (<i>data</i> is ignored; but see NOTES.)</p>
<dt><code>PTRACE_POKETEXT</code>, <code>PTRACE_POKEDATA</code></p>
<dd> Copy the word <i>data</i> to the address <i>addr</i> in the tracee&#8217;s memory. As for <code>PTRACE_PEEKTEXT</code> and <code>PTRACE_PEEKDATA</code>, these two requests are currently equivalent.</p>
<dt><code>PTRACE_POKEUSER</code></p>
<dd> Copy the word <i>data</i> to offset <i>addr</i> in the tracee&#8217;s USER area. As for <code>PTRACE_PEEKUSER</code>, the offset must typically be word-aligned. In order to maintain the integrity of the kernel, some modifications to the USER area are disallowed.</p>
<dt><code>PTRACE_GETREGS</code>, <code>PTRACE_GETFPREGS</code></p>
<dd> Copy the tracee&#8217;s general-purpose or floating-point registers, respectively, to the address <i>data</i> in the tracer. See <i>&lt;sys/user.h&gt;</i> for information on the format of this data. (<i>addr</i> is ignored.) Note that SPARC systems have the meaning of <i>data</i> and <i>addr</i> reversed; that is, <i>data</i> is ignored and the registers are copied to the address <i>addr</i>. <code>PTRACE_GETREGS</code> and <code>PTRACE_GETFPREGS</code> are not present on all architectures.</p>
<dt><code>PTRACE_GETREGSET</code> (since Linux 2.6.34)</p>
<dd> Read the tracee&#8217;s registers. <i>addr</i> specifies, in an architecture-dependent way, the type of registers to be read. <code>NT_PRSTATUS</code> (with numerical value 1) usually results in reading of general-purpose registers. If the CPU has, for example, floating-point and/or vector registers, they can be retrieved by setting <i>addr</i> to the corresponding <code>NT_foo</code> constant. <i>data</i> points to a <code>struct iovec</code>, which describes the destination buffer&#8217;s location and length. On return, the kernel modifies <code>iov.len</code> to indicate the actual number of bytes returned.</p>
<dt><code>PTRACE_SETREGS</code>, <code>PTRACE_SETFPREGS</code></p>
<dd> Modify the tracee&#8217;s general-purpose or floating-point registers, respectively, from the address <i>data</i> in the tracer. As for <code>PTRACE_POKEUSER</code>, some general-purpose register modifications may be disallowed. (<i>addr</i> is ignored.) Note that SPARC systems have the meaning of <i>data</i> and <i>addr</i> reversed; that is, <i>data</i> is ignored and the registers are copied from the address <i>addr</i>. <code>PTRACE_SETREGS</code> and <code>PTRACE_SETFPREGS</code> are not present on all architectures.</p>
<dt><code>PTRACE_SETREGSET</code> (since Linux 2.6.34)</p>
<dd> Modify the tracee&#8217;s registers. The meaning of <i>addr</i> and <i>data</i> is analogous to <code>PTRACE_GETREGSET</code>.</p>
<dt><code>PTRACE_GETSIGINFO</code> (since Linux 2.3.99-pre6)</p>
<dd> Retrieve information about the signal that caused the stop. Copy a <i>siginfo_t</i> structure (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) from the tracee to the address <i>data</i> in the tracer. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_SETSIGINFO</code> (since Linux 2.3.99-pre6)</p>
<dd> Set signal information: copy a <i>siginfo_t</i> structure from the address <i>data</i> in the tracer to the tracee. This will affect only signals that would normally be delivered to the tracee and were caught by the tracer. It may be difficult to tell these normal signals from synthetic signals generated by <code>ptrace</code>() itself. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_PEEKSIGINFO</code> (since Linux 3.10)</p>
<dd> Retrieve <i>siginfo_t</i> structures without removing signals from a queue. <i>addr</i> points to a <i>ptrace_peeksiginfo_args</i> structure that specifies the ordinal position from which copying of signals should start, and the number of signals to copy. <i>siginfo_t</i> structures are copied into the buffer pointed to by <i>data</i>. The return value contains the number of copied signals (zero indicates that there is no signal corresponding to the specified ordinal position). Within the returned <i>siginfo</i> structures, the <i>si_code</i> field includes information (<code>__SI_CHLD</code>, <code>__SI_FAULT</code>, etc.) that are not otherwise exposed to user space.</dl>
<p> struct ptrace_peeksiginfo_args {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 off;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ordinal position in queue at which<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to start copying signals&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 flags;&nbsp;<wbr>&nbsp;/*&nbsp;PTRACE_PEEKSIGINFO_SHARED or 0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s32 nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of signals to copy&nbsp;*/ };</p>
<dl>
<dt>
<dd> Currently, there is only one flag, <code>PTRACE_PEEKSIGINFO_SHARED</code>, for dumping signals from the process-wide signal queue. If this flag is not set, signals are read from the per-thread queue of the specified thread.</p>
<dt><code>PTRACE_GETSIGMASK</code> (since Linux 3.11)</p>
<dd> Place a copy of the mask of blocked signals (see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)) in the buffer pointed to by <i>data</i>, which should be a pointer to a buffer of type <i>sigset_t</i>. The <i>addr</i> argument contains the size of the buffer pointed to by <i>data</i> (i.e., <i>sizeof(sigset_t)</i>).</p>
<dt><code>PTRACE_SETSIGMASK</code> (since Linux 3.11)</p>
<dd> Change the mask of blocked signals (see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)) to the value specified in the buffer pointed to by <i>data</i>, which should be a pointer to a buffer of type <i>sigset_t</i>. The <i>addr</i> argument contains the size of the buffer pointed to by <i>data</i> (i.e., <i>sizeof(sigset_t)</i>).</p>
<dt><code>PTRACE_SETOPTIONS</code> (since Linux 2.4.6; see BUGS for caveats)</p>
<dd> Set ptrace options from <i>data</i>. (<i>addr</i> is ignored.) <i>data</i> is interpreted as a bit mask of options, which are specified by the following flags:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PTRACE_O_EXITKILL</code> (since Linux 3.8)</p>
<dd> Send a <code>SIGKILL</code> signal to the tracee if the tracer exits. This option is useful for ptrace jailers that want to ensure that tracees can never escape the tracer&#8217;s control.</p>
<dt><code>PTRACE_O_TRACECLONE</code> (since Linux 2.5.46)</p>
<dd> Stop the tracee at the next <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and automatically start tracing the newly cloned process, which will start with a <code>SIGSTOP</code>, or <code>PTRACE_EVENT_STOP</code> if <code>PTRACE_SEIZE</code> was used. A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_CLONE&lt;&lt;8))
</pre>
<dt>
<dd> The PID of the new process can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt>
<dd> This option may not catch <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) calls in all cases. If the tracee calls <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_VFORK</code> flag, <code>PTRACE_EVENT_VFORK</code> will be delivered instead if <code>PTRACE_O_TRACEVFORK</code> is set; otherwise if the tracee calls <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the exit signal set to <code>SIGCHLD</code>, <code>PTRACE_EVENT_FORK</code> will be delivered if <code>PTRACE_O_TRACEFORK</code> is set.</p>
<dt><code>PTRACE_O_TRACEEXEC</code> (since Linux 2.5.46)</p>
<dd> Stop the tracee at the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_EXEC&lt;&lt;8))
</pre>
<dt>
<dd> If the execing thread is not a thread group leader, the thread ID is reset to thread group leader&#8217;s ID before this stop. Since Linux 3.0, the former thread ID can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt><code>PTRACE_O_TRACEEXIT</code> (since Linux 2.5.60)</p>
<dd> Stop the tracee at exit. A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_EXIT&lt;&lt;8))
</pre>
<dt>
<dd> The tracee&#8217;s exit status can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt>
<dd> The tracee is stopped early during process exit, when registers are still available, allowing the tracer to see where the exit occurred, whereas the normal exit notification is done after the process is finished exiting. Even though context is available, the tracer cannot prevent the exit from happening at this point.</p>
<dt><code>PTRACE_O_TRACEFORK</code> (since Linux 2.5.46)</p>
<dd> Stop the tracee at the next <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and automatically start tracing the newly forked process, which will start with a <code>SIGSTOP</code>, or <code>PTRACE_EVENT_STOP</code> if <code>PTRACE_SEIZE</code> was used. A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_FORK&lt;&lt;8))
</pre>
<dt>
<dd> The PID of the new process can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt><code>PTRACE_O_TRACESYSGOOD</code> (since Linux 2.4.6)</p>
<dd> When delivering system call traps, set bit 7 in the signal number (i.e., deliver <i>SIGTRAP|0x80</i>). This makes it easy for the tracer to distinguish normal traps from those caused by a system call.</p>
<dt><code>PTRACE_O_TRACEVFORK</code> (since Linux 2.5.46)</p>
<dd> Stop the tracee at the next <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) and automatically start tracing the newly vforked process, which will start with a <code>SIGSTOP</code>, or <code>PTRACE_EVENT_STOP</code> if <code>PTRACE_SEIZE</code> was used. A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_VFORK&lt;&lt;8))
</pre>
<dt>
<dd> The PID of the new process can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt><code>PTRACE_O_TRACEVFORKDONE</code> (since Linux 2.5.60)</p>
<dd> Stop the tracee at the completion of the next <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2). A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_VFORK_DONE&lt;&lt;8))
</pre>
<dt>
<dd> The PID of the new process can (since Linux 2.6.18) be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt><code>PTRACE_O_TRACESECCOMP</code> (since Linux 3.5)</p>
<dd> Stop the tracee when a <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) <code>SECCOMP_RET_TRACE</code> rule is triggered. A <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) by the tracer will return a <i>status</i> value such that</p>
<dt>
<dd>
<pre>
  status&gt;&gt;8 == (SIGTRAP | (PTRACE_EVENT_SECCOMP&lt;&lt;8))
</pre>
<dt>
<dd> While this triggers a <code>PTRACE_EVENT</code> stop, it is similar to a syscall-enter-stop. For details, see the note on <code>PTRACE_EVENT_SECCOMP</code> below. The seccomp event message data (from the <code>SECCOMP_RET_DATA</code> portion of the seccomp filter rule) can be retrieved with <code>PTRACE_GETEVENTMSG</code>.</p>
<dt><code>PTRACE_O_SUSPEND_SECCOMP</code> (since Linux 4.3)</p>
<dd> Suspend the tracee&#8217;s seccomp protections. This applies regardless of mode, and can be used when the tracee has not yet installed seccomp filters. That is, a valid use case is to suspend a tracee&#8217;s seccomp protections before they are installed by the tracee, let the tracee install the filters, and then clear this flag when the filters should be resumed. Setting this option requires that the tracer have the <code>CAP_SYS_ADMIN</code> capability, not have any seccomp protections installed, and not have <code>PTRACE_O_SUSPEND_SECCOMP</code> set on itself.</dl>
</dl>
<dt><code>PTRACE_GETEVENTMSG</code> (since Linux 2.5.46)</p>
<dd> Retrieve a message (as an <i>unsigned long</i>) about the ptrace event that just happened, placing it at the address <i>data</i> in the tracer. For <code>PTRACE_EVENT_EXIT</code>, this is the tracee&#8217;s exit status. For <code>PTRACE_EVENT_FORK</code>, <code>PTRACE_EVENT_VFORK</code>, <code>PTRACE_EVENT_VFORK_DONE</code>, and <code>PTRACE_EVENT_CLONE</code>, this is the PID of the new process. For <code>PTRACE_EVENT_SECCOMP</code>, this is the <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) filter&#8217;s <code>SECCOMP_RET_DATA</code> associated with the triggered rule. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_CONT</code></p>
<dd> Restart the stopped tracee process. If <i>data</i> is nonzero, it is interpreted as the number of a signal to be delivered to the tracee; otherwise, no signal is delivered. Thus, for example, the tracer can control whether a signal sent to the tracee is delivered or not. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_SYSCALL</code>, <code>PTRACE_SINGLESTEP</code></p>
<dd> Restart the stopped tracee as for <code>PTRACE_CONT</code>, but arrange for the tracee to be stopped at the next entry to or exit from a system call, or after execution of a single instruction, respectively. (The tracee will also, as usual, be stopped upon receipt of a signal.) From the tracer&#8217;s perspective, the tracee will appear to have been stopped by receipt of a <code>SIGTRAP</code>. So, for <code>PTRACE_SYSCALL</code>, for example, the idea is to inspect the arguments to the system call at the first stop, then do another <code>PTRACE_SYSCALL</code> and inspect the return value of the system call at the second stop. The <i>data</i> argument is treated as for <code>PTRACE_CONT</code>. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_SET_SYSCALL</code> (since Linux 2.6.16)</p>
<dd> When in syscall-enter-stop, change the number of the system call that is about to be executed to the number specified in the <i>data</i> argument. The <i>addr</i> argument is ignored. This request is currently supported only on arm (and arm64, though only for backwards compatibility), but most other architectures have other means of accomplishing this (usually by changing the register that the userland code passed the system call number in).</p>
<dt><code>PTRACE_SYSEMU</code>, <code>PTRACE_SYSEMU_SINGLESTEP</code> (since Linux 2.6.14)</p>
<dd> For <code>PTRACE_SYSEMU</code>, continue and stop on entry to the next system call, which will not be executed. See the documentation on syscall-stops below. For <code>PTRACE_SYSEMU_SINGLESTEP</code>, do the same but also singlestep if not a system call. This call is used by programs like User Mode Linux that want to emulate all the tracee&#8217;s system calls. The <i>data</i> argument is treated as for <code>PTRACE_CONT</code>. The <i>addr</i> argument is ignored. These requests are currently supported only on x86.</p>
<dt><code>PTRACE_LISTEN</code> (since Linux 3.4)</p>
<dd> Restart the stopped tracee, but prevent it from executing. The resulting state of the tracee is similar to a process which has been stopped by a <code>SIGSTOP</code> (or other stopping signal). See the &quot;group-stop&quot; subsection for additional information. <code>PTRACE_LISTEN</code> works only on tracees attached by <code>PTRACE_SEIZE</code>.</p>
<dt><code>PTRACE_KILL</code></p>
<dd> Send the tracee a <code>SIGKILL</code> to terminate it. (<i>addr</i> and <i>data</i> are ignored.)</p>
<dt>
<dd> <i>This operation is deprecated; do not use it!</i> Instead, send a <code>SIGKILL</code> directly using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) or <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2). The problem with <code>PTRACE_KILL</code> is that it requires the tracee to be in signal-delivery-stop, otherwise it may not work (i.e., may complete successfully but won&#8217;t kill the tracee). By contrast, sending a <code>SIGKILL</code> directly has no such limitation.</p>
<dt><code>PTRACE_INTERRUPT</code> (since Linux 3.4)</p>
<dd> Stop a tracee. If the tracee is running or sleeping in kernel space and <code>PTRACE_SYSCALL</code> is in effect, the system call is interrupted and syscall-exit-stop is reported. (The interrupted system call is restarted when the tracee is restarted.) If the tracee was already stopped by a signal and <code>PTRACE_LISTEN</code> was sent to it, the tracee stops with <code>PTRACE_EVENT_STOP</code> and <i>WSTOPSIG(status)</i> returns the stop signal. If any other ptrace-stop is generated at the same time (for example, if a signal is sent to the tracee), this ptrace-stop happens. If none of the above applies (for example, if the tracee is running in user space), it stops with <code>PTRACE_EVENT_STOP</code> with <i>WSTOPSIG(status)</i> == <code>SIGTRAP</code>. <code>PTRACE_INTERRUPT</code> only works on tracees attached by <code>PTRACE_SEIZE</code>.</p>
<dt><code>PTRACE_ATTACH</code></p>
<dd> Attach to the process specified in <i>pid</i>, making it a tracee of the calling process. The tracee is sent a <code>SIGSTOP</code>, but will not necessarily have stopped by the completion of this call; use <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) to wait for the tracee to stop. See the &quot;Attaching and detaching&quot; subsection for additional information. (<i>addr</i> and <i>data</i> are ignored.)</p>
<dt>
<dd> Permission to perform a <code>PTRACE_ATTACH</code> is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_REALCREDS</code> check; see below.</p>
<dt><code>PTRACE_SEIZE</code> (since Linux 3.4)</p>
<dd> Attach to the process specified in <i>pid</i>, making it a tracee of the calling process. Unlike <code>PTRACE_ATTACH</code>, <code>PTRACE_SEIZE</code> does not stop the process. Group-stops are reported as <code>PTRACE_EVENT_STOP</code> and <i>WSTOPSIG(status)</i> returns the stop signal. Automatically attached children stop with <code>PTRACE_EVENT_STOP</code> and <i>WSTOPSIG(status)</i> returns <code>SIGTRAP</code> instead of having <code>SIGSTOP</code> signal delivered to them. <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) does not deliver an extra <code>SIGTRAP</code>. Only a <code>PTRACE_SEIZE</code>d process can accept <code>PTRACE_INTERRUPT</code> and <code>PTRACE_LISTEN</code> commands. The &quot;seized&quot; behavior just described is inherited by children that are automatically attached using <code>PTRACE_O_TRACEFORK</code>, <code>PTRACE_O_TRACEVFORK</code>, and <code>PTRACE_O_TRACECLONE</code>. <i>addr</i> must be zero. <i>data</i> contains a bit mask of ptrace options to activate immediately.</p>
<dt>
<dd> Permission to perform a <code>PTRACE_SEIZE</code> is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_REALCREDS</code> check; see below.</p>
<dt><code>PTRACE_SECCOMP_GET_FILTER</code> (since Linux 4.4)</p>
<dd> This operation allows the tracer to dump the tracee&#8217;s classic BPF filters.</p>
<dt>
<dd> <i>addr</i> is an integer specifying the index of the filter to be dumped. The most recently installed filter has the index 0. If <i>addr</i> is greater than the number of installed filters, the operation fails with the error <code>ENOENT</code>.</p>
<dt>
<dd> <i>data</i> is either a pointer to a <i>struct sock_filter</i> array that is large enough to store the BPF program, or NULL if the program is not to be stored.</p>
<dt>
<dd> Upon success, the return value is the number of instructions in the BPF program. If <i>data</i> was NULL, then this return value can be used to correctly size the <i>struct sock_filter</i> array passed in a subsequent call.</p>
<dt>
<dd> This operation fails with the error <code>EACCES</code> if the caller does not have the <code>CAP_SYS_ADMIN</code> capability or if the caller is in strict or filter seccomp mode. If the filter referred to by <i>addr</i> is not a classic BPF filter, the operation fails with the error <code>EMEDIUMTYPE</code>.</p>
<dt>
<dd> This operation is available if the kernel was configured with both the <code>CONFIG_SECCOMP_FILTER</code> and the <code>CONFIG_CHECKPOINT_RESTORE</code> options.</p>
<dt><code>PTRACE_DETACH</code></p>
<dd> Restart the stopped tracee as for <code>PTRACE_CONT</code>, but first detach from it. Under Linux, a tracee can be detached in this way regardless of which method was used to initiate tracing. (<i>addr</i> is ignored.)</p>
<dt><code>PTRACE_GET_THREAD_AREA</code> (since Linux 2.6.0)</p>
<dd> This operation performs a similar task to <code><a href="/docs/linux/man/2-get_thread_area/">get_thread_area</a></code>(2). It reads the TLS entry in the GDT whose index is given in <i>addr</i>, placing a copy of the entry into the <i>struct user_desc</i> pointed to by <i>data</i>. (By contrast with <code><a href="/docs/linux/man/2-get_thread_area/">get_thread_area</a></code>(2), the <i>entry_number</i> of the <i>struct user_desc</i> is ignored.)</p>
<dt><code>PTRACE_SET_THREAD_AREA</code> (since Linux 2.6.0)</p>
<dd> This operation performs a similar task to <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2). It sets the TLS entry in the GDT whose index is given in <i>addr</i>, assigning it the data supplied in the <i>struct user_desc</i> pointed to by <i>data</i>. (By contrast with <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2), the <i>entry_number</i> of the <i>struct user_desc</i> is ignored; in other words, this ptrace operation can&#8217;t be used to allocate a free TLS entry.)</p>
<dt><code>PTRACE_GET_SYSCALL_INFO</code> (since Linux 5.3)</p>
<dd> Retrieve information about the system call that caused the stop. The information is placed into the buffer pointed by the <i>data</i> argument, which should be a pointer to a buffer of type <i>struct ptrace_syscall_info</i>. The <i>addr</i> argument contains the size of the buffer pointed to by the <i>data</i> argument (i.e., <i>sizeof(struct ptrace_syscall_info)</i>). The return value contains the number of bytes available to be written by the kernel. If the size of the data to be written by the kernel exceeds the size specified by the <i>addr</i> argument, the output data is truncated.</p>
<dt>
<dd> The <i>ptrace_syscall_info</i> structure contains the following fields:</p>
<dt>
<dd> struct ptrace_syscal_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8 op;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type of system call stop&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 arch;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;AUDIT_ARCH_*&nbsp;value;&nbsp;see&nbsp;<a href="/docs/linux/man/2-seccomp/">seccomp</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 instruction_pointer;&nbsp;/*&nbsp;CPU instruction pointer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 stack_pointer;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;CPU stack pointer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;op&nbsp;==&nbsp;PTRACE_SYSCALL_INFO_ENTRY&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System call number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 args[6];&nbsp;<wbr>&nbsp;/*&nbsp;System call arguments&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;entry;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;op&nbsp;==&nbsp;PTRACE_SYSCALL_INFO_EXIT&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 rval;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System call return value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8 is_error;&nbsp;<wbr>&nbsp;/*&nbsp;System call error flag;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Boolean: does rval contain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;an error value&nbsp;(-ERRCODE)&nbsp;or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a nonerror return value?&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;exit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;op&nbsp;==&nbsp;PTRACE_SYSCALL_INFO_SECCOMP&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System call number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 args[6];&nbsp;<wbr>&nbsp;/*&nbsp;System call arguments&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 ret_data;&nbsp;/*&nbsp;SECCOMP_RET_DATA portion<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of SECCOMP_RET_TRACE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;seccomp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; };</p>
<dt>
<dd> The <i>op</i>, <i>arch</i>, <i>instruction_pointer</i>, and <i>stack_pointer</i> fields are defined for all kinds of ptrace system call stops. The rest of the structure is a union; one should read only those fields that are meaningful for the kind of system call stop specified by the <i>op</i> field.</p>
<dt>
<dd> The <i>op</i> field has one of the following values (defined in <i>&lt;linux/ptrace.h&gt;)</i> indicating what type of stop occurred and which part of the union is filled:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PTRACE_SYSCALL_INFO_ENTRY</code></p>
<dd> The <i>entry</i> component of the union contains information relating to a system call entry stop.</p>
<dt><code>PTRACE_SYSCALL_INFO_EXIT</code></p>
<dd> The <i>exit</i> component of the union contains information relating to a system call exit stop.</p>
<dt><code>PTRACE_SYSCALL_INFO_SECCOMP</code></p>
<dd> The <i>seccomp</i> component of the union contains information relating to a <code>PTRACE_EVENT_SECCOMP</code> stop.</p>
<dt><code>PTRACE_SYSCALL_INFO_NONE</code></p>
<dd> No component of the union contains relevant information.</dl>
</dl>
</dl>
<h3>Death under ptrace</h3>
<p> When a (possibly multithreaded) process receives a killing signal (one whose disposition is set to <code>SIG_DFL</code> and whose default action is to kill the process), all threads exit. Tracees report their death to their tracer(s). Notification of this event is delivered via <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2). </p>
<p> Note that the killing signal will first cause signal-delivery-stop (on one tracee only), and only after it is injected by the tracer (or after it was dispatched to a thread which isn&#8217;t traced), will death from the signal happen on <i>all</i> tracees within a multithreaded process. (The term &quot;signal-delivery-stop&quot; is explained below.) </p>
<p> <code>SIGKILL</code> does not generate signal-delivery-stop and therefore the tracer can&#8217;t suppress it. <code>SIGKILL</code> kills even within system calls (syscall-exit-stop is not generated prior to death by <code>SIGKILL</code>). The net effect is that <code>SIGKILL</code> always kills the process (all its threads), even if some threads of the process are ptraced. </p>
<p> When the tracee calls <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), it reports its death to its tracer. Other threads are not affected. </p>
<p> When any thread executes <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2), every tracee in its thread group reports its death to its tracer. </p>
<p> If the <code>PTRACE_O_TRACEEXIT</code> option is on, <code>PTRACE_EVENT_EXIT</code> will happen before actual death. This applies to exits via <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2), <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2), and signal deaths (except <code>SIGKILL</code>, depending on the kernel version; see BUGS below), and when threads are torn down on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in a multithreaded process. </p>
<p> The tracer cannot assume that the ptrace-stopped tracee exists. There are many scenarios when the tracee may die while stopped (such as <code>SIGKILL</code>). Therefore, the tracer must be prepared to handle an <code>ESRCH</code> error on any ptrace operation. Unfortunately, the same error is returned if the tracee exists but is not ptrace-stopped (for commands which require a stopped tracee), or if it is not traced by the process which issued the ptrace call. The tracer needs to keep track of the stopped/running state of the tracee, and interpret <code>ESRCH</code> as &quot;tracee died unexpectedly&quot; only if it knows that the tracee has been observed to enter ptrace-stop. Note that there is no guarantee that <i>waitpid(WNOHANG)</i> will reliably report the tracee&#8217;s death status if a ptrace operation returned <code>ESRCH</code>. <i>waitpid(WNOHANG)</i> may return 0 instead. In other words, the tracee may be &quot;not yet fully dead&quot;, but already refusing ptrace requests. </p>
<p> The tracer can&#8217;t assume that the tracee <i>always</i> ends its life by reporting <i>WIFEXITED(status)</i> or <i>WIFSIGNALED(status)</i>; there are cases where this does not occur. For example, if a thread other than thread group leader does an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), it disappears; its PID will never be seen again, and any subsequent ptrace stops will be reported under the thread group leader&#8217;s PID.</p>
<h3>Stopped states</h3>
<p> A tracee can be in two states: running or stopped. For the purposes of ptrace, a tracee which is blocked in a system call (such as <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), etc.) is nevertheless considered to be running, even if the tracee is blocked for a long time. The state of the tracee after <code>PTRACE_LISTEN</code> is somewhat of a gray area: it is not in any ptrace-stop (ptrace commands won&#8217;t work on it, and it will deliver <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) notifications), but it also may be considered &quot;stopped&quot; because it is not executing instructions (is not scheduled), and if it was in group-stop before <code>PTRACE_LISTEN</code>, it will not respond to signals until <code>SIGCONT</code> is received. </p>
<p> There are many kinds of states when the tracee is stopped, and in ptrace discussions they are often conflated. Therefore, it is important to use precise terms. </p>
<p> In this manual page, any stopped state in which the tracee is ready to accept ptrace commands from the tracer is called <i>ptrace-stop</i>. Ptrace-stops can be further subdivided into <i>signal-delivery-stop</i>, <i>group-stop</i>, <i>syscall-stop</i>, <i>PTRACE_EVENT stops</i>, and so on. These stopped states are described in detail below. </p>
<p> When the running tracee enters ptrace-stop, it notifies its tracer using <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) (or one of the other &quot;wait&quot; system calls). Most of this manual page assumes that the tracer waits with: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid&nbsp;=&nbsp;waitpid(pid_or_minus_1,&nbsp;&amp;status,&nbsp;__WALL); </p>
<p> Ptrace-stopped tracees are reported as returns with <i>pid</i> greater than 0 and <i>WIFSTOPPED(status)</i> true. </p>
<p> The <code>__WALL</code> flag does not include the <code>WSTOPPED</code> and <code>WEXITED</code> flags, but implies their functionality. </p>
<p> Setting the <code>WCONTINUED</code> flag when calling <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) is not recommended: the &quot;continued&quot; state is per-process and consuming it can confuse the real parent of the tracee. </p>
<p> Use of the <code>WNOHANG</code> flag may cause <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) to return 0 (&quot;no wait results available yet&quot;) even if the tracer knows there should be a notification. Example: </p>
<p> errno = 0; ptrace(PTRACE_CONT, pid, 0L, 0L); if (errno == ESRCH) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;tracee is dead&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r&nbsp;=&nbsp;waitpid(tracee,&nbsp;&amp;status,&nbsp;__WALL | WNOHANG);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;r can still be 0 here!&nbsp;*/ } </p>
<p> The following kinds of ptrace-stops exist: signal-delivery-stops, group-stops, <code>PTRACE_EVENT</code> stops, syscall-stops. They all are reported by <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) with <i>WIFSTOPPED(status)</i> true. They may be differentiated by examining the value <i>status&gt;&gt;8</i>, and if there is ambiguity in that value, by querying <code>PTRACE_GETSIGINFO</code>. (Note: the <i>WSTOPSIG(status)</i> macro can&#8217;t be used to perform this examination, because it returns the value <i>(status&gt;&gt;8)&nbsp;&amp;&nbsp;0xff</i>.)</p>
<h3>Signal-delivery-stop</h3>
<p> When a (possibly multithreaded) process receives any signal except <code>SIGKILL</code>, the kernel selects an arbitrary thread which handles the signal. (If the signal is generated with <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), the target thread can be explicitly selected by the caller.) If the selected thread is traced, it enters signal-delivery-stop. At this point, the signal is not yet delivered to the process, and can be suppressed by the tracer. If the tracer doesn&#8217;t suppress the signal, it passes the signal to the tracee in the next ptrace restart request. This second step of signal delivery is called <i>signal injection</i> in this manual page. Note that if the signal is blocked, signal-delivery-stop doesn&#8217;t happen until the signal is unblocked, with the usual exception that <code>SIGSTOP</code> can&#8217;t be blocked. </p>
<p> Signal-delivery-stop is observed by the tracer as <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) returning with <i>WIFSTOPPED(status)</i> true, with the signal returned by <i>WSTOPSIG(status)</i>. If the signal is <code>SIGTRAP</code>, this may be a different kind of ptrace-stop; see the &quot;Syscall-stops&quot; and &quot;execve&quot; sections below for details. If <i>WSTOPSIG(status)</i> returns a stopping signal, this may be a group-stop; see below.</p>
<h3>Signal injection and suppression</h3>
<p> After signal-delivery-stop is observed by the tracer, the tracer should restart the tracee with the call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_restart, pid, 0, sig) </p>
<p> where <code>PTRACE_restart</code> is one of the restarting ptrace requests. If <i>sig</i> is 0, then a signal is not delivered. Otherwise, the signal <i>sig</i> is delivered. This operation is called <i>signal injection</i> in this manual page, to distinguish it from signal-delivery-stop. </p>
<p> The <i>sig</i> value may be different from the <i>WSTOPSIG(status)</i> value: the tracer can cause a different signal to be injected. </p>
<p> Note that a suppressed signal still causes system calls to return prematurely. In this case, system calls will be restarted: the tracer will observe the tracee to reexecute the interrupted system call (or <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2) system call for a few system calls which use a different mechanism for restarting) if the tracer uses <code>PTRACE_SYSCALL</code>. Even system calls (such as <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)) which are not restartable after signal are restarted after signal is suppressed; however, kernel bugs exist which cause some system calls to fail with <code>EINTR</code> even though no observable signal is injected to the tracee. </p>
<p> Restarting ptrace commands issued in ptrace-stops other than signal-delivery-stop are not guaranteed to inject a signal, even if <i>sig</i> is nonzero. No error is reported; a nonzero <i>sig</i> may simply be ignored. Ptrace users should not try to &quot;create a new signal&quot; this way: use <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2) instead. </p>
<p> The fact that signal injection requests may be ignored when restarting the tracee after ptrace stops that are not signal-delivery-stops is a cause of confusion among ptrace users. One typical scenario is that the tracer observes group-stop, mistakes it for signal-delivery-stop, restarts the tracee with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_restart, pid, 0, stopsig) </p>
<p> with the intention of injecting <i>stopsig</i>, but <i>stopsig</i> gets ignored and the tracee continues to run. </p>
<p> The <code>SIGCONT</code> signal has a side effect of waking up (all threads of) a group-stopped process. This side effect happens before signal-delivery-stop. The tracer can&#8217;t suppress this side effect (it can only suppress signal injection, which only causes the <code>SIGCONT</code> handler to not be executed in the tracee, if such a handler is installed). In fact, waking up from group-stop may be followed by signal-delivery-stop for signal(s) <i>other than</i> <code>SIGCONT</code>, if they were pending when <code>SIGCONT</code> was delivered. In other words, <code>SIGCONT</code> may be not the first signal observed by the tracee after it was sent. </p>
<p> Stopping signals cause (all threads of) a process to enter group-stop. This side effect happens after signal injection, and therefore can be suppressed by the tracer. </p>
<p> In Linux 2.4 and earlier, the <code>SIGSTOP</code> signal can&#8217;t be injected. </p>
<p> <code>PTRACE_GETSIGINFO</code> can be used to retrieve a <i>siginfo_t</i> structure which corresponds to the delivered signal. <code>PTRACE_SETSIGINFO</code> may be used to modify it. If <code>PTRACE_SETSIGINFO</code> has been used to alter <i>siginfo_t</i>, the <i>si_signo</i> field and the <i>sig</i> parameter in the restarting command must match, otherwise the result is undefined.</p>
<h3>Group-stop</h3>
<p> When a (possibly multithreaded) process receives a stopping signal, all threads stop. If some threads are traced, they enter a group-stop. Note that the stopping signal will first cause signal-delivery-stop (on one tracee only), and only after it is injected by the tracer (or after it was dispatched to a thread which isn&#8217;t traced), will group-stop be initiated on <i>all</i> tracees within the multithreaded process. As usual, every tracee reports its group-stop separately to the corresponding tracer. </p>
<p> Group-stop is observed by the tracer as <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) returning with <i>WIFSTOPPED(status)</i> true, with the stopping signal available via <i>WSTOPSIG(status)</i>. The same result is returned by some other classes of ptrace-stops, therefore the recommended practice is to perform the call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_GETSIGINFO, pid, 0,&nbsp;&amp;siginfo) </p>
<p> The call can be avoided if the signal is not <code>SIGSTOP</code>, <code>SIGTSTP</code>, <code>SIGTTIN</code>, or <code>SIGTTOU</code>; only these four signals are stopping signals. If the tracer sees something else, it can&#8217;t be a group-stop. Otherwise, the tracer needs to call <code>PTRACE_GETSIGINFO</code>. If <code>PTRACE_GETSIGINFO</code> fails with <code>EINVAL</code>, then it is definitely a group-stop. (Other failure codes are possible, such as <code>ESRCH</code> (&quot;no such process&quot;) if a <code>SIGKILL</code> killed the tracee.) </p>
<p> If tracee was attached using <code>PTRACE_SEIZE</code>, group-stop is indicated by <code>PTRACE_EVENT_STOP</code>: <i>status&gt;&gt;16 == PTRACE_EVENT_STOP</i>. This allows detection of group-stops without requiring an extra <code>PTRACE_GETSIGINFO</code> call. </p>
<p> As of Linux 2.6.38, after the tracer sees the tracee ptrace-stop and until it restarts or kills it, the tracee will not run, and will not send notifications (except <code>SIGKILL</code> death) to the tracer, even if the tracer enters into another <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) call. </p>
<p> The kernel behavior described in the previous paragraph causes a problem with transparent handling of stopping signals. If the tracer restarts the tracee after group-stop, the stopping signal is effectively ignored&#8212;the tracee doesn&#8217;t remain stopped, it runs. If the tracer doesn&#8217;t restart the tracee before entering into the next <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), future <code>SIGCONT</code> signals will not be reported to the tracer; this would cause the <code>SIGCONT</code> signals to have no effect on the tracee. </p>
<p> Since Linux 3.4, there is a method to overcome this problem: instead of <code>PTRACE_CONT</code>, a <code>PTRACE_LISTEN</code> command can be used to restart a tracee in a way where it does not execute, but waits for a new event which it can report via <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) (such as when it is restarted by a <code>SIGCONT</code>).</p>
<h3>PTRACE_EVENT stops</h3>
<p> If the tracer sets <code>PTRACE_O_TRACE_*</code> options, the tracee will enter ptrace-stops called <code>PTRACE_EVENT</code> stops. </p>
<p> <code>PTRACE_EVENT</code> stops are observed by the tracer as <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) returning with <i>WIFSTOPPED(status)</i>, and <i>WSTOPSIG(status)</i> returns <code>SIGTRAP</code> (or for <code>PTRACE_EVENT_STOP</code>, returns the stopping signal if tracee is in a group-stop). An additional bit is set in the higher byte of the status word: the value <i>status&gt;&gt;8</i> will be </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;((PTRACE_EVENT_foo&lt;&lt;8)&nbsp;| SIGTRAP). </p>
<p> The following events exist:</p>
<dl>
<dt><code>PTRACE_EVENT_VFORK</code></p>
<dd> Stop before return from <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_VFORK</code> flag. When the tracee is continued after this stop, it will wait for child to exit/exec before continuing its execution (in other words, the usual behavior on <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2)).</p>
<dt><code>PTRACE_EVENT_FORK</code></p>
<dd> Stop before return from <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the exit signal set to <code>SIGCHLD</code>.</p>
<dt><code>PTRACE_EVENT_CLONE</code></p>
<dd> Stop before return from <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt><code>PTRACE_EVENT_VFORK_DONE</code></p>
<dd> Stop before return from <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_VFORK</code> flag, but after the child unblocked this tracee by exiting or execing.</dl>
<p> For all four stops described above, the stop occurs in the parent (i.e., the tracee), not in the newly created thread. <code>PTRACE_GETEVENTMSG</code> can be used to retrieve the new thread&#8217;s ID.</p>
<dl>
<dt><code>PTRACE_EVENT_EXEC</code></p>
<dd> Stop before return from <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Since Linux 3.0, <code>PTRACE_GETEVENTMSG</code> returns the former thread ID.</p>
<dt><code>PTRACE_EVENT_EXIT</code></p>
<dd> Stop before exit (including death from <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2)), signal death, or exit caused by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in a multithreaded process. <code>PTRACE_GETEVENTMSG</code> returns the exit status. Registers can be examined (unlike when &quot;real&quot; exit happens). The tracee is still alive; it needs to be <code>PTRACE_CONT</code>ed or <code>PTRACE_DETACH</code>ed to finish exiting.</p>
<dt><code>PTRACE_EVENT_STOP</code></p>
<dd> Stop induced by <code>PTRACE_INTERRUPT</code> command, or group-stop, or initial ptrace-stop when a new child is attached (only if attached using <code>PTRACE_SEIZE</code>).</p>
<dt><code>PTRACE_EVENT_SECCOMP</code></p>
<dd> Stop triggered by a <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) rule on tracee syscall entry when <code>PTRACE_O_TRACESECCOMP</code> has been set by the tracer. The seccomp event message data (from the <code>SECCOMP_RET_DATA</code> portion of the seccomp filter rule) can be retrieved with <code>PTRACE_GETEVENTMSG</code>. The semantics of this stop are described in detail in a separate section below.</dl>
<p> <code>PTRACE_GETSIGINFO</code> on <code>PTRACE_EVENT</code> stops returns <code>SIGTRAP</code> in <i>si_signo</i>, with <i>si_code</i> set to <i>(event&lt;&lt;8)&nbsp;| SIGTRAP</i>.</p>
<h3>Syscall-stops</h3>
<p> If the tracee was restarted by <code>PTRACE_SYSCALL</code> or <code>PTRACE_SYSEMU</code>, the tracee enters syscall-enter-stop just prior to entering any system call (which will not be executed if the restart was using <code>PTRACE_SYSEMU</code>, regardless of any change made to registers at this point or how the tracee is restarted after this stop). No matter which method caused the syscall-entry-stop, if the tracer restarts the tracee with <code>PTRACE_SYSCALL</code>, the tracee enters syscall-exit-stop when the system call is finished, or if it is interrupted by a signal. (That is, signal-delivery-stop never happens between syscall-enter-stop and syscall-exit-stop; it happens <i>after</i> syscall-exit-stop.). If the tracee is continued using any other method (including <code>PTRACE_SYSEMU</code>), no syscall-exit-stop occurs. Note that all mentions <code>PTRACE_SYSEMU</code> apply equally to <code>PTRACE_SYSEMU_SINGLESTEP</code>. </p>
<p> However, even if the tracee was continued using <code>PTRACE_SYSCALL</code>, it is not guaranteed that the next stop will be a syscall-exit-stop. Other possibilities are that the tracee may stop in a <code>PTRACE_EVENT</code> stop (including seccomp stops), exit (if it entered <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) or <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2)), be killed by <code>SIGKILL</code>, or die silently (if it is a thread group leader, the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) happened in another thread, and that thread is not traced by the same tracer; this situation is discussed later). </p>
<p> Syscall-enter-stop and syscall-exit-stop are observed by the tracer as <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) returning with <i>WIFSTOPPED(status)</i> true, and <i>WSTOPSIG(status)</i> giving <code>SIGTRAP</code>. If the <code>PTRACE_O_TRACESYSGOOD</code> option was set by the tracer, then <i>WSTOPSIG(status)</i> will give the value <i>(SIGTRAP | 0x80)</i>. </p>
<p> Syscall-stops can be distinguished from signal-delivery-stop with <code>SIGTRAP</code> by querying <code>PTRACE_GETSIGINFO</code> for the following cases:</p>
<dl>
<dt><i>si_code</i> &lt;= 0</p>
<dd> <code>SIGTRAP</code> was delivered as a result of a user-space action, for example, a system call (<code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), etc.), expiration of a POSIX timer, change of state on a POSIX message queue, or completion of an asynchronous I/O request.</p>
<dt><i>si_code</i> == SI_KERNEL (0x80)</p>
<dd> <code>SIGTRAP</code> was sent by the kernel.</p>
<dt><i>si_code</i> == SIGTRAP or <i>si_code</i> == (SIGTRAP|0x80)</p>
<dd> This is a syscall-stop.</dl>
<p> However, syscall-stops happen very often (twice per system call), and performing <code>PTRACE_GETSIGINFO</code> for every syscall-stop may be somewhat expensive. </p>
<p> Some architectures allow the cases to be distinguished by examining registers. For example, on x86, <i>rax</i> == &#8211;<code>ENOSYS</code> in syscall-enter-stop. Since <code>SIGTRAP</code> (like any other signal) always happens <i>after</i> syscall-exit-stop, and at this point <i>rax</i> almost never contains &#8211;<code>ENOSYS</code>, the <code>SIGTRAP</code> looks like &quot;syscall-stop which is not syscall-enter-stop&quot;; in other words, it looks like a &quot;stray syscall-exit-stop&quot; and can be detected this way. But such detection is fragile and is best avoided. </p>
<p> Using the <code>PTRACE_O_TRACESYSGOOD</code> option is the recommended method to distinguish syscall-stops from other kinds of ptrace-stops, since it is reliable and does not incur a performance penalty. </p>
<p> Syscall-enter-stop and syscall-exit-stop are indistinguishable from each other by the tracer. The tracer needs to keep track of the sequence of ptrace-stops in order to not misinterpret syscall-enter-stop as syscall-exit-stop or vice versa. In general, a syscall-enter-stop is always followed by syscall-exit-stop, <code>PTRACE_EVENT</code> stop, or the tracee&#8217;s death; no other kinds of ptrace-stop can occur in between. However, note that seccomp stops (see below) can cause syscall-exit-stops, without preceding syscall-entry-stops. If seccomp is in use, care needs to be taken not to misinterpret such stops as syscall-entry-stops. </p>
<p> If after syscall-enter-stop, the tracer uses a restarting command other than <code>PTRACE_SYSCALL</code>, syscall-exit-stop is not generated. </p>
<p> <code>PTRACE_GETSIGINFO</code> on syscall-stops returns <code>SIGTRAP</code> in <i>si_signo</i>, with <i>si_code</i> set to <code>SIGTRAP</code> or <i>(SIGTRAP|0x80)</i>.</p>
<h3>PTRACE_EVENT_SECCOMP stops (Linux 3.5 to 4.7)</h3>
<p> The behavior of <code>PTRACE_EVENT_SECCOMP</code> stops and their interaction with other kinds of ptrace stops has changed between kernel versions. This documents the behavior from their introduction until Linux 4.7 (inclusive). The behavior in later kernel versions is documented in the next section. </p>
<p> A <code>PTRACE_EVENT_SECCOMP</code> stop occurs whenever a <code>SECCOMP_RET_TRACE</code> rule is triggered. This is independent of which methods was used to restart the system call. Notably, seccomp still runs even if the tracee was restarted using <code>PTRACE_SYSEMU</code> and this system call is unconditionally skipped. </p>
<p> Restarts from this stop will behave as if the stop had occurred right before the system call in question. In particular, both <code>PTRACE_SYSCALL</code> and <code>PTRACE_SYSEMU</code> will normally cause a subsequent syscall-entry-stop. However, if after the <code>PTRACE_EVENT_SECCOMP</code> the system call number is negative, both the syscall-entry-stop and the system call itself will be skipped. This means that if the system call number is negative after a <code>PTRACE_EVENT_SECCOMP</code> and the tracee is restarted using <code>PTRACE_SYSCALL</code>, the next observed stop will be a syscall-exit-stop, rather than the syscall-entry-stop that might have been expected.</p>
<h3>PTRACE_EVENT_SECCOMP stops (since Linux 4.8)</h3>
<p> Starting with Linux 4.8, the <code>PTRACE_EVENT_SECCOMP</code> stop was reordered to occur between syscall-entry-stop and syscall-exit-stop. Note that seccomp no longer runs (and no <code>PTRACE_EVENT_SECCOMP</code> will be reported) if the system call is skipped due to <code>PTRACE_SYSEMU</code>. </p>
<p> Functionally, a <code>PTRACE_EVENT_SECCOMP</code> stop functions comparably to a syscall-entry-stop (i.e., continuations using <code>PTRACE_SYSCALL</code> will cause syscall-exit-stops, the system call number may be changed and any other modified registers are visible to the to-be-executed system call as well). Note that there may be, but need not have been a preceding syscall-entry-stop. </p>
<p> After a <code>PTRACE_EVENT_SECCOMP</code> stop, seccomp will be rerun, with a <code>SECCOMP_RET_TRACE</code> rule now functioning the same as a <code>SECCOMP_RET_ALLOW</code>. Specifically, this means that if registers are not modified during the <code>PTRACE_EVENT_SECCOMP</code> stop, the system call will then be allowed.</p>
<h3>PTRACE_SINGLESTEP stops</h3>
<p> [Details of these kinds of stops are yet to be documented.]</p>
<h3>Informational and restarting ptrace commands</h3>
<p> Most ptrace commands (all except <code>PTRACE_ATTACH</code>, <code>PTRACE_SEIZE</code>, <code>PTRACE_TRACEME</code>, <code>PTRACE_INTERRUPT</code>, and <code>PTRACE_KILL</code>) require the tracee to be in a ptrace-stop, otherwise they fail with <code>ESRCH</code>. </p>
<p> When the tracee is in ptrace-stop, the tracer can read and write data to the tracee using informational commands. These commands leave the tracee in ptrace-stopped state: </p>
<p> ptrace(PTRACE_PEEKTEXT/PEEKDATA/PEEKUSER, pid, addr, 0); ptrace(PTRACE_POKETEXT/POKEDATA/POKEUSER, pid, addr, long_val); ptrace(PTRACE_GETREGS/GETFPREGS, pid, 0, &amp;struct); ptrace(PTRACE_SETREGS/SETFPREGS, pid, 0, &amp;struct); ptrace(PTRACE_GETREGSET, pid, NT_foo, &amp;iov); ptrace(PTRACE_SETREGSET, pid, NT_foo, &amp;iov); ptrace(PTRACE_GETSIGINFO, pid, 0, &amp;siginfo); ptrace(PTRACE_SETSIGINFO, pid, 0, &amp;siginfo); ptrace(PTRACE_GETEVENTMSG, pid, 0, &amp;long_var); ptrace(PTRACE_SETOPTIONS, pid, 0, PTRACE_O_flags); </p>
<p> Note that some errors are not reported. For example, setting signal information (<i>siginfo</i>) may have no effect in some ptrace-stops, yet the call may succeed (return 0 and not set <i>errno</i>); querying <code>PTRACE_GETEVENTMSG</code> may succeed and return some random value if current ptrace-stop is not documented as returning a meaningful event message. </p>
<p> The call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_SETOPTIONS, pid, 0, PTRACE_O_flags); </p>
<p> affects one tracee. The tracee&#8217;s current flags are replaced. Flags are inherited by new tracees created and &quot;auto-attached&quot; via active <code>PTRACE_O_TRACEFORK</code>, <code>PTRACE_O_TRACEVFORK</code>, or <code>PTRACE_O_TRACECLONE</code> options. </p>
<p> Another group of commands makes the ptrace-stopped tracee run. They have the form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(cmd, pid, 0, sig); </p>
<p> where <i>cmd</i> is <code>PTRACE_CONT</code>, <code>PTRACE_LISTEN</code>, <code>PTRACE_DETACH</code>, <code>PTRACE_SYSCALL</code>, <code>PTRACE_SINGLESTEP</code>, <code>PTRACE_SYSEMU</code>, or <code>PTRACE_SYSEMU_SINGLESTEP</code>. If the tracee is in signal-delivery-stop, <i>sig</i> is the signal to be injected (if it is nonzero). Otherwise, <i>sig</i> may be ignored. (When restarting a tracee from a ptrace-stop other than signal-delivery-stop, recommended practice is to always pass 0 in <i>sig</i>.)</p>
<h3>Attaching and detaching</h3>
<p> A thread can be attached to the tracer using the call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_ATTACH, pid, 0, 0); </p>
<p> or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_SEIZE, pid, 0, PTRACE_O_flags); </p>
<p> <code>PTRACE_ATTACH</code> sends <code>SIGSTOP</code> to this thread. If the tracer wants this <code>SIGSTOP</code> to have no effect, it needs to suppress it. Note that if other signals are concurrently sent to this thread during attach, the tracer may see the tracee enter signal-delivery-stop with other signal(s) first! The usual practice is to reinject these signals until <code>SIGSTOP</code> is seen, then suppress <code>SIGSTOP</code> injection. The design bug here is that a ptrace attach and a concurrently delivered <code>SIGSTOP</code> may race and the concurrent <code>SIGSTOP</code> may be lost. </p>
<p> Since attaching sends <code>SIGSTOP</code> and the tracer usually suppresses it, this may cause a stray <code>EINTR</code> return from the currently executing system call in the tracee, as described in the &quot;Signal injection and suppression&quot; section. </p>
<p> Since Linux 3.4, <code>PTRACE_SEIZE</code> can be used instead of <code>PTRACE_ATTACH</code>. <code>PTRACE_SEIZE</code> does not stop the attached process. If you need to stop it after attach (or at any other time) without sending it any signals, use <code>PTRACE_INTERRUPT</code> command. </p>
<p> The request </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_TRACEME, 0, 0, 0); </p>
<p> turns the calling thread into a tracee. The thread continues to run (doesn&#8217;t enter ptrace-stop). A common practice is to follow the <code>PTRACE_TRACEME</code> with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;raise(SIGSTOP); </p>
<p> and allow the parent (which is our tracer now) to observe our signal-delivery-stop. </p>
<p> If the <code>PTRACE_O_TRACEFORK</code>, <code>PTRACE_O_TRACEVFORK</code>, or <code>PTRACE_O_TRACECLONE</code> options are in effect, then children created by, respectively, <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_VFORK</code> flag, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the exit signal set to <code>SIGCHLD</code>, and other kinds of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), are automatically attached to the same tracer which traced their parent. <code>SIGSTOP</code> is delivered to the children, causing them to enter signal-delivery-stop after they exit the system call which created them. </p>
<p> Detaching of the tracee is performed by: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ptrace(PTRACE_DETACH, pid, 0, sig); </p>
<p> <code>PTRACE_DETACH</code> is a restarting operation; therefore it requires the tracee to be in ptrace-stop. If the tracee is in signal-delivery-stop, a signal can be injected. Otherwise, the <i>sig</i> parameter may be silently ignored. </p>
<p> If the tracee is running when the tracer wants to detach it, the usual solution is to send <code>SIGSTOP</code> (using <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), to make sure it goes to the correct thread), wait for the tracee to stop in signal-delivery-stop for <code>SIGSTOP</code> and then detach it (suppressing <code>SIGSTOP</code> injection). A design bug is that this can race with concurrent <code>SIGSTOP</code>s. Another complication is that the tracee may enter other ptrace-stops and needs to be restarted and waited for again, until <code>SIGSTOP</code> is seen. Yet another complication is to be sure that the tracee is not already ptrace-stopped, because no signal delivery happens while it is&#8212;not even <code>SIGSTOP</code>. </p>
<p> If the tracer dies, all tracees are automatically detached and restarted, unless they were in group-stop. Handling of restart from group-stop is currently buggy, but the &quot;as planned&quot; behavior is to leave tracee stopped and waiting for <code>SIGCONT</code>. If the tracee is restarted from signal-delivery-stop, the pending signal is injected.</p>
<h3><a href="/docs/linux/man/2-execve/">execve</a>(2) under ptrace</h3>
<p> When one thread in a multithreaded process calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the kernel destroys all other threads in the process, and resets the thread ID of the execing thread to the thread group ID (process ID). (Or, to put things another way, when a multithreaded process does an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), at completion of the call, it appears as though the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) occurred in the thread group leader, regardless of which thread did the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).) This resetting of the thread ID looks very confusing to tracers:</p>
<dl>
<dt>*</p>
<dd> All other threads stop in <code>PTRACE_EVENT_EXIT</code> stop, if the <code>PTRACE_O_TRACEEXIT</code> option was turned on. Then all other threads except the thread group leader report death as if they exited via <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) with exit code 0.</p>
<dt>*</p>
<dd> The execing tracee changes its thread ID while it is in the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). (Remember, under ptrace, the &quot;pid&quot; returned from <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), or fed into ptrace calls, is the tracee&#8217;s thread ID.) That is, the tracee&#8217;s thread ID is reset to be the same as its process ID, which is the same as the thread group leader&#8217;s thread ID.</p>
<dt>*</p>
<dd> Then a <code>PTRACE_EVENT_EXEC</code> stop happens, if the <code>PTRACE_O_TRACEEXEC</code> option was turned on.</p>
<dt>*</p>
<dd> If the thread group leader has reported its <code>PTRACE_EVENT_EXIT</code> stop by this time, it appears to the tracer that the dead thread leader &quot;reappears from nowhere&quot;. (Note: the thread group leader does not report death via <i>WIFEXITED(status)</i> until there is at least one other live thread. This eliminates the possibility that the tracer will see it dying and then reappearing.) If the thread group leader was still alive, for the tracer this may look as if thread group leader returns from a different system call than it entered, or even &quot;returned from a system call even though it was not in any system call&quot;. If the thread group leader was not traced (or was traced by a different tracer), then during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) it will appear as if it has become a tracee of the tracer of the execing tracee.</dl>
<p> All of the above effects are the artifacts of the thread ID change in the tracee. </p>
<p> The <code>PTRACE_O_TRACEEXEC</code> option is the recommended tool for dealing with this situation. First, it enables <code>PTRACE_EVENT_EXEC</code> stop, which occurs before <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) returns. In this stop, the tracer can use <code>PTRACE_GETEVENTMSG</code> to retrieve the tracee&#8217;s former thread ID. (This feature was introduced in Linux 3.0.) Second, the <code>PTRACE_O_TRACEEXEC</code> option disables legacy <code>SIGTRAP</code> generation on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> When the tracer receives <code>PTRACE_EVENT_EXEC</code> stop notification, it is guaranteed that except this tracee and the thread group leader, no other threads from the process are alive. </p>
<p> On receiving the <code>PTRACE_EVENT_EXEC</code> stop notification, the tracer should clean up all its internal data structures describing the threads of this process, and retain only one data structure&#8212;one which describes the single still running tracee, with </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;thread ID&nbsp;==&nbsp;thread group ID&nbsp;==&nbsp;process ID. </p>
<p> Example: two threads call <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) at the same time: </p>
<pre><code>
*** we get syscall-enter-stop in thread 1: **
PID1 execve("/bin/foo", "foo" &lt;unfinished ...&gt;
*** we issue PTRACE_SYSCALL for thread 1 **
*** we get syscall-enter-stop in thread 2: **
PID2 execve("/bin/bar", "bar" &lt;unfinished ...&gt;
*** we issue PTRACE_SYSCALL for thread 2 **
*** we get PTRACE_EVENT_EXEC for PID0, we issue PTRACE_SYSCALL **
*** we get syscall-exit-stop for PID0: **
PID0 &lt;... execve resumed&gt; )             = 0
</code></pre>
<p> If the <code>PTRACE_O_TRACEEXEC</code> option is <i>not</i> in effect for the execing tracee, and if the tracee was <code>PTRACE_ATTACH</code>ed rather that <code>PTRACE_SEIZE</code>d, the kernel delivers an extra <code>SIGTRAP</code> to the tracee after <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) returns. This is an ordinary signal (similar to one which can be generated by <i>kill -TRAP</i>), not a special kind of ptrace-stop. Employing <code>PTRACE_GETSIGINFO</code> for this signal returns <i>si_code</i> set to 0 (<i>SI_USER</i>). This signal may be blocked by signal mask, and thus may be delivered (much) later. </p>
<p> Usually, the tracer (for example, <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1)) would not want to show this extra post-execve <code>SIGTRAP</code> signal to the user, and would suppress its delivery to the tracee (if <code>SIGTRAP</code> is set to <code>SIG_DFL</code>, it is a killing signal). However, determining <i>which</i> <code>SIGTRAP</code> to suppress is not easy. Setting the <code>PTRACE_O_TRACEEXEC</code> option or using <code>PTRACE_SEIZE</code> and thus suppressing this extra <code>SIGTRAP</code> is the recommended approach.</p>
<h3>Real parent</h3>
<p> The ptrace API (ab)uses the standard UNIX parent/child signaling over <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2). This used to cause the real parent of the process to stop receiving several kinds of <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) notifications when the child process is traced by some other process. </p>
<p> Many of these bugs have been fixed, but as of Linux 2.6.38 several still exist; see BUGS below. </p>
<p> As of Linux 2.6.38, the following is believed to work correctly:</p>
<dl>
<dt>*</p>
<dd> exit/death by signal is reported first to the tracer, then, when the tracer consumes the <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) result, to the real parent (to the real parent only when the whole multithreaded process exits). If the tracer and the real parent are the same process, the report is sent only once.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the <code>PTRACE_PEEK*</code> requests return the requested data (but see NOTES), the <code>PTRACE_SECCOMP_GET_FILTER</code> request returns the number of instructions in the BPF program, and other requests return zero. </p>
<p> On error, all requests return -1, and <i>errno</i> is set appropriately. Since the value returned by a successful <code>PTRACE_PEEK*</code> request may be -1, the caller must clear <i>errno</i> before the call, and then check it afterward to determine whether or not an error occurred.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBUSY</code></p>
<dd> (i386 only) There was an error with allocating or freeing a debug register.</p>
<dt><code>EFAULT</code></p>
<dd> There was an attempt to read from or write to an invalid area in the tracer&#8217;s or the tracee&#8217;s memory, probably because the area wasn&#8217;t mapped or accessible. Unfortunately, under Linux, different variations of this fault will return <code>EIO</code> or <code>EFAULT</code> more or less arbitrarily.</p>
<dt><code>EINVAL</code></p>
<dd> An attempt was made to set an invalid option.</p>
<dt><code>EIO</code></p>
<dd> <i>request</i> is invalid, or an attempt was made to read from or write to an invalid area in the tracer&#8217;s or the tracee&#8217;s memory, or there was a word-alignment violation, or an invalid signal was specified during a restart request.</p>
<dt><code>EPERM</code></p>
<dd> The specified process cannot be traced. This could be because the tracer has insufficient privileges (the required capability is <code>CAP_SYS_PTRACE</code>); unprivileged processes cannot trace processes that they cannot send signals to or those running set-user-ID/set-group-ID programs, for obvious reasons. Alternatively, the process may already be being traced, or (on kernels before 2.6.26) be <code><a href="/docs/linux/man/1-init/">init</a></code>(1) (PID 1).</p>
<dt><code>ESRCH</code></p>
<dd> The specified process does not exist, or is not currently being traced by the caller, or is not stopped (for requests that require a stopped tracee).</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Although arguments to <code>ptrace</code>() are interpreted according to the prototype given, glibc currently declares <code>ptrace</code>() as a variadic function with only the <i>request</i> argument fixed. It is recommended to always supply four arguments, even if the requested operation does not use them, setting unused/ignored arguments to <i>0L</i> or <i>(void&nbsp;*)&nbsp;0.</i> </p>
<p> In Linux kernels before 2.6.26, <code><a href="/docs/linux/man/1-init/">init</a></code>(1), the process with PID 1, may not be traced. </p>
<p> A tracees parent continues to be the tracer even if that tracer calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The layout of the contents of memory and the USER area are quite operating-system- and architecture-specific. The offset supplied, and the data returned, might not entirely match with the definition of <i>struct user</i>. </p>
<p> The size of a &quot;word&quot; is determined by the operating-system variant (e.g., for 32-bit Linux it is 32 bits). </p>
<p> This page documents the way the <code>ptrace</code>() call works currently in Linux. Its behavior differs significantly on other flavors of UNIX. In any case, use of <code>ptrace</code>() is highly specific to the operating system and architecture.</p>
<h3>Ptrace access mode checking</h3>
<p> Various parts of the kernel-user-space API (not just <code>ptrace</code>() operations), require so-called &quot;ptrace access mode&quot; checks, whose outcome determines whether an operation is permitted (or, in a few cases, causes a &quot;read&quot; operation to return sanitized data). These checks are performed in cases where one process can inspect sensitive information about, or in some cases modify the state of, another process. The checks are based on factors such as the credentials and capabilities of the two processes, whether or not the &quot;target&quot; process is dumpable, and the results of checks performed by any enabled Linux Security Module (LSM)&#8212;for example, SELinux, Yama, or Smack&#8212;and by the commoncap LSM (which is always invoked). </p>
<p> Prior to Linux 2.6.27, all access checks were of a single type. Since Linux 2.6.27, two access mode levels are distinguished:</p>
<dl>
<dt><code>PTRACE_MODE_READ</code></p>
<dd> For &quot;read&quot; operations or other operations that are less dangerous, such as: <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2); <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2); reading <i>/proc/[pid]/auxv</i>, <i>/proc/[pid]/environ</i>, or <i>/proc/[pid]/stat</i>; or <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) of a <i>/proc/[pid]/ns/*</i> file.</p>
<dt><code>PTRACE_MODE_ATTACH</code></p>
<dd> For &quot;write&quot; operations, or other operations that are more dangerous, such as: ptrace attaching (<code>PTRACE_ATTACH</code>) to another process or calling <code><a href="/docs/linux/man/2-process_vm_writev/">process_vm_writev</a></code>(2). (<code>PTRACE_MODE_ATTACH</code> was effectively the default before Linux 2.6.27.)</dl>
<p> Since Linux 4.5, the above access mode checks are combined (ORed) with one of the following modifiers:</p>
<dl>
<dt><code>PTRACE_MODE_FSCREDS</code></p>
<dd> Use the caller&#8217;s filesystem UID and GID (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)) or effective capabilities for LSM checks.</p>
<dt><code>PTRACE_MODE_REALCREDS</code></p>
<dd> Use the caller&#8217;s real UID and GID or permitted capabilities for LSM checks. This was effectively the default before Linux 4.5.</dl>
<p> Because combining one of the credential modifiers with one of the aforementioned access modes is typical, some macros are defined in the kernel sources for the combinations:</p>
<dl>
<dt><code>PTRACE_MODE_READ_FSCREDS</code></p>
<dd> Defined as <code>PTRACE_MODE_READ | PTRACE_MODE_FSCREDS</code>.</p>
<dt><code>PTRACE_MODE_READ_REALCREDS</code></p>
<dd> Defined as <code>PTRACE_MODE_READ | PTRACE_MODE_REALCREDS</code>.</p>
<dt><code>PTRACE_MODE_ATTACH_FSCREDS</code></p>
<dd> Defined as <code>PTRACE_MODE_ATTACH | PTRACE_MODE_FSCREDS</code>.</p>
<dt><code>PTRACE_MODE_ATTACH_REALCREDS</code></p>
<dd> Defined as <code>PTRACE_MODE_ATTACH | PTRACE_MODE_REALCREDS</code>.</dl>
<p> One further modifier can be ORed with the access mode:</p>
<dl>
<dt><code>PTRACE_MODE_NOAUDIT</code> (since Linux 3.3)</p>
<dd> Don&#8217;t audit this access mode check. This modifier is employed for ptrace access mode checks (such as checks when reading <i>/proc/[pid]/stat</i>) that merely cause the output to be filtered or sanitized, rather than causing an error to be returned to the caller. In these cases, accessing the file is not a security violation and there is no reason to generate a security audit record. This modifier suppresses the generation of such an audit record for the particular access check.</dl>
<p> Note that all of the <code>PTRACE_MODE_*</code> constants described in this subsection are kernel-internal, and not visible to user space. The constant names are mentioned here in order to label the various kinds of ptrace access mode checks that are performed for various system calls and accesses to various pseudofiles (e.g., under <i>/proc</i>). These names are used in other manual pages to provide a simple shorthand for labeling the different kernel checks. </p>
<p> The algorithm employed for ptrace access mode checking determines whether the calling process is allowed to perform the corresponding action on the target process. (In the case of opening <i>/proc/[pid]</i> files, the &quot;calling process&quot; is the one opening the file, and the process with the corresponding PID is the &quot;target process&quot;.) The algorithm is as follows:</p>
<dl>
<dt>1.</p>
<dd> If the calling thread and the target thread are in the same thread group, access is always allowed.</p>
<dt>2.</p>
<dd> If the access mode specifies <code>PTRACE_MODE_FSCREDS</code>, then, for the check in the next step, employ the caller&#8217;s filesystem UID and GID. (As noted in <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), the filesystem UID and GID almost always have the same values as the corresponding effective IDs.)</p>
<dt>
<dd> Otherwise, the access mode specifies <code>PTRACE_MODE_REALCREDS</code>, so use the caller&#8217;s real UID and GID for the checks in the next step. (Most APIs that check the caller&#8217;s UID and GID use the effective IDs. For historical reasons, the <code>PTRACE_MODE_REALCREDS</code> check uses the real IDs instead.)</p>
<dt>3.</p>
<dd> Deny access if <i>neither</i> of the following is true:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The real, effective, and saved-set user IDs of the target match the caller&#8217;s user ID, <i>and</i> the real, effective, and saved-set group IDs of the target match the caller&#8217;s group ID.</p>
<dt>&bull;</p>
<dd> The caller has the <code>CAP_SYS_PTRACE</code> capability in the user namespace of the target.</dl>
</dl>
<dt>4.</p>
<dd> Deny access if the target process &quot;dumpable&quot; attribute has a value other than 1 (<code>SUID_DUMP_USER</code>; see the discussion of <code>PR_SET_DUMPABLE</code> in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2)), and the caller does not have the <code>CAP_SYS_PTRACE</code> capability in the user namespace of the target process.</p>
<dt>5.</p>
<dd> The kernel LSM <i>security_ptrace_access_check</i>() interface is invoked to see if ptrace access is permitted. The results depend on the LSM(s). The implementation of this interface in the commoncap LSM performs the following steps:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a)</p>
<dd> If the access mode includes <code>PTRACE_MODE_FSCREDS</code>, then use the caller&#8217;s <i>effective</i> capability set in the following check; otherwise (the access mode specifies <code>PTRACE_MODE_REALCREDS</code>, so) use the caller&#8217;s <i>permitted</i> capability set.</p>
<dt>b)</p>
<dd> Deny access if <i>neither</i> of the following is true:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The caller and the target process are in the same user namespace, and the caller&#8217;s capabilities are a superset of the target process&#8217;s <i>permitted</i> capabilities.</p>
<dt>&bull;</p>
<dd> The caller has the <code>CAP_SYS_PTRACE</code> capability in the target process&#8217;s user namespace.</dl>
</dl>
<dt>
<dd> Note that the commoncap LSM does not distinguish between <code>PTRACE_MODE_READ</code> and <code>PTRACE_MODE_ATTACH</code>.</dl>
</dl>
<dt>6.</p>
<dd> If access has not been denied by any of the preceding steps, then access is allowed.</dl>
<h3>/proc/sys/kernel/yama/ptrace_scope</h3>
<p> On systems with the Yama Linux Security Module (LSM) installed (i.e., the kernel was configured with <code>CONFIG_SECURITY_YAMA</code>), the <i>/proc/sys/kernel/yama/ptrace_scope</i> file (available since Linux 3.4) can be used to restrict the ability to trace a process with <code>ptrace</code>() (and thus also the ability to use tools such as <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1) and <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1)). The goal of such restrictions is to prevent attack escalation whereby a compromised process can ptrace-attach to other sensitive processes (e.g., a GPG agent or an SSH session) owned by the user in order to gain additional credentials that may exist in memory and thus expand the scope of the attack. </p>
<p> More precisely, the Yama LSM limits two types of operations:</p>
<dl>
<dt>*</p>
<dd> Any operation that performs a ptrace access mode <code>PTRACE_MODE_ATTACH</code> check&#8212;for example, <code>ptrace</code>() <code>PTRACE_ATTACH</code>. (See the &quot;Ptrace access mode checking&quot; discussion above.)</p>
<dt>*</p>
<dd> <code>ptrace</code>() <code>PTRACE_TRACEME</code>.</dl>
<p> A process that has the <code>CAP_SYS_PTRACE</code> capability can update the <i>/proc/sys/kernel/yama/ptrace_scope</i> file with one of the following values:</p>
<dl>
<dt>0 (&quot;classic ptrace permissions&quot;)</p>
<dd> No additional restrictions on operations that perform <code>PTRACE_MODE_ATTACH</code> checks (beyond those imposed by the commoncap and other LSMs).</p>
<dt>
<dd> The use of <code>PTRACE_TRACEME</code> is unchanged.</p>
<dt>1 (&quot;restricted ptrace&quot;) [default value]</p>
<dd> When performing an operation that requires a <code>PTRACE_MODE_ATTACH</code> check, the calling process must either have the <code>CAP_SYS_PTRACE</code> capability in the user namespace of the target process or it must have a predefined relationship with the target process. By default, the predefined relationship is that the target process must be a descendant of the caller.</p>
<dt>
<dd> A target process can employ the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_PTRACER</code> operation to declare an additional PID that is allowed to perform <code>PTRACE_MODE_ATTACH</code> operations on the target. See the kernel source file <i>Documentation/admin-guide/LSM/Yama.rst</i> (or <i>Documentation/security/Yama.txt</i> before Linux 4.13) for further details.</p>
<dt>
<dd> The use of <code>PTRACE_TRACEME</code> is unchanged.</p>
<dt>2 (&quot;admin-only attach&quot;)</p>
<dd> Only processes with the <code>CAP_SYS_PTRACE</code> capability in the user namespace of the target process may perform <code>PTRACE_MODE_ATTACH</code> operations or trace children that employ <code>PTRACE_TRACEME</code>.</p>
<dt>3 (&quot;no attach&quot;)</p>
<dd> No process may perform <code>PTRACE_MODE_ATTACH</code> operations or trace children that employ <code>PTRACE_TRACEME</code>.</p>
<dt>
<dd> Once this value has been written to the file, it cannot be changed.</dl>
<p> With respect to values 1 and 2, note that creating a new user namespace effectively removes the protection offered by Yama. This is because a process in the parent user namespace whose effective UID matches the UID of the creator of a child namespace has all capabilities (including <code>CAP_SYS_PTRACE</code>) when performing operations within the child user namespace (and further-removed descendants of that namespace). Consequently, when a process tries to use user namespaces to sandbox itself, it inadvertently weakens the protections offered by the Yama LSM.</p>
<h3>C library/kernel differences</h3>
<p> At the system call level, the <code>PTRACE_PEEKTEXT</code>, <code>PTRACE_PEEKDATA</code>, and <code>PTRACE_PEEKUSER</code> requests have a different API: they store the result at the address specified by the <i>data</i> parameter, and the return value is the error flag. The glibc wrapper function provides the API given in DESCRIPTION above, with the result being returned via the function return value.</p>
<h2>BUGS</h2>
<p> On hosts with 2.6 kernel headers, <code>PTRACE_SETOPTIONS</code> is declared with a different value than the one for 2.4. This leads to applications compiled with 2.6 kernel headers failing when run on 2.4 kernels. This can be worked around by redefining <code>PTRACE_SETOPTIONS</code> to <code>PTRACE_OLDSETOPTIONS</code>, if that is defined. </p>
<p> Group-stop notifications are sent to the tracer, but not to real parent. Last confirmed on 2.6.38.6. </p>
<p> If a thread group leader is traced and exits by calling <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), a <code>PTRACE_EVENT_EXIT</code> stop will happen for it (if requested), but the subsequent <code>WIFEXITED</code> notification will not be delivered until all other threads exit. As explained above, if one of other threads calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the death of the thread group leader will <i>never</i> be reported. If the execed thread is not traced by this tracer, the tracer will never know that <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) happened. One possible workaround is to <code>PTRACE_DETACH</code> the thread group leader instead of restarting it in this case. Last confirmed on 2.6.38.6. </p>
<p> A <code>SIGKILL</code> signal may still cause a <code>PTRACE_EVENT_EXIT</code> stop before actual signal death. This may be changed in the future; <code>SIGKILL</code> is meant to always immediately kill tasks even under ptrace. Last confirmed on Linux 3.13. </p>
<p> Some system calls return with <code>EINTR</code> if a signal was sent to a tracee, but delivery was suppressed by the tracer. (This is very typical operation: it is usually done by debuggers on every attach, in order to not introduce a bogus <code>SIGSTOP</code>). As of Linux 3.2.9, the following system calls are affected (this list is likely incomplete): <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), and <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from an <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) file descriptor. The usual symptom of this bug is that when you attach to a quiescent process with the command </p>
<p> strace -p &lt;process-ID&gt; </p>
<p> then, instead of the usual and expected one-line output such as </p>
<p> restart_syscall(&lt;&#8230; resuming interrupted call &#8230;&gt;_ </p>
<p> or </p>
<p> select(6, [5], NULL, [5], NULL_ </p>
<p> (&#8216;_&#8217; denotes the cursor position), you observe more than one line. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_gettime(CLOCK_MONOTONIC,&nbsp;{15370, 690928118})&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;epoll_wait(4,_ </p>
<p> What is not visible here is that the process was blocked in <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) before <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1) has attached to it. Attaching caused <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) to return to user space with the error <code>EINTR</code>. In this particular case, the program reacted to <code>EINTR</code> by checking the current time, and then executing <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) again. (Programs which do not expect such &quot;stray&quot; <code>EINTR</code> errors may behave in an unintended way upon an <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1) attach.) </p>
<p> Contrary to the normal rules, the glibc wrapper for <code>ptrace</code>() can set <i>errno</i> to zero.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-ltrace/">ltrace</a></code>(1), <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
