---
title: "sem_open(3)"
name: "sem_open"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_open/"
description: "sem_open – initialize and open a named semaphore"
---

<p>sem_open &#8211; initialize and open a named semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;fcntl.h&gt; /* For O_* constants */
#include &lt;semaphore.h&gt;
#include &lt;sys/stat.h&gt; /* For mode constants */

sem_t *sem_open(const char *name, int oflag);
sem_t *sem_open(const char *name, int oflag,
                mode_t mode, unsigned int value);</code></pre>
<p> Link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>sem_open</code>() creates a new POSIX semaphore or opens an existing semaphore. The semaphore is identified by <i>name</i>. For details of the construction of <i>name</i>, see <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7). </p>
<p> The <i>oflag</i> argument specifies flags that control the operation of the call. (Definitions of the flags values can be obtained by including <i>&lt;fcntl.h&gt;</i>.) If <code>O_CREAT</code> is specified in <i>oflag</i>, then the semaphore is created if it does not already exist. The owner (user ID) of the semaphore is set to the effective user ID of the calling process. The group ownership (group ID) is set to the effective group ID of the calling process. If both <code>O_CREAT</code> and <code>O_EXCL</code> are specified in <i>oflag</i>, then an error is returned if a semaphore with the given <i>name</i> already exists. </p>
<p> If <code>O_CREAT</code> is specified in <i>oflag</i>, then two additional arguments must be supplied. The <i>mode</i> argument specifies the permissions to be placed on the new semaphore, as for <code><a href="/docs/linux/man/2-open/">open</a></code>(2). (Symbolic definitions for the permissions bits can be obtained by including <i>&lt;sys/stat.h&gt;</i>.) The permissions settings are masked against the process umask. Both read and write permission should be granted to each class of user that will access the semaphore. The <i>value</i> argument specifies the initial value for the new semaphore. If <code>O_CREAT</code> is specified, and a semaphore with the given <i>name</i> already exists, then <i>mode</i> and <i>value</i> are ignored.</p>
<h2>Return Value</h2>
<p>On success, <code>sem_open</code>() returns the address of the new semaphore; this address is used when calling other semaphore-related functions. On error, <code>sem_open</code>() returns <code>SEM_FAILED</code>, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>The semaphore exists, but the caller does not have permission to open it.</p>
<dt><code>EEXIST</code></p>
<dd>Both <code>O_CREAT</code> and <code>O_EXCL</code> were specified in <i>oflag</i>, but a semaphore with this <i>name</i> already exists.</p>
<dt><code>EINVAL</code></p>
<dd><i>value</i> was greater than <code>SEM_VALUE_MAX</code>.</p>
<dt><code>EINVAL</code></p>
<dd><i>name</i> consists of just &quot;/&quot;, followed by no other characters.</p>
<dt><code>EMFILE</code></p>
<dd>The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd><i>name</i> was too long.</p>
<dt><code>ENFILE</code></p>
<dd>The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd>The <code>O_CREAT</code> flag was not specified in <i>oflag</i> and no semaphore with this <i>name</i> exists; or, <code>O_CREAT</code> was specified, but <i>name</i> wasn&#8217;t well formed.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory.</dl>
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
<td> <code>sem_open</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sem_close/">sem_close</a></code>(3), <code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/3-sem_unlink/">sem_unlink</a></code>(3), <code><a href="/docs/linux/man/3-sem_wait/">sem_wait</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
