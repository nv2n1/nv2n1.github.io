---
title: "fchown(2)"
name: "fchown"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fchown/"
description: "chown, fchown, lchown, fchownat – change ownership of a file"
---

<h2 class="name">NAME</h2>
<p> chown, fchown, lchown, fchownat &#8211; change ownership of a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int chown(const char *pathname, uid_t owner, gid_t group);
int fchown(int fd, uid_t owner, gid_t group);
int lchown(const char *pathname, uid_t owner, gid_t group);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
int fchownat(int dirfd, const char *pathname,
             uid_t owner, gid_t group, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fchown</code>(), <code>lchown</code>():</p>
<dl>
<dt>
<dd> /* Since glibc 2.12: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>fchownat</code>():</p>
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
<p> These system calls change the owner and group of a file. The <code>chown</code>(), <code>fchown</code>(), and <code>lchown</code>() system calls differ only in how the file is specified:</p>
<dl>
<dt>*</p>
<dd> <code>chown</code>() changes the ownership of the file specified by <i>pathname</i>, which is dereferenced if it is a symbolic link.</p>
<dt>*</p>
<dd> <code>fchown</code>() changes the ownership of the file referred to by the open file descriptor <i>fd</i>.</p>
<dt>*</p>
<dd> <code>lchown</code>() is like <code>chown</code>(), but does not dereference symbolic links.</dl>
<p> Only a privileged process (Linux: one with the <code>CAP_CHOWN</code> capability) may change the owner of a file. The owner of a file may change the group of the file to any group of which that owner is a member. A privileged process (Linux: with <code>CAP_CHOWN</code>) may change the group arbitrarily. </p>
<p> If the <i>owner</i> or <i>group</i> is specified as -1, then that ID is not changed. </p>
<p> When the owner or group of an executable file is changed by an unprivileged user, the <code>S_ISUID</code> and <code>S_ISGID</code> mode bits are cleared. POSIX does not specify whether this also should happen when root does the <code>chown</code>(); the Linux behavior depends on the kernel version, and since Linux 2.2.13, root is treated like other users. In case of a non-group-executable file (i.e., one for which the <code>S_IXGRP</code> bit is not set) the <code>S_ISGID</code> bit indicates mandatory locking, and is not cleared by a <code>chown</code>(). </p>
<p> When the owner or group of an executable file is changed (by any user), all capability sets for the file are cleared.</p>
<h3>fchownat()</h3>
<p> The <code>fchownat</code>() system call operates in exactly the same way as <code>chown</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>chown</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>chown</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> The <i>flags</i> argument is a bit mask created by ORing together 0 or more of the following values;</p>
<dl>
<dt><code>AT_EMPTY_PATH</code> (since Linux 2.6.39)</p>
<dd> If <i>pathname</i> is an empty string, operate on the file referred to by <i>dirfd</i> (which may have been obtained using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_PATH</code> flag). In this case, <i>dirfd</i> can refer to any type of file, not just a directory. If <i>dirfd</i> is <code>AT_FDCWD</code>, the call operates on the current working directory. This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, do not dereference it: instead operate on the link itself, like <code>lchown</code>(). (By default, <code>fchownat</code>() dereferences symbolic links, like <code>chown</code>().)</dl>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>fchownat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Depending on the filesystem, errors other than those listed below can be returned. </p>
<p> The more general errors for <code>chown</code>() are listed below.</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied on a component of the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
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
<dd> The calling process did not have the required permissions (see above) to change owner and/or group.</p>
<dt><code>EPERM</code></p>
<dd> The file is marked immutable or append-only. (See <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2).)</p>
<dt><code>EROFS</code></p>
<dd> The named file resides on a read-only filesystem.</dl>
<p> The general errors for <code>fchown</code>() are listed below:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid open file descriptor.</p>
<dt><code>EIO</code></p>
<dd> A low-level I/O error occurred while modifying the inode.</p>
<dt><code>ENOENT</code></p>
<dd> See above.</p>
<dt><code>EPERM</code></p>
<dd> See above.</p>
<dt><code>EROFS</code></p>
<dd> See above.</dl>
<p> The same errors that occur for <code>chown</code>() can also occur for <code>fchownat</code>(). The following additional errors can occur for <code>fchownat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>fchownat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>chown</code>(), <code>fchown</code>(), <code>lchown</code>(): 4.4BSD, SVr4, POSIX.1-2001, POSIX.1-2008. </p>
<p> The 4.4BSD version can be used only by the superuser (that is, ordinary users cannot give away files). </p>
<p> <code>fchownat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<h3>Ownership of new files</h3>
<p> When a new file is created (by, for example, <code><a href="/docs/linux/man/2-open/">open</a></code>(2) or <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2)), its owner is made the same as the filesystem user ID of the creating process. The group of the file depends on a range of factors, including the type of filesystem, the options used to mount the filesystem, and whether or not the set-group-ID mode bit is enabled on the parent directory. If the filesystem supports the <code>-o grpid</code> (or, synonymously <code>-o bsdgroups</code>) and <code>-o nogrpid</code> (or, synonymously <code>-o sysvgroups</code>) <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) options, then the rules are as follows:</p>
<dl>
<dt>*</p>
<dd> If the filesystem is mounted with <code>-o grpid</code>, then the group of a new file is made the same as that of the parent directory.</p>
<dt>*</p>
<dd> If the filesystem is mounted with <code>-o nogrpid</code> and the set-group-ID bit is disabled on the parent directory, then the group of a new file is made the same as the process&#8217;s filesystem GID.</p>
<dt>*</p>
<dd> If the filesystem is mounted with <code>-o nogrpid</code> and the set-group-ID bit is enabled on the parent directory, then the group of a new file is made the same as that of the parent directory.</dl>
<p> As at Linux 4.12, the <code>-o grpid</code> and <code>-o nogrpid</code> mount options are supported by ext2, ext3, ext4, and XFS. Filesystems that don&#8217;t support these mount options follow the <code>-o nogrpid</code> rules.</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>fchownat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>chown</code>() and <code>lchown</code>(). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h3>NFS</h3>
<p> The <code>chown</code>() semantics are deliberately violated on NFS filesystems which have UID mapping enabled. Additionally, the semantics of all system calls which access the file contents are violated, because <code>chown</code>() may cause immediate access revocation on already open files. Client side caching may lead to a delay between the time where ownership have been changed to allow access for a user and the time where the file can actually be accessed by the user on other clients.</p>
<h3>Historical details</h3>
<p> The original Linux <code>chown</code>(), <code>fchown</code>(), and <code>lchown</code>() system calls supported only 16-bit user and group IDs. Subsequently, Linux 2.4 added <code>chown32</code>(), <code>fchown32</code>(), and <code>lchown32</code>(), supporting 32-bit IDs. The glibc <code>chown</code>(), <code>fchown</code>(), and <code>lchown</code>() wrapper functions transparently deal with the variations across kernel versions. </p>
<p> In versions of Linux prior to 2.1.81 (and distinct from 2.1.46), <code>chown</code>() did not follow symbolic links. Since Linux 2.1.81, <code>chown</code>() does follow symbolic links, and there is a new system call <code>lchown</code>() that does not follow symbolic links. Since Linux 2.1.86, this new call (that has the same semantics as the old <code>chown</code>()) has got the same syscall number, and <code>chown</code>() got the newly introduced number.</p>
<h2>EXAMPLES</h2>
<p> The following program changes the ownership of the file named in its second command-line argument to the value specified in its first command-line argument. The new owner can be specified either as a numeric user ID, or as a username (which is converted to a user ID by using <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) to perform a lookup in the system password file).</p>
<h3>Program source</h3>
<p> #include &lt;pwd.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t uid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct passwd&nbsp;*pwd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*endptr; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3 || argv[1][0]&nbsp;==&nbsp;&#8216;
