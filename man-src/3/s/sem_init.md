---
title: "sem_init(3)"
name: "sem_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_init/"
description: "sem_init – initialize an unnamed semaphore"
---

<p>sem_init &#8211; initialize an unnamed semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_init(sem_t *sem, int pshared, unsigned int value);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_init</code>() initializes the unnamed semaphore at the address pointed to by <i>sem</i>. The <i>value</i> argument specifies the initial value for the semaphore. </p>
<p> The <i>pshared</i> argument indicates whether this semaphore is to be shared between the threads of a process, or between processes. </p>
<p> If <i>pshared</i> has the value 0, then the semaphore is shared between the threads of a process, and should be located at some address that is visible to all threads (e.g., a global variable, or a variable allocated dynamically on the heap). </p>
<p> If <i>pshared</i> is nonzero, then the semaphore is shared between processes, and should be located in a region of shared memory (see <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), and <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)). (Since a child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s memory mappings, it can also access the semaphore.) Any process that can access the shared memory region can operate on the semaphore using <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), and so on. </p>
<p> Initializing a semaphore that has already been initialized results in undefined behavior.</p>
<h2>Return Value</h2>
<p><code>sem_init</code>() returns 0 on success; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>value</i> exceeds <code>SEM_VALUE_MAX</code>.</p>
<dt><code>ENOSYS</code></p>
<dd><i>pshared</i> is nonzero, but the system does not support process-shared semaphores (see <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)).</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sem_init</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001.</p>
<h2>Notes</h2>
<p>Bizarrely, POSIX.1-2001 does not specify the value that should be returned by a successful call to <code>sem_init</code>(). POSIX.1-2008 rectifies this, specifying the zero return on success.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3) and <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_destroy/">sem_destroy</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
