---
title: "mkdirat(2)"
name: "mkdirat"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mkdirat/"
description: "mkdir, mkdirat – create a directory"
---

<h2 class="name">NAME</h2>
<p> mkdir, mkdirat &#8211; create a directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
int mkdir(const char *pathname, mode_t mode);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int mkdirat(int dirfd, const char *pathname, mode_t mode);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mkdirat</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _ATFILE_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>mkdir</code>() attempts to create a directory named <i>pathname</i>. </p>
<p> The argument <i>mode</i> specifies the mode for the new directory (see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)). It is modified by the process&#8217;s <i>umask</i> in the usual way: in the absence of a default ACL, the mode of the created directory is (<i>mode</i> &amp; ~<i>umask</i> &amp; 0777). Whether other <i>mode</i> bits are honored for the created directory depends on the operating system. For Linux, see NOTES below. </p>
<p> The newly created directory will be owned by the effective user ID of the process. If the directory containing the file has the set-group-ID bit set, or if the filesystem is mounted with BSD group semantics (<i>mount -o bsdgroups</i> or, synonymously <i>mount -o grpid</i>), the new directory will inherit the group ownership from its parent; otherwise it will be owned by the effective group ID of the process. </p>
<p> If the parent directory has the set-group-ID bit set, then so will the newly created directory.</p>
<h3>mkdirat()</h3>
<p> The <code>mkdirat</code>() system call operates in exactly the same way as <code>mkdir</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>mkdir</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>mkdir</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>mkdirat</code>().</p>
<h2>RETURN VALUE</h2>
<p> <code>mkdir</code>() and <code>mkdirat</code>() return zero on success, or -1 if an error occurred (in which case, <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The parent directory does not allow write permission to the process, or one of the directories in <i>pathname</i> did not allow search permission. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks or inodes on the filesystem has been exhausted.</p>
<dt><code>EEXIST</code></p>
<dd> <i>pathname</i> already exists (not necessarily as a directory). This includes the case where <i>pathname</i> is a symbolic link, dangling or not.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The final component (&quot;basename&quot;) of the new directory&#8217;s <i>pathname</i> is invalid (e.g., it contains characters not permitted by the underlying filesystem).</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>EMLINK</code></p>
<dd> The number of links to the parent directory would exceed <code>LINK_MAX</code>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing <i>pathname</i> has no room for the new directory.</p>
<dt><code>ENOSPC</code></p>
<dd> The new directory cannot be created because the user&#8217;s disk quota is exhausted.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory.</p>
<dt><code>EPERM</code></p>
<dd> The filesystem containing <i>pathname</i> does not support the creation of directories.</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a file on a read-only filesystem.</dl>
<p> The following additional errors can occur for <code>mkdirat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>mkdirat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>mkdir</code>(): SVr4, BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>mkdirat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Under Linux, apart from the permission bits, the <code>S_ISVTX</code> <i>mode</i> bit is also honored. </p>
<p> There are many infelicities in the protocol underlying NFS. Some of these affect <code>mkdir</code>().</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>mkdirat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>mkdir</code>(). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkdir/">mkdir</a></code>(1), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
