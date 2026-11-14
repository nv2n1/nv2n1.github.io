---
title: "getresgid(2)"
name: "getresgid"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getresgid/"
description: "getresuid, getresgid – get real, effective and saved user/group IDs"
---

<h2 class="name">NAME</h2>
<p> getresuid, getresgid &#8211; get real, effective and saved user/group IDs </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getresuid(uid_t *</code><i>ruid</i><code>, uid_t *</code><i>euid</i><code>, uid_t *</code><i>suid</i><code>);</code><br />
 <code>int getresgid(gid_t *</code><i>rgid</i><code>, gid_t *</code><i>egid</i><code>, gid_t *</code><i>sgid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getresuid</code>() returns the real UID, the effective UID, and the saved set-user-ID of the calling process, in the arguments <i>ruid</i>, <i>euid</i>, and <i>suid</i>, respectively. <code>getresgid</code>() performs the analogous task for the process&#8217;s group IDs.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> One of the arguments specified an address outside the calling program&#8217;s address space.</dl>
<h2>VERSIONS</h2>
<p> These system calls appeared on Linux starting with kernel 2.1.44. </p>
<p> The prototypes are given by glibc since version 2.3.2, provided <code>_GNU_SOURCE</code> is defined.</p>
<h2>CONFORMING TO</h2>
<p> These calls are nonstandard; they also appear on HP-UX and some of the BSDs.</p>
<h2>NOTES</h2>
<p> The original Linux <code>getresuid</code>() and <code>getresgid</code>() system calls supported only 16-bit user and group IDs. Subsequently, Linux 2.4 added <code>getresuid32</code>() and <code>getresgid32</code>(), supporting 32-bit IDs. The glibc <code>getresuid</code>() and <code>getresgid</code>() wrapper functions transparently deal with the variations across kernel versions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
