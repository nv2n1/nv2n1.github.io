---
title: "seccomp(2)"
name: "seccomp"
section: "2"
letter: "s"
url: "/docs/linux/man/2-seccomp/"
description: "seccomp – operate on Secure Computing state of the process"
---

<h2 class="name">NAME</h2>
<p> seccomp &#8211; operate on Secure Computing state of the process </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/audit.h&gt;
#include &lt;linux/filter.h&gt;
#include &lt;linux/seccomp.h&gt;
#include &lt;linux/signal.h&gt;
#include &lt;sys/ptrace.h&gt;
int seccomp(unsigned int operation, unsigned int flags, void *args);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>seccomp</code>() system call operates on the Secure Computing (seccomp) state of the calling process. </p>
<p> Currently, Linux supports the following <i>operation</i> values:</p>
<dl>
<dt><code>SECCOMP_SET_MODE_STRICT</code></p>
<dd> The only system calls that the calling thread is permitted to make are <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) (but not <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2)), and <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2). Other system calls result in the delivery of a <code>SIGKILL</code> signal. Strict secure computing mode is useful for number-crunching applications that may need to execute untrusted byte code, perhaps obtained by reading from a pipe or socket.</p>
<dt>
<dd> Note that although the calling thread can no longer call <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), it can use <code><a href="/docs/linux/man/2-sigreturn/">sigreturn</a></code>(2) to block all signals apart from <code>SIGKILL</code> and <code>SIGSTOP</code>. This means that <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2) (for example) is not sufficient for restricting the process&#8217;s execution time. Instead, to reliably terminate the process, <code>SIGKILL</code> must be used. This can be done by using <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2) with <code>SIGEV_SIGNAL</code> and <i>sigev_signo</i> set to <code>SIGKILL</code>, or by using <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) to set the hard limit for <code>RLIMIT_CPU</code>.</p>
<dt>
<dd> This operation is available only if the kernel is configured with <code>CONFIG_SECCOMP</code> enabled.</p>
<dt>
<dd> The value of <i>flags</i> must be 0, and <i>args</i> must be NULL.</p>
<dt>
<dd> This operation is functionally identical to the call:</p>
<dt>
<dd> prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);</p>
<dt><code>SECCOMP_SET_MODE_FILTER</code></p>
<dd> The system calls allowed are defined by a pointer to a Berkeley Packet Filter (BPF) passed via <i>args</i>. This argument is a pointer to a <i>struct sock_fprog</i>; it can be designed to filter arbitrary system calls and system call arguments. If the filter is invalid, <code>seccomp</code>() fails, returning <code>EINVAL</code> in <i>errno</i>.</p>
<dt>
<dd> If <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) is allowed by the filter, any child processes will be constrained to the same system call filters as the parent. If <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) is allowed, the existing filters will be preserved across a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> In order to use the <code>SECCOMP_SET_MODE_FILTER</code> operation, either the calling thread must have the <code>CAP_SYS_ADMIN</code> capability in its user namespace, or the thread must already have the <i>no_new_privs</i> bit set. If that bit was not already set by an ancestor of this thread, the thread must make the following call:</p>
<dt>
<dd> prctl(PR_SET_NO_NEW_PRIVS, 1);</p>
<dt>
<dd> Otherwise, the <code>SECCOMP_SET_MODE_FILTER</code> operation fails and returns <code>EACCES</code> in <i>errno</i>. This requirement ensures that an unprivileged process cannot apply a malicious filter and then invoke a set-user-ID or other privileged program using <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), thus potentially compromising that program. (Such a malicious filter might, for example, cause an attempt to use <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) to set the caller&#8217;s user IDs to nonzero values to instead return 0 without actually making the system call. Thus, the program might be tricked into retaining superuser privileges in circumstances where it is possible to influence it to do dangerous things because it did not actually drop privileges.)</p>
<dt>
<dd> If <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) or <code>seccomp</code>() is allowed by the attached filter, further filters may be added. This will increase evaluation time, but allows for further reduction of the attack surface during execution of a thread.</p>
<dt>
<dd> The <code>SECCOMP_SET_MODE_FILTER</code> operation is available only if the kernel is configured with <code>CONFIG_SECCOMP_FILTER</code> enabled.</p>
<dt>
<dd> When <i>flags</i> is 0, this operation is functionally identical to the call:</p>
<dt>
<dd> prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, args);</p>
<dt>
<dd> The recognized <i>flags</i> are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SECCOMP_FILTER_FLAG_TSYNC</code></p>
<dd> When adding a new filter, synchronize all other threads of the calling process to the same seccomp filter tree. A &quot;filter tree&quot; is the ordered list of filters attached to a thread. (Attaching identical filters in separate <code>seccomp</code>() calls results in different filters from this perspective.)</p>
<dt>
<dd> If any thread cannot synchronize to the same filter tree, the call will not attach the new seccomp filter, and will fail, returning the first thread ID found that cannot synchronize. Synchronization will fail if another thread in the same process is in <code>SECCOMP_MODE_STRICT</code> or if it has attached new seccomp filters to itself, diverging from the calling thread&#8217;s filter tree.</p>
<dt><code>SECCOMP_FILTER_FLAG_LOG</code> (since Linux 4.14)</p>
<dd> All filter return actions except <code>SECCOMP_RET_ALLOW</code> should be logged. An administrator may override this filter flag by preventing specific actions from being logged via the <i>/proc/sys/kernel/seccomp/actions_logged</i> file.</p>
<dt><code>SECCOMP_FILTER_FLAG_SPEC_ALLOW</code> (since Linux 4.17)</p>
<dd> Disable Speculative Store Bypass mitigation.</dl>
</dl>
<dt><code>SECCOMP_GET_ACTION_AVAIL</code> (since Linux 4.14)</p>
<dd> Test to see if an action is supported by the kernel. This operation is helpful to confirm that the kernel knows of a more recently added filter return action since the kernel treats all unknown actions as <code>SECCOMP_RET_KILL_PROCESS</code>.</p>
<dt>
<dd> The value of <i>flags</i> must be 0, and <i>args</i> must be a pointer to an unsigned 32-bit filter return action.</dl>
<h3>Filters</h3>
<p> When adding filters via <code>SECCOMP_SET_MODE_FILTER</code>, <i>args</i> points to a filter program: </p>
<p> struct sock_fprog {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of BPF instructions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sock_filter&nbsp;*filter;&nbsp;/*&nbsp;Pointer to array of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF instructions&nbsp;*/ }; </p>
<p> Each program must contain one or more BPF instructions: </p>
<p> struct sock_filter { /* Filter block */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Actual filter code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8&nbsp;<wbr>&nbsp;jt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Jump true&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8&nbsp;<wbr>&nbsp;jf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Jump false&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 k;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Generic multiuse field&nbsp;*/ }; </p>
<p> When executing the instructions, the BPF program operates on the system call information made available (i.e., use the <code>BPF_ABS</code> addressing mode) as a (read-only) buffer of the following form: </p>
<p> struct seccomp_data {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System call number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 arch;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;AUDIT_ARCH_*&nbsp;value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(see&nbsp;&lt;linux/audit.h&gt;)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 instruction_pointer;&nbsp;<wbr>&nbsp;/*&nbsp;CPU instruction pointer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 args[6];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Up to 6 system call arguments&nbsp;*/ }; </p>
<p> Because numbering of system calls varies between architectures and some architectures (e.g., x86-64) allow user-space code to use the calling conventions of multiple architectures (and the convention being used may vary over the life of a process that uses <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to execute binaries that employ the different conventions), it is usually necessary to verify the value of the <i>arch</i> field. </p>
<p> It is strongly recommended to use an allow-list approach whenever possible because such an approach is more robust and simple. A deny-list will have to be updated whenever a potentially dangerous system call is added (or a dangerous flag or option if those are deny-listed), and it is often possible to alter the representation of a value without altering its meaning, leading to a deny-list bypass. See also <i>Caveats</i> below. </p>
<p> The <i>arch</i> field is not unique for all calling conventions. The x86-64 ABI and the x32 ABI both use <code>AUDIT_ARCH_X86_64</code> as <i>arch</i>, and they run on the same processors. Instead, the mask <code>__X32_SYSCALL_BIT</code> is used on the system call number to tell the two ABIs apart. </p>
<p> This means that a policy must either deny all syscalls with <code>__X32_SYSCALL_BIT</code> or it must recognize syscalls with and without <code>__X32_SYSCALL_BIT</code> set. A list of system calls to be denied based on <i>nr</i> that does not also contain <i>nr</i> values with <code>__X32_SYSCALL_BIT</code> set can be bypassed by a malicious program that sets <code>__X32_SYSCALL_BIT</code>. </p>
<p> Additionally, kernels prior to Linux 5.4 incorrectly permitted <i>nr</i> in the ranges 512-547 as well as the corresponding non-x32 syscalls ORed with <code>__X32_SYSCALL_BIT</code>. For example, <i>nr</i> == 521 and <i>nr</i> == (101 | <code>__X32_SYSCALL_BIT</code>) would result in invocations of <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) with potentially confused x32-vs-x86_64 semantics in the kernel. Policies intended to work on kernels before Linux 5.4 must ensure that they deny or otherwise correctly handle these system calls. On Linux 5.4 and newer, such system calls will fail with the error <code>ENOSYS</code>, without doing anything. </p>
<p> The <i>instruction_pointer</i> field provides the address of the machine-language instruction that performed the system call. This might be useful in conjunction with the use of <i>/proc/[pid]/maps</i> to perform checks based on which region (mapping) of the program made the system call. (Probably, it is wise to lock down the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) and <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2) system calls to prevent the program from subverting such checks.) </p>
<p> When checking values from <i>args</i>, keep in mind that arguments are often silently truncated before being processed, but after the seccomp check. For example, this happens if the i386 ABI is used on an x86-64 kernel: although the kernel will normally not look beyond the 32 lowest bits of the arguments, the values of the full 64-bit registers will be present in the seccomp data. A less surprising example is that if the x86-64 ABI is used to perform a system call that takes an argument of type <i>int</i>, the more-significant half of the argument register is ignored by the system call, but visible in the seccomp data. </p>
<p> A seccomp filter returns a 32-bit value consisting of two parts: the most significant 16 bits (corresponding to the mask defined by the constant <code>SECCOMP_RET_ACTION_FULL</code>) contain one of the &quot;action&quot; values listed below; the least significant 16-bits (defined by the constant <code>SECCOMP_RET_DATA</code>) are &quot;data&quot; to be associated with this return value. </p>
<p> If multiple filters exist, they are <i>all</i> executed, in reverse order of their addition to the filter tree&#8212;that is, the most recently installed filter is executed first. (Note that all filters will be called even if one of the earlier filters returns <code>SECCOMP_RET_KILL</code>. This is done to simplify the kernel code and to provide a tiny speed-up in the execution of sets of filters by avoiding a check for this uncommon case.) The return value for the evaluation of a given system call is the first-seen action value of highest precedence (along with its accompanying data) returned by execution of all of the filters. </p>
<p> In decreasing order of precedence, the action values that may be returned by a seccomp filter are:</p>
<dl>
<dt><code>SECCOMP_RET_KILL_PROCESS</code> (since Linux 4.14)</p>
<dd> This value results in immediate termination of the process, with a core dump. The system call is not executed. By contrast with <code>SECCOMP_RET_KILL_THREAD</code> below, all threads in the thread group are terminated. (For a discussion of thread groups, see the description of the <code>CLONE_THREAD</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).)</p>
<dt>
<dd> The process terminates <i>as though</i> killed by a <code>SIGSYS</code> signal. Even if a signal handler has been registered for <code>SIGSYS</code>, the handler will be ignored in this case and the process always terminates. To a parent process that is waiting on this process (using <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) or similar), the returned <i>wstatus</i> will indicate that its child was terminated as though by a <code>SIGSYS</code> signal.</p>
<dt><code>SECCOMP_RET_KILL_THREAD</code> (or <code>SECCOMP_RET_KILL</code>)</p>
<dd> This value results in immediate termination of the thread that made the system call. The system call is not executed. Other threads in the same thread group will continue to execute.</p>
<dt>
<dd> The thread terminates <i>as though</i> killed by a <code>SIGSYS</code> signal. See <code>SECCOMP_RET_KILL_PROCESS</code> above.</p>
<dt>
<dd> Before Linux 4.11, any process terminated in this way would not trigger a coredump (even though <code>SIGSYS</code> is documented in <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) as having a default action of termination with a core dump). Since Linux 4.11, a single-threaded process will dump core if terminated in this way.</p>
<dt>
<dd> With the addition of <code>SECCOMP_RET_KILL_PROCESS</code> in Linux 4.14, <code>SECCOMP_RET_KILL_THREAD</code> was added as a synonym for <code>SECCOMP_RET_KILL</code>, in order to more clearly distinguish the two actions.</p>
<dt>
<dd> <code>Note</code>: the use of <code>SECCOMP_RET_KILL_THREAD</code> to kill a single thread in a multithreaded process is likely to leave the process in a permanently inconsistent and possibly corrupt state.</p>
<dt><code>SECCOMP_RET_TRAP</code></p>
<dd> This value results in the kernel sending a thread-directed <code>SIGSYS</code> signal to the triggering thread. (The system call is not executed.) Various fields will be set in the <i>siginfo_t</i> structure (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) associated with signal:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>si_signo</i> will contain <code>SIGSYS</code>.</p>
<dt>*</p>
<dd> <i>si_call_addr</i> will show the address of the system call instruction.</p>
<dt>*</p>
<dd> <i>si_syscall</i> and <i>si_arch</i> will indicate which system call was attempted.</p>
<dt>*</p>
<dd> <i>si_code</i> will contain <code>SYS_SECCOMP</code>.</p>
<dt>*</p>
<dd> <i>si_errno</i> will contain the <code>SECCOMP_RET_DATA</code> portion of the filter return value.</dl>
</dl>
<dt>
<dd> The program counter will be as though the system call happened (i.e., the program counter will not point to the system call instruction). The return value register will contain an architecture-dependent value; if resuming execution, set it to something appropriate for the system call. (The architecture dependency is because replacing it with <code>ENOSYS</code> could overwrite some useful information.)</p>
<dt><code>SECCOMP_RET_ERRNO</code></p>
<dd> This value results in the <code>SECCOMP_RET_DATA</code> portion of the filter&#8217;s return value being passed to user space as the <i>errno</i> value without executing the system call.</p>
<dt><code>SECCOMP_RET_TRACE</code></p>
<dd> When returned, this value will cause the kernel to attempt to notify a <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)-based tracer prior to executing the system call. If there is no tracer present, the system call is not executed and returns a failure status with <i>errno</i> set to <code>ENOSYS</code>.</p>
<dt>
<dd> A tracer will be notified if it requests <code>PTRACE_O_TRACESECCOMP</code> using <i>ptrace(PTRACE_SETOPTIONS)</i>. The tracer will be notified of a <code>PTRACE_EVENT_SECCOMP</code> and the <code>SECCOMP_RET_DATA</code> portion of the filter&#8217;s return value will be available to the tracer via <code>PTRACE_GETEVENTMSG</code>.</p>
<dt>
<dd> The tracer can skip the system call by changing the system call number to -1. Alternatively, the tracer can change the system call requested by changing the system call to a valid system call number. If the tracer asks to skip the system call, then the system call will appear to return the value that the tracer puts in the return value register.</p>
<dt>
<dd> Before kernel 4.8, the seccomp check will not be run again after the tracer is notified. (This means that, on older kernels, seccomp-based sandboxes <code>must not</code> allow use of <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)&#8212;even of other sandboxed processes&#8212;without extreme care; ptracers can use this mechanism to escape from the seccomp sandbox.)</p>
<dt>
<dd> Note that a tracer process will not be notified if another filter returns an action value with a precedence greater than <code>SECCOMP_RET_TRACE</code>.</p>
<dt><code>SECCOMP_RET_LOG</code> (since Linux 4.14)</p>
<dd> This value results in the system call being executed after the filter return action is logged. An administrator may override the logging of this action via the <i>/proc/sys/kernel/seccomp/actions_logged</i> file.</p>
<dt><code>SECCOMP_RET_ALLOW</code></p>
<dd> This value results in the system call being executed.</dl>
<p> If an action value other than one of the above is specified, then the filter action is treated as either <code>SECCOMP_RET_KILL_PROCESS</code> (since Linux 4.14) or <code>SECCOMP_RET_KILL_THREAD</code> (in Linux 4.13 and earlier).</p>
<h3>/proc interfaces</h3>
<p> The files in the directory <i>/proc/sys/kernel/seccomp</i> provide additional seccomp information and configuration:</p>
<dl>
<dt><i>actions_avail</i> (since Linux 4.14)</p>
<dd> A read-only ordered list of seccomp filter return actions in string form. The ordering, from left-to-right, is in decreasing order of precedence. The list represents the set of seccomp filter return actions supported by the kernel.</p>
<dt><i>actions_logged</i> (since Linux 4.14)</p>
<dd> A read-write ordered list of seccomp filter return actions that are allowed to be logged. Writes to the file do not need to be in ordered form but reads from the file will be ordered in the same way as the <i>actions_avail</i> file.</p>
<dt>
<dd> It is important to note that the value of <i>actions_logged</i> does not prevent certain filter return actions from being logged when the audit subsystem is configured to audit a task. If the action is not found in the <i>actions_logged</i> file, the final decision on whether to audit the action for that task is ultimately left up to the audit subsystem to decide for all filter return actions other than <code>SECCOMP_RET_ALLOW</code>.</p>
<dt>
<dd> The &quot;allow&quot; string is not accepted in the <i>actions_logged</i> file as it is not possible to log <code>SECCOMP_RET_ALLOW</code> actions. Attempting to write &quot;allow&quot; to the file will fail with the error <code>EINVAL</code>.</dl>
<h3>Audit logging of seccomp actions</h3>
<p> Since Linux 4.14, the kernel provides the facility to log the actions returned by seccomp filters in the audit log. The kernel makes the decision to log an action based on the action type, whether or not the action is present in the <i>actions_logged</i> file, and whether kernel auditing is enabled (e.g., via the kernel boot option <i>audit=1</i>). The rules are as follows:</p>
<dl>
<dt>*</p>
<dd> If the action is <code>SECCOMP_RET_ALLOW</code>, the action is not logged.</p>
<dt>*</p>
<dd> Otherwise, if the action is either <code>SECCOMP_RET_KILL_PROCESS</code> or <code>SECCOMP_RET_KILL_THREAD</code>, and that action appears in the <i>actions_logged</i> file, the action is logged.</p>
<dt>*</p>
<dd> Otherwise, if the filter has requested logging (the <code>SECCOMP_FILTER_FLAG_LOG</code> flag) and the action appears in the <i>actions_logged</i> file, the action is logged.</p>
<dt>*</p>
<dd> Otherwise, if kernel auditing is enabled and the process is being audited (<code><a href="/docs/linux/man/8-autrace/">autrace</a></code>(8)), the action is logged.</p>
<dt>*</p>
<dd> Otherwise, the action is not logged.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>seccomp</code>() returns 0. On error, if <code>SECCOMP_FILTER_FLAG_TSYNC</code> was used, the return value is the ID of the thread that caused the synchronization failure. (This ID is a kernel thread ID of the type returned by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).) On other errors, -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>seccomp</code>() can fail for the following reasons:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The caller did not have the <code>CAP_SYS_ADMIN</code> capability in its user namespace, or had not set <i>no_new_privs</i> before using <code>SECCOMP_SET_MODE_FILTER</code>.</p>
<dt><code>EFAULT</code></p>
<dd> <i>args</i> was not a valid address.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> is unknown or is not supported by this kernel version or configuration.</p>
<dt><code>EINVAL</code></p>
<dd> The specified <i>flags</i> are invalid for the given <i>operation</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> included <code>BPF_ABS</code>, but the specified offset was not aligned to a 32-bit boundary or exceeded <i>sizeof(struct seccomp_data)</i>.</p>
<dt><code>EINVAL</code></p>
<dd> A secure computing mode has already been set, and <i>operation</i> differs from the existing setting.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> specified <code>SECCOMP_SET_MODE_FILTER</code>, but the filter program pointed to by <i>args</i> was not valid or the length of the filter program was zero or exceeded <code>BPF_MAXINSNS</code> (4096) instructions.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ENOMEM</code></p>
<dd> The total length of all filter programs attached to the calling thread would exceed <code>MAX_INSNS_PER_PATH</code> (32768) instructions. Note that for the purposes of calculating this limit, each already existing filter program incurs an overhead penalty of 4 instructions.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> <i>operation</i> specified <code>SECCOMP_GET_ACTION_AVAIL</code>, but the kernel does not support the filter return action specified by <i>args</i>.</p>
<dt><code>ESRCH</code></p>
<dd> Another thread caused a failure during thread sync, but its ID could not be determined.</dl>
<h2>VERSIONS</h2>
<p> The <code>seccomp</code>() system call first appeared in Linux 3.17.</p>
<h2>CONFORMING TO</h2>
<p> The <code>seccomp</code>() system call is a nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> Rather than hand-coding seccomp filters as shown in the example below, you may prefer to employ the <i>libseccomp</i> library, which provides a front-end for generating seccomp filters. </p>
<p> The <i>Seccomp</i> field of the <i>/proc/[pid]/status</i> file provides a method of viewing the seccomp mode of a process; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). </p>
<p> <code>seccomp</code>() provides a superset of the functionality provided by the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_SECCOMP</code> operation (which does not support <i>flags</i>). </p>
<p> Since Linux 4.4, the <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2) <code>PTRACE_SECCOMP_GET_FILTER</code> operation can be used to dump a process&#8217;s seccomp filters.</p>
<h3>Architecture support for seccomp BPF</h3>
<p> Architecture support for seccomp BPF filtering is available on the following architectures:</p>
<dl>
<dt>*</p>
<dd> x86-64, i386, x32 (since Linux 3.5)</p>
<dt>*</p>
<dd> ARM (since Linux 3.8)</p>
<dt>*</p>
<dd> s390 (since Linux 3.8)</p>
<dt>*</p>
<dd> MIPS (since Linux 3.16)</p>
<dt>*</p>
<dd> ARM-64 (since Linux 3.19)</p>
<dt>*</p>
<dd> PowerPC (since Linux 4.3)</p>
<dt>*</p>
<dd> Tile (since Linux 4.3)</p>
<dt>*</p>
<dd> PA-RISC (since Linux 4.6)</dl>
<h3>Caveats</h3>
<p> There are various subtleties to consider when applying seccomp filters to a program, including the following:</p>
<dl>
<dt>*</p>
<dd> Some traditional system calls have user-space implementations in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7) on many architectures. Notable examples include <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), and <code><a href="/docs/linux/man/2-time/">time</a></code>(2). On such architectures, seccomp filtering for these system calls will have no effect. (However, there are cases where the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7) implementations may fall back to invoking the true system call, in which case seccomp filters would see the system call.)</p>
<dt>*</p>
<dd> Seccomp filtering is based on system call numbers. However, applications typically do not directly invoke system calls, but instead call wrapper functions in the C library which in turn invoke the system calls. Consequently, one must be aware of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The glibc wrappers for some traditional system calls may actually employ system calls with different names in the kernel. For example, the <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2) wrapper function actually employs the <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2) system call, and the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) wrapper function actually calls <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<dt>&bull;</p>
<dd> The behavior of wrapper functions may vary across architectures, according to the range of system calls provided on those architectures. In other words, the same wrapper function may invoke different system calls on different architectures.</p>
<dt>&bull;</p>
<dd> Finally, the behavior of wrapper functions can change across glibc versions. For example, in older versions, the glibc wrapper function for <code><a href="/docs/linux/man/2-open/">open</a></code>(2) invoked the system call of the same name, but starting in glibc 2.26, the implementation switched to calling <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) on all architectures.</dl>
</dl>
</dl>
<p> The consequence of the above points is that it may be necessary to filter for a system call other than might be expected. Various manual pages in Section 2 provide helpful details about the differences between wrapper functions and the underlying system calls in subsections entitled <i>C library/kernel differences</i>. </p>
<p> Furthermore, note that the application of seccomp filters even risks causing bugs in an application, when the filters cause unexpected failures for legitimate operations that the application might need to perform. Such bugs may not easily be discovered when testing the seccomp filters if the bugs occur in rarely used application code paths.</p>
<h3>Seccomp-specific BPF details</h3>
<p> Note the following BPF details specific to seccomp filters:</p>
<dl>
<dt>*</p>
<dd> The <code>BPF_H</code> and <code>BPF_B</code> size modifiers are not supported: all operations must load and store (4-byte) words (<code>BPF_W</code>).</p>
<dt>*</p>
<dd> To access the contents of the <i>seccomp_data</i> buffer, use the <code>BPF_ABS</code> addressing mode modifier.</p>
<dt>*</p>
<dd> The <code>BPF_LEN</code> addressing mode modifier yields an immediate mode operand whose value is the size of the <i>seccomp_data</i> buffer.</dl>
<h2>EXAMPLES</h2>
<p> The program below accepts four or more arguments. The first three arguments are a system call number, a numeric architecture identifier, and an error number. The program uses these values to construct a BPF filter that is used at run time to perform the following checks:</p>
<dl>
<dt>[1]</p>
<dd> If the program is not running on the specified architecture, the BPF filter causes system calls to fail with the error <code>ENOSYS</code>.</p>
<dt>[2]</p>
<dd> If the program attempts to execute the system call with the specified number, the BPF filter causes the system call to fail, with <i>errno</i> being set to the specified error number.</dl>
<p> The remaining command-line arguments specify the pathname and additional arguments of a program that the example program should attempt to execute using <code><a href="/docs/linux/man/3-execv/">execv</a></code>(3) (a library function that employs the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) system call). Some example runs of the program are shown below. </p>
<p> First, we display the architecture that we are running on (x86-64) and then construct a shell function that looks up system call numbers on this architecture: </p>
<p> $ <code>uname -m</code> x86_64 $ <code>syscall_nr() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cat&nbsp;/usr/src/linux/arch/x86/syscalls/syscall_64.tbl |&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;awk&nbsp;&#8216;$2&nbsp;!=&nbsp;&quot;x32&quot;&nbsp;&amp;&amp;&nbsp;$3&nbsp;==&nbsp;&quot;&#8217;$1&#8217;&quot;&nbsp;{&nbsp;print&nbsp;$1&nbsp;}&#8217; }</code> </p>
<p> When the BPF filter rejects a system call (case [2] above), it causes the system call to fail with the error number specified on the command line. In the experiments shown here, we&#8217;ll use error number 99: </p>
<p> $ <code>errno 99</code> EADDRNOTAVAIL 99 Cannot assign requested address </p>
<p> In the following example, we attempt to run the command <code><a href="/docs/linux/man/1-whoami/">whoami</a></code>(1), but the BPF filter rejects the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) system call, so that the command is not even executed: </p>
<p> $ <code>syscall_nr execve</code> 59 $ <code>./a.out</code> Usage: ./a.out &lt;syscall_nr&gt; &lt;arch&gt; &lt;errno&gt; &lt;prog&gt; [&lt;args&gt;] Hint for &lt;arch&gt;: AUDIT_ARCH_I386: 0x40000003<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;AUDIT_ARCH_X86_64: 0xC000003E $ <code>./a.out 59 0xC000003E 99 /bin/whoami</code> execv: Cannot assign requested address </p>
<p> In the next example, the BPF filter rejects the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call, so that, although it is successfully started, the <code><a href="/docs/linux/man/1-whoami/">whoami</a></code>(1) command is not able to write output: </p>
<p> $ <code>syscall_nr write</code> 1 $ <code>./a.out 1 0xC000003E 99 /bin/whoami</code> </p>
<p> In the final example, the BPF filter rejects a system call that is not used by the <code><a href="/docs/linux/man/1-whoami/">whoami</a></code>(1) command, so it is able to successfully execute and produce output: </p>
<p> $ <code>syscall_nr preadv</code> 295 $ <code>./a.out 295 0xC000003E 99 /bin/whoami</code> cecilia</p>
<h3>Program source</h3>
<p> #include &lt;errno.h&gt; #include &lt;stddef.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;linux/audit.h&gt; #include &lt;linux/filter.h&gt; #include &lt;linux/seccomp.h&gt; #include &lt;sys/prctl.h&gt; </p>
<p> #define X32_SYSCALL_BIT 0x40000000 #define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0])) </p>
<p> static int install_filter(int syscall_nr, int t_arch, int f_errno) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int upper_nr_limit&nbsp;=&nbsp;0xffffffff; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Assume that AUDIT_ARCH_X86_64 means the normal x86-64 ABI<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(in the x32 ABI, all system calls have bit 30 set in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8216;nr&#8217;&nbsp;field, meaning the numbers are&nbsp;&gt;=&nbsp;X32_SYSCALL_BIT)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(t_arch&nbsp;==&nbsp;AUDIT_ARCH_X86_64)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;upper_nr_limit&nbsp;=&nbsp;X32_SYSCALL_BIT &#8211; 1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sock_filter filter[]&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[0]&nbsp;Load architecture from&nbsp;&#8216;seccomp_data&#8217;&nbsp;buffer into<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accumulator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STMT(BPF_LD | BPF_W | BPF_ABS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(offsetof(struct seccomp_data, arch))), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[1]&nbsp;Jump forward 5 instructions if architecture does not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match&nbsp;&#8216;t_arch&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, t_arch, 0, 5), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[2]&nbsp;Load system call number from&nbsp;&#8216;seccomp_data&#8217;&nbsp;buffer into<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accumulator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STMT(BPF_LD | BPF_W | BPF_ABS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(offsetof(struct seccomp_data, nr))), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[3]&nbsp;Check ABI &#8211; only needed for x86-64 in deny-list use<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cases.&nbsp;<wbr>&nbsp;Use BPF_JGT instead of checking against the bit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mask to avoid having to reload the syscall number.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_JUMP(BPF_JMP | BPF_JGT | BPF_K, upper_nr_limit, 3, 0), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[4]&nbsp;Jump forward 1 instruction if system call number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;does not match&nbsp;&#8216;syscall_nr&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, syscall_nr, 0, 1), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[5]&nbsp;Matching architecture and system call: don&#8217;t execute<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the system call, and return&nbsp;&#8216;f_errno&#8217;&nbsp;in&nbsp;&#8216;errno&#8217;&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STMT(BPF_RET | BPF_K,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SECCOMP_RET_ERRNO |&nbsp;(f_errno&nbsp;&amp;&nbsp;SECCOMP_RET_DATA)), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[6]&nbsp;Destination of system call number mismatch: allow other<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;system calls&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW), </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;[7]&nbsp;Destination of architecture mismatch: kill process&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL_PROCESS),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sock_fprog prog&nbsp;=&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.len&nbsp;=&nbsp;ARRAY_SIZE(filter),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.filter&nbsp;=&nbsp;filter,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(seccomp(SECCOMP_SET_MODE_FILTER, 0,&nbsp;&amp;prog))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;seccomp&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0; } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;5)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;%s&nbsp;&lt;syscall_nr&gt;&nbsp;&lt;arch&gt;&nbsp;&lt;errno&gt;&nbsp;&lt;prog&gt;&nbsp;[&lt;args&gt;]
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;Hint for&nbsp;&lt;arch&gt;: AUDIT_ARCH_I386: 0x%X
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;AUDIT_ARCH_X86_64: 0x%X
&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;
&quot;, argv[0], AUDIT_ARCH_I386, AUDIT_ARCH_X86_64);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;prctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(install_filter(strtol(argv[1], NULL, 0),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strtol(argv[2], NULL, 0),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strtol(argv[3], NULL, 0)))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execv(argv[4],&nbsp;&amp;argv[4]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;execv&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bpfc/">bpfc</a></code>(1), <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1), <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) </p>
<p> Various pages from the <i>libseccomp</i> library, including: <code><a href="/docs/linux/man/1-scmp_sys_resolver/">scmp_sys_resolver</a></code>(1), <code><a href="/docs/linux/man/3-seccomp_export_bpf/">seccomp_export_bpf</a></code>(3), <code><a href="/docs/linux/man/3-seccomp_init/">seccomp_init</a></code>(3), <code><a href="/docs/linux/man/3-seccomp_load/">seccomp_load</a></code>(3), and <code><a href="/docs/linux/man/3-seccomp_rule_add/">seccomp_rule_add</a></code>(3). </p>
<p> The kernel source files <i>Documentation/networking/filter.txt</i> and <i>Documentation/userspace-api/seccomp_filter.rst</i> (or <i>Documentation/prctl/seccomp_filter.txt</i> before Linux 4.13). </p>
<p> McCanne, S. and Jacobson, V. (1992) <i>The BSD Packet Filter: A New Architecture for User-level Packet Capture</i>, Proceedings of the USENIX Winter 1993 Conference</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
