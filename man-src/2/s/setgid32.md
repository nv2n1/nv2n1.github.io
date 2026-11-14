---
title: "setgid32(2)"
name: "setgid32"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setgid32/"
description: "setgid – set group identity"
---

<h2 class="name">NAME</h2>
<p> setgid &#8211; set group identity </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setgid(gid_t </code><i>gid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>setgid</code>() sets the effective group ID of the calling process. If the calling process is privileged (more precisely: has the <code>CAP_SETGID</code> capability in its user namespace), the real GID and saved set-group-ID are also set. </p>
<p> Under Linux, <code>setgid</code>() is implemented like the POSIX version with the <code>_POSIX_SAVED_IDS</code> feature. This allows a set-group-ID program that is not set-user-ID-root to drop all of its group privileges, do some un-privileged work, and then reengage the original effective group ID in a secure manner.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The group ID specified in <i>gid</i> is not valid in this user namespace.</p>
<dt><code>EPERM</code></p>
<dd> The calling process is not privileged (does not have the <code>CAP_SETGID</code> capability in its user namespace), and <i>gid</i> does not match the real group ID or saved set-group-ID of the calling process.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> The original Linux <code>setgid</code>() system call supported only 16-bit group IDs. Subsequently, Linux 2.4 added <code>setgid32</code>() supporting 32-bit IDs. The glibc <code>setgid</code>() wrapper function transparently deals with the variation across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> At the kernel level, user IDs and group IDs are a per-thread attribute. However, POSIX requires that all threads in a process share the same credentials. The NPTL threading implementation handles the POSIX requirements by providing wrapper functions for the various system calls that change process UIDs and GIDs. These wrapper functions (including the one for <code>setgid</code>()) employ a signal-based technique to ensure that when one thread changes credentials, all of the other threads in the process also change their credentials. For details, see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-setegid/">setegid</a></code>(2), <code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
