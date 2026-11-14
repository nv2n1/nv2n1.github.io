---
title: "setfsgid(2)"
name: "setfsgid"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setfsgid/"
description: "setfsgid – set group identity used for filesystem checks"
---

<h2 class="name">NAME</h2>
<p> setfsgid &#8211; set group identity used for filesystem checks </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/fsuid.h&gt;</code> </p>
<p> <code>int setfsgid(uid_t </code><i>fsgid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> On Linux, a process has both a filesystem group ID and an effective group ID. The (Linux-specific) filesystem group ID is used for permissions checking when accessing filesystem objects, while the effective group ID is used for some other kinds of permissions checks (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)). </p>
<p> Normally, the value of the process&#8217;s filesystem group ID is the same as the value of its effective group ID. This is so, because whenever a process&#8217;s effective group ID is changed, the kernel also changes the filesystem group ID to be the same as the new value of the effective group ID. A process can cause the value of its filesystem group ID to diverge from its effective group ID by using <code>setfsgid</code>() to change its filesystem group ID to the value given in <i>fsgid</i>. </p>
<p> <code>setfsgid</code>() will succeed only if the caller is the superuser or if <i>fsgid</i> matches either the caller&#8217;s real group ID, effective group ID, saved set-group-ID, or current the filesystem user ID.</p>
<h2>RETURN VALUE</h2>
<p> On both success and failure, this call returns the previous filesystem group ID of the caller.</p>
<h2>VERSIONS</h2>
<p> This system call is present in Linux since version 1.2.</p>
<h2>CONFORMING TO</h2>
<p> <code>setfsgid</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> The filesystem group ID concept and the <code>setfsgid</code>() system call were invented for historical reasons that are no longer applicable on modern Linux kernels. See <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2) for a discussion of why the use of both <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2) and <code>setfsgid</code>() is nowadays unneeded. </p>
<p> The original Linux <code>setfsgid</code>() system call supported only 16-bit group IDs. Subsequently, Linux 2.4 added <code>setfsgid32</code>() supporting 32-bit IDs. The glibc <code>setfsgid</code>() wrapper function transparently deals with the variation across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> In glibc 2.15 and earlier, when the wrapper for this system call determines that the argument can&#8217;t be passed to the kernel without integer truncation (because the kernel is old and does not support 32-bit group IDs), it will return -1 and set <i>errno</i> to <code>EINVAL</code> without attempting the system call.</p>
<h2>BUGS</h2>
<p> No error indications of any kind are returned to the caller, and the fact that both successful and unsuccessful calls return the same value makes it impossible to directly determine whether the call succeeded or failed. Instead, the caller must resort to looking at the return value from a further call such as <i>setfsgid(-1)</i> (which will always fail), in order to determine if a preceding call to <code>setfsgid</code>() changed the filesystem group ID. At the very least, <code>EPERM</code> should be returned when the call fails (because the caller lacks the <code>CAP_SETGID</code> capability).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-setfsuid/">setfsuid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
