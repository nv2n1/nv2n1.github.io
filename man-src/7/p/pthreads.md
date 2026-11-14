---
title: "pthreads(7)"
name: "pthreads"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pthreads/"
description: "pthreads – POSIX threads"
---

<p>pthreads &#8211; POSIX threads</p>
<h2>Description</h2>
<p>POSIX.1 specifies a set of interfaces (functions, header files) for threaded programming commonly known as POSIX threads, or Pthreads. A single process can contain multiple threads, all of which are executing the same program. These threads share the same global memory (data and heap segments), but each thread has its own stack (automatic variables). </p>
<p> POSIX.1 also requires that threads share a range of other attributes (i.e., these attributes are process-wide rather than per-thread):</p>
<dl>
<dt>&#8211;</p>
<dd>process ID</p>
<dt>&#8211;</p>
<dd>parent process ID</p>
<dt>&#8211;</p>
<dd>process group ID and session ID</p>
<dt>&#8211;</p>
<dd>controlling terminal</p>
<dt>&#8211;</p>
<dd>user and group IDs</p>
<dt>&#8211;</p>
<dd>open file descriptors</p>
<dt>&#8211;</p>
<dd>record locks (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2))</p>
<dt>&#8211;</p>
<dd>signal dispositions</p>
<dt>&#8211;</p>
<dd>file mode creation mask (<code><a href="/docs/linux/man/2-umask/">umask</a></code>(2))</p>
<dt>&#8211;</p>
<dd>current directory (<code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2)) and root directory (<code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2))</p>
<dt>&#8211;</p>
<dd>interval timers (<code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2)) and POSIX timers (<code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2))</p>
<dt>&#8211;</p>
<dd>nice value (<code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2))</p>
<dt>&#8211;</p>
<dd>resource limits (<code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2))</p>
<dt>&#8211;</p>
<dd>measurements of the consumption of CPU time (<code><a href="/docs/linux/man/2-times/">times</a></code>(2)) and resources (<code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2))</dl>
<p> As well as the stack, POSIX.1 specifies that various other attributes are distinct for each thread, including:</p>
<dl>
<dt>&#8211;</p>
<dd>thread ID (the <i>pthread_t</i> data type)</p>
<dt>&#8211;</p>
<dd>signal mask (<code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3))</p>
<dt>&#8211;</p>
<dd>the <i>errno</i> variable</p>
<dt>&#8211;</p>
<dd>alternate signal stack (<code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2))</p>
<dt>&#8211;</p>
<dd>real-time scheduling policy and priority (<code><a href="/docs/linux/man/7-sched/">sched</a></code>(7))</dl>
<p> The following Linux-specific features are also per-thread:</p>
<dl>
<dt>&#8211;</p>
<dd>capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7))</p>
<dt>&#8211;</p>
<dd>CPU affinity (<code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2))</dl>
<h3>Pthreads function return values</h3>
<p>Most pthreads functions return 0 on success, and an error number on failure. The error numbers that can be returned have the same meaning as the error numbers returned in <i>errno</i> by conventional system calls and C library functions. Note that the pthreads functions do not set <i>errno</i>. For each of the pthreads functions that can return an error, POSIX.1-2001 specifies that the function can never fail with the error <code>EINTR</code>.</p>
<h3>Thread IDs</h3>
<p>Each of the threads in a process has a unique thread identifier (stored in the type <i>pthread_t</i>). This identifier is returned to the caller of <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), and a thread can obtain its own thread identifier using <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3). </p>
<p> Thread IDs are guaranteed to be unique only within a process. (In all pthreads functions that accept a thread ID as an argument, that ID by definition refers to a thread in the same process as the caller.) </p>
<p> The system may reuse a thread ID after a terminated thread has been joined, or a detached thread has terminated. POSIX says: &quot;If an application attempts to use a thread ID whose lifetime has ended, the behavior is undefined.&quot;</p>
<h3>Thread-safe functions</h3>
<p>A thread-safe function is one that can be safely (i.e., it will deliver the same results regardless of whether it is) called from multiple threads at the same time. </p>
<p> POSIX.1-2001 and POSIX.1-2008 require that all functions specified in the standard shall be thread-safe, except for the following functions: </p>
<p> asctime() basename() catgets() crypt() ctermid() if passed a non-NULL argument ctime() dbm_clearerr() dbm_close() dbm_delete() dbm_error() dbm_fetch() dbm_firstkey() dbm_nextkey() dbm_open() dbm_store() dirname() dlerror() drand48() ecvt() [POSIX.1-2001 only (function removed in POSIX.1-2008)] encrypt() endgrent() endpwent() endutxent() fcvt() [POSIX.1-2001 only (function removed in POSIX.1-2008)] ftw() gcvt() [POSIX.1-2001 only (function removed in POSIX.1-2008)] getc_unlocked() getchar_unlocked() getdate() getenv() getgrent() getgrgid() getgrnam() gethostbyaddr() [POSIX.1-2001 only (function removed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1-2008)] gethostbyname() [POSIX.1-2001 only (function removed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1-2008)] gethostent() getlogin() getnetbyaddr() getnetbyname() getnetent() getopt() getprotobyname() getprotobynumber() getprotoent() getpwent() getpwnam() getpwuid() getservbyname() getservbyport() getservent() getutxent() getutxid() getutxline() gmtime() hcreate() hdestroy() hsearch() inet_ntoa() l64a() lgamma() lgammaf() lgammal() localeconv() localtime() lrand48() mrand48() nftw() nl_langinfo() ptsname() putc_unlocked() putchar_unlocked() putenv() pututxline() rand() readdir() setenv() setgrent() setkey() setpwent() setutxent() strerror() strsignal() [Added in POSIX.1-2008] strtok() system() [Added in POSIX.1-2008] tmpnam() if passed a non-NULL argument ttyname() unsetenv() wcrtomb() if its final argument is NULL wcsrtombs() if its final argument is NULL wcstombs() wctomb()</p>
<h3>Async-cancel-safe functions</h3>
<p>An async-cancel-safe function is one that can be safely called in an application where asynchronous cancelability is enabled (see <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3)). </p>
<p> Only the following functions are required to be async-cancel-safe by POSIX.1-2001 and POSIX.1-2008: </p>
<p> pthread_cancel() pthread_setcancelstate() pthread_setcanceltype()</p>
<h3>Cancellation points</h3>
<p>POSIX.1 specifies that certain functions must, and certain other functions may, be cancellation points. If a thread is cancelable, its cancelability type is deferred, and a cancellation request is pending for the thread, then the thread is canceled when it calls a function that is a cancellation point. </p>
<p> The following functions are required to be cancellation points by POSIX.1-2001 and/or POSIX.1-2008: </p>
<p> accept() aio_suspend() clock_nanosleep() close() connect() creat() fcntl() F_SETLKW fdatasync() fsync() getmsg() getpmsg() lockf() F_LOCK mq_receive() mq_send() mq_timedreceive() mq_timedsend() msgrcv() msgsnd() msync() nanosleep() open() openat() [Added in POSIX.1-2008] pause() poll() pread() pselect() pthread_cond_timedwait() pthread_cond_wait() pthread_join() pthread_testcancel() putmsg() putpmsg() pwrite() read() readv() recv() recvfrom() recvmsg() select() sem_timedwait() sem_wait() send() sendmsg() sendto() sigpause() [POSIX.1-2001 only (moves to &quot;may&quot; list in POSIX.1-2008)] sigsuspend() sigtimedwait() sigwait() sigwaitinfo() sleep() system() tcdrain() usleep() [POSIX.1-2001 only (function removed in POSIX.1-2008)] wait() waitid() waitpid() write() writev() </p>
<p> The following functions may be cancellation points according to POSIX.1-2001 and/or POSIX.1-2008: </p>
<p> access() asctime() asctime_r() catclose() catgets() catopen() chmod() [Added in POSIX.1-2008] chown() [Added in POSIX.1-2008] closedir() closelog() ctermid() ctime() ctime_r() dbm_close() dbm_delete() dbm_fetch() dbm_nextkey() dbm_open() dbm_store() dlclose() dlopen() dprintf() [Added in POSIX.1-2008] endgrent() endhostent() endnetent() endprotoent() endpwent() endservent() endutxent() faccessat() [Added in POSIX.1-2008] fchmod() [Added in POSIX.1-2008] fchmodat() [Added in POSIX.1-2008] fchown() [Added in POSIX.1-2008] fchownat() [Added in POSIX.1-2008] fclose() fcntl() (for any value of cmd argument) fflush() fgetc() fgetpos() fgets() fgetwc() fgetws() fmtmsg() fopen() fpathconf() fprintf() fputc() fputs() fputwc() fputws() fread() freopen() fscanf() fseek() fseeko() fsetpos() fstat() fstatat() [Added in POSIX.1-2008] ftell() ftello() ftw() futimens() [Added in POSIX.1-2008] fwprintf() fwrite() fwscanf() getaddrinfo() getc() getc_unlocked() getchar() getchar_unlocked() getcwd() getdate() getdelim() [Added in POSIX.1-2008] getgrent() getgrgid() getgrgid_r() getgrnam() getgrnam_r() gethostbyaddr() [POSIX.1-2001 only (function removed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1-2008)] gethostbyname() [POSIX.1-2001 only (function removed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX.1-2008)] gethostent() gethostid() gethostname() getline() [Added in POSIX.1-2008] getlogin() getlogin_r() getnameinfo() getnetbyaddr() getnetbyname() getnetent() getopt() (if opterr is nonzero) getprotobyname() getprotobynumber() getprotoent() getpwent() getpwnam() getpwnam_r() getpwuid() getpwuid_r() gets() getservbyname() getservbyport() getservent() getutxent() getutxid() getutxline() getwc() getwchar() getwd() [POSIX.1-2001 only (function removed in POSIX.1-2008)] glob() iconv_close() iconv_open() ioctl() link() linkat() [Added in POSIX.1-2008] lio_listio() [Added in POSIX.1-2008] localtime() localtime_r() lockf() [Added in POSIX.1-2008] lseek() lstat() mkdir() [Added in POSIX.1-2008] mkdirat() [Added in POSIX.1-2008] mkdtemp() [Added in POSIX.1-2008] mkfifo() [Added in POSIX.1-2008] mkfifoat() [Added in POSIX.1-2008] mknod() [Added in POSIX.1-2008] mknodat() [Added in POSIX.1-2008] mkstemp() mktime() nftw() opendir() openlog() pathconf() pclose() perror() popen() posix_fadvise() posix_fallocate() posix_madvise() posix_openpt() posix_spawn() posix_spawnp() posix_trace_clear() posix_trace_close() posix_trace_create() posix_trace_create_withlog() posix_trace_eventtypelist_getnext_id() posix_trace_eventtypelist_rewind() posix_trace_flush() posix_trace_get_attr() posix_trace_get_filter() posix_trace_get_status() posix_trace_getnext_event() posix_trace_open() posix_trace_rewind() posix_trace_set_filter() posix_trace_shutdown() posix_trace_timedgetnext_event() posix_typed_mem_open() printf() psiginfo() [Added in POSIX.1-2008] psignal() [Added in POSIX.1-2008] pthread_rwlock_rdlock() pthread_rwlock_timedrdlock() pthread_rwlock_timedwrlock() pthread_rwlock_wrlock() putc() putc_unlocked() putchar() putchar_unlocked() puts() pututxline() putwc() putwchar() readdir() readdir_r() readlink() [Added in POSIX.1-2008] readlinkat() [Added in POSIX.1-2008] remove() rename() renameat() [Added in POSIX.1-2008] rewind() rewinddir() scandir() [Added in POSIX.1-2008] scanf() seekdir() semop() setgrent() sethostent() setnetent() setprotoent() setpwent() setservent() setutxent() sigpause() [Added in POSIX.1-2008] stat() strerror() strerror_r() strftime() symlink() symlinkat() [Added in POSIX.1-2008] sync() syslog() tmpfile() tmpnam() ttyname() ttyname_r() tzset() ungetc() ungetwc() unlink() unlinkat() [Added in POSIX.1-2008] utime() [Added in POSIX.1-2008] utimensat() [Added in POSIX.1-2008] utimes() [Added in POSIX.1-2008] vdprintf() [Added in POSIX.1-2008] vfprintf() vfwprintf() vprintf() vwprintf() wcsftime() wordexp() wprintf() wscanf() </p>
<p> An implementation may also mark other functions not specified in the standard as cancellation points. In particular, an implementation is likely to mark any nonstandard function that may block as a cancellation point. (This includes most functions that can touch files.) </p>
<p> It should be noted that even if an application is not using asynchronous cancellation, that calling a function from the above list from an asynchronous signal handler may cause the equivalent of asynchronous cancellation. The underlying user code may not expect asynchronous cancellation and the state of the user data may become inconsistent. Therefore signals should be used with caution when entering a region of deferred cancellation.</p>
<h3>Compiling on Linux</h3>
<p>On Linux, programs that use the Pthreads API should be compiled using <i>cc -pthread</i>.</p>
<h3>Linux implementations of POSIX threads</h3>
<p>Over time, two threading implementations have been provided by the GNU C library on Linux:</p>
<dl>
<dt><code>LinuxThreads</code></p>
<dd>This is the original Pthreads implementation. Since glibc 2.4, this implementation is no longer supported.</p>
<dt><code>NPTL</code> (Native POSIX Threads Library)</p>
<dd>This is the modern Pthreads implementation. By comparison with LinuxThreads, NPTL provides closer conformance to the requirements of the POSIX.1 specification and better performance when creating large numbers of threads. NPTL is available since glibc 2.3.2, and requires features that are present in the Linux 2.6 kernel.</dl>
<p> Both of these are so-called 1:1 implementations, meaning that each thread maps to a kernel scheduling entity. Both threading implementations employ the Linux <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) system call. In NPTL, thread synchronization primitives (mutexes, thread joining, and so on) are implemented using the Linux <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) system call.</p>
<h3>LinuxThreads</h3>
<p>The notable features of this implementation are the following:</p>
<dl>
<dt>&#8211;</p>
<dd>In addition to the main (initial) thread, and the threads that the program creates using <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), the implementation creates a &quot;manager&quot; thread. This thread handles thread creation and termination. (Problems can result if this thread is inadvertently killed.)</p>
<dt>&#8211;</p>
<dd>Signals are used internally by the implementation. On Linux 2.2 and later, the first three real-time signals are used (see also <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). On older Linux kernels, <code>SIGUSR1</code> and <code>SIGUSR2</code> are used. Applications must avoid the use of whichever set of signals is employed by the implementation.</p>
<dt>&#8211;</p>
<dd>Threads do not share process IDs. (In effect, LinuxThreads threads are implemented as processes which share more information than usual, but which do not share a common process ID.) LinuxThreads threads (including the manager thread) are visible as separate processes using <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1).</dl>
<p> The LinuxThreads implementation deviates from the POSIX.1 specification in a number of ways, including the following:</p>
<dl>
<dt>&#8211;</p>
<dd>Calls to <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) return a different value in each thread.</p>
<dt>&#8211;</p>
<dd>Calls to <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) in threads other than the main thread return the process ID of the manager thread; instead <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) in these threads should return the same value as <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) in the main thread.</p>
<dt>&#8211;</p>
<dd>When one thread creates a new child process using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), any thread should be able to <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) on the child. However, the implementation allows only the thread that created the child to <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) on it.</p>
<dt>&#8211;</p>
<dd>When a thread calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), all other threads are terminated (as required by POSIX.1). However, the resulting process has the same PID as the thread that called <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2): it should have the same PID as the main thread.</p>
<dt>&#8211;</p>
<dd>Threads do not share user and group IDs. This can cause complications with set-user-ID programs and can cause failures in Pthreads functions if an application changes its credentials using <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2) or similar.</p>
<dt>&#8211;</p>
<dd>Threads do not share a common session ID and process group ID.</p>
<dt>&#8211;</p>
<dd>Threads do not share record locks created using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt>&#8211;</p>
<dd>The information returned by <code><a href="/docs/linux/man/2-times/">times</a></code>(2) and <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2) is per-thread rather than process-wide.</p>
<dt>&#8211;</p>
<dd>Threads do not share semaphore undo values (see <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)).</p>
<dt>&#8211;</p>
<dd>Threads do not share interval timers.</p>
<dt>&#8211;</p>
<dd>Threads do not share a common nice value.</p>
<dt>&#8211;</p>
<dd>POSIX.1 distinguishes the notions of signals that are directed to the process as a whole and signals that are directed to individual threads. According to POSIX.1, a process-directed signal (sent using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), for example) should be handled by a single, arbitrarily selected thread within the process. LinuxThreads does not support the notion of process-directed signals: signals may be sent only to specific threads.</p>
<dt>&#8211;</p>
<dd>Threads have distinct alternate signal stack settings. However, a new thread&#8217;s alternate signal stack settings are copied from the thread that created it, so that the threads initially share an alternate signal stack. (A new thread should start with no alternate signal stack defined. If two threads handle signals on their shared alternate signal stack at the same time, unpredictable program failures are likely to occur.)</dl>
<h3>Nptl</h3>
<p>With NPTL, all of the threads in a process are placed in the same thread group; all members of a thread group share the same PID. NPTL does not employ a manager thread. </p>
<p> NPTL makes internal use of the first two real-time signals; these signals cannot be used in applications. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for further details. </p>
<p> NPTL still has at least one nonconformance with POSIX.1:</p>
<dl>
<dt>&#8211;</p>
<dd>Threads do not share a common nice value.</dl>
<p> Some NPTL nonconformances occur only with older kernels:</p>
<dl>
<dt>&#8211;</p>
<dd>The information returned by <code><a href="/docs/linux/man/2-times/">times</a></code>(2) and <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2) is per-thread rather than process-wide (fixed in kernel 2.6.9).</p>
<dt>&#8211;</p>
<dd>Threads do not share resource limits (fixed in kernel 2.6.10).</p>
<dt>&#8211;</p>
<dd>Threads do not share interval timers (fixed in kernel 2.6.12).</p>
<dt>&#8211;</p>
<dd>Only the main thread is permitted to start a new session using <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2) (fixed in kernel 2.6.16).</p>
<dt>&#8211;</p>
<dd>Only the main thread is permitted to make the process into a process group leader using <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2) (fixed in kernel 2.6.16).</p>
<dt>&#8211;</p>
<dd>Threads have distinct alternate signal stack settings. However, a new thread&#8217;s alternate signal stack settings are copied from the thread that created it, so that the threads initially share an alternate signal stack (fixed in kernel 2.6.16).</dl>
<p> Note the following further points about the NPTL implementation:</p>
<dl>
<dt>&#8211;</p>
<dd>If the stack size soft resource limit (see the description of <code>RLIMIT_STACK</code> in <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)) is set to a value other than <i>unlimited</i>, then this value defines the default stack size for new threads. To be effective, this limit must be set before the program is executed, perhaps using the <i>ulimit -s</i> shell built-in command (<i>limit stacksize</i> in the C shell).</dl>
<h3>Determining the threading implementation</h3>
<p>Since glibc 2.3.2, the <code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1) command can be used to determine the system&#8217;s threading implementation, for example: </p>
<p> bash$ getconf GNU_LIBPTHREAD_VERSION NPTL 2.3.4 </p>
<p> With older glibc versions, a command such as the following should be sufficient to determine the default threading implementation: </p>
<p> bash$ $( ldd /bin/ls | grep libc.so | awk &#8216;{print $3}&#8217; ) | \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;egrep -i&nbsp;&#8216;threads|nptl&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Native POSIX Threads Library by Ulrich Drepper et al</p>
<h3>Selecting the threading implementation: LD_ASSUME_KERNEL</h3>
<p>On systems with a glibc that supports both LinuxThreads and NPTL (i.e., glibc 2.3.<i>x</i>), the <code>LD_ASSUME_KERNEL</code> environment variable can be used to override the dynamic linker&#8217;s default choice of threading implementation. This variable tells the dynamic linker to assume that it is running on top of a particular kernel version. By specifying a kernel version that does not provide the support required by NPTL, we can force the use of LinuxThreads. (The most likely reason for doing this is to run a (broken) application that depends on some nonconformant behavior in LinuxThreads.) For example: </p>
<p> bash$ $( LD_ASSUME_KERNEL=2.2.5 ldd /bin/ls | grep libc.so | \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;awk&nbsp;&#8216;{print&nbsp;$3}&#8217;&nbsp;)&nbsp;| egrep -i&nbsp;&#8216;threads|nptl&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linuxthreads-0.10 by Xavier Leroy</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7), <code><a href="/docs/linux/man/7-futex/">futex</a></code>(7), <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) </p>
<p> Various Pthreads manual pages, for example: <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cond_signal/">pthread_cond_signal</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cond_wait/">pthread_cond_wait</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_detach/">pthread_detach</a></code>(3), <code><a href="/docs/linux/man/3-pthread_equal/">pthread_equal</a></code>(3), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_key_create/">pthread_key_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_unlock/">pthread_mutex_unlock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutexattr_destroy/">pthread_mutexattr_destroy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutexattr_init/">pthread_mutexattr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_once/">pthread_once</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_init/">pthread_spin_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_lock/">pthread_spin_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_rwlockattr_setkind_np/">pthread_rwlockattr_setkind_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcanceltype/">pthread_setcanceltype</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setspecific/">pthread_setspecific</a></code>(3), <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3), <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3), and <code><a href="/docs/linux/man/3-pthread_testcancel/">pthread_testcancel</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
