---
title: "mknod(2)"
name: "mknod"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mknod/"
description: "mknod, mknodat – create a special or ordinary file"
---

<h2 class="name">NAME</h2>
<p> mknod, mknodat &#8211; create a special or ordinary file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
int mknod(const char *pathname, mode_t mode, dev_t dev);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int mknodat(int dirfd, const char *pathname, mode_t mode, dev_t dev);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mknod</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The system call <code>mknod</code>() creates a filesystem node (file, device special file, or named pipe) named <i>pathname</i>, with attributes specified by <i>mode</i> and <i>dev</i>. </p>
<p> The <i>mode</i> argument specifies both the file mode to use and the type of node to be created. It should be a combination (using bitwise OR) of one of the file types listed below and zero or more of the file mode bits listed in <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7). </p>
<p> The file mode is modified by the process&#8217;s <i>umask</i> in the usual way: in the absence of a default ACL, the permissions of the created node are (<i>mode</i> &amp; ~<i>umask</i>). </p>
<p> The file type must be one of <code>S_IFREG</code>, <code>S_IFCHR</code>, <code>S_IFBLK</code>, <code>S_IFIFO</code>, or <code>S_IFSOCK</code> to specify a regular file (which will be created empty), character special file, block special file, FIFO (named pipe), or UNIX domain socket, respectively. (Zero file type is equivalent to type <code>S_IFREG</code>.) </p>
<p> If the file type is <code>S_IFCHR</code> or <code>S_IFBLK</code>, then <i>dev</i> specifies the major and minor numbers of the newly created device special file (<code><a href="/docs/linux/man/3-makedev/">makedev</a></code>(3) may be useful to build the value for <i>dev</i>); otherwise it is ignored. </p>
<p> If <i>pathname</i> already exists, or is a symbolic link, this call fails with an <code>EEXIST</code> error. </p>
<p> The newly created node will be owned by the effective user ID of the process. If the directory containing the node has the set-group-ID bit set, or if the filesystem is mounted with BSD group semantics, the new node will inherit the group ownership from its parent directory; otherwise it will be owned by the effective group ID of the process.</p>
<h3>mknodat()</h3>
<p> The <code>mknodat</code>() system call operates in exactly the same way as <code>mknod</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>mknod</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>mknod</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>mknodat</code>().</p>
<h2>RETURN VALUE</h2>
<p> <code>mknod</code>() and <code>mknodat</code>() return zero on success, or -1 if an error occurred (in which case, <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The parent directory does not allow write permission to the process, or one of the directories in the path prefix of <i>pathname</i> did not allow search permission. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks or inodes on the filesystem has been exhausted.</p>
<dt><code>EEXIST</code></p>
<dd> <i>pathname</i> already exists. This includes the case where <i>pathname</i> is a symbolic link, dangling or not.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> requested creation of something other than a regular file, device special file, FIFO or socket.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing <i>pathname</i> has no room for the new node.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory.</p>
<dt><code>EPERM</code></p>
<dd> <i>mode</i> requested creation of something other than a regular file, FIFO (named pipe), or UNIX domain socket, and the caller is not privileged (Linux: does not have the <code>CAP_MKNOD</code> capability); also returned if the filesystem containing <i>pathname</i> does not support the type of node requested.</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a file on a read-only filesystem.</dl>
<p> The following additional errors can occur for <code>mknodat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>mknodat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>mknod</code>(): SVr4, 4.4BSD, POSIX.1-2001 (but see below), POSIX.1-2008. </p>
<p> <code>mknodat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> POSIX.1-2001 says: &quot;The only portable use of <code>mknod</code>() is to create a FIFO-special file. If <i>mode</i> is not <code>S_IFIFO</code> or <i>dev</i> is not 0, the behavior of <code>mknod</code>() is unspecified.&quot; However, nowadays one should never use <code>mknod</code>() for this purpose; one should use <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), a function especially defined for this purpose. </p>
<p> Under Linux, <code>mknod</code>() cannot be used to create directories. One should make directories with <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2). </p>
<p> There are many infelicities in the protocol underlying NFS. Some of these affect <code>mknod</code>() and <code>mknodat</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/3-makedev/">makedev</a></code>(3), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/5-acl/">acl</a></code>(5), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
