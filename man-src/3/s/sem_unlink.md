---
title: "sem_unlink(3)"
name: "sem_unlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_unlink/"
description: "sem_unlink – remove a named semaphore"
---

<p>sem_unlink &#8211; remove a named semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_unlink(const char *name);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_unlink</code>() removes the named semaphore referred to by <i>name</i>. The semaphore name is removed immediately. The semaphore is destroyed once all other processes that have the semaphore open close it.</p>
<h2>Return Value</h2>
<p>On success <code>sem_unlink</code>() returns 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>The caller does not have permission to unlink this semaphore.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd><i>name</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd>There is no semaphore with the given <i>name</i>.</dl>
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
<td> <code>sem_unlink</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_open/">sem_open</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
