---
title: "prlimit64(2)"
name: "prlimit64"
section: "2"
letter: "p"
url: "/docs/linux/man/2-prlimit64/"
description: "getrlimit, setrlimit, prlimit – get/set resource limits"
---

<h2 class="name">NAME</h2>
<p> getrlimit, setrlimit, prlimit &#8211; get/set resource limits </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/time.h&gt;</code><br />
 <code>#include &lt;sys/resource.h&gt;</code> </p>
<p> <code>int getrlimit(int </code><i>resource</i><code>, struct rlimit *</code><i>rlim</i><code>);</code><br />
 <code>int setrlimit(int </code><i>resource</i><code>, const struct rlimit *</code><i>rlim</i><code>);</code> </p>
<p> <code>int prlimit(pid_t </code><i>pid</i><code>, int </code><i>resource</i><code>, const struct rlimit *</code><i>new_limit</i><code>,</code><br />
 <code> struct rlimit *</code><i>old_limit</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>prlimit</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getrlimit</code>() and <code>setrlimit</code>() system calls get and set resource limits. Each resource has an associated soft and hard limit, as defined by the <i>rlimit</i> structure: </p>
<p> struct rlimit {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rlim_t rlim_cur;&nbsp;<wbr>&nbsp;/*&nbsp;Soft limit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rlim_t rlim_max;&nbsp;<wbr>&nbsp;/*&nbsp;Hard limit&nbsp;(ceiling for rlim_cur)&nbsp;*/ }; </p>
<p> The soft limit is the value that the kernel enforces for the corresponding resource. The hard limit acts as a ceiling for the soft limit: an unprivileged process may set only its soft limit to a value in the range from 0 up to the hard limit, and (irreversibly) lower its hard limit. A privileged process (under Linux: one with the <code>CAP_SYS_RESOURCE</code> capability in the initial user namespace) may make arbitrary changes to either limit value. </p>
<p> The value <code>RLIM_INFINITY</code> denotes no limit on a resource (both in the structure returned by <code>getrlimit</code>() and in the structure passed to <code>setrlimit</code>()). </p>
<p> The <i>resource</i> argument must be one of:</p>
<dl>
<dt><code>RLIMIT_AS</code></p>
<dd> This is the maximum size of the process&#8217;s virtual memory (address space). The limit is specified in bytes, and is rounded down to the system page size. This limit affects calls to <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), which fail with the error <code>ENOMEM</code> upon exceeding this limit. In addition, automatic stack expansion fails (and generates a <code>SIGSEGV</code> that kills the process if no alternate stack has been made available via <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)). Since the value is a <i>long</i>, on machines with a 32-bit <i>long</i> either this limit is at most 2 GiB, or this resource is unlimited.</p>
<dt><code>RLIMIT_CORE</code></p>
<dd> This is the maximum size of a <i>core</i> file (see <code><a href="/docs/linux/man/5-core/">core</a></code>(5)) in bytes that the process may dump. When 0 no core dump files are created. When nonzero, larger dumps are truncated to this size.</p>
<dt><code>RLIMIT_CPU</code></p>
<dd> This is a limit, in seconds, on the amount of CPU time that the process can consume. When the process reaches the soft limit, it is sent a <code>SIGXCPU</code> signal. The default action for this signal is to terminate the process. However, the signal can be caught, and the handler can return control to the main program. If the process continues to consume CPU time, it will be sent <code>SIGXCPU</code> once per second until the hard limit is reached, at which time it is sent <code>SIGKILL</code>. (This latter point describes Linux behavior. Implementations vary in how they treat processes which continue to consume CPU time after reaching the soft limit. Portable applications that need to catch this signal should perform an orderly termination upon first receipt of <code>SIGXCPU</code>.)</p>
<dt><code>RLIMIT_DATA</code></p>
<dd> This is the maximum size of the process&#8217;s data segment (initialized data, uninitialized data, and heap). The limit is specified in bytes, and is rounded down to the system page size. This limit affects calls to <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), and (since Linux 4.7) <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), which fail with the error <code>ENOMEM</code> upon encountering the soft limit of this resource.</p>
<dt><code>RLIMIT_FSIZE</code></p>
<dd> This is the maximum size in bytes of files that the process may create. Attempts to extend a file beyond this limit result in delivery of a <code>SIGXFSZ</code> signal. By default, this signal terminates a process, but a process can catch this signal instead, in which case the relevant system call (e.g., <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-truncate/">truncate</a></code>(2)) fails with the error <code>EFBIG</code>.</p>
<dt><code>RLIMIT_LOCKS</code> (Linux 2.4.0 to 2.4.24)</p>
<dd> This is a limit on the combined number of <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locks and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) leases that this process may establish.</p>
<dt><code>RLIMIT_MEMLOCK</code></p>
<dd> This is the maximum number of bytes of memory that may be locked into RAM. This limit is in effect rounded down to the nearest multiple of the system page size. This limit affects <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2), and the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_LOCKED</code> operation. Since Linux 2.6.9, it also affects the <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2) <code>SHM_LOCK</code> operation, where it sets a maximum on the total bytes in shared memory segments (see <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)) that may be locked by the real user ID of the calling process. The <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2) <code>SHM_LOCK</code> locks are accounted for separately from the per-process memory locks established by <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2), and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_LOCKED</code>; a process can lock bytes up to this limit in each of these two categories.</p>
<dt>
<dd> In Linux kernels before 2.6.9, this limit controlled the amount of memory that could be locked by a privileged process. Since Linux 2.6.9, no limits are placed on the amount of memory that a privileged process may lock, and this limit instead governs the amount of memory that an unprivileged process may lock.</p>
<dt><code>RLIMIT_MSGQUEUE</code> (since Linux 2.6.8)</p>
<dd> This is a limit on the number of bytes that can be allocated for POSIX message queues for the real user ID of the calling process. This limit is enforced for <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). Each message queue that the user creates counts (until it is removed) against this limit according to the formula:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since Linux 3.5:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bytes&nbsp;=&nbsp;attr.mq_maxmsg&nbsp;*&nbsp;sizeof(struct msg_msg)&nbsp;+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;min(attr.mq_maxmsg, MQ_PRIO_MAX)&nbsp;*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(struct posix_msg_tree_node)+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For overhead&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attr.mq_maxmsg&nbsp;*&nbsp;attr.mq_msgsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For message data&nbsp;*/</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Linux 3.4 and earlier:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bytes&nbsp;=&nbsp;attr.mq_maxmsg&nbsp;*&nbsp;sizeof(struct msg_msg&nbsp;*)&nbsp;+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For overhead&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attr.mq_maxmsg&nbsp;*&nbsp;attr.mq_msgsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For message data&nbsp;*/</p>
<dt>
<dd> where <i>attr</i> is the <i>mq_attr</i> structure specified as the fourth argument to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), and the <i>msg_msg</i> and <i>posix_msg_tree_node</i> structures are kernel-internal structures.</p>
<dt>
<dd> The &quot;overhead&quot; addend in the formula accounts for overhead bytes required by the implementation and ensures that the user cannot create an unlimited number of zero-length messages (such messages nevertheless each consume some system memory for bookkeeping overhead).</p>
<dt><code>RLIMIT_NICE</code> (since Linux 2.6.12, but see BUGS below)</p>
<dd> This specifies a ceiling to which the process&#8217;s nice value can be raised using <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2) or <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2). The actual ceiling for the nice value is calculated as <i>20 &#8211; rlim_cur</i>. The useful range for this limit is thus from 1 (corresponding to a nice value of 19) to 40 (corresponding to a nice value of -20). This unusual choice of range was necessary because negative numbers cannot be specified as resource limit values, since they typically have special meanings. For example, <code>RLIM_INFINITY</code> typically is the same as -1. For more detail on the nice value, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><code>RLIMIT_NOFILE</code></p>
<dd> This specifies a value one greater than the maximum file descriptor number that can be opened by this process. Attempts (<code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), etc.) to exceed this limit yield the error <code>EMFILE</code>. (Historically, this limit was named <code>RLIMIT_OFILE</code> on BSD.)</p>
<dt>
<dd> Since Linux 4.5, this limit also defines the maximum number of file descriptors that an unprivileged process (one without the <code>CAP_SYS_RESOURCE</code> capability) may have &quot;in flight&quot; to other processes, by being passed across UNIX domain sockets. This limit applies to the <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) system call. For further details, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7).</p>
<dt><code>RLIMIT_NPROC</code></p>
<dd> This is a limit on the number of extant process (or, more precisely on Linux, threads) for the real user ID of the calling process. So long as the current number of processes belonging to this process&#8217;s real user ID is greater than or equal to this limit, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) fails with the error <code>EAGAIN</code>.</p>
<dt>
<dd> The <code>RLIMIT_NPROC</code> limit is not enforced for processes that have either the <code>CAP_SYS_ADMIN</code> or the <code>CAP_SYS_RESOURCE</code> capability.</p>
<dt><code>RLIMIT_RSS</code></p>
<dd> This is a limit (in bytes) on the process&#8217;s resident set (the number of virtual pages resident in RAM). This limit has effect only in Linux 2.4.x, x &lt; 30, and there affects only calls to <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) specifying <code>MADV_WILLNEED</code>.</p>
<dt><code>RLIMIT_RTPRIO</code> (since Linux 2.6.12, but see BUGS)</p>
<dd> This specifies a ceiling on the real-time priority that may be set for this process using <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) and <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2).</p>
<dt>
<dd> For further details on real-time scheduling policies, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<dt><code>RLIMIT_RTTIME</code> (since Linux 2.6.25)</p>
<dd> This is a limit (in microseconds) on the amount of CPU time that a process scheduled under a real-time scheduling policy may consume without making a blocking system call. For the purpose of this limit, each time a process makes a blocking system call, the count of its consumed CPU time is reset to zero. The CPU time count is not reset if the process continues trying to use the CPU but is preempted, its time slice expires, or it calls <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2).</p>
<dt>
<dd> Upon reaching the soft limit, the process is sent a <code>SIGXCPU</code> signal. If the process catches or ignores this signal and continues consuming CPU time, then <code>SIGXCPU</code> will be generated once each second until the hard limit is reached, at which point the process is sent a <code>SIGKILL</code> signal.</p>
<dt>
<dd> The intended use of this limit is to stop a runaway real-time process from locking up the system.</p>
<dt>
<dd> For further details on real-time scheduling policies, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<dt><code>RLIMIT_SIGPENDING</code> (since Linux 2.6.8)</p>
<dd> This is a limit on the number of signals that may be queued for the real user ID of the calling process. Both standard and real-time signals are counted for the purpose of checking this limit. However, the limit is enforced only for <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3); it is always possible to use <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) to queue one instance of any of the signals that are not already queued to the process.</p>
<dt><code>RLIMIT_STACK</code></p>
<dd> This is the maximum size of the process stack, in bytes. Upon reaching this limit, a <code>SIGSEGV</code> signal is generated. To handle this signal, a process must employ an alternate signal stack (<code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)).</p>
<dt>
<dd> Since Linux 2.6.23, this limit also determines the amount of space used for the process&#8217;s command-line arguments and environment variables; for details, see <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</dl>
<h3>prlimit()</h3>
<p> The Linux-specific <code>prlimit</code>() system call combines and extends the functionality of <code>setrlimit</code>() and <code>getrlimit</code>(). It can be used to both set and get the resource limits of an arbitrary process. </p>
<p> The <i>resource</i> argument has the same meaning as for <code>setrlimit</code>() and <code>getrlimit</code>(). </p>
<p> If the <i>new_limit</i> argument is a not NULL, then the <i>rlimit</i> structure to which it points is used to set new values for the soft and hard limits for <i>resource</i>. If the <i>old_limit</i> argument is a not NULL, then a successful call to <code>prlimit</code>() places the previous soft and hard limits for <i>resource</i> in the <i>rlimit</i> structure pointed to by <i>old_limit</i>. </p>
<p> The <i>pid</i> argument specifies the ID of the process on which the call is to operate. If <i>pid</i> is 0, then the call applies to the calling process. To set or get the resources of a process other than itself, the caller must have the <code>CAP_SYS_RESOURCE</code> capability in the user namespace of the process whose resource limits are being changed, or the real, effective, and saved set user IDs of the target process must match the real user ID of the caller <i>and</i> the real, effective, and saved set group IDs of the target process must match the real group ID of the caller.</p>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> A pointer argument points to a location outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>resource</i> is not valid; or, for <code>setrlimit</code>() or <code>prlimit</code>(): <i>rlim-&gt;rlim_cur</i> was greater than <i>rlim-&gt;rlim_max</i>.</p>
<dt><code>EPERM</code></p>
<dd> An unprivileged process tried to raise the hard limit; the <code>CAP_SYS_RESOURCE</code> capability is required to do this.</p>
<dt><code>EPERM</code></p>
<dd> The caller tried to increase the hard <code>RLIMIT_NOFILE</code> limit above the maximum defined by <i>/proc/sys/fs/nr_open</i> (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5))</p>
<dt><code>EPERM</code></p>
<dd> (<code>prlimit</code>()) The calling process did not have permission to set limits for the process specified by <i>pid</i>.</p>
<dt><code>ESRCH</code></p>
<dd> Could not find a process with the ID specified in <i>pid</i>.</dl>
<h2>VERSIONS</h2>
<p> The <code>prlimit</code>() system call is available since Linux 2.6.36. Library support is available since glibc 2.13.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrlimit</code>(), <code>setrlimit</code>(), <code>prlimit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>getrlimit</code>(), <code>setrlimit</code>(): POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. </p>
<p> <code>prlimit</code>(): Linux-specific. </p>
<p> <code>RLIMIT_MEMLOCK</code> and <code>RLIMIT_NPROC</code> derive from BSD and are not specified in POSIX.1; they are present on the BSDs and Linux, but on few other implementations. <code>RLIMIT_RSS</code> derives from BSD and is not specified in POSIX.1; it is nevertheless present on most implementations. <code>RLIMIT_MSGQUEUE</code>, <code>RLIMIT_NICE</code>, <code>RLIMIT_RTPRIO</code>, <code>RLIMIT_RTTIME</code>, and <code>RLIMIT_SIGPENDING</code> are Linux-specific.</p>
<h2>NOTES</h2>
<p> A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s resource limits. Resource limits are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Resource limits are per-process attributes that are shared by all of the threads in a process. </p>
<p> Lowering the soft limit for a resource below the process&#8217;s current consumption of that resource will succeed (but will prevent the process from further increasing its consumption of the resource). </p>
<p> One can set the resource limits of the shell using the built-in <i>ulimit</i> command (<i>limit</i> in <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1)). The shell&#8217;s resource limits are inherited by the processes that it creates to execute commands. </p>
<p> Since Linux 2.6.24, the resource limits of any process can be inspected via <i>/proc/[pid]/limits</i>; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). </p>
<p> Ancient systems provided a <code>vlimit</code>() function with a similar purpose to <code>setrlimit</code>(). For backward compatibility, glibc also provides <code>vlimit</code>(). All new applications should be written using <code>setrlimit</code>().</p>
<h3>C library/kernel ABI differences</h3>
<p> Since version 2.13, the glibc <code>getrlimit</code>() and <code>setrlimit</code>() wrapper functions no longer invoke the corresponding system calls, but instead employ <code>prlimit</code>(), for the reasons described in BUGS. </p>
<p> The name of the glibc wrapper function is <code>prlimit</code>(); the underlying system call is <code>prlimit64</code>().</p>
<h2>BUGS</h2>
<p> In older Linux kernels, the <code>SIGXCPU</code> and <code>SIGKILL</code> signals delivered when a process encountered the soft and hard <code>RLIMIT_CPU</code> limits were delivered one (CPU) second later than they should have been. This was fixed in kernel 2.6.8. </p>
<p> In 2.6.x kernels before 2.6.17, a <code>RLIMIT_CPU</code> limit of 0 is wrongly treated as &quot;no limit&quot; (like <code>RLIM_INFINITY</code>). Since Linux 2.6.17, setting a limit of 0 does have an effect, but is actually treated as a limit of 1 second. </p>
<p> A kernel bug means that <code>RLIMIT_RTPRIO</code> does not work in kernel 2.6.12; the problem is fixed in kernel 2.6.13. </p>
<p> In kernel 2.6.12, there was an off-by-one mismatch between the priority ranges returned by <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2) and <code>RLIMIT_NICE</code>. This had the effect that the actual ceiling for the nice value was calculated as <i>19 &#8211; rlim_cur</i>. This was fixed in kernel 2.6.13. </p>
<p> Since Linux 2.6.12, if a process reaches its soft <code>RLIMIT_CPU</code> limit and has a handler installed for <code>SIGXCPU</code>, then, in addition to invoking the signal handler, the kernel increases the soft limit by one second. This behavior repeats if the process continues to consume CPU time, until the hard limit is reached, at which point the process is killed. Other implementations do not change the <code>RLIMIT_CPU</code> soft limit in this manner, and the Linux behavior is probably not standards conformant; portable applications should avoid relying on this Linux-specific behavior. The Linux-specific <code>RLIMIT_RTTIME</code> limit exhibits the same behavior when the soft limit is encountered. </p>
<p> Kernels before 2.4.22 did not diagnose the error <code>EINVAL</code> for <code>setrlimit</code>() when <i>rlim-&gt;rlim_cur</i> was greater than <i>rlim-&gt;rlim_max</i>. </p>
<p> Linux doesn&#8217;t return an error when an attempt to set <code>RLIMIT_CPU</code> has failed, for compatibility reasons.</p>
<h3>Representation of large resource limit values on 32-bit platforms</h3>
<p> The glibc <code>getrlimit</code>() and <code>setrlimit</code>() wrapper functions use a 64-bit <i>rlim_t</i> data type, even on 32-bit platforms. However, the <i>rlim_t</i> data type used in the <code>getrlimit</code>() and <code>setrlimit</code>() system calls is a (32-bit) <i>unsigned long</i>. Furthermore, in Linux, the kernel represents resource limits on 32-bit platforms as <i>unsigned long</i>. However, a 32-bit data type is not wide enough. The most pertinent limit here is <code>RLIMIT_FSIZE</code>, which specifies the maximum size to which a file can grow: to be useful, this limit must be represented using a type that is as wide as the type used to represent file offsets&#8212;that is, as wide as a 64-bit <code>off_t</code> (assuming a program compiled with <i>_FILE_OFFSET_BITS=64</i>). </p>
<p> To work around this kernel limitation, if a program tried to set a resource limit to a value larger than can be represented in a 32-bit <i>unsigned long</i>, then the glibc <code>setrlimit</code>() wrapper function silently converted the limit value to <code>RLIM_INFINITY</code>. In other words, the requested resource limit setting was silently ignored. </p>
<p> Since version 2.13, glibc works around the limitations of the <code>getrlimit</code>() and <code>setrlimit</code>() system calls by implementing <code>setrlimit</code>() and <code>getrlimit</code>() as wrapper functions that call <code>prlimit</code>().</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>prlimit</code>(). </p>
<p> #define _GNU_SOURCE #define _FILE_OFFSET_BITS 64 #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;time.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/resource.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct rlimit old, new;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct rlimit&nbsp;*newp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t pid; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!(argc&nbsp;==&nbsp;2 || argc&nbsp;==&nbsp;4))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;pid&gt;&nbsp;[&lt;new-soft-limit&gt;&nbsp;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;&lt;new-hard-limit&gt;]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid&nbsp;=&nbsp;atoi(argv[1]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of target process&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;newp&nbsp;=&nbsp;NULL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;==&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new.rlim_cur&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new.rlim_max&nbsp;=&nbsp;atoi(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;newp&nbsp;=&nbsp;&amp;new;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Set CPU time limit of target process;&nbsp;retrieve and display<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;previous limit&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(prlimit(pid, RLIMIT_CPU, newp,&nbsp;&amp;old)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;prlimit-1&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Previous limits: soft=%jd;&nbsp;hard=%jd
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;old.rlim_cur,&nbsp;(intmax_t)&nbsp;old.rlim_max); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Retrieve and display new CPU time limit&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(prlimit(pid, RLIMIT_CPU, NULL,&nbsp;&amp;old)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;prlimit-2&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;New limits: soft=%jd;&nbsp;hard=%jd
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;old.rlim_cur,&nbsp;(intmax_t)&nbsp;old.rlim_max); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-prlimit/">prlimit</a></code>(1), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2), <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-quotactl/">quotactl</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-ulimit/">ulimit</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
