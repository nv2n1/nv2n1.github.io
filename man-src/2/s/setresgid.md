---
title: "setresgid(2)"
name: "setresgid"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setresgid/"
description: "setresuid, setresgid – set real, effective and saved user or group ID"
---

<h2 class="name">NAME</h2>
<p> setresuid, setresgid &#8211; set real, effective and saved user or group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setresuid(uid_t </code><i>ruid</i><code>, uid_t </code><i>euid</i><code>, uid_t </code><i>suid</i><code>);</code><br />
 <code>int setresgid(gid_t </code><i>rgid</i><code>, gid_t </code><i>egid</i><code>, gid_t </code><i>sgid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>setresuid</code>() sets the real user ID, the effective user ID, and the saved set-user-ID of the calling process. </p>
<p> An unprivileged process may change its real UID, effective UID, and saved set-user-ID, each to one of: the current real UID, the current effective UID or the current saved set-user-ID. </p>
<p> A privileged process (on Linux, one having the <code>CAP_SETUID</code> capability) may set its real UID, effective UID, and saved set-user-ID to arbitrary values. </p>
<p> If one of the arguments equals -1, the corresponding value is not changed. </p>
<p> Regardless of what changes are made to the real UID, effective UID, and saved set-user-ID, the filesystem UID is always set to the same value as the (possibly new) effective UID. </p>
<p> Completely analogously, <code>setresgid</code>() sets the real GID, effective GID, and saved set-group-ID of the calling process (and always modifies the filesystem GID to be the same as the effective GID), with the same restrictions for unprivileged processes.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> <i>Note</i>: there are cases where <code>setresuid</code>() can fail even when the caller is UID 0; it is a grave security error to omit checking for a failure return from <code>setresuid</code>().</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The call would change the caller&#8217;s real UID (i.e., <i>ruid</i> does not match the caller&#8217;s real UID), but there was a temporary failure allocating the necessary kernel data structures.</p>
<dt><code>EAGAIN</code></p>
<dd> <i>ruid</i> does not match the caller&#8217;s real UID and this call would bring the number of processes belonging to the real user ID <i>ruid</i> over the caller&#8217;s <code>RLIMIT_NPROC</code> resource limit. Since Linux 3.1, this error case no longer occurs (but robust applications should check for this error); see the description of <code>EAGAIN</code> in <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>EINVAL</code></p>
<dd> One or more of the target user or group IDs is not valid in this user namespace.</p>
<dt><code>EPERM</code></p>
<dd> The calling process is not privileged (did not have the necessary capability in its user namespace) and tried to change the IDs to values that are not permitted. For <code>setresuid</code>(), the necessary capability is <code>CAP_SETUID</code>; for <code>setresgid</code>(), it is <code>CAP_SETGID</code>.</dl>
<h2>VERSIONS</h2>
<p> These calls are available under Linux since Linux 2.1.44.</p>
<h2>CONFORMING TO</h2>
<p> These calls are nonstandard; they also appear on HP-UX and some of the BSDs.</p>
<h2>NOTES</h2>
<p> Under HP-UX and FreeBSD, the prototype is found in <i>&lt;unistd.h&gt;</i>. Under Linux, the prototype is provided by glibc since version 2.3.2. </p>
<p> The original Linux <code>setresuid</code>() and <code>setresgid</code>() system calls supported only 16-bit user and group IDs. Subsequently, Linux 2.4 added <code>setresuid32</code>() and <code>setresgid32</code>(), supporting 32-bit IDs. The glibc <code>setresuid</code>() and <code>setresgid</code>() wrapper functions transparently deal with the variations across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> At the kernel level, user IDs and group IDs are a per-thread attribute. However, POSIX requires that all threads in a process share the same credentials. The NPTL threading implementation handles the POSIX requirements by providing wrapper functions for the various system calls that change process UIDs and GIDs. These wrapper functions (including those for <code>setresuid</code>() and <code>setresgid</code>()) employ a signal-based technique to ensure that when one thread changes credentials, all of the other threads in the process also change their credentials. For details, see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getresuid/">getresuid</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
