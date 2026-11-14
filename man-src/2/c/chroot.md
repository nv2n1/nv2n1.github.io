---
title: "chroot(2)"
name: "chroot"
section: "2"
letter: "c"
url: "/docs/linux/man/2-chroot/"
description: "chroot – change root directory"
---

<h2 class="name">NAME</h2>
<p> chroot &#8211; change root directory </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int chroot(const char *</code><i>path</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>chroot</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.2.2:</p>
<dd>
<pre><code>
_XOPEN_SOURCE &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L) || /* Since glibc 2.20: */ _DEFAULT_SOURCE || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE
</code></pre>
<dt>Before glibc 2.2.2: none</p>
<dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>chroot</code>() changes the root directory of the calling process to that specified in <i>path</i>. This directory will be used for pathnames beginning with <i>/</i>. The root directory is inherited by all children of the calling process. </p>
<p> Only a privileged process (Linux: one with the <code>CAP_SYS_CHROOT</code> capability in its user namespace) may call <code>chroot</code>(). </p>
<p> This call changes an ingredient in the pathname resolution process and does nothing else. In particular, it is not intended to be used for any kind of security purpose, neither to fully sandbox a process nor to restrict filesystem system calls. In the past, <code>chroot</code>() has been used by daemons to restrict themselves prior to passing paths supplied by untrusted users to system calls such as <code><a href="/docs/linux/man/2-open/">open</a></code>(2). However, if a folder is moved out of the chroot directory, an attacker can exploit that to get out of the chroot directory as well. The easiest way to do that is to <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) to the to-be-moved directory, wait for it to be moved out, then open a path like ../../../etc/passwd. </p>
<p> A slightly trickier variation also works under some circumstances if <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) is not permitted. If a daemon allows a &quot;chroot directory&quot; to be specified, that usually means that if you want to prevent remote users from accessing files outside the chroot directory, you must ensure that folders are never moved out of it. </p>
<p> This call does not change the current working directory, so that after the call &#8216;<i>.</i>&#8216; can be outside the tree rooted at &#8216;<i>/</i>&#8216;. In particular, the superuser can escape from a &quot;chroot jail&quot; by doing: </p>
<p> mkdir foo; chroot foo; cd .. </p>
<p> This call does not close open file descriptors, and such file descriptors may allow access to files outside the chroot tree.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Depending on the filesystem, other errors can be returned. The more general errors are listed below:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied on a component of the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EFAULT</code></p>
<dd> <i>path</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>path</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>path</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> The file does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of <i>path</i> is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The caller has insufficient privilege.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.4BSD, SUSv2 (marked LEGACY). This function is not part of POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s root directory. The root directory is left unchanged by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The magic symbolic link, <i>/proc/[pid]/root</i>, can be used to discover a process&#8217;s root directory; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details. </p>
<p> FreeBSD has a stronger <code>jail</code>() system call.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chroot/">chroot</a></code>(1), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/2-pivot_root/">pivot_root</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/8-switch_root/">switch_root</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
