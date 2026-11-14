---
title: "semtimedop(2)"
name: "semtimedop"
section: "2"
letter: "s"
url: "/docs/linux/man/2-semtimedop/"
description: "semop, semtimedop – System V semaphore operations"
---

<h2 class="name">NAME</h2>
<p> semop, semtimedop &#8211; System V semaphore operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;
#include &lt;sys/types.h&gt;
int semop(int semid, struct sembuf *sops, size_t nsops);
int semtimedop(int semid, struct sembuf *sops, size_t nsops,
               const struct timespec *timeout);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>semtimedop</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> Each semaphore in a System V semaphore set has the following associated values: </p>
<p> unsigned short semval; /* semaphore value */ unsigned short semzcnt; /* # waiting for zero */ unsigned short semncnt; /* # waiting for increase */ pid_t sempid; /* PID of process that last </p>
<p> <code>semop</code>() performs operations on selected semaphores in the set indicated by <i>semid</i>. Each of the <i>nsops</i> elements in the array pointed to by <i>sops</i> is a structure that specifies an operation to be performed on a single semaphore. The elements of this structure are of type <i>struct sembuf</i>, containing the following members: </p>
<p> unsigned short sem_num; /* semaphore number */ short sem_op; /* semaphore operation */ short sem_flg; /* operation flags */ </p>
<p> Flags recognized in <i>sem_flg</i> are <code>IPC_NOWAIT</code> and <code>SEM_UNDO</code>. If an operation specifies <code>SEM_UNDO</code>, it will be automatically undone when the process terminates. </p>
<p> The set of operations contained in <i>sops</i> is performed in <i>array order</i>, and <i>atomically</i>, that is, the operations are performed either as a complete unit, or not at all. The behavior of the system call if not all operations can be performed immediately depends on the presence of the <code>IPC_NOWAIT</code> flag in the individual <i>sem_flg</i> fields, as noted below. </p>
<p> Each operation is performed on the <i>sem_num</i>-th semaphore of the semaphore set, where the first semaphore of the set is numbered 0. There are three types of operation, distinguished by the value of <i>sem_op</i>. </p>
<p> If <i>sem_op</i> is a positive integer, the operation adds this value to the semaphore value (<i>semval</i>). Furthermore, if <code>SEM_UNDO</code> is specified for this operation, the system subtracts the value <i>sem_op</i> from the semaphore adjustment (<i>semadj</i>) value for this semaphore. This operation can always proceed&#8212;it never forces a thread to wait. The calling process must have alter permission on the semaphore set. </p>
<p> If <i>sem_op</i> is zero, the process must have read permission on the semaphore set. This is a &quot;wait-for-zero&quot; operation: if <i>semval</i> is zero, the operation can immediately proceed. Otherwise, if <code>IPC_NOWAIT</code> is specified in <i>sem_flg</i>, <code>semop</code>() fails with <i>errno</i> set to <code>EAGAIN</code> (and none of the operations in <i>sops</i> is performed). Otherwise, <i>semzcnt</i> (the count of threads waiting until this semaphore&#8217;s value becomes zero) is incremented by one and the thread sleeps until one of the following occurs:</p>
<dl>
<dt>&bull;</p>
<dd> <i>semval</i> becomes 0, at which time the value of <i>semzcnt</i> is decremented.</p>
<dt>&bull;</p>
<dd> The semaphore set is removed: <code>semop</code>() fails, with <i>errno</i> set to <code>EIDRM</code>.</p>
<dt>&bull;</p>
<dd> The calling thread catches a signal: the value of <i>semzcnt</i> is decremented and <code>semop</code>() fails, with <i>errno</i> set to <code>EINTR</code>.</dl>
<p> If <i>sem_op</i> is less than zero, the process must have alter permission on the semaphore set. If <i>semval</i> is greater than or equal to the absolute value of <i>sem_op</i>, the operation can proceed immediately: the absolute value of <i>sem_op</i> is subtracted from <i>semval</i>, and, if <code>SEM_UNDO</code> is specified for this operation, the system adds the absolute value of <i>sem_op</i> to the semaphore adjustment (<i>semadj</i>) value for this semaphore. If the absolute value of <i>sem_op</i> is greater than <i>semval</i>, and <code>IPC_NOWAIT</code> is specified in <i>sem_flg</i>, <code>semop</code>() fails, with <i>errno</i> set to <code>EAGAIN</code> (and none of the operations in <i>sops</i> is performed). Otherwise, <i>semncnt</i> (the counter of threads waiting for this semaphore&#8217;s value to increase) is incremented by one and the thread sleeps until one of the following occurs:</p>
<dl>
<dt>&bull;</p>
<dd> <i>semval</i> becomes greater than or equal to the absolute value of <i>sem_op</i>: the operation now proceeds, as described above.</p>
<dt>&bull;</p>
<dd> The semaphore set is removed from the system: <code>semop</code>() fails, with <i>errno</i> set to <code>EIDRM</code>.</p>
<dt>&bull;</p>
<dd> The calling thread catches a signal: the value of <i>semncnt</i> is decremented and <code>semop</code>() fails, with <i>errno</i> set to <code>EINTR</code>.</dl>
<p> On successful completion, the <i>sempid</i> value for each semaphore specified in the array pointed to by <i>sops</i> is set to the caller&#8217;s process ID. In addition, the <i>sem_otime</i> is set to the current time.</p>
<h3>semtimedop()</h3>
<p> <code>semtimedop</code>() behaves identically to <code>semop</code>() except that in those cases where the calling thread would sleep, the duration of that sleep is limited by the amount of elapsed time specified by the <i>timespec</i> structure whose address is passed in the <i>timeout</i> argument. (This sleep interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the interval may overrun by a small amount.) If the specified time limit has been reached, <code>semtimedop</code>() fails with <i>errno</i> set to <code>EAGAIN</code> (and none of the operations in <i>sops</i> is performed). If the <i>timeout</i> argument is NULL, then <code>semtimedop</code>() behaves exactly like <code>semop</code>(). </p>
<p> Note that if <code>semtimedop</code>() is interrupted by a signal, causing the call to fail with the error <code>EINTR</code>, the contents of <i>timeout</i> are left unchanged.</p>
<h2>RETURN VALUE</h2>
<p> If successful, <code>semop</code>() and <code>semtimedop</code>() return 0; otherwise they return -1 with <i>errno</i> indicating the error.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> is set to one of the following:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> The argument <i>nsops</i> is greater than <code>SEMOPM</code>, the maximum number of operations allowed per system call.</p>
<dt><code>EACCES</code></p>
<dd> The calling process does not have the permissions required to perform the specified semaphore operations, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EAGAIN</code></p>
<dd> An operation could not proceed immediately and either <code>IPC_NOWAIT</code> was specified in <i>sem_flg</i> or the time limit specified in <i>timeout</i> expired.</p>
<dt><code>EFAULT</code></p>
<dd> An address specified in either the <i>sops</i> or the <i>timeout</i> argument isn&#8217;t accessible.</p>
<dt><code>EFBIG</code></p>
<dd> For some operation the value of <i>sem_num</i> is less than 0 or greater than or equal to the number of semaphores in the set.</p>
<dt><code>EIDRM</code></p>
<dd> The semaphore set was removed.</p>
<dt><code>EINTR</code></p>
<dd> While blocked in this system call, the thread caught a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The semaphore set doesn&#8217;t exist, or <i>semid</i> is less than zero, or <i>nsops</i> has a nonpositive value.</p>
<dt><code>ENOMEM</code></p>
<dd> The <i>sem_flg</i> of some operation specified <code>SEM_UNDO</code> and the system does not have enough memory to allocate the undo structure.</p>
<dt><code>ERANGE</code></p>
<dd> For some operation <i>sem_op+semval</i> is greater than <code>SEMVMX</code>, the implementation dependent maximum value for <i>semval</i>.</dl>
<h2>VERSIONS</h2>
<p> <code>semtimedop</code>() first appeared in Linux 2.5.52, and was subsequently backported into kernel 2.4.22. Glibc support for <code>semtimedop</code>() first appeared in version 2.3.3.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> The <i>sem_undo</i> structures of a process aren&#8217;t inherited by the child produced by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), but they are inherited across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) system call. </p>
<p> <code>semop</code>() is never automatically restarted after being interrupted by a signal handler, regardless of the setting of the <code>SA_RESTART</code> flag when establishing a signal handler. </p>
<p> A semaphore adjustment (<i>semadj</i>) value is a per-process, per-semaphore integer that is the negated sum of all operations performed on a semaphore specifying the <code>SEM_UNDO</code> flag. Each process has a list of <i>semadj</i> values&#8212;one value for each semaphore on which it has operated using <code>SEM_UNDO</code>. When a process terminates, each of its per-semaphore <i>semadj</i> values is added to the corresponding semaphore, thus undoing the effect of that process&#8217;s operations on the semaphore (but see BUGS below). When a semaphore&#8217;s value is directly set using the <code>SETVAL</code> or <code>SETALL</code> request to <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), the corresponding <i>semadj</i> values in all processes are cleared. The <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_SYSVSEM</code> flag allows more than one process to share a <i>semadj</i> list; see <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) for details. </p>
<p> The <i>semval</i>, <i>sempid</i>, <i>semzcnt</i>, and <i>semnct</i> values for a semaphore can all be retrieved using appropriate <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2) calls.</p>
<h3>Semaphore limits</h3>
<p> The following limits on semaphore set resources affect the <code>semop</code>() call:</p>
<dl>
<dt><code>SEMOPM</code></p>
<dd> Maximum number of operations allowed for one <code>semop</code>() call. Before Linux 3.19, the default value for this limit was 32. Since Linux 3.19, the default value is 500. On Linux, this limit can be read and modified via the third field of <i>/proc/sys/kernel/sem</i>. <i>Note</i>: this limit should not be raised above 1000, because of the risk of that <code>semop</code>() fails due to kernel memory fragmentation when allocating memory to copy the <i>sops</i> array.</p>
<dt><code>SEMVMX</code></p>
<dd> Maximum allowable value for <i>semval</i>: implementation dependent (32767).</dl>
<p> The implementation has no intrinsic limits for the adjust on exit maximum value (<code>SEMAEM</code>), the system wide maximum number of undo structures (<code>SEMMNU</code>) and the per-process maximum number of undo entries system parameters.</p>
<h2>BUGS</h2>
<p> When a process terminates, its set of associated <i>semadj</i> structures is used to undo the effect of all of the semaphore operations it performed with the <code>SEM_UNDO</code> flag. This raises a difficulty: if one (or more) of these semaphore adjustments would result in an attempt to decrease a semaphore&#8217;s value below zero, what should an implementation do? One possible approach would be to block until all the semaphore adjustments could be performed. This is however undesirable since it could force process termination to block for arbitrarily long periods. Another possibility is that such semaphore adjustments could be ignored altogether (somewhat analogously to failing when <code>IPC_NOWAIT</code> is specified for a semaphore operation). Linux adopts a third approach: decreasing the semaphore value as far as possible (i.e., to zero) and allowing process termination to proceed immediately. </p>
<p> In kernels 2.6.x, x &lt;= 10, there is a bug that in some circumstances prevents a thread that is waiting for a semaphore value to become zero from being woken up when the value does actually become zero. This bug is fixed in kernel 2.6.11.</p>
<h2>EXAMPLES</h2>
<p> The following code segment uses <code>semop</code>() to atomically wait for the value of semaphore 0 to become zero, and then increment the semaphore value by one. </p>
<p> struct sembuf sops[2]; int semid; </p>
<p> /* Code to set <i>semid</i> omitted */ </p>
<p> sops[0].sem_num = 0; /* Operate on semaphore 0 */ sops[0].sem_op = 0; /* Wait for value to equal 0 */ sops[0].sem_flg = 0; </p>
<p> sops[1].sem_num = 0; /* Operate on semaphore 0 */ sops[1].sem_op = 1; /* Increment value by one */ sops[1].sem_flg = 0; </p>
<p> if (semop(semid, sops, 2) == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;semop&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> A further example of the use of <code>semop</code>() can be found in <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
