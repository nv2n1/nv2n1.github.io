---
title: "setfsuid32(2)"
name: "setfsuid32"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setfsuid32/"
description: "setfsuid – set user identity used for filesystem checks"
---

<h2 class="name">NAME</h2>
<p> setfsuid &#8211; set user identity used for filesystem checks </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/fsuid.h&gt;</code> </p>
<p> <code>int setfsuid(uid_t </code><i>fsuid</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> On Linux, a process has both a filesystem user ID and an effective user ID. The (Linux-specific) filesystem user ID is used for permissions checking when accessing filesystem objects, while the effective user ID is used for various other kinds of permissions checks (see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)). </p>
<p> Normally, the value of the process&#8217;s filesystem user ID is the same as the value of its effective user ID. This is so, because whenever a process&#8217;s effective user ID is changed, the kernel also changes the filesystem user ID to be the same as the new value of the effective user ID. A process can cause the value of its filesystem user ID to diverge from its effective user ID by using <code>setfsuid</code>() to change its filesystem user ID to the value given in <i>fsuid</i>. </p>
<p> Explicit calls to <code>setfsuid</code>() and <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2) are (were) usually used only by programs such as the Linux NFS server that need to change what user and group ID is used for file access without a corresponding change in the real and effective user and group IDs. A change in the normal user IDs for a program such as the NFS server is (was) a security hole that can expose it to unwanted signals. (However, this issue is historical; see below.) </p>
<p> <code>setfsuid</code>() will succeed only if the caller is the superuser or if <i>fsuid</i> matches either the caller&#8217;s real user ID, effective user ID, saved set-user-ID, or current filesystem user ID.</p>
<h2>RETURN VALUE</h2>
<p> On both success and failure, this call returns the previous filesystem user ID of the caller.</p>
<h2>VERSIONS</h2>
<p> This system call is present in Linux since version 1.2.</p>
<h2>CONFORMING TO</h2>
<p> <code>setfsuid</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> At the time when this system call was introduced, one process could send a signal to another process with the same effective user ID. This meant that if a privileged process changed its effective user ID for the purpose of file permission checking, then it could become vulnerable to receiving signals sent by another (unprivileged) process with the same user ID. The filesystem user ID attribute was thus added to allow a process to change its user ID for the purposes of file permission checking without at the same time becoming vulnerable to receiving unwanted signals. Since Linux 2.0, signal permission handling is different (see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)), with the result that a process can change its effective user ID without being vulnerable to receiving signals from unwanted processes. Thus, <code>setfsuid</code>() is nowadays unneeded and should be avoided in new applications (likewise for <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2)). </p>
<p> The original Linux <code>setfsuid</code>() system call supported only 16-bit user IDs. Subsequently, Linux 2.4 added <code>setfsuid32</code>() supporting 32-bit IDs. The glibc <code>setfsuid</code>() wrapper function transparently deals with the variation across kernel versions.</p>
<h3>C library/kernel differences</h3>
<p> In glibc 2.15 and earlier, when the wrapper for this system call determines that the argument can&#8217;t be passed to the kernel without integer truncation (because the kernel is old and does not support 32-bit user IDs), it will return -1 and set <i>errno</i> to <code>EINVAL</code> without attempting the system call.</p>
<h2>BUGS</h2>
<p> No error indications of any kind are returned to the caller, and the fact that both successful and unsuccessful calls return the same value makes it impossible to directly determine whether the call succeeded or failed. Instead, the caller must resort to looking at the return value from a further call such as <i>setfsuid(-1)</i> (which will always fail), in order to determine if a preceding call to <code>setfsuid</code>() changed the filesystem user ID. At the very least, <code>EPERM</code> should be returned when the call fails (because the caller lacks the <code>CAP_SETUID</code> capability).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-setfsgid/">setfsgid</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
