---
title: "sem_getvalue(3)"
name: "sem_getvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_getvalue/"
description: "sem_getvalue – get the value of a semaphore"
---

<p>sem_getvalue &#8211; get the value of a semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_getvalue(sem_t *sem, int *sval);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_getvalue</code>() places the current value of the semaphore pointed to <i>sem</i> into the integer pointed to by <i>sval</i>. </p>
<p> If one or more processes or threads are blocked waiting to lock the semaphore with <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), POSIX.1 permits two possibilities for the value returned in <i>sval</i>: either 0 is returned; or a negative number whose absolute value is the count of the number of processes and threads currently blocked in <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3). Linux adopts the former behavior.</p>
<h2>Return Value</h2>
<p><code>sem_getvalue</code>() returns 0 on success; on error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>sem</i> is not a valid semaphore. (The glibc implementation currently does not check whether <i>sem</i> is valid.)</dl>
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
<td> <code>sem_getvalue</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The value of the semaphore may already have changed by the time <code>sem_getvalue</code>() returns.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
