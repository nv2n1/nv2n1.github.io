---
title: "sigaction(2)"
name: "sigaction"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sigaction/"
description: "sigaction, rt_sigaction – examine and change a signal action"
---

<h2 class="name">NAME</h2>
<p> sigaction, rt_sigaction &#8211; examine and change a signal action </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;signal.h&gt;
int sigaction(int signum, const struct sigaction *act,
              struct sigaction *oldact);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sigaction</code>(): _POSIX_C_SOURCE </p>
<p> <i>siginfo_t</i>: _POSIX_C_SOURCE &gt;= 199309L</p>
<h2>DESCRIPTION</h2>
<p> The <code>sigaction</code>() system call is used to change the action taken by a process on receipt of a specific signal. (See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for an overview of signals.) </p>
<p> <i>signum</i> specifies the signal and can be any valid signal except <code>SIGKILL</code> and <code>SIGSTOP</code>. </p>
<p> If <i>act</i> is non-NULL, the new action for signal <i>signum</i> is installed from <i>act</i>. If <i>oldact</i> is non-NULL, the previous action is saved in <i>oldact</i>. </p>
<p> The <i>sigaction</i> structure is defined as something like: </p>
<p> struct sigaction {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*sa_handler)(int);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*sa_sigaction)(int, siginfo_t&nbsp;*, void&nbsp;*);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigset_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*sa_restorer)(void); }; </p>
<p> On some architectures a union is involved: do not assign to both <i>sa_handler</i> and <i>sa_sigaction</i>. </p>
<p> The <i>sa_restorer</i> field is not intended for application use. (POSIX does not specify a <i>sa_restorer</i> field.) Some further details of the purpose of this field can be found in <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2). </p>
<p> <i>sa_handler</i> specifies the action to be associated with <i>signum</i> and is be one of the following:</p>
<dl>
<dt>*</p>
<dd> <code>SIG_DFL</code> for the default action.</p>
<dt>*</p>
<dd> <code>SIG_IGN</code> to ignore this signal.</p>
<dt>*</p>
<dd> A pointer to a signal handling function. This function receives the signal number as its only argument.</dl>
<p> If <code>SA_SIGINFO</code> is specified in <i>sa_flags</i>, then <i>sa_sigaction</i> (instead of <i>sa_handler</i>) specifies the signal-handling function for <i>signum</i>. This function receives three arguments, as described below. </p>
<p> <i>sa_mask</i> specifies a mask of signals which should be blocked (i.e., added to the signal mask of the thread in which the signal handler is invoked) during execution of the signal handler. In addition, the signal which triggered the handler will be blocked, unless the <code>SA_NODEFER</code> flag is used. </p>
<p> <i>sa_flags</i> specifies a set of flags which modify the behavior of the signal. It is formed by the bitwise OR of zero or more of the following:</p>
<dl>
<dt><code>SA_NOCLDSTOP</code></p>
<dd> If <i>signum</i> is <code>SIGCHLD</code>, do not receive notification when child processes stop (i.e., when they receive one of <code>SIGSTOP</code>, <code>SIGTSTP</code>, <code>SIGTTIN</code>, or <code>SIGTTOU</code>) or resume (i.e., they receive <code>SIGCONT</code>) (see <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)). This flag is meaningful only when establishing a handler for <code>SIGCHLD</code>.</p>
<dt><code>SA_NOCLDWAIT</code> (since Linux 2.6)</p>
<dd> If <i>signum</i> is <code>SIGCHLD</code>, do not transform children into zombies when they terminate. See also <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2). This flag is meaningful only when establishing a handler for <code>SIGCHLD</code>, or when setting that signal&#8217;s disposition to <code>SIG_DFL</code>.</p>
<dt>
<dd> If the <code>SA_NOCLDWAIT</code> flag is set when establishing a handler for <code>SIGCHLD</code>, POSIX.1 leaves it unspecified whether a <code>SIGCHLD</code> signal is generated when a child process terminates. On Linux, a <code>SIGCHLD</code> signal is generated in this case; on some other implementations, it is not.</p>
<dt><code>SA_NODEFER</code></p>
<dd> Do not add the signal to the thread&#8217;s signal mask while the handler is executing, unless the signal is specified in <i>act.sa_mask</i>. Consequently, a further instance of the signal may be delivered to the thread while it is executing the handler. This flag is meaningful only when establishing a signal handler.</p>
<dt>
<dd> <code>SA_NOMASK</code> is an obsolete, nonstandard synonym for this flag.</p>
<dt><code>SA_ONSTACK</code></p>
<dd> Call the signal handler on an alternate signal stack provided by <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2). If an alternate stack is not available, the default stack will be used. This flag is meaningful only when establishing a signal handler.</p>
<dt><code>SA_RESETHAND</code></p>
<dd> Restore the signal action to the default upon entry to the signal handler. This flag is meaningful only when establishing a signal handler.</p>
<dt>
<dd> <code>SA_ONESHOT</code> is an obsolete, nonstandard synonym for this flag.</p>
<dt><code>SA_RESTART</code></p>
<dd> Provide behavior compatible with BSD signal semantics by making certain system calls restartable across signals. This flag is meaningful only when establishing a signal handler. See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for a discussion of system call restarting.</p>
<dt><code>SA_RESTORER</code></p>
<dd> <i>Not intended for application use</i>. This flag is used by C libraries to indicate that the <i>sa_restorer</i> field contains the address of a &quot;signal trampoline&quot;. See <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2) for more details.</p>
<dt><code>SA_SIGINFO</code> (since Linux 2.2)</p>
<dd> The signal handler takes three arguments, not one. In this case, <i>sa_sigaction</i> should be set instead of <i>sa_handler</i>. This flag is meaningful only when establishing a signal handler.</dl>
<h3>The siginfo_t argument to a SA_SIGINFO handler</h3>
<p> When the <code>SA_SIGINFO</code> flag is specified in <i>act.sa_flags</i>, the signal handler address is passed via the <i>act.sa_sigaction</i> field. This handler takes three arguments, as follows: </p>
<p> void handler(int sig, siginfo_t *info, void *ucontext) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; } </p>
<p> These three arguments are as follows</p>
<dl>
<dt><i>sig</i></p>
<dd> The number of the signal that caused invocation of the handler.</p>
<dt><i>info</i></p>
<dd> A pointer to a <i>siginfo_t</i>, which is a structure containing further information about the signal, as described below.</p>
<dt><i>ucontext</i></p>
<dd> This is a pointer to a <i>ucontext_t</i> structure, cast to <i>void&nbsp;*</i>. The structure pointed to by this field contains signal context information that was saved on the user-space stack by the kernel; for details, see <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2). Further information about the <i>ucontext_t</i> structure can be found in <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3) and <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). Commonly, the handler function doesn&#8217;t make any use of the third argument.</dl>
<p> The <i>siginfo_t</i> data type is a structure with the following fields: </p>
<p> siginfo_t {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_signo;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Signal number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_errno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;An errno value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Signal code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_trapno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Trap number that caused<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hardware-generated signal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(unused on most architectures)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_pid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sending process ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Real user ID of sending process&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_status;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Exit value or signal&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t&nbsp;<wbr>&nbsp;si_utime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User time consumed&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clock_t&nbsp;<wbr>&nbsp;si_stime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System time consumed&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union sigval si_value;&nbsp;/*&nbsp;Signal value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_int;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;POSIX.1b signal&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_ptr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;POSIX.1b signal&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_overrun;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Timer overrun count;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1b timers&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_timerid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Timer ID;&nbsp;POSIX.1b timers&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Memory location which caused fault&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_band;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Band event&nbsp;(was&nbsp;<i>int</i>&nbsp;in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;glibc 2.3.2 and earlier)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_fd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File descriptor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_addr_lsb;&nbsp;<wbr>&nbsp;/*&nbsp;Least significant bit of address<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.32)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_lower;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Lower bound when address violation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;occurred&nbsp;(since Linux 3.19)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_upper;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Upper bound when address violation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;occurred&nbsp;(since Linux 3.19)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_pkey;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Protection key on PTE that caused<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fault&nbsp;(since Linux 4.6)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*si_call_addr;&nbsp;/*&nbsp;Address of system call instruction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 3.5)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;si_syscall;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of attempted system call<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 3.5)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int si_arch;&nbsp;<wbr>&nbsp;/*&nbsp;Architecture of attempted system call<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 3.5)&nbsp;*/ } </p>
<p> <i>si_signo</i>, <i>si_errno</i> and <i>si_code</i> are defined for all signals. (<i>si_errno</i> is generally unused on Linux.) The rest of the struct may be a union, so that one should read only the fields that are meaningful for the given signal:</p>
<dl>
<dt>*</p>
<dd> Signals sent with <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) and <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3) fill in <i>si_pid</i> and <i>si_uid</i>. In addition, signals sent with <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3) fill in <i>si_int</i> and <i>si_ptr</i> with the values specified by the sender of the signal; see <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3) for more details.</p>
<dt>*</p>
<dd> Signals sent by POSIX.1b timers (since Linux 2.6) fill in <i>si_overrun</i> and <i>si_timerid</i>. The <i>si_timerid</i> field is an internal ID used by the kernel to identify the timer; it is not the same as the timer ID returned by <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2). The <i>si_overrun</i> field is the timer overrun count; this is the same information as is obtained by a call to <code><a href="/docs/linux/man/2-timer_getoverrun/">timer_getoverrun</a></code>(2). These fields are nonstandard Linux extensions.</p>
<dt>*</p>
<dd> Signals sent for message queue notification (see the description of <code>SIGEV_SIGNAL</code> in <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3)) fill in <i>si_int</i>/<i>si_ptr</i>, with the <i>sigev_value</i> supplied to <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3); <i>si_pid</i>, with the process ID of the message sender; and <i>si_uid</i>, with the real user ID of the message sender.</p>
<dt>*</p>
<dd> <code>SIGCHLD</code> fills in <i>si_pid</i>, <i>si_uid</i>, <i>si_status</i>, <i>si_utime</i>, and <i>si_stime</i>, providing information about the child. The <i>si_pid</i> field is the process ID of the child; <i>si_uid</i> is the child&#8217;s real user ID. The <i>si_status</i> field contains the exit status of the child (if <i>si_code</i> is <code>CLD_EXITED</code>), or the signal number that caused the process to change state. The <i>si_utime</i> and <i>si_stime</i> contain the user and system CPU time used by the child process; these fields do not include the times used by waited-for children (unlike <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2) and <code><a href="/docs/linux/man/2-times/">times</a></code>(2)). In kernels up to 2.6, and since 2.6.27, these fields report CPU time in units of <i>sysconf(_SC_CLK_TCK)</i>. In 2.6 kernels before 2.6.27, a bug meant that these fields reported time in units of the (configurable) system jiffy (see <code><a href="/docs/linux/man/7-time/">time</a></code>(7)).</p>
<dt>*</p>
<dd> <code>SIGILL</code>, <code>SIGFPE</code>, <code>SIGSEGV</code>, <code>SIGBUS</code>, and <code>SIGTRAP</code> fill in <i>si_addr</i> with the address of the fault. On some architectures, these signals also fill in the <i>si_trapno</i> field.</p>
<dt>
<dd> Some suberrors of <code>SIGBUS</code>, in particular <code>BUS_MCEERR_AO</code> and <code>BUS_MCEERR_AR</code>, also fill in <i>si_addr_lsb</i>. This field indicates the least significant bit of the reported address and therefore the extent of the corruption. For example, if a full page was corrupted, <i>si_addr_lsb</i> contains <i>log2(sysconf(_SC_PAGESIZE))</i>. When <code>SIGTRAP</code> is delivered in response to a <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) event (PTRACE_EVENT_foo), <i>si_addr</i> is not populated, but <i>si_pid</i> and <i>si_uid</i> are populated with the respective process ID and user ID responsible for delivering the trap. In the case of <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2), the tracee will be shown as delivering the event. <code>BUS_MCEERR_*</code> and <i>si_addr_lsb</i> are Linux-specific extensions.</p>
<dt>
<dd> The <code>SEGV_BNDERR</code> suberror of <code>SIGSEGV</code> populates <i>si_lower</i> and <i>si_upper</i>.</p>
<dt>
<dd> The <code>SEGV_PKUERR</code> suberror of <code>SIGSEGV</code> populates <i>si_pkey</i>.</p>
<dt>*</p>
<dd> <code>SIGIO</code>/<code>SIGPOLL</code> (the two names are synonyms on Linux) fills in <i>si_band</i> and <i>si_fd</i>. The <i>si_band</i> event is a bit mask containing the same values as are filled in the <i>revents</i> field by <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2). The <i>si_fd</i> field indicates the file descriptor for which the I/O event occurred; for further details, see the description of <code>F_SETSIG</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt>*</p>
<dd> <code>SIGSYS</code>, generated (since Linux 3.5) when a seccomp filter returns <code>SECCOMP_RET_TRAP</code>, fills in <i>si_call_addr</i>, <i>si_syscall</i>, <i>si_arch</i>, <i>si_errno</i>, and other fields as described in <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2).</dl>
<h3>The si_code field</h3>
<p> The <i>si_code</i> field inside the <i>siginfo_t</i> argument that is passed to a <code>SA_SIGINFO</code> signal handler is a value (not a bit mask) indicating why this signal was sent. For a <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) event, <i>si_code</i> will contain <code>SIGTRAP</code> and have the ptrace event in the high byte: </p>
<p> (SIGTRAP | PTRACE_EVENT_foo &lt;&lt; 8). </p>
<p> For a non-<code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) event, the values that can appear in <i>si_code</i> are described in the remainder of this section. Since glibc 2.20, the definitions of most of these symbols are obtained from <i>&lt;signal.h&gt;</i> by defining feature test macros (before including <i>any</i> header file) as follows:</p>
<dl>
<dt>*</p>
<dd> <code>_XOPEN_SOURCE</code> with the value 500 or greater;</p>
<dt>*</p>
<dd> <code>_XOPEN_SOURCE</code> and <code>_XOPEN_SOURCE_EXTENDED</code>; or</p>
<dt>*</p>
<dd> <code>_POSIX_C_SOURCE</code> with the value 200809L or greater.</dl>
<p> For the <code>TRAP_*</code> constants, the symbol definitions are provided only in the first two cases. Before glibc 2.20, no feature test macros were required to obtain these symbols. </p>
<p> For a regular signal, the following list shows the values which can be placed in <i>si_code</i> for any signal, along with the reason that the signal was generated.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SI_USER</code></p>
<dd> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<dt><code>SI_KERNEL</code></p>
<dd> Sent by the kernel.</p>
<dt><code>SI_QUEUE</code></p>
<dd> <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3).</p>
<dt><code>SI_TIMER</code></p>
<dd> POSIX timer expired.</p>
<dt><code>SI_MESGQ</code> (since Linux 2.6.6)</p>
<dd> POSIX message queue state changed; see <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3).</p>
<dt><code>SI_ASYNCIO</code></p>
<dd> AIO completed.</p>
<dt><code>SI_SIGIO</code></p>
<dd> Queued <code>SIGIO</code> (only in kernels up to Linux 2.2; from Linux 2.4 onward <code>SIGIO</code>/<code>SIGPOLL</code> fills in <i>si_code</i> as described below).</p>
<dt><code>SI_TKILL</code> (since Linux 2.4.19)</p>
<dd> <code><a href="/docs/linux/man/2-tkill/">tkill</a></code>(2) or <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2).</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGILL</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ILL_ILLOPC</code></p>
<dd> Illegal opcode.</p>
<dt><code>ILL_ILLOPN</code></p>
<dd> Illegal operand.</p>
<dt><code>ILL_ILLADR</code></p>
<dd> Illegal addressing mode.</p>
<dt><code>ILL_ILLTRP</code></p>
<dd> Illegal trap.</p>
<dt><code>ILL_PRVOPC</code></p>
<dd> Privileged opcode.</p>
<dt><code>ILL_PRVREG</code></p>
<dd> Privileged register.</p>
<dt><code>ILL_COPROC</code></p>
<dd> Coprocessor error.</p>
<dt><code>ILL_BADSTK</code></p>
<dd> Internal stack error.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGFPE</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>FPE_INTDIV</code></p>
<dd> Integer divide by zero.</p>
<dt><code>FPE_INTOVF</code></p>
<dd> Integer overflow.</p>
<dt><code>FPE_FLTDIV</code></p>
<dd> Floating-point divide by zero.</p>
<dt><code>FPE_FLTOVF</code></p>
<dd> Floating-point overflow.</p>
<dt><code>FPE_FLTUND</code></p>
<dd> Floating-point underflow.</p>
<dt><code>FPE_FLTRES</code></p>
<dd> Floating-point inexact result.</p>
<dt><code>FPE_FLTINV</code></p>
<dd> Floating-point invalid operation.</p>
<dt><code>FPE_FLTSUB</code></p>
<dd> Subscript out of range.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGSEGV</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SEGV_MAPERR</code></p>
<dd> Address not mapped to object.</p>
<dt><code>SEGV_ACCERR</code></p>
<dd> Invalid permissions for mapped object.</p>
<dt><code>SEGV_BNDERR</code> (since Linux 3.19)</p>
<dd> Failed address bound checks.</p>
<dt><code>SEGV_PKUERR</code> (since Linux 4.6)</p>
<dd> Access was denied by memory protection keys. See <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7). The protection key which applied to this access is available via <i>si_pkey</i>.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGBUS</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>BUS_ADRALN</code></p>
<dd> Invalid address alignment.</p>
<dt><code>BUS_ADRERR</code></p>
<dd> Nonexistent physical address.</p>
<dt><code>BUS_OBJERR</code></p>
<dd> Object-specific hardware error.</p>
<dt><code>BUS_MCEERR_AR</code> (since Linux 2.6.32)</p>
<dd> Hardware memory error consumed on a machine check; action required.</p>
<dt><code>BUS_MCEERR_AO</code> (since Linux 2.6.32)</p>
<dd> Hardware memory error detected in process but not consumed; action optional.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGTRAP</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>TRAP_BRKPT</code></p>
<dd> Process breakpoint.</p>
<dt><code>TRAP_TRACE</code></p>
<dd> Process trace trap.</p>
<dt><code>TRAP_BRANCH</code> (since Linux 2.4, IA64 only)</p>
<dd> Process taken branch trap.</p>
<dt><code>TRAP_HWBKPT</code> (since Linux 2.4, IA64 only)</p>
<dd> Hardware breakpoint/watchpoint.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGCHLD</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>CLD_EXITED</code></p>
<dd> Child has exited.</p>
<dt><code>CLD_KILLED</code></p>
<dd> Child was killed.</p>
<dt><code>CLD_DUMPED</code></p>
<dd> Child terminated abnormally.</p>
<dt><code>CLD_TRAPPED</code></p>
<dd> Traced child has trapped.</p>
<dt><code>CLD_STOPPED</code></p>
<dd> Child has stopped.</p>
<dt><code>CLD_CONTINUED</code> (since Linux 2.6.9)</p>
<dd> Stopped child has continued.</dl>
</dl>
<p> The following values can be placed in <i>si_code</i> for a <code>SIGIO</code>/<code>SIGPOLL</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>POLL_IN</code></p>
<dd> Data input available.</p>
<dt><code>POLL_OUT</code></p>
<dd> Output buffers available.</p>
<dt><code>POLL_MSG</code></p>
<dd> Input message available.</p>
<dt><code>POLL_ERR</code></p>
<dd> I/O error.</p>
<dt><code>POLL_PRI</code></p>
<dd> High priority input available.</p>
<dt><code>POLL_HUP</code></p>
<dd> Device disconnected.</dl>
</dl>
<p> The following value can be placed in <i>si_code</i> for a <code>SIGSYS</code> signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SYS_SECCOMP</code> (since Linux 3.5)</p>
<dd> Triggered by a <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2) filter rule.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> <code>sigaction</code>() returns 0 on success; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>act</i> or <i>oldact</i> points to memory which is not a valid part of the process address space.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid signal was specified. This will also be generated if an attempt is made to change the action for <code>SIGKILL</code> or <code>SIGSTOP</code>, which cannot be caught or ignored.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits a copy of its parent&#8217;s signal dispositions. During an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), the dispositions of handled signals are reset to the default; the dispositions of ignored signals are left unchanged. </p>
<p> According to POSIX, the behavior of a process is undefined after it ignores a <code>SIGFPE</code>, <code>SIGILL</code>, or <code>SIGSEGV</code> signal that was not generated by <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) or <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3). Integer division by zero has undefined result. On some architectures it will generate a <code>SIGFPE</code> signal. (Also dividing the most negative integer by -1 may generate <code>SIGFPE</code>.) Ignoring this signal might lead to an endless loop. </p>
<p> POSIX.1-1990 disallowed setting the action for <code>SIGCHLD</code> to <code>SIG_IGN</code>. POSIX.1-2001 and later allow this possibility, so that ignoring <code>SIGCHLD</code> can be used to prevent the creation of zombies (see <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)). Nevertheless, the historical BSD and System V behaviors for ignoring <code>SIGCHLD</code> differ, so that the only completely portable method of ensuring that terminated children do not become zombies is to catch the <code>SIGCHLD</code> signal and perform a <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) or similar. </p>
<p> POSIX.1-1990 specified only <code>SA_NOCLDSTOP</code>. POSIX.1-2001 added <code>SA_NOCLDSTOP</code>, <code>SA_NOCLDWAIT</code>, <code>SA_NODEFER</code>, <code>SA_ONSTACK</code>, <code>SA_RESETHAND</code>, <code>SA_RESTART</code>, and <code>SA_SIGINFO</code>. Use of these latter values in <i>sa_flags</i> may be less portable in applications intended for older UNIX implementations. </p>
<p> The <code>SA_RESETHAND</code> flag is compatible with the SVr4 flag of the same name. </p>
<p> The <code>SA_NODEFER</code> flag is compatible with the SVr4 flag of the same name under kernels 1.3.9 and later. On older kernels the Linux implementation allowed the receipt of any signal, not just the one we are installing (effectively overriding any <i>sa_mask</i> settings). </p>
<p> <code>sigaction</code>() can be called with a NULL second argument to query the current signal handler. It can also be used to check whether a given signal is valid for the current machine by calling it with NULL second and third arguments. </p>
<p> It is not possible to block <code>SIGKILL</code> or <code>SIGSTOP</code> (by specifying them in <i>sa_mask</i>). Attempts to do so are silently ignored. </p>
<p> See <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3) for details on manipulating signal sets. </p>
<p> See <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7) for a list of the async-signal-safe functions that can be safely called inside from inside a signal handler.</p>
<h3>C library/kernel differences</h3>
<p> The glibc wrapper function for <code>sigaction</code>() gives an error (<code>EINVAL</code>) on attempts to change the disposition of the two real-time signals used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details. </p>
<p> On architectures where the signal trampoline resides in the C library, the glibc wrapper function for <code>sigaction</code>() places the address of the trampoline code in the <i>act.sa_restorer</i> field and sets the <code>SA_RESTORER</code> flag in the <i>act.sa_flags</i> field. See <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2). </p>
<p> The original Linux system call was named <code>sigaction</code>(). However, with the addition of real-time signals in Linux 2.2, the fixed-size, 32-bit <i>sigset_t</i> type supported by that system call was no longer fit for purpose. Consequently, a new system call, <code>rt_sigaction</code>(), was added to support an enlarged <i>sigset_t</i> type. The new system call takes a fourth argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the signal sets in <i>act.sa_mask</i> and <i>oldact.sa_mask</i>. This argument is currently required to have the value <i>sizeof(sigset_t)</i> (or the error <code>EINVAL</code> results). The glibc <code>sigaction</code>() wrapper function hides these details from us, transparently calling <code>rt_sigaction</code>() when the kernel provides it.</p>
<h3>Undocumented</h3>
<p> Before the introduction of <code>SA_SIGINFO</code>, it was also possible to get some additional information about the signal. This was done by providing an <i>sa_handler</i> signal handler with a second argument of type <i>struct sigcontext</i>, which is the same structure as the one that is passed in the <i>uc_mcontext</i> field of the <i>ucontext</i> structure that is passed (via a pointer) in the third argument of the <i>sa_sigaction</i> handler. See the relevant Linux kernel sources for details. This use is obsolete now.</p>
<h2>BUGS</h2>
<p> When delivering a signal with a <code>SA_SIGINFO</code> handler, the kernel does not always provide meaningful values for all of the fields of the <i>siginfo_t</i> that are relevant for that signal. </p>
<p> In kernels up to and including 2.6.13, specifying <code>SA_NODEFER</code> in <i>sa_flags</i> prevents not only the delivered signal from being masked during execution of the handler, but also the signals specified in <i>sa_mask</i>. This bug was fixed in kernel 2.6.14.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-killpg/">killpg</a></code>(3), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3), <code><a href="/docs/linux/man/3-siginterrupt/">siginterrupt</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/3-sigvec/">sigvec</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
