---
title: "setuid(2)"
name: "setuid"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setuid/"
description: "setuid – set user identity"
---

<h2 class="name">NAME</h2>
<p> setuid &#8211; set user identity </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setuid(uid_t </code><i>uid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>setuid</code>() sets the effective user ID of the calling process. If the calling process is privileged (more precisely: if the process has the <code>CAP_SETUID</code> capability in its user namespace), the real UID and saved set-user-ID are also set. </p>
<p> Under Linux, <code>setuid</code>() is implemented like the POSIX version with the <code>_POSIX_SAVED_IDS</code> feature. This allows a set-user-ID (other than root) program to drop all of its user privileges, do some un-privileged work, and then reengage the original effective user ID in a secure manner. </p>
<p> If the user is root or the program is set-user-ID-root, special care must be taken: <code>setuid</code>() checks the effective user ID of the caller and if it is the superuser, all process-related user ID&#8217;s are set to <i>uid</i>. After this has occurred, it is impossible for the program to regain root privileges. </p>
<p> Thus, a set-user-ID-root program wishing to temporarily drop root privileges, assume the identity of an unprivileged user, and then regain root privileges afterward cannot use <code>setuid</code>(). You can accomplish this with <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> <i>Note</i>: there are cases where <code>setuid</code>() can fail even when the caller is UID 0; it is a grave security error to omit checking for a failure return from <code>setuid</code>().</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The call would change the caller&#8217;s real UID (i.e., <i>uid</i> does not match the caller&#8217;s real UID), but there was a temporary failure allocating the necessary kernel data structures.</p>
<dt><code>EAGAIN</code></p>
<dd> <i>uid</i> does not match the real user ID of the caller and this call would bring the number of processes belonging to the real user ID <i>uid</i> over the caller&#8217;s <code>RLIMIT_NPROC</code> resource limit. Since Linux 3.1, this error case no longer occurs (but robust applications should check for this error); see the description of <code>EAGAIN</code> in <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>EINVAL</code></p>
<dd> The user ID specified in <i>uid</i> is not valid in this user namespace.</p>
<dt><code>EPERM</code></p>
<dd> The user is not privileged (Linux: does not have the <code>CAP_SETUID</code> capability in its user namespace) and <i>uid</i> does not match the real UID or saved set-user-ID of the calling process.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. Not quite compatible with the 4.4BSD call, which sets all of the real, saved, and effective user IDs.</p>
<h2>NOTES</h2>
<p> Linux has the concept of the filesystem user ID, normally equal to the effective user ID. The <code>setuid</code>() call also sets the filesystem user ID of the calling process. See <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2). </p>
<p> If <i>uid</i> is different from the old effective UID, the process will be forbidden from leaving core dumps. </p>
<p> The original Linux <code>setuid</code>() system call supported only 16-bit user IDs. Subsequently, Linux 2.4 added <code>setuid32</code>() supporting 32-bit IDs. The glibc <code>setuid</code>() wrapper function transparently deals with the variation across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> At the kernel level, user IDs and group IDs are a per-thread attribute. However, POSIX requires that all threads in a process share the same credentials. The NPTL threading implementation handles the POSIX requirements by providing wrapper functions for the various system calls that change process UIDs and GIDs. These wrapper functions (including the one for <code>setuid</code>()) employ a signal-based technique to ensure that when one thread changes credentials, all of the other threads in the process also change their credentials. For details, see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
