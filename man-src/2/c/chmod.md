---
title: "chmod(2)"
name: "chmod"
section: "2"
letter: "c"
url: "/docs/linux/man/2-chmod/"
description: "chmod, fchmod, fchmodat – change permissions of a file"
---

<h2 class="name">NAME</h2>
<p> chmod, fchmod, fchmodat &#8211; change permissions of a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/stat.h&gt;
int chmod(const char *pathname, mode_t mode);
int fchmod(int fd, mode_t mode);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int fchmodat(int dirfd, const char *pathname, mode_t mode, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fchmod</code>():</p>
<dl>
<dt>
<dd> Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L </p>
<p> Glibc 2.19 to 2.23<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE </p>
<p> Glibc 2.16 to 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_POSIX_C_SOURCE </p>
<p> Glibc 2.12 to 2.16:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L </p>
<p> Glibc 2.11 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<p> <code>fchmodat</code>():</p>
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
<p> The <code>chmod</code>() and <code>fchmod</code>() system calls change a files mode bits. (The file mode consists of the file permission bits plus the set-user-ID, set-group-ID, and sticky bits.) These system calls differ only in how the file is specified:</p>
<dl>
<dt>*</p>
<dd> <code>chmod</code>() changes the mode of the file specified whose pathname is given in <i>pathname</i>, which is dereferenced if it is a symbolic link.</p>
<dt>*</p>
<dd> <code>fchmod</code>() changes the mode of the file referred to by the open file descriptor <i>fd</i>.</dl>
<p> The new file mode is specified in <i>mode</i>, which is a bit mask created by ORing together zero or more of the following:</p>
<dl>
<dt><code>S_ISUID</code> (04000)</p>
<dd> set-user-ID (set process effective user ID on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2))</p>
<dt><code>S_ISGID</code> (02000)</p>
<dd> set-group-ID (set process effective group ID on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2); mandatory locking, as described in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2); take a new file&#8217;s group from parent directory, as described in <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2) and <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2))</p>
<dt><code>S_ISVTX</code> (01000)</p>
<dd> sticky bit (restricted deletion flag, as described in <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2))</p>
<dt><code>S_IRUSR</code> (00400)</p>
<dd> read by owner</p>
<dt><code>S_IWUSR</code> (00200)</p>
<dd> write by owner</p>
<dt><code>S_IXUSR</code> (00100)</p>
<dd> execute/search by owner (&quot;search&quot; applies for directories, and means that entries within the directory can be accessed)</p>
<dt><code>S_IRGRP</code> (00040)</p>
<dd> read by group</p>
<dt><code>S_IWGRP</code> (00020)</p>
<dd> write by group</p>
<dt><code>S_IXGRP</code> (00010)</p>
<dd> execute/search by group</p>
<dt><code>S_IROTH</code> (00004)</p>
<dd> read by others</p>
<dt><code>S_IWOTH</code> (00002)</p>
<dd> write by others</p>
<dt><code>S_IXOTH</code> (00001)</p>
<dd> execute/search by others</dl>
<p> The effective UID of the calling process must match the owner of the file, or the process must be privileged (Linux: it must have the <code>CAP_FOWNER</code> capability). </p>
<p> If the calling process is not privileged (Linux: does not have the <code>CAP_FSETID</code> capability), and the group of the file does not match the effective group ID of the process or one of its supplementary group IDs, the <code>S_ISGID</code> bit will be turned off, but this will not cause an error to be returned. </p>
<p> As a security measure, depending on the filesystem, the set-user-ID and set-group-ID execution bits may be turned off if a file is written. (On Linux, this occurs if the writing process does not have the <code>CAP_FSETID</code> capability.) On some filesystems, only the superuser can set the sticky bit, which may have a special meaning. For the sticky bit, and for set-user-ID and set-group-ID bits on directories, see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7). </p>
<p> On NFS filesystems, restricting the permissions will immediately influence already open files, because the access control is done on the server, but open files are maintained by the client. Widening the permissions may be delayed for other clients if attribute caching is enabled on them.</p>
<h3>fchmodat()</h3>
<p> The <code>fchmodat</code>() system call operates in exactly the same way as <code>chmod</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>chmod</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>chmod</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> <i>flags</i> can either be 0, or include the following flag:</p>
<dl>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, do not dereference it: instead operate on the link itself. This flag is not currently implemented.</dl>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>fchmodat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Depending on the filesystem, errors other than those listed below can be returned. </p>
<p> The more general errors for <code>chmod</code>() are listed below:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied on a component of the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> The file does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The effective UID does not match the owner of the file, and the process is not privileged (Linux: it does not have the <code>CAP_FOWNER</code> capability).</p>
<dt><code>EPERM</code></p>
<dd> The file is marked immutable or append-only. (See <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2).)</p>
<dt><code>EROFS</code></p>
<dd> The named file resides on a read-only filesystem.</dl>
<p> The general errors for <code>fchmod</code>() are listed below:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> The file descriptor <i>fd</i> is not valid.</p>
<dt><code>EIO</code></p>
<dd> See above.</p>
<dt><code>EPERM</code></p>
<dd> See above.</p>
<dt><code>EROFS</code></p>
<dd> See above.</dl>
<p> The same errors that occur for <code>chmod</code>() can also occur for <code>fchmodat</code>(). The following additional errors can occur for <code>fchmodat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</p>
<dt><code>ENOTSUP</code></p>
<dd> <i>flags</i> specified <code>AT_SYMLINK_NOFOLLOW</code>, which is not supported.</dl>
<h2>VERSIONS</h2>
<p> <code>fchmodat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>chmod</code>(), <code>fchmod</code>(): 4.4BSD, SVr4, POSIX.1-2001i, POSIX.1-2008. </p>
<p> <code>fchmodat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<h3>C library/kernel differences</h3>
<p> The GNU C library <code>fchmodat</code>() wrapper function implements the POSIX-specified interface described in this page. This interface differs from the underlying Linux system call, which does <i>not</i> have a <i>flags</i> argument.</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>fchmodat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>chmod</code>(). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
