---
title: "faccessat(2)"
name: "faccessat"
section: "2"
letter: "f"
url: "/docs/linux/man/2-faccessat/"
description: "access, faccessat, faccessat2 – check user’s permissions for a file"
---

<h2 class="name">NAME</h2>
<p> access, faccessat, faccessat2 &#8211; check user&#8217;s permissions for a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int access(const char *pathname, int mode);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
int faccessat(int dirfd, const char *pathname, int mode, int flags);
/* But see C library/kernel differences, below */
int faccessat2(int dirfd, const char *pathname, int mode, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>faccessat</code>():</p>
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
<p> <code>access</code>() checks whether the calling process can access the file <i>pathname</i>. If <i>pathname</i> is a symbolic link, it is dereferenced. </p>
<p> The <i>mode</i> specifies the accessibility check(s) to be performed, and is either the value <code>F_OK</code>, or a mask consisting of the bitwise OR of one or more of <code>R_OK</code>, <code>W_OK</code>, and <code>X_OK</code>. <code>F_OK</code> tests for the existence of the file. <code>R_OK</code>, <code>W_OK</code>, and <code>X_OK</code> test whether the file exists and grants read, write, and execute permissions, respectively. </p>
<p> The check is done using the calling process&#8217;s <i>real</i> UID and GID, rather than the effective IDs as is done when actually attempting an operation (e.g., <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) on the file. Similarly, for the root user, the check uses the set of permitted capabilities rather than the set of effective capabilities; and for non-root users, the check uses an empty set of capabilities. </p>
<p> This allows set-user-ID programs and capability-endowed programs to easily determine the invoking user&#8217;s authority. In other words, <code>access</code>() does not answer the &quot;can I read/write/execute this file?&quot; question. It answers a slightly different question: &quot;(assuming I&#8217;m a setuid binary) can <i>the user who invoked me</i> read/write/execute this file?&quot;, which gives set-user-ID programs the possibility to prevent malicious users from causing them to read files which users shouldn&#8217;t be able to read. </p>
<p> If the calling process is privileged (i.e., its real UID is zero), then an <code>X_OK</code> check is successful for a regular file if execute permission is enabled for any of the file owner, group, or other.</p>
<h3>faccessat()</h3>
<p> <code>faccessat</code>() operates in exactly the same way as <code>access</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>access</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>access</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> <i>flags</i> is constructed by ORing together zero or more of the following values:</p>
<dl>
<dt><code>AT_EACCESS</code></p>
<dd> Perform access checks using the effective user and group IDs. By default, <code>faccessat</code>() uses the real IDs (like <code>access</code>()).</p>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, do not dereference it: instead return information about the link itself.</dl>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>faccessat</code>().</p>
<h3>faccessat2()</h3>
<p> The description of <code>faccessat</code>() given above corresponds to POSIX.1 and to the implementation provided by glibc. However, the glibc implementation was an imperfect emulation (see BUGS) that papered over the fact that the raw Linux <code>faccessat</code>() system call does not have a <i>flags</i> argument. To allow for a proper implementation, Linux 5.8 added the <code>faccessat2</code>() system call, which supports the <i>flags</i> argument and allows a correct implementation of the <code>faccessat</code>() wrapper function.</p>
<h2>RETURN VALUE</h2>
<p> On success (all requested permissions granted, or <i>mode</i> is <code>F_OK</code> and the file exists), zero is returned. On error (at least one bit in <i>mode</i> asked for a permission that is denied, or <i>mode</i> is <code>F_OK</code> and the file does not exist, or some other error occurred), -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>access</code>() and <code>faccessat</code>() shall fail if:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The requested access would be denied to the file, or search permission is denied for one of the directories in the path prefix of <i>pathname</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> A component of <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory.</p>
<dt><code>EROFS</code></p>
<dd> Write permission was requested for a file on a read-only filesystem.</dl>
<p> <code>access</code>() and <code>faccessat</code>() may fail if:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> was incorrectly specified.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ETXTBSY</code></p>
<dd> Write access was requested to an executable which is being executed.</dl>
<p> The following additional errors can occur for <code>faccessat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>faccessat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4. </p>
<p> <code>faccessat2</code>() was added to Linux in version 5.8.</p>
<h2>CONFORMING TO</h2>
<p> <code>access</code>(): SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>faccessat</code>(): POSIX.1-2008. </p>
<p> <code>faccessat2</code>(): Linux-specific.</p>
<h2>NOTES</h2>
<p> <code>Warning</code>: Using these calls to check if a user is authorized to, for example, open a file before actually doing so using <code><a href="/docs/linux/man/2-open/">open</a></code>(2) creates a security hole, because the user might exploit the short time interval between checking and opening the file to manipulate it. <code>For this reason, the use of this system call should be avoided</code>. (In the example just described, a safer alternative would be to temporarily switch the process&#8217;s effective user ID to the real ID and then call <code><a href="/docs/linux/man/2-open/">open</a></code>(2).) </p>
<p> <code>access</code>() always dereferences symbolic links. If you need to check the permissions on a symbolic link, use <code>faccessat</code>() with the flag <code>AT_SYMLINK_NOFOLLOW</code>. </p>
<p> These calls return an error if any of the access types in <i>mode</i> is denied, even if some of the other access types in <i>mode</i> are permitted. </p>
<p> If the calling process has appropriate privileges (i.e., is superuser), POSIX.1-2001 permits an implementation to indicate success for an <code>X_OK</code> check even if none of the execute file permission bits are set. Linux does not do this. </p>
<p> A file is accessible only if the permissions on each of the directories in the path prefix of <i>pathname</i> grant search (i.e., execute) access. If any directory is inaccessible, then the <code>access</code>() call fails, regardless of the permissions on the file itself. </p>
<p> Only access bits are checked, not the file type or contents. Therefore, if a directory is found to be writable, it probably means that files can be created in the directory, and not that the directory can be written as a file. Similarly, a DOS file may be found to be &quot;executable,&quot; but the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call will still fail. </p>
<p> These calls may not work correctly on NFSv2 filesystems with UID mapping enabled, because UID mapping is done on the server and hidden from the client, which checks permissions. (NFS versions 3 and higher perform the check on the server.) Similar problems can occur to FUSE mounts.</p>
<h3>C library/kernel differences</h3>
<p> The raw <code>faccessat</code>() system call takes only the first three arguments. The <code>AT_EACCESS</code> and <code>AT_SYMLINK_NOFOLLOW</code> flags are actually implemented within the glibc wrapper function for <code>faccessat</code>(). If either of these flags is specified, then the wrapper function employs <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2) to determine access permissions, but see BUGS.</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>faccessat</code>() is unavailable (and when the <code>AT_EACCESS</code> and <code>AT_SYMLINK_NOFOLLOW</code> flags are not specified), the glibc wrapper function falls back to the use of <code>access</code>(). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h2>BUGS</h2>
<p> Because the Linux kernel&#8217;s <code>faccessat</code>() system call does not support a <i>flags</i> argument, the glibc <code>faccessat</code>() wrapper function provided in glibc 2.32 and earlier emulates the required functionality using a combination of the <code>faccessat</code>() system call and <code><a href="/docs/linux/man/2-fstatat/">fstatat</a></code>(2). However, this emulation does not take ACLs into account. Starting with glibc 2.33, the wrapper function avoids this bug by making use of the <code>faccessat2</code>() system call where it is provided by the underlying kernel. </p>
<p> In kernel 2.4 (and earlier) there is some strangeness in the handling of <code>X_OK</code> tests for superuser. If all categories of execute permission are disabled for a nondirectory file, then the only <code>access</code>() test that returns -1 is when <i>mode</i> is specified as just <code>X_OK</code>; if <code>R_OK</code> or <code>W_OK</code> is also specified in <i>mode</i>, then <code>access</code>() returns 0 for such files. Early 2.6 kernels (up to and including 2.6.3) also behaved in the same way as kernel 2.4. </p>
<p> In kernels before 2.6.20, these calls ignored the effect of the <code>MS_NOEXEC</code> flag if it was used to <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) the underlying filesystem. Since kernel 2.6.20, the <code>MS_NOEXEC</code> flag is honored.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-euidaccess/">euidaccess</a></code>(3), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
