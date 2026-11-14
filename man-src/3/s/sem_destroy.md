---
title: "sem_destroy(3)"
name: "sem_destroy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_destroy/"
description: "sem_destroy – destroy an unnamed semaphore"
---

<p>sem_destroy &#8211; destroy an unnamed semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_destroy(sem_t *sem);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_destroy</code>() destroys the unnamed semaphore at the address pointed to by <i>sem</i>. </p>
<p> Only a semaphore that has been initialized by <code><a href="/docs/linux/man/3-sem_init/">sem_init</a></code>(3) should be destroyed using <code>sem_destroy</code>(). </p>
<p> Destroying a semaphore that other processes or threads are currently blocked on (in <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3)) produces undefined behavior. </p>
<p> Using a semaphore that has been destroyed produces undefined results, until the semaphore has been reinitialized using <code><a href="/docs/linux/man/3-sem_init/">sem_init</a></code>(3).</p>
<h2>Return Value</h2>
<p><code>sem_destroy</code>() returns 0 on success; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>sem</i> is not a valid semaphore.</dl>
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
<td> <code>sem_destroy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>An unnamed semaphore should be destroyed with <code>sem_destroy</code>() before the memory in which it is located is deallocated. Failure to do this can result in resource leaks on some implementations.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_init/">sem_init</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
