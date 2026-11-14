---
title: "getgid(2)"
name: "getgid"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getgid/"
description: "getgid, getegid – get group identity"
---

<h2 class="name">NAME</h2>
<p> getgid, getegid &#8211; get group identity </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/types.h&gt;</code> </p>
<p> <code>gid_t getgid(void);</code><br />
 <code>gid_t getegid(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getgid</code>() returns the real group ID of the calling process. </p>
<p> <code>getegid</code>() returns the effective group ID of the calling process.</p>
<h2>ERRORS</h2>
<p> These functions are always successful.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The original Linux <code>getgid</code>() and <code>getegid</code>() system calls supported only 16-bit group IDs. Subsequently, Linux 2.4 added <code>getgid32</code>() and <code>getegid32</code>(), supporting 32-bit IDs. The glibc <code>getgid</code>() and <code>getegid</code>() wrapper functions transparently deal with the variations across kernel versions. </p>
<p> On Alpha, instead of a pair of <code>getgid</code>() and <code>getegid</code>() system calls, a single <code>getxgid</code>() system call is provided, which returns a pair of real and effective GIDs. The glibc <code>getgid</code>() and <code>getegid</code>() wrapper functions transparently deal with this. See <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for details regarding register mapping.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getresgid/">getresgid</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
