---
title: "sem_overview(7)"
name: "sem_overview"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sem_overview/"
description: "sem_overview – overview of POSIX semaphores"
---

<p>sem_overview &#8211; overview of POSIX semaphores</p>
<h2>Description</h2>
<p>POSIX semaphores allow processes and threads to synchronize their actions. </p>
<p> A semaphore is an integer whose value is never allowed to fall below zero. Two operations can be performed on semaphores: increment the semaphore value by one (<code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3)); and decrement the semaphore value by one (<code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3)). If the value of a semaphore is currently zero, then a <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3) operation will block until the value becomes greater than zero. </p>
<p> POSIX semaphores come in two forms: named semaphores and unnamed semaphores.</p>
<dl>
<dt><code>Named semaphores</code></p>
<dd>A named semaphore is identified by a name of the form <i>/somename</i>; that is, a null-terminated string of up to <code>NAME_MAX</code><i>-4</i> (i.e., 251) characters consisting of an initial slash, followed by one or more characters, none of which are slashes. Two processes can operate on the same named semaphore by passing the same name to <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3).</p>
<dd>The <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3) function creates a new named semaphore or opens an existing named semaphore. After the semaphore has been opened, it can be operated on using <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3) and <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3). When a process has finished using the semaphore, it can use <code><a href="/docs/linux/man/3-sem_close/">sem_close</a></code>(3) to close the semaphore. When all processes have finished using the semaphore, it can be removed from the system using <code><a href="/docs/linux/man/3-sem_unlink/">sem_unlink</a></code>(3).</p>
<dt><code>Unnamed semaphores (memory-based semaphores)</code></p>
<dd>An unnamed semaphore does not have a name. Instead the semaphore is placed in a region of memory that is shared between multiple threads (a <i>thread-shared semaphore</i>) or processes (a <i>process-shared semaphore</i>). A thread-shared semaphore is placed in an area of memory shared between the threads of a process, for example, a global variable. A process-shared semaphore must be placed in a shared memory region (e.g., a System V shared memory segment created using <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), or a POSIX shared memory object built created using <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)).</p>
<dd>Before being used, an unnamed semaphore must be initialized using <code><a href="/docs/linux/man/3-sem_init/">sem_init</a></code>(3). It can then be operated on using <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3) and <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3). When the semaphore is no longer required, and before the memory in which it is located is deallocated, the semaphore should be destroyed using <code><a href="/docs/linux/man/3-sem_destroy/">sem_destroy</a></code>(3).</dl>
<p> The remainder of this section describes some specific details of the Linux implementation of POSIX semaphores.</p>
<h3>Versions</h3>
<p>Prior to kernel 2.6, Linux supported only unnamed, thread-shared semaphores. On a system with Linux 2.6 and a glibc that provides the NPTL threading implementation, a complete implementation of POSIX semaphores is provided.</p>
<h3>Persistence</h3>
<p>POSIX named semaphores have kernel persistence: if not removed by <code><a href="/docs/linux/man/3-sem_unlink/">sem_unlink</a></code>(3), a semaphore will exist until the system is shut down.</p>
<h3>Linking</h3>
<p>Programs using the POSIX semaphores API must be compiled with <i>cc -pthread</i> to link against the real-time library, <i>librt</i>.</p>
<h3>Accessing named semaphores via the filesystem</h3>
<p>On Linux, named semaphores are created in a virtual filesystem, normally mounted under <i>/dev/shm</i>, with names of the form <i></i><code>sem.</code>somename. (This is the reason that semaphore names are limited to <code>NAME_MAX</code><i>-4</i> rather than <code>NAME_MAX</code> characters.) </p>
<p> Since Linux 2.6.19, ACLs can be placed on files under this directory, to control object permissions on a per-user and per-group basis.</p>
<h2>Notes</h2>
<p>System V semaphores (<code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), etc.) are an older semaphore API. POSIX semaphores provide a simpler, and better designed interface than System V semaphores; on the other hand POSIX semaphores are less widely available (especially on older systems) than System V semaphores.</p>
<h2>Examples</h2>
<p>An example of the use of various POSIX semaphore functions is shown in <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_close/">sem_close</a></code>(3), <code><a href="/docs/linux/man/3-sem_destroy/">sem_destroy</a></code>(3), <code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_init/">sem_init</a></code>(3), <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_unlink/">sem_unlink</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
