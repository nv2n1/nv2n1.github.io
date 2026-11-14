---
title: "dup(2)"
name: "dup"
section: "2"
letter: "d"
url: "/docs/linux/man/2-dup/"
description: "dup, dup2, dup3 – duplicate a file descriptor"
---

<h2 class="name">NAME</h2>
<p> dup, dup2, dup3 &#8211; duplicate a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int dup(int oldfd);
int dup2(int oldfd, int newfd);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;  /* Obtain O_* constant definitions */
#include &lt;unistd.h&gt;
int dup3(int oldfd, int newfd, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dup</code>() system call creates a copy of the file descriptor <i>oldfd</i>, using the lowest-numbered unused file descriptor for the new descriptor. </p>
<p> After a successful return, the old and new file descriptors may be used interchangeably. They refer to the same open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) and thus share file offset and file status flags; for example, if the file offset is modified by using <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) on one of the file descriptors, the offset is also changed for the other. </p>
<p> The two file descriptors do not share file descriptor flags (the close-on-exec flag). The close-on-exec flag (<code>FD_CLOEXEC</code>; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) for the duplicate descriptor is off.</p>
<h3>dup2()</h3>
<p> The <code>dup2</code>() system call performs the same task as <code>dup</code>(), but instead of using the lowest-numbered unused file descriptor, it uses the file descriptor number specified in <i>newfd</i>. If the file descriptor <i>newfd</i> was previously open, it is silently closed before being reused. </p>
<p> The steps of closing and reusing the file descriptor <i>newfd</i> are performed <i>atomically</i>. This is important, because trying to implement equivalent functionality using <code><a href="/docs/linux/man/2-close/">close</a></code>(2) and <code>dup</code>() would be subject to race conditions, whereby <i>newfd</i> might be reused between the two steps. Such reuse could happen because the main program is interrupted by a signal handler that allocates a file descriptor, or because a parallel thread allocates a file descriptor. </p>
<p> Note the following points:</p>
<dl>
<dt>*</p>
<dd> If <i>oldfd</i> is not a valid file descriptor, then the call fails, and <i>newfd</i> is not closed.</p>
<dt>*</p>
<dd> If <i>oldfd</i> is a valid file descriptor, and <i>newfd</i> has the same value as <i>oldfd</i>, then <code>dup2</code>() does nothing, and returns <i>newfd</i>.</dl>
<h3>dup3()</h3>
<p> <code>dup3</code>() is the same as <code>dup2</code>(), except that:</p>
<dl>
<dt>*</p>
<dd> The caller can force the close-on-exec flag to be set for the new file descriptor by specifying <code>O_CLOEXEC</code> in <i>flags</i>. See the description of the same flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</p>
<dt>*</p>
<dd> If <i>oldfd</i> equals <i>newfd</i>, then <code>dup3</code>() fails with the error <code>EINVAL</code>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return the new file descriptor. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>oldfd</i> isn&#8217;t an open file descriptor.</p>
<dt><code>EBADF</code></p>
<dd> <i>newfd</i> is out of the allowed range for file descriptors (see the discussion of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>EBUSY</code></p>
<dd> (Linux only) This may be returned by <code>dup2</code>() or <code>dup3</code>() during a race condition with <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code>dup</code>().</p>
<dt><code>EINTR</code></p>
<dd> The <code>dup2</code>() or <code>dup3</code>() call was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> (<code>dup3</code>()) <i>flags</i> contain an invalid value.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>dup3</code>()) <i>oldfd</i> was equal to <i>newfd</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached (see the discussion of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</dl>
<h2>VERSIONS</h2>
<p> <code>dup3</code>() was added to Linux in version 2.6.27; glibc support is available starting with version 2.9.</p>
<h2>CONFORMING TO</h2>
<p> <code>dup</code>(), <code>dup2</code>(): POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. </p>
<p> <code>dup3</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The error returned by <code>dup2</code>() is different from that returned by <code>fcntl(</code>&#8230;, <code>F_DUPFD</code>, &#8230;<code>)</code> when <i>newfd</i> is out of range. On some systems, <code>dup2</code>() also sometimes returns <code>EINVAL</code> like <code>F_DUPFD</code>. </p>
<p> If <i>newfd</i> was open, any errors that would have been reported at <code><a href="/docs/linux/man/2-close/">close</a></code>(2) time are lost. If this is of concern, then&#8212;unless the program is single-threaded and does not allocate file descriptors in signal handlers&#8212;the correct approach is <i>not</i> to close <i>newfd</i> before calling <code>dup2</code>(), because of the race condition described above. Instead, code something like the following could be used: </p>
<p> /* Obtain a duplicate of &#8216;newfd&#8217; that can subsequently<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;be used to check for close()&nbsp;errors;&nbsp;an EBADF error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;means that&nbsp;&#8216;newfd&#8217;&nbsp;was not open.&nbsp;*/ </p>
<p> tmpfd = dup(newfd); if (tmpfd == -1 &amp;&amp; errno != EBADF) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle unexpected dup()&nbsp;error&nbsp;*/ } </p>
<p> /* Atomically duplicate &#8216;oldfd&#8217; on &#8216;newfd&#8217; */ </p>
<p> if (dup2(oldfd, newfd) == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle dup2()&nbsp;error&nbsp;*/ } </p>
<p> /* Now check for close() errors on the file originally<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;referred to by&nbsp;&#8216;newfd&#8217;&nbsp;*/ </p>
<p> if (tmpfd != -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(close(tmpfd)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Handle errors from close&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_getfd/">pidfd_getfd</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dt><a href="#lbAG">RETURN VALUE</a></p>
<dd>
<dt><a href="#lbAH">ERRORS</a></p>
<dd>
<dt><a href="#lbAI">VERSIONS</a></p>
<dd>
<dt><a href="#lbAJ">CONFORMING TO</a></p>
<dd>
<dt><a href="#lbAK">NOTES</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">COLOPHON</a></p>
<dd></dl>
