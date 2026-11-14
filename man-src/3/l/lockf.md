---
title: "lockf(3)"
name: "lockf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lockf/"
description: "lockf – apply, test or remove a POSIX lock on an open file"
---

<h2 class="name">NAME</h2>
<p> lockf &#8211; apply, test or remove a POSIX lock on an open file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int lockf(int </code><i>fd</i><code>, int </code><i>cmd</i><code>, off_t </code><i>len</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>lockf</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> Apply, test or remove a POSIX lock on a section of an open file. The file is specified by <i>fd</i>, a file descriptor open for writing, the action by <i>cmd</i>, and the section consists of byte positions <i>pos</i>..<i>pos</i>+<i>len</i>-1 if <i>len</i> is positive, and <i>pos</i>&#8211;<i>len</i>..<i>pos</i>-1 if <i>len</i> is negative, where <i>pos</i> is the current file position, and if <i>len</i> is zero, the section extends from the current file position to infinity, encompassing the present and future end-of-file positions. In all cases, the section may extend past current end-of-file. </p>
<p> On Linux, <code>lockf</code>() is just an interface on top of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locking. Many other systems implement <code>lockf</code>() in this way, but note that POSIX.1 leaves the relationship between <code>lockf</code>() and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) locks unspecified. A portable application should probably avoid mixing calls to these interfaces. </p>
<p> Valid operations are given below:</p>
<dl>
<dt><code>F_LOCK</code></p>
<dd> Set an exclusive lock on the specified section of the file. If (part of) this section is already locked, the call blocks until the previous lock is released. If this section overlaps an earlier locked section, both are merged. File locks are released as soon as the process holding the locks closes some file descriptor for the file. A child process does not inherit these locks.</p>
<dt><code>F_TLOCK</code></p>
<dd> Same as <code>F_LOCK</code> but the call never blocks and returns an error instead if the file is already locked.</p>
<dt><code>F_ULOCK</code></p>
<dd> Unlock the indicated section of the file. This may cause a locked section to be split into two locked sections.</p>
<dt><code>F_TEST</code></p>
<dd> Test the lock: return 0 if the specified section is unlocked or locked by this process; return -1, set <i>errno</i> to <code>EAGAIN</code> (<code>EACCES</code> on some other systems), if another process holds a lock.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code> or <code>EAGAIN</code></p>
<dd> The file is locked and <code>F_TLOCK</code> or <code>F_TEST</code> was specified, or the operation is prohibited because the file has been memory-mapped by another process.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not an open file descriptor; or <i>cmd</i> is <code>F_LOCK</code> or <code>F_TLOCK</code> and <i>fd</i> is not a writable file descriptor.</p>
<dt><code>EDEADLK</code></p>
<dd> The command was <code>F_LOCK</code> and this lock operation would cause a deadlock.</p>
<dt><code>EINTR</code></p>
<dd> While waiting to acquire a lock, the call was interrupted by delivery of a signal caught by a handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> An invalid operation was specified in <i>cmd</i>.</p>
<dt><code>ENOLCK</code></p>
<dd> Too many segment locks open, lock table is full.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>lockf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2) </p>
<p> <i>locks.txt</i> and <i>mandatory-locking.txt</i> in the Linux kernel source directory <i>Documentation/filesystems</i> (on older kernels, these files are directly under the <i>Documentation</i> directory, and <i>mandatory-locking.txt</i> is called <i>mandatory.txt</i>)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
