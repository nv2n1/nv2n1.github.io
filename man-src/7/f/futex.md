---
title: "futex(7)"
name: "futex"
section: "7"
letter: "f"
url: "/docs/linux/man/7-futex/"
description: "futex – fast user-space locking"
---

<p>futex &#8211; fast user-space locking</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/futex.h&gt;</code></pre>
<h2>Description</h2>
<p>The Linux kernel provides futexes (&quot;Fast user-space mutexes&quot;) as a building block for fast user-space locking and semaphores. Futexes are very basic and lend themselves well for building higher-level locking abstractions such as mutexes, condition variables, read-write locks, barriers, and semaphores. </p>
<p> Most programmers will in fact not be using futexes directly but will instead rely on system libraries built on them, such as the Native POSIX Thread Library (NPTL) (see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)). </p>
<p> A futex is identified by a piece of memory which can be shared between processes or threads. In these different processes, the futex need not have identical addresses. In its bare form, a futex has semaphore semantics; it is a counter that can be incremented and decremented atomically; processes can wait for the value to become positive. </p>
<p> Futex operation occurs entirely in user space for the noncontended case. The kernel is involved only to arbitrate the contended case. As any sane design will strive for noncontention, futexes are also optimized for this situation. </p>
<p> In its bare form, a futex is an aligned integer which is touched only by atomic assembler instructions. This integer is four bytes long on all platforms. Processes can share this integer using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), via shared memory segments, or because they share memory space, in which case the application is commonly called multithreaded.</p>
<h3>Semantics</h3>
<p>Any futex operation starts in user space, but it may be necessary to communicate with the kernel using the <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) system call. </p>
<p> To &quot;up&quot; a futex, execute the proper assembler instructions that will cause the host CPU to atomically increment the integer. Afterward, check if it has in fact changed from 0 to 1, in which case there were no waiters and the operation is done. This is the noncontended case which is fast and should be common. </p>
<p> In the contended case, the atomic increment changed the counter from -1 (or some other negative number). If this is detected, there are waiters. User space should now set the counter to 1 and instruct the kernel to wake up any waiters using the <code>FUTEX_WAKE</code> operation. </p>
<p> Waiting on a futex, to &quot;down&quot; it, is the reverse operation. Atomically decrement the counter and check if it changed to 0, in which case the operation is done and the futex was uncontended. In all other circumstances, the process should set the counter to -1 and request that the kernel wait for another process to up the futex. This is done using the <code>FUTEX_WAIT</code> operation. </p>
<p> The <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) system call can optionally be passed a timeout specifying how long the kernel should wait for the futex to be upped. In this case, semantics are more complex and the programmer is referred to <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) for more details. The same holds for asynchronous futex waiting.</p>
<h2>Versions</h2>
<p>Initial futex support was merged in Linux 2.5.7 but with different semantics from those described above. Current semantics are available from Linux 2.5.40 onward.</p>
<h2>Notes</h2>
<p>To reiterate, bare futexes are not intended as an easy-to-use abstraction for end users. Implementors are expected to be assembly literate and to have read the sources of the futex user-space library referenced below. </p>
<p> This man page illustrates the most common use of the <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2) primitives; it is by no means the only one.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-set_robust_list/">set_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-set_tid_address/">set_tid_address</a></code>(2), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7) </p>
<p> <i>Fuss, Futexes and Furwocks: Fast Userlevel Locking in Linux</i> (proceedings of the Ottawa Linux Symposium 2002), futex example library, futex-*.tar.bz2</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
