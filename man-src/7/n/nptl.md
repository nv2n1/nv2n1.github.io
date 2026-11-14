---
title: "nptl(7)"
name: "nptl"
section: "7"
letter: "n"
url: "/docs/linux/man/7-nptl/"
description: "nptl – Native POSIX Threads Library"
---

<p>nptl &#8211; Native POSIX Threads Library</p>
<h2>Description</h2>
<p>NPTL (Native POSIX Threads Library) is the GNU C library POSIX threads implementation that is used on modern Linux systems.</p>
<h3>NPTL and signals</h3>
<p>NPTL makes internal use of the first two real-time signals (signal numbers 32 and 33). One of these signals is used to support thread cancellation and POSIX timers (see <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2)); the other is used as part of a mechanism that ensures all threads in a process always have the same UIDs and GIDs, as required by POSIX. These signals cannot be used in applications. </p>
<p> To prevent accidental use of these signals in applications, which might interfere with the operation of the NPTL implementation, various glibc library functions and system call wrapper functions attempt to hide these signals from applications, as follows:</p>
<dl>
<dt>*</p>
<dd><code>SIGRTMIN</code> is defined with the value 34 (rather than 32).</p>
<dt>*</p>
<dd>The <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2), and <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3) interfaces silently ignore requests to wait for these two signals if they are specified in the signal set argument of these calls.</p>
<dt>*</p>
<dd>The <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) and <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3) interfaces silently ignore attempts to block these two signals.</p>
<dt>*</p>
<dd>The <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3), and <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3) interfaces fail with the error <code>EINVAL</code> (indicating an invalid signal number) if these signals are specified.</p>
<dt>*</p>
<dd><code><a href="/docs/linux/man/3-sigfillset/">sigfillset</a></code>(3) does not include these two signals when it creates a full signal set.</dl>
<h3>NPTL and process credential changes</h3>
<p>At the Linux kernel level, credentials (user and group IDs) are a per-thread attribute. However, POSIX requires that all of the POSIX threads in a process have the same credentials. To accommodate this requirement, the NPTL implementation wraps all of the system calls that change process credentials with functions that, in addition to invoking the underlying system call, arrange for all other threads in the process to also change their credentials. </p>
<p> The implementation of each of these system calls involves the use of a real-time signal that is sent (using <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2)) to each of the other threads that must change its credentials. Before sending these signals, the thread that is changing credentials saves the new credential(s) and records the system call being employed in a global buffer. A signal handler in the receiving thread(s) fetches this information and then uses the same system call to change its credentials. </p>
<p> Wrapper functions employing this technique are provided for <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setegid/">setegid</a></code>(2), <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2), <code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setresgid/">setresgid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), and <code><a href="/docs/linux/man/2-setgroups/">setgroups</a></code>(2).</p>
<h2>Conforming To</h2>
<p>For details of the conformance of NPTL to the POSIX standard, see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7).</p>
<h2>Notes</h2>
<p>POSIX says that any thread in any process with access to the memory containing a process-shared (<code>PTHREAD_PROCESS_SHARED</code>) mutex can operate on that mutex. However, on 64-bit x86 systems, the mutex definition for x86-64 is incompatible with the mutex definition for i386, meaning that 32-bit and 64-bit binaries can&#8217;t share mutexes on x86-64 systems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
