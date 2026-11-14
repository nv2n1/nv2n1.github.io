---
title: "sem_close(3)"
name: "sem_close"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_close/"
description: "sem_close – close a named semaphore"
---

<p>sem_close &#8211; close a named semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_close(sem_t *sem);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_close</code>() closes the named semaphore referred to by <i>sem</i>, allowing any resources that the system has allocated to the calling process for this semaphore to be freed.</p>
<h2>Return Value</h2>
<p>On success <code>sem_close</code>() returns 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
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
<td> <code>sem_close</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>All open named semaphores are automatically closed on process termination, or upon <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_unlink/">sem_unlink</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
