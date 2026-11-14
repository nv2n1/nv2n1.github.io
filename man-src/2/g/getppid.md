---
title: "getppid(2)"
name: "getppid"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getppid/"
description: "getpid, getppid – get process identification"
---

<h2 class="name">NAME</h2>
<p> getpid, getppid &#8211; get process identification </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>pid_t getpid(void);</code><br />
 <code>pid_t getppid(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getpid</code>() returns the process ID (PID) of the calling process. (This is often used by routines that generate unique temporary filenames.) </p>
<p> <code>getppid</code>() returns the process ID of the parent of the calling process. This will be either the ID of the process that created this process using <code>fork</code>(), or, if that process has already terminated, the ID of the process to which this process has been reparented (either <code><a href="/docs/linux/man/1-init/">init</a></code>(1) or a &quot;subreaper&quot; process defined via the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_CHILD_SUBREAPER</code> operation).</p>
<h2>ERRORS</h2>
<p> These functions are always successful.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD, SVr4.</p>
<h2>NOTES</h2>
<p> If the caller&#8217;s parent is in a different PID namespace (see <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)), <code>getppid</code>() returns 0. </p>
<p> From a kernel perspective, the PID (which is shared by all of the threads in a multithreaded process) is sometimes also known as the thread group ID (TGID). This contrasts with the kernel thread ID (TID), which is unique for each thread. For further details, see <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) and the discussion of the <code>CLONE_THREAD</code> flag in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<h3>C library/kernel differences</h3>
<p> From glibc version 2.3.4 up to and including version 2.24, the glibc wrapper function for <code>getpid</code>() cached PIDs, with the goal of avoiding additional system calls when a process calls <code>getpid</code>() repeatedly. Normally this caching was invisible, but its correct operation relied on support in the wrapper functions for <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2): if an application bypassed the glibc wrappers for these system calls by using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then a call to <code>getpid</code>() in the child would return the wrong value (to be precise: it would return the PID of the parent process). In addition, there were cases where <code>getpid</code>() could return the wrong value even when invoking <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) via the glibc wrapper function. (For a discussion of one such case, see BUGS in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).) Furthermore, the complexity of the caching code had been the source of a few bugs within glibc over the years. </p>
<p> Because of the aforementioned problems, since glibc version 2.25, the PID cache is removed: calls to <code>getpid</code>() always invoke the actual system call, rather than returning a cached value. </p>
<p> On Alpha, instead of a pair of <code>getpid</code>() and <code>getppid</code>() system calls, a single <code>getxpid</code>() system call is provided, which returns a pair of PID and parent PID. The glibc <code>getpid</code>() and <code>getppid</code>() wrapper functions transparently deal with this. See <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for details regarding register mapping.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
