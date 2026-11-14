---
title: "setgroups(2)"
name: "setgroups"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setgroups/"
description: "getgroups, setgroups – get/set list of supplementary group IDs"
---

<h2 class="name">NAME</h2>
<p> getgroups, setgroups &#8211; get/set list of supplementary group IDs </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getgroups(int </code><i>size</i><code>, gid_t </code><i>list</i><code>[]);</code> </p>
<p> <code>#include &lt;grp.h&gt;</code> </p>
<p> <code>int setgroups(size_t </code><i>size</i><code>, const gid_t *</code><i>list</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>setgroups</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>getgroups</code>() returns the supplementary group IDs of the calling process in <i>list</i>. The argument <i>size</i> should be set to the maximum number of items that can be stored in the buffer pointed to by <i>list</i>. If the calling process is a member of more than <i>size</i> supplementary groups, then an error results. </p>
<p> It is unspecified whether the effective group ID of the calling process is included in the returned list. (Thus, an application should also call <code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2) and add or remove the resulting value.) </p>
<p> If <i>size</i> is zero, <i>list</i> is not modified, but the total number of supplementary group IDs for the process is returned. This allows the caller to determine the size of a dynamically allocated <i>list</i> to be used in a further call to <code>getgroups</code>(). </p>
<p> <code>setgroups</code>() sets the supplementary group IDs for the calling process. Appropriate privileges are required (see the description of the <code>EPERM</code> error, below). The <i>size</i> argument specifies the number of supplementary group IDs in the buffer pointed to by <i>list</i>. A process can drop all of its supplementary groups with the call: </p>
<p> setgroups(0, NULL);</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>getgroups</code>() returns the number of supplementary group IDs. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> On success, <code>setgroups</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>list</i> has an invalid address.</dl>
<p> <code>getgroups</code>() can additionally fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>size</i> is less than the number of supplementary group IDs, but is not zero.</dl>
<p> <code>setgroups</code>() can additionally fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>size</i> is greater than <code>NGROUPS_MAX</code> (32 before Linux 2.6.4; 65536 since Linux 2.6.4).</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege (the caller does not have the <code>CAP_SETGID</code> capability in the user namespace in which it resides).</p>
<dt><code>EPERM</code> (since Linux 3.19)</p>
<dd> The use of <code>setgroups</code>() is denied in this user namespace. See the description of <i>/proc/[pid]/setgroups</i> in <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7).</dl>
<h2>CONFORMING TO</h2>
<p> <code>getgroups</code>(): SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>setgroups</code>(): SVr4, 4.3BSD. Since <code>setgroups</code>() requires privilege, it is not covered by POSIX.1.</p>
<h2>NOTES</h2>
<p> A process can have up to <code>NGROUPS_MAX</code> supplementary group IDs in addition to the effective group ID. The constant <code>NGROUPS_MAX</code> is defined in <i>&lt;limits.h&gt;</i>. The set of supplementary group IDs is inherited from the parent process, and preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The maximum number of supplementary group IDs can be found at run time using <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3): </p>
<p> long ngroups_max; ngroups_max = sysconf(_SC_NGROUPS_MAX); </p>
<p> The maximum return value of <code>getgroups</code>() cannot be larger than one more than this value. Since Linux 2.6.4, the maximum number of supplementary group IDs is also exposed via the Linux-specific read-only file, <i>/proc/sys/kernel/ngroups_max</i>. </p>
<p> The original Linux <code>getgroups</code>() system call supported only 16-bit group IDs. Subsequently, Linux 2.4 added <code>getgroups32</code>(), supporting 32-bit IDs. The glibc <code>getgroups</code>() wrapper function transparently deals with the variation across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> At the kernel level, user IDs and group IDs are a per-thread attribute. However, POSIX requires that all threads in a process share the same credentials. The NPTL threading implementation handles the POSIX requirements by providing wrapper functions for the various system calls that change process UIDs and GIDs. These wrapper functions (including the one for <code>setgroups</code>()) employ a signal-based technique to ensure that when one thread changes credentials, all of the other threads in the process also change their credentials. For details, see <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3), <code><a href="/docs/linux/man/3-group_member/">group_member</a></code>(3), <code><a href="/docs/linux/man/3-initgroups/">initgroups</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
