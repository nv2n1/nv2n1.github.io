---
title: "sem_post(3)"
name: "sem_post"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_post/"
description: "sem_post – unlock a semaphore"
---

<p>sem_post &#8211; unlock a semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_post(sem_t *sem);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_post</code>() increments (unlocks) the semaphore pointed to by <i>sem</i>. If the semaphore&#8217;s value consequently becomes greater than zero, then another process or thread blocked in a <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3) call will be woken up and proceed to lock the semaphore.</p>
<h2>Return Value</h2>
<p><code>sem_post</code>() returns 0 on success; on error, the value of the semaphore is left unchanged, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>sem</i> is not a valid semaphore.</p>
<dt><code>EOVERFLOW</code></p>
<dd>The maximum allowable value for a semaphore would be exceeded.</dl>
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
<td> <code>sem_post</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001.</p>
<h2>Notes</h2>
<p><code>sem_post</code>() is async-signal-safe: it may be safely called within a signal handler.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3) and <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
