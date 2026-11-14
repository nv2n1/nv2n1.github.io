---
title: "flock(2)"
name: "flock"
section: "2"
letter: "f"
url: "/docs/linux/man/2-flock/"
description: "flock – apply or remove an advisory lock on an open file"
---

<h2 class="name">NAME</h2>
<p> flock &#8211; apply or remove an advisory lock on an open file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/file.h&gt;</code> </p>
<p> <code>int flock(int </code><i>fd</i><code>, int </code><i>operation</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> Apply or remove an advisory lock on the open file specified by <i>fd</i>. The argument <i>operation</i> is one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>LOCK_SH</code></p>
<dd> Place a shared lock. More than one process may hold a shared lock for a given file at a given time.</p>
<dt><code>LOCK_EX</code></p>
<dd> Place an exclusive lock. Only one process may hold an exclusive lock for a given file at a given time.</p>
<dt><code>LOCK_UN</code></p>
<dd> Remove an existing lock held by this process.</dl>
</dl>
<p> A call to <code>flock</code>() may block if an incompatible lock is held by another process. To make a nonblocking request, include <code>LOCK_NB</code> (by ORing) with any of the above operations. </p>
<p> A single file may not simultaneously have both shared and exclusive locks. </p>
<p> Locks created by <code>flock</code>() are associated with an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). This means that duplicate file descriptors (created by, for example, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2)) refer to the same lock, and this lock may be modified or released using any of these file descriptors. Furthermore, the lock is released either by an explicit <code>LOCK_UN</code> operation on any of these duplicate file descriptors, or when all such file descriptors have been closed. </p>
<p> If a process uses <code><a href="/docs/linux/man/2-open/">open</a></code>(2) (or similar) to obtain more than one file descriptor for the same file, these file descriptors are treated independently by <code>flock</code>(). An attempt to lock the file using one of these file descriptors may be denied by a lock that the calling process has already placed via another file descriptor. </p>
<p> A process may hold only one type of lock (shared or exclusive) on a file. Subsequent <code>flock</code>() calls on an already locked file will convert an existing lock to the new lock mode. </p>
<p> Locks created by <code>flock</code>() are preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> A shared or exclusive lock can be placed on a file regardless of the mode in which the file was opened.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not an open file descriptor.</p>
<dt><code>EINTR</code></p>
<dd> While waiting to acquire a lock, the call was interrupted by delivery of a signal caught by a handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> is invalid.</p>
<dt><code>ENOLCK</code></p>
<dd> The kernel ran out of memory for allocating lock records.</p>
<dt><code>EWOULDBLOCK</code></p>
<dd> The file is locked and the <code>LOCK_NB</code> flag was selected.</dl>
<h2>CONFORMING TO</h2>
<p> 4.4BSD (the <code>flock</code>() call first appeared in 4.2BSD). A version of <code>flock</code>(), possibly implemented in terms of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), appears on most UNIX systems.</p>
<h2>NOTES</h2>
<p> Since kernel 2.0, <code>flock</code>() is implemented as a system call in its own right rather than being emulated in the GNU C library as a call to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). With this implementation, there is no interaction between the types of lock placed by <code>flock</code>() and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), and <code>flock</code>() does not detect deadlock. (Note, however, that on some systems, such as the modern BSDs, <code>flock</code>() and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locks <i>do</i> interact with one another.) </p>
<p> <code>flock</code>() places advisory locks only; given suitable permissions on a file, a process is free to ignore the use of <code>flock</code>() and perform I/O on the file. </p>
<p> <code>flock</code>() and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locks have different semantics with respect to forked processes and <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2). On systems that implement <code>flock</code>() using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), the semantics of <code>flock</code>() will be different from those described in this manual page. </p>
<p> Converting a lock (shared to exclusive, or vice versa) is not guaranteed to be atomic: the existing lock is first removed, and then a new lock is established. Between these two steps, a pending lock request by another process may be granted, with the result that the conversion either blocks, or fails if <code>LOCK_NB</code> was specified. (This is the original BSD behavior, and occurs on many other implementations.)</p>
<h3>NFS details</h3>
<p> In Linux kernels up to 2.6.11, <code>flock</code>() does not lock files over NFS (i.e., the scope of locks was limited to the local system). Instead, one could use <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) byte-range locking, which does work over NFS, given a sufficiently recent version of Linux and a server which supports locking. </p>
<p> Since Linux 2.6.12, NFS clients support <code>flock</code>() locks by emulating them as <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) byte-range locks on the entire file. This means that <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and <code>flock</code>() locks <i>do</i> interact with one another over NFS. It also means that in order to place an exclusive lock, the file must be opened for writing. </p>
<p> Since Linux 2.6.37, the kernel supports a compatibility mode that allows <code>flock</code>() locks (and also <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) byte region locks) to be treated as local; see the discussion of the <i>local_lock</i> option in <code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flock/">flock</a></code>(1), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3), <code><a href="/docs/linux/man/8-lslocks/">lslocks</a></code>(8) </p>
<p> <i>Documentation/filesystems/locks.txt</i> in the Linux kernel source tree (<i>Documentation/locks.txt</i> in older kernels)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
