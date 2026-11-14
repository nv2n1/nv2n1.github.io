---
title: "ipcrm(1)"
name: "ipcrm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipcrm/"
description: "ipcrm – remove certain IPC resources"
---

<h2 class="name">NAME</h2>
<p> ipcrm &#8211; remove certain IPC resources </p>
<h2>SYNOPSIS</h2>
<p> <code>ipcrm</code> [options] </p>
<p> <code>ipcrm</code> [<code>shm</code>|<code>msg</code>|<code>sem</code>] <i>ID</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ipcrm</code> removes System V inter-process communication (IPC) objects and associated data structures from the system. In order to delete such objects, you must be superuser, or the creator or owner of the object. </p>
<p> System V IPC objects are of three types: shared memory, message queues, and semaphores. Deletion of a message queue or semaphore object is immediate (regardless of whether any process still holds an IPC identifier for the object). A shared memory object is only removed after all currently attached processes have detached (<code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2)) the object from their virtual address space. </p>
<p> Two syntax styles are supported. The old Linux historical syntax specifies a three-letter keyword indicating which class of object is to be deleted, followed by one or more IPC identifiers for objects of this type. </p>
<p> The SUS-compliant syntax allows the specification of zero or more objects of all three types in a single command line, with objects specified either by key or by identifier (see below). Both keys and identifiers may be specified in decimal, hexadecimal (specified with an initial &#8216;0x&#8217; or &#8216;0X&#8217;), or octal (specified with an initial &#8216;0&#8217;). </p>
<p> The details of the removes are described in <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), and <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2). The identifiers and keys can be found by using <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code> [<code>shm</code>] [<code>msg</code>] [<code>sem</code>]</p>
<dl>
<dt>
<dd> Remove all resources. When an option argument is provided, the removal is performed only for the specified resource types. </p>
<p> <i>Warning!</i> Do not use <code>-a</code> if you are unsure how the software using the resources might react to missing objects. Some programs create these resources at startup and may not have any code to deal with an unexpected disappearance.</dl>
<p> <code>-M</code>, <code>&#8211;shmem-key</code> <i>shmkey</i></p>
<dl>
<dt>
<dd> Remove the shared memory segment created with <i>shmkey</i> after the last detach is performed.</dl>
<p> <code>-m</code>, <code>&#8211;shmem-id</code> <i>shmid</i></p>
<dl>
<dt>
<dd> Remove the shared memory segment identified by <i>shmid</i> after the last detach is performed.</dl>
<p> <code>-Q</code>, <code>&#8211;queue-key</code> <i>msgkey</i></p>
<dl>
<dt>
<dd> Remove the message queue created with <i>msgkey</i>.</dl>
<p> <code>-q</code>, <code>&#8211;queue-id</code> <i>msgid</i></p>
<dl>
<dt>
<dd> Remove the message queue identified by <i>msgid</i>.</dl>
<p> <code>-S</code>, <code>&#8211;semaphore-key</code> <i>semkey</i></p>
<dl>
<dt>
<dd> Remove the semaphore created with <i>semkey</i>.</dl>
<p> <code>-s</code>, <code>&#8211;semaphore-id</code> <i>semid</i></p>
<dl>
<dt>
<dd> Remove the semaphore identified by <i>semid</i>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>NOTES</h2>
<p> In its first Linux implementation, <code>ipcrm</code> used the deprecated syntax shown in the second line of the <code>SYNOPSIS</code>. Functionality present in other *nix implementations of <code>ipcrm</code> has since been added, namely the ability to delete resources by key (not just identifier), and to respect the same command-line syntax. For backward compatibility the previous syntax is still supported.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1), <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>ipcrm</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
