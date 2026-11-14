---
title: "setegid(2)"
name: "setegid"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setegid/"
description: "seteuid, setegid – set effective user or group ID"
---

<h2 class="name">NAME</h2>
<p> seteuid, setegid &#8211; set effective user or group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int seteuid(uid_t </code><i>euid</i><code>);</code><br />
 <code>int setegid(gid_t </code><i>egid</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>seteuid</code>(), <code>setegid</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>seteuid</code>() sets the effective user ID of the calling process. Unprivileged processes may only set the effective user ID to the real user ID, the effective user ID or the saved set-user-ID. </p>
<p> Precisely the same holds for <code>setegid</code>() with &quot;group&quot; instead of &quot;user&quot;.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> <i>Note</i>: there are cases where <code>seteuid</code>() can fail even when the caller is UID 0; it is a grave security error to omit checking for a failure return from <code>seteuid</code>().</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The target user or group ID is not valid in this user namespace.</p>
<dt><code>EPERM</code></p>
<dd> In the case of <code>seteuid</code>(): the calling process is not privileged (does not have the <code>CAP_SETUID</code> capability in its user namespace) and <i>euid</i> does not match the current real user ID, current effective user ID, or current saved set-user-ID.</p>
<dt>
<dd> In the case of <code>setegid</code>(): the calling process is not privileged (does not have the <code>CAP_SETGID</code> capability in its user namespace) and <i>egid</i> does not match the current real group ID, current effective group ID, or current saved set-group-ID.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Setting the effective user (group) ID to the saved set-user-ID (saved set-group-ID) is possible since Linux 1.1.37 (1.1.38). On an arbitrary system one should check <code>_POSIX_SAVED_IDS</code>. </p>
<p> Under glibc 2.0, <code>seteuid(</code><i>euid</i><code>)</code> is equivalent to <code>setreuid(-1,</code><i> euid</i><code>)</code> and hence may change the saved set-user-ID. Under glibc 2.1 and later, it is equivalent to <code>setresuid(-1,</code><i> euid</i><code>, -1)</code> and hence does not change the saved set-user-ID. Analogous remarks hold for <code>setegid</code>(), with the difference that the change in implementation from <code>setregid(-1,</code><i> egid</i><code>)</code> to <code>setresgid(-1,</code><i> egid</i><code>, -1)</code> occurred in glibc 2.2 or 2.3 (depending on the hardware architecture). </p>
<p> According to POSIX.1, <code>seteuid</code>() (<code>setegid</code>()) need not permit <i>euid</i> (<i>egid</i>) to be the same value as the current effective user (group) ID, and some implementations do not permit this.</p>
<h3>C library/kernel differences</h3>
<p> On Linux, <code>seteuid</code>() and <code>setegid</code>() are implemented as library functions that call, respectively, <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2) and <code><a href="/docs/linux/man/2-setregid/">setregid</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2), <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
