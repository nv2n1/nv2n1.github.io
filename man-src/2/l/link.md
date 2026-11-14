---
title: "link(2)"
name: "link"
section: "2"
letter: "l"
url: "/docs/linux/man/2-link/"
description: "link, linkat – make a new name for a file"
---

<h2 class="name">NAME</h2>
<p> link, linkat &#8211; make a new name for a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int link(const char *oldpath, const char *newpath);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
int linkat(int olddirfd, const char *oldpath,
           int newdirfd, const char *newpath, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>linkat</code>():</p>
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
<p> <code>link</code>() creates a new link (also known as a hard link) to an existing file. </p>
<p> If <i>newpath</i> exists, it will <i>not</i> be overwritten. </p>
<p> This new name may be used exactly as the old one for any operation; both names refer to the same file (and so have the same permissions and ownership) and it is impossible to tell which name was the &quot;original&quot;.</p>
<h3>linkat()</h3>
<p> The <code>linkat</code>() system call operates in exactly the same way as <code>link</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>oldpath</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>olddirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>link</code>() for a relative pathname). </p>
<p> If <i>oldpath</i> is relative and <i>olddirfd</i> is the special value <code>AT_FDCWD</code>, then <i>oldpath</i> is interpreted relative to the current working directory of the calling process (like <code>link</code>()). </p>
<p> If <i>oldpath</i> is absolute, then <i>olddirfd</i> is ignored. </p>
<p> The interpretation of <i>newpath</i> is as for <i>oldpath</i>, except that a relative pathname is interpreted relative to the directory referred to by the file descriptor <i>newdirfd</i>. </p>
<p> The following values can be bitwise ORed in <i>flags</i>:</p>
<dl>
<dt><code>AT_EMPTY_PATH</code> (since Linux 2.6.39)</p>
<dd> If <i>oldpath</i> is an empty string, create a link to the file referenced by <i>olddirfd</i> (which may have been obtained using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_PATH</code> flag). In this case, <i>olddirfd</i> can refer to any type of file except a directory. This will generally not work if the file has a link count of zero (files created with <code>O_TMPFILE</code> and without <code>O_EXCL</code> are an exception). The caller must have the <code>CAP_DAC_READ_SEARCH</code> capability in order to use this flag. This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_SYMLINK_FOLLOW</code> (since Linux 2.6.18)</p>
<dd> By default, <code>linkat</code>(), does not dereference <i>oldpath</i> if it is a symbolic link (like <code>link</code>()). The flag <code>AT_SYMLINK_FOLLOW</code> can be specified in <i>flags</i> to cause <i>oldpath</i> to be dereferenced if it is a symbolic link. If procfs is mounted, this can be used as an alternative to <code>AT_EMPTY_PATH</code>, like this:</p>
<dt>
<dd> linkat(AT_FDCWD, &quot;/proc/self/fd/&lt;fd&gt;&quot;, newdirfd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;newname, AT_SYMLINK_FOLLOW);</dl>
<p> Before kernel 2.6.18, the <i>flags</i> argument was unused, and had to be specified as 0. </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>linkat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write access to the directory containing <i>newpath</i> is denied, or search permission is denied for one of the directories in the path prefix of <i>oldpath</i> or <i>newpath</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks on the filesystem has been exhausted.</p>
<dt><code>EEXIST</code></p>
<dd> <i>newpath</i> already exists.</p>
<dt><code>EFAULT</code></p>
<dd> <i>oldpath</i> or <i>newpath</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>oldpath</i> or <i>newpath</i>.</p>
<dt><code>EMLINK</code></p>
<dd> The file referred to by <i>oldpath</i> already has the maximum number of links to it. For example, on an <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5) filesystem that does not employ the <i>dir_index</i> feature, the limit on the number of hard links to a file is 65,000; on <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), the limit is 65,535 links.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>oldpath</i> or <i>newpath</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>oldpath</i> or <i>newpath</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing the file has no room for the new directory entry.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>oldpath</i> or <i>newpath</i> is not, in fact, a directory.</p>
<dt><code>EPERM</code></p>
<dd> <i>oldpath</i> is a directory.</p>
<dt><code>EPERM</code></p>
<dd> The filesystem containing <i>oldpath</i> and <i>newpath</i> does not support the creation of hard links.</p>
<dt><code>EPERM</code> (since Linux 3.6)</p>
<dd> The caller does not have permission to create a hard link to this file (see the description of <i>/proc/sys/fs/protected_hardlinks</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt><code>EPERM</code></p>
<dd> <i>oldpath</i> is marked immutable or append-only. (See <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2).)</p>
<dt><code>EROFS</code></p>
<dd> The file is on a read-only filesystem.</p>
<dt><code>EXDEV</code></p>
<dd> <i>oldpath</i> and <i>newpath</i> are not on the same mounted filesystem. (Linux permits a filesystem to be mounted at multiple points, but <code>link</code>() does not work across different mount points, even if the same filesystem is mounted on both.)</dl>
<p> The following additional errors can occur for <code>linkat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>olddirfd</i> or <i>newdirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid flag value was specified in <i>flags</i>.</p>
<dt><code>ENOENT</code></p>
<dd> <code>AT_EMPTY_PATH</code> was specified in <i>flags</i>, but the caller did not have the <code>CAP_DAC_READ_SEARCH</code> capability.</p>
<dt><code>ENOENT</code></p>
<dd> An attempt was made to link to the <i>/proc/self/fd/NN</i> file corresponding to a file descriptor created with</p>
<dt>
<dd> open(path, O_TMPFILE | O_EXCL, mode);</p>
<dt>
<dd> See <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<dt><code>ENOENT</code></p>
<dd> An attempt was made to link to a <i>/proc/self/fd/NN</i> file corresponding to a file that has been deleted.</p>
<dt><code>ENOENT</code></p>
<dd> <i>oldpath</i> is a relative pathname and <i>olddirfd</i> refers to a directory that has been deleted, or <i>newpath</i> is a relative pathname and <i>newdirfd</i> refers to a directory that has been deleted.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>oldpath</i> is relative and <i>olddirfd</i> is a file descriptor referring to a file other than a directory; or similar for <i>newpath</i> and <i>newdirfd</i></p>
<dt><code>EPERM</code></p>
<dd> <code>AT_EMPTY_PATH</code> was specified in <i>flags</i>, <i>oldpath</i> is an empty string, and <i>olddirfd</i> refers to a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>linkat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>link</code>(): SVr4, 4.3BSD, POSIX.1-2001 (but see NOTES), POSIX.1-2008. </p>
<p> <code>linkat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Hard links, as created by <code>link</code>(), cannot span filesystems. Use <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2) if this is required. </p>
<p> POSIX.1-2001 says that <code>link</code>() should dereference <i>oldpath</i> if it is a symbolic link. However, since kernel 2.0, Linux does not do so: if <i>oldpath</i> is a symbolic link, then <i>newpath</i> is created as a (hard) link to the same symbolic link file (i.e., <i>newpath</i> becomes a symbolic link to the same file that <i>oldpath</i> refers to). Some other implementations behave in the same manner as Linux. POSIX.1-2008 changes the specification of <code>link</code>(), making it implementation-dependent whether or not <i>oldpath</i> is dereferenced if it is a symbolic link. For precise control over the treatment of symbolic links when creating a link, use <code>linkat</code>().</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>linkat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>link</code>(), unless the <code>AT_SYMLINK_FOLLOW</code> is specified. When <i>oldpath</i> and <i>newpath</i> are relative pathnames, glibc constructs pathnames based on the symbolic links in <i>/proc/self/fd</i> that correspond to the <i>olddirfd</i> and <i>newdirfd</i> arguments.</p>
<h2>BUGS</h2>
<p> On NFS filesystems, the return code may be wrong in case the NFS server performs the link creation and dies before it can say so. Use <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) to find out if the link got created.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
