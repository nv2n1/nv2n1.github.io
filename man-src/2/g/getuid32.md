---
title: "getuid32(2)"
name: "getuid32"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getuid32/"
description: "getuid, geteuid – get user identity"
---

<h2 class="name">NAME</h2>
<p> getuid, geteuid &#8211; get user identity </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/types.h&gt;</code> </p>
<p> <code>uid_t getuid(void);</code><br />
 <code>uid_t geteuid(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getuid</code>() returns the real user ID of the calling process. </p>
<p> <code>geteuid</code>() returns the effective user ID of the calling process.</p>
<h2>ERRORS</h2>
<p> These functions are always successful.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>NOTES</h2>
<h3>History</h3>
<p> In UNIX V6 the <code>getuid</code>() call returned <i>(euid &lt;&lt; 8) + uid</i>. UNIX V7 introduced separate calls <code>getuid</code>() and <code>geteuid</code>(). </p>
<p> The original Linux <code>getuid</code>() and <code>geteuid</code>() system calls supported only 16-bit user IDs. Subsequently, Linux 2.4 added <code>getuid32</code>() and <code>geteuid32</code>(), supporting 32-bit IDs. The glibc <code>getuid</code>() and <code>geteuid</code>() wrapper functions transparently deal with the variations across kernel versions. </p>
<p> On Alpha, instead of a pair of <code>getuid</code>() and <code>geteuid</code>() system calls, a single <code>getxuid</code>() system call is provided, which returns a pair of real and effective UIDs. The glibc <code>getuid</code>() and <code>geteuid</code>() wrapper functions transparently deal with this. See <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for details regarding register mapping.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getresuid/">getresuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
