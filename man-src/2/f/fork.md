---
title: "fork(2)"
name: "fork"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fork/"
description: "fork – create a child process"
---

<h2 class="name">NAME</h2>
<p> fork &#8211; create a child process </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>pid_t fork(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>fork</code>() creates a new process by duplicating the calling process. The new process is referred to as the <i>child</i> process. The calling process is referred to as the <i>parent</i> process. </p>
<p> The child process and the parent process run in separate memory spaces. At the time of <code>fork</code>() both memory spaces have the same content. Memory writes, file mappings (<code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)), and unmappings (<code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2)) performed by one of the processes do not affect the other. </p>
<p> The child process is an exact duplicate of the parent process except for the following points:</p>
<dl>
<dt>*</p>
<dd> The child has its own unique process ID, and this PID does not match the ID of any existing process group (<code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2)) or session.</p>
<dt>*</p>
<dd> The child&#8217;s parent process ID is the same as the parent&#8217;s process ID.</p>
<dt>*</p>
<dd> The child does not inherit its parent&#8217;s memory locks (<code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2)).</p>
<dt>*</p>
<dd> Process resource utilizations (<code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2)) and CPU time counters (<code><a href="/docs/linux/man/2-times/">times</a></code>(2)) are reset to zero in the child.</p>
<dt>*</p>
<dd> The child&#8217;s set of pending signals is initially empty (<code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2)).</p>
<dt>*</p>
<dd> The child does not inherit semaphore adjustments from its parent (<code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)).</p>
<dt>*</p>
<dd> The child does not inherit process-associated record locks from its parent (<code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)). (On the other hand, it does inherit <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) open file description locks and <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) locks from its parent.)</p>
<dt>*</p>
<dd> The child does not inherit timers from its parent (<code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2)).</p>
<dt>*</p>
<dd> The child does not inherit outstanding asynchronous I/O operations from its parent (<code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3)), nor does it inherit any asynchronous I/O contexts from its parent (see <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2)).</dl>
<p> The process attributes in the preceding list are all specified in POSIX.1. The parent and child also differ with respect to the following Linux-specific process attributes:</p>
<dl>
<dt>*</p>
<dd> The child does not inherit directory change notifications (dnotify) from its parent (see the description of <code>F_NOTIFY</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</p>
<dt>*</p>
<dd> The <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_PDEATHSIG</code> setting is reset so that the child does not receive a signal when its parent terminates.</p>
<dt>*</p>
<dd> The default timer slack value is set to the parent&#8217;s current timer slack value. See the description of <code>PR_SET_TIMERSLACK</code> in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2).</p>
<dt>*</p>
<dd> Memory mappings that have been marked with the <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) <code>MADV_DONTFORK</code> flag are not inherited across a <code>fork</code>().</p>
<dt>*</p>
<dd> Memory in address ranges that have been marked with the <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) <code>MADV_WIPEONFORK</code> flag is zeroed in the child after a <code>fork</code>(). (The <code>MADV_WIPEONFORK</code> setting remains in place for those address ranges in the child.)</p>
<dt>*</p>
<dd> The termination signal of the child is always <code>SIGCHLD</code> (see <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)).</p>
<dt>*</p>
<dd> The port access permission bits set by <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2) are not inherited by the child; the child must turn on any bits that it requires using <code><a href="/docs/linux/man/2-ioperm/">ioperm</a></code>(2).</dl>
<p> Note the following further points:</p>
<dl>
<dt>*</p>
<dd> The child process is created with a single thread&#8212;the one that called <code>fork</code>(). The entire virtual address space of the parent is replicated in the child, including the states of mutexes, condition variables, and other pthreads objects; the use of <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) may be helpful for dealing with problems that this can cause.</p>
<dt>*</p>
<dd> After a <code>fork</code>() in a multithreaded program, the child can safely call only async-signal-safe functions (see <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7)) until such time as it calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>*</p>
<dd> The child inherits copies of the parent&#8217;s set of open file descriptors. Each file descriptor in the child refers to the same open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) as the corresponding file descriptor in the parent. This means that the two file descriptors share open file status flags, file offset, and signal-driven I/O attributes (see the description of <code>F_SETOWN</code> and <code>F_SETSIG</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</p>
<dt>*</p>
<dd> The child inherits copies of the parent&#8217;s set of open message queue descriptors (see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)). Each file descriptor in the child refers to the same open message queue description as the corresponding file descriptor in the parent. This means that the two file descriptors share the same flags (<i>mq_flags</i>).</p>
<dt>*</p>
<dd> The child inherits copies of the parent&#8217;s set of open directory streams (see <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3)). POSIX.1 says that the corresponding directory streams in the parent and child <i>may</i> share the directory stream positioning; on Linux/glibc they do not.</dl>
<h2>RETURN VALUE</h2>
<p> On success, the PID of the child process is returned in the parent, and 0 is returned in the child. On failure, -1 is returned in the parent, no child process is created, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> A system-imposed limit on the number of threads was encountered. There are a number of limits that may trigger this error:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> the <code>RLIMIT_NPROC</code> soft resource limit (set via <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)), which limits the number of processes and threads for a real user ID, was reached;</p>
<dt>*</p>
<dd> the kernel&#8217;s system-wide limit on the number of processes and threads, <i>/proc/sys/kernel/threads-max</i>, was reached (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5));</p>
<dt>*</p>
<dd> the maximum number of PIDs, <i>/proc/sys/kernel/pid_max</i>, was reached (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)); or</p>
<dt>*</p>
<dd> the PID limit (<i>pids.max</i>) imposed by the cgroup &quot;process number&quot; (PIDs) controller was reached.</dl>
</dl>
<dt><code>EAGAIN</code></p>
<dd> The caller is operating under the <code>SCHED_DEADLINE</code> scheduling policy and does not have the reset-on-fork flag set. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><code>ENOMEM</code></p>
<dd> <code>fork</code>() failed to allocate the necessary kernel structures because memory is tight.</p>
<dt><code>ENOMEM</code></p>
<dd> An attempt was made to create a child process in a PID namespace whose &quot;init&quot; process has terminated. See <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7).</p>
<dt><code>ENOSYS</code></p>
<dd> <code>fork</code>() is not supported on this platform (for example, hardware without a Memory-Management Unit).</p>
<dt><code>ERESTARTNOINTR</code> (since Linux 2.6.17)</p>
<dd> System call was interrupted by a signal and will be restarted. (This can be seen only during a trace.)</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Under Linux, <code>fork</code>() is implemented using copy-on-write pages, so the only penalty that it incurs is the time and memory required to duplicate the parent&#8217;s page tables, and to create a unique task structure for the child.</p>
<h3>C library/kernel differences</h3>
<p> Since version 2.3.3, rather than invoking the kernel&#8217;s <code>fork</code>() system call, the glibc <code>fork</code>() wrapper that is provided as part of the NPTL threading implementation invokes <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with flags that provide the same effect as the traditional system call. (A call to <code>fork</code>() is equivalent to a call to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) specifying <i>flags</i> as just <code>SIGCHLD</code>.) The glibc wrapper invokes any fork handlers that have been established using <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3).</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) and <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-daemon/">daemon</a></code>(3), <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
