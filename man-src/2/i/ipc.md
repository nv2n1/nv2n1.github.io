---
title: "ipc(2)"
name: "ipc"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ipc/"
description: "ipc – System V IPC system calls"
---

<h2 class="name">NAME</h2>
<p> ipc &#8211; System V IPC system calls </p>
<h2>SYNOPSIS</h2>
<pre><code>
int ipc(unsigned int call, int first, int second, int third,
        void *ptr, long fifth);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ipc</code>() is a common kernel entry point for the System V IPC calls for messages, semaphores, and shared memory. <i>call</i> determines which IPC function to invoke; the other arguments are passed through to the appropriate call. </p>
<p> User-space programs should call the appropriate functions by their usual names. Only standard library implementors and kernel hackers need to know about <code>ipc</code>().</p>
<h2>CONFORMING TO</h2>
<p> <code>ipc</code>() is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> On some architectures&#8212;for example x86-64 and ARM&#8212;there is no <code>ipc</code>() system call; instead, <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), and so on really are implemented as separate system calls.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-semtimedop/">semtimedop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
