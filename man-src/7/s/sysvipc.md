---
title: "sysvipc(7)"
name: "sysvipc"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sysvipc/"
description: "sysvipc – System V interprocess communication mechanisms"
---

<p>sysvipc &#8211; System V interprocess communication mechanisms</p>
<h2>Description</h2>
<p>System V IPC is the name given to three interprocess communication mechanisms that are widely available on UNIX systems: message queues, semaphore, and shared memory.</p>
<h3>Message queues</h3>
<p>System V message queues allow data to be exchanged in units called messages. Each messages can have an associated priority, POSIX message queues provide an alternative API for achieving the same result; see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7). </p>
<p> The System V message queue API consists of the following system calls:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2)</p>
<dd>Create a new message queue or obtain the ID of an existing message queue. This call returns an identifier that is used in the remaining APIs.</p>
<dt><code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2)</p>
<dd>Add a message to a queue.</p>
<dt><code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2)</p>
<dd>Remove a message from a queue.</p>
<dt><code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2)</p>
<dd>Perform various control operations on a queue, including deletion.</dl>
<h3>Semaphore sets</h3>
<p>System V semaphores allow processes to synchronize their actions System V semaphores are allocated in groups called sets; each semaphore in a set is a counting semaphore. POSIX semaphores provide an alternative API for achieving the same result; see <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7). </p>
<p> The System V semaphore API consists of the following system calls:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-semget/">semget</a></code>(2)</p>
<dd>Create a new set or obtain the ID of an existing set. This call returns an identifier that is used in the remaining APIs.</p>
<dt><code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)</p>
<dd>Perform operations on the semaphores in a set.</p>
<dt><code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2)</p>
<dd>Perform various control operations on a set, including deletion.</dl>
<h3>Shared memory segments</h3>
<p>System V shared memory allows processes to share a region a memory (a &quot;segment&quot;). POSIX shared memory is an alternative API for achieving the same result; see <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7). </p>
<p> The System V shared memory API consists of the following system calls:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)</p>
<dd>Create a new segment or obtain the ID of an existing segment. This call returns an identifier that is used in the remaining APIs.</p>
<dt><code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2)</p>
<dd>Attach an existing shared memory object into the calling process&#8217;s address space.</p>
<dt><code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2)</p>
<dd>Detach a segment from the calling process&#8217;s address space.</p>
<dt><code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2)</p>
<dd>Perform various control operations on a segment, including deletion.</dl>
<h3>IPC namespaces</h3>
<p>For a discussion of the interaction of System V IPC objects and IPC namespaces, see <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1), <code><a href="/docs/linux/man/1-lsipc/">lsipc</a></code>(1), <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2), <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
