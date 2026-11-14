---
title: "setreuid32(2)"
name: "setreuid32"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setreuid32/"
description: "setreuid, setregid – set real and/or effective user or group ID"
---

<h2 class="name">NAME</h2>
<p> setreuid, setregid &#8211; set real and/or effective user or group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setreuid(uid_t </code><i>ruid</i><code>, uid_t </code><i>euid</i><code>);</code><br />
 <code>int setregid(gid_t </code><i>rgid</i><code>, gid_t </code><i>egid</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>setreuid</code>(), <code>setregid</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>setreuid</code>() sets real and effective user IDs of the calling process. </p>
<p> Supplying a value of -1 for either the real or effective user ID forces the system to leave that ID unchanged. </p>
<p> Unprivileged processes may only set the effective user ID to the real user ID, the effective user ID, or the saved set-user-ID. </p>
<p> Unprivileged users may only set the real user ID to the real user ID or the effective user ID. </p>
<p> If the real user ID is set (i.e., <i>ruid</i> is not -1) or the effective user ID is set to a value not equal to the previous real user ID, the saved set-user-ID will be set to the new effective user ID. </p>
<p> Completely analogously, <code>setregid</code>() sets real and effective group ID&#8217;s of the calling process, and all of the above holds with &quot;group&quot; instead of &quot;user&quot;.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> <i>Note</i>: there are cases where <code>setreuid</code>() can fail even when the caller is UID 0; it is a grave security error to omit checking for a failure return from <code>setreuid</code>().</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The call would change the caller&#8217;s real UID (i.e., <i>ruid</i> does not match the caller&#8217;s real UID), but there was a temporary failure allocating the necessary kernel data structures.</p>
<dt><code>EAGAIN</code></p>
<dd> <i>ruid</i> does not match the caller&#8217;s real UID and this call would bring the number of processes belonging to the real user ID <i>ruid</i> over the caller&#8217;s <code>RLIMIT_NPROC</code> resource limit. Since Linux 3.1, this error case no longer occurs (but robust applications should check for this error); see the description of <code>EAGAIN</code> in <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>EINVAL</code></p>
<dd> One or more of the target user or group IDs is not valid in this user namespace.</p>
<dt><code>EPERM</code></p>
<dd> The calling process is not privileged (on Linux, does not have the necessary capability in its user namespace: <code>CAP_SETUID</code> in the case of <code>setreuid</code>(), or <code>CAP_SETGID</code> in the case of <code>setregid</code>()) and a change other than (i) swapping the effective user (group) ID with the real user (group) ID, or (ii) setting one to the value of the other or (iii) setting the effective user (group) ID to the value of the saved set-user-ID (saved set-group-ID) was specified.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD (<code>setreuid</code>() and <code>setregid</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> Setting the effective user (group) ID to the saved set-user-ID (saved set-group-ID) is possible since Linux 1.1.37 (1.1.38). </p>
<p> POSIX.1 does not specify all of the UID changes that Linux permits for an unprivileged process. For <code>setreuid</code>(), the effective user ID can be made the same as the real user ID or the saved set-user-ID, and it is unspecified whether unprivileged processes may set the real user ID to the real user ID, the effective user ID, or the saved set-user-ID. For <code>setregid</code>(), the real group ID can be changed to the value of the saved set-group-ID, and the effective group ID can be changed to the value of the real group ID or the saved set-group-ID. The precise details of what ID changes are permitted vary across implementations. </p>
<p> POSIX.1 makes no specification about the effect of these calls on the saved set-user-ID and saved set-group-ID. </p>
<p> The original Linux <code>setreuid</code>() and <code>setregid</code>() system calls supported only 16-bit user and group IDs. Subsequently, Linux 2.4 added <code>setreuid32</code>() and <code>setregid32</code>(), supporting 32-bit IDs. The glibc <code>setreuid</code>() and <code>setregid</code>() wrapper functions transparently deal with the variations across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> At the kernel level, user IDs and group IDs are a per-thread attribute. However, POSIX requires that all threads in a process share the same credentials. The NPTL threading implementation handles the POSIX requirements by providing wrapper functions for the various system calls that change process UIDs and GIDs. These wrapper functions (including those for <code>setreuid</code>() and <code>setregid</code>()) employ a signal-based technique to ensure that when one thread changes credentials, all of the other threads in the process also change their credentials. For details, see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
