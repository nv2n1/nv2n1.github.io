---
title: "renameat(2)"
name: "renameat"
section: "2"
letter: "r"
url: "/docs/linux/man/2-renameat/"
description: "rename, renameat, renameat2 – change the name or location of a file"
---

<h2 class="name">NAME</h2>
<p> rename, renameat, renameat2 &#8211; change the name or location of a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
int rename(const char *oldpath, const char *newpath);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;stdio.h&gt;
int renameat(int olddirfd, const char *oldpath,
             int newdirfd, const char *newpath);
int renameat2(int olddirfd, const char *oldpath,
              int newdirfd, const char *newpath, unsigned int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>renameat</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _ATFILE_SOURCE</dl>
</dl>
<p> <code>renameat2</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>_GNU_SOURCE</p>
<dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>rename</code>() renames a file, moving it between directories if required. Any other hard links to the file (as created using <code><a href="/docs/linux/man/2-link/">link</a></code>(2)) are unaffected. Open file descriptors for <i>oldpath</i> are also unaffected. </p>
<p> Various restrictions determine whether or not the rename operation succeeds: see ERRORS below. </p>
<p> If <i>newpath</i> already exists, it will be atomically replaced, so that there is no point at which another process attempting to access <i>newpath</i> will find it missing. However, there will probably be a window in which both <i>oldpath</i> and <i>newpath</i> refer to the file being renamed. </p>
<p> If <i>oldpath</i> and <i>newpath</i> are existing hard links referring to the same file, then <code>rename</code>() does nothing, and returns a success status. </p>
<p> If <i>newpath</i> exists but the operation fails for some reason, <code>rename</code>() guarantees to leave an instance of <i>newpath</i> in place. </p>
<p> <i>oldpath</i> can specify a directory. In this case, <i>newpath</i> must either not exist, or it must specify an empty directory. </p>
<p> If <i>oldpath</i> refers to a symbolic link, the link is renamed; if <i>newpath</i> refers to a symbolic link, the link will be overwritten.</p>
<h3>renameat()</h3>
<p> The <code>renameat</code>() system call operates in exactly the same way as <code>rename</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>oldpath</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>olddirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>rename</code>() for a relative pathname). </p>
<p> If <i>oldpath</i> is relative and <i>olddirfd</i> is the special value <code>AT_FDCWD</code>, then <i>oldpath</i> is interpreted relative to the current working directory of the calling process (like <code>rename</code>()). </p>
<p> If <i>oldpath</i> is absolute, then <i>olddirfd</i> is ignored. </p>
<p> The interpretation of <i>newpath</i> is as for <i>oldpath</i>, except that a relative pathname is interpreted relative to the directory referred to by the file descriptor <i>newdirfd</i>. </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>renameat</code>().</p>
<h3>renameat2()</h3>
<p> <code>renameat2</code>() has an additional <i>flags</i> argument. A <code>renameat2</code>() call with a zero <i>flags</i> argument is equivalent to <code>renameat</code>(). </p>
<p> The <i>flags</i> argument is a bit mask consisting of zero or more of the following flags:</p>
<dl>
<dt><code>RENAME_EXCHANGE</code></p>
<dd> Atomically exchange <i>oldpath</i> and <i>newpath</i>. Both pathnames must exist but may be of different types (e.g., one could be a non-empty directory and the other a symbolic link).</p>
<dt><code>RENAME_NOREPLACE</code></p>
<dd> Don&#8217;t overwrite <i>newpath</i> of the rename. Return an error if <i>newpath</i> already exists.</p>
<dt>
<dd> <code>RENAME_NOREPLACE</code> can&#8217;t be employed together with <code>RENAME_EXCHANGE</code>.</p>
<dt>
<dd> <code>RENAME_NOREPLACE</code> requires support from the underlying filesystem. Support for various filesystems was added as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> ext4 (Linux 3.15);</p>
<dt>*</p>
<dd> btrfs, shmem, and cifs (Linux 3.17);</p>
<dt>*</p>
<dd> xfs (Linux 4.0);</p>
<dt>*</p>
<dd> Support for many other filesystems was added in Linux 4.9, including ext2, minix, reiserfs, jfs, vfat, and bpf.</dl>
</dl>
<dt><code>RENAME_WHITEOUT</code> (since Linux 3.18)</p>
<dd> This operation makes sense only for overlay/union filesystem implementations.</p>
<dt>
<dd> Specifying <code>RENAME_WHITEOUT</code> creates a &quot;whiteout&quot; object at the source of the rename at the same time as performing the rename. The whole operation is atomic, so that if the rename succeeds then the whiteout will also have been created.</p>
<dt>
<dd> A &quot;whiteout&quot; is an object that has special meaning in union/overlay filesystem constructs. In these constructs, multiple layers exist and only the top one is ever modified. A whiteout on an upper layer will effectively hide a matching file in the lower layer, making it appear as if the file didn&#8217;t exist.</p>
<dt>
<dd> When a file that exists on the lower layer is renamed, the file is first copied up (if not already on the upper layer) and then renamed on the upper, read-write layer. At the same time, the source file needs to be &quot;whiteouted&quot; (so that the version of the source file in the lower layer is rendered invisible). The whole operation needs to be done atomically.</p>
<dt>
<dd> When not part of a union/overlay, the whiteout appears as a character device with a {0,0} device number. (Note that other union/overlay implementations may employ different methods for storing whiteout entries; specifically, BSD union mount employs a separate inode type, <code>DT_WHT</code>, which, while supported by some filesystems available in Linux, such as CODA and XFS, is ignored by the kernel&#8217;s whiteout support code, as of Linux 4.19, at least.)</p>
<dt>
<dd> <code>RENAME_WHITEOUT</code> requires the same privileges as creating a device node (i.e., the <code>CAP_MKNOD</code> capability).</p>
<dt>
<dd> <code>RENAME_WHITEOUT</code> can&#8217;t be employed together with <code>RENAME_EXCHANGE</code>.</p>
<dt>
<dd> <code>RENAME_WHITEOUT</code> requires support from the underlying filesystem. Among the filesystems that provide that support are tmpfs (since Linux 3.18), ext4 (since Linux 3.18), XFS (since Linux 4.1), f2fs (since Linux 4.2), btrfs (since Linux 4.7), and ubifs (since Linux 4.9).</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write permission is denied for the directory containing <i>oldpath</i> or <i>newpath</i>, or, search permission is denied for one of the directories in the path prefix of <i>oldpath</i> or <i>newpath</i>, or <i>oldpath</i> is a directory and does not allow write permission (needed to update the <i>..</i> entry). (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBUSY</code></p>
<dd> The rename fails because <i>oldpath</i> or <i>newpath</i> is a directory that is in use by some process (perhaps as current working directory, or as root directory, or because it was open for reading) or is in use by the system (for example as mount point), while the system considers this an error. (Note that there is no requirement to return <code>EBUSY</code> in such cases&#8212;there is nothing wrong with doing the rename anyway&#8212;but it is allowed to return <code>EBUSY</code> if the system cannot otherwise handle such situations.)</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks on the filesystem has been exhausted.</p>
<dt><code>EFAULT</code></p>
<dd> <i>oldpath</i> or <i>newpath</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The new pathname contained a path prefix of the old, or, more generally, an attempt was made to make a directory a subdirectory of itself.</p>
<dt><code>EISDIR</code></p>
<dd> <i>newpath</i> is an existing directory, but <i>oldpath</i> is not a directory.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>oldpath</i> or <i>newpath</i>.</p>
<dt><code>EMLINK</code></p>
<dd> <i>oldpath</i> already has the maximum number of links to it, or it was a directory and the directory containing <i>newpath</i> has the maximum number of links.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>oldpath</i> or <i>newpath</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> The link named by <i>oldpath</i> does not exist; or, a directory component in <i>newpath</i> does not exist; or, <i>oldpath</i> or <i>newpath</i> is an empty string.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing the file has no room for the new directory entry.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>oldpath</i> or <i>newpath</i> is not, in fact, a directory. Or, <i>oldpath</i> is a directory, and <i>newpath</i> exists but is not a directory.</p>
<dt><code>ENOTEMPTY</code> or <code>EEXIST</code></p>
<dd> <i>newpath</i> is a nonempty directory, that is, contains entries other than &quot;.&quot; and &quot;..&quot;.</p>
<dt><code>EPERM</code> or <code>EACCES</code></p>
<dd> The directory containing <i>oldpath</i> has the sticky bit (<code>S_ISVTX</code>) set and the process&#8217;s effective user ID is neither the user ID of the file to be deleted nor that of the directory containing it, and the process is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability); or <i>newpath</i> is an existing file and the directory containing it has the sticky bit set and the process&#8217;s effective user ID is neither the user ID of the file to be replaced nor that of the directory containing it, and the process is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability); or the filesystem containing <i>pathname</i> does not support renaming of the type requested.</p>
<dt><code>EROFS</code></p>
<dd> The file is on a read-only filesystem.</p>
<dt><code>EXDEV</code></p>
<dd> <i>oldpath</i> and <i>newpath</i> are not on the same mounted filesystem. (Linux permits a filesystem to be mounted at multiple points, but <code>rename</code>() does not work across different mount points, even if the same filesystem is mounted on both.)</dl>
<p> The following additional errors can occur for <code>renameat</code>() and <code>renameat2</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>olddirfd</i> or <i>newdirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>oldpath</i> is relative and <i>olddirfd</i> is a file descriptor referring to a file other than a directory; or similar for <i>newpath</i> and <i>newdirfd</i></dl>
<p> The following additional errors can occur for <code>renameat2</code>():</p>
<dl>
<dt><code>EEXIST</code></p>
<dd> <i>flags</i> contains <code>RENAME_NOREPLACE</code> and <i>newpath</i> already exists.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid flag was specified in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>RENAME_NOREPLACE</code> and <code>RENAME_EXCHANGE</code> were specified in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> Both <code>RENAME_WHITEOUT</code> and <code>RENAME_EXCHANGE</code> were specified in <i>flags</i>.</p>
<dt><code>EINVAL</code></p>
<dd> The filesystem does not support one of the flags in <i>flags</i>.</p>
<dt><code>ENOENT</code></p>
<dd> <i>flags</i> contains <code>RENAME_EXCHANGE</code> and <i>newpath</i> does not exist.</p>
<dt><code>EPERM</code></p>
<dd> <code>RENAME_WHITEOUT</code> was specified in <i>flags</i>, but the caller does not have the <code>CAP_MKNOD</code> capability.</dl>
<h2>VERSIONS</h2>
<p> <code>renameat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4. </p>
<p> <code>renameat2</code>() was added to Linux in kernel 3.15; library support was added in glibc 2.28.</p>
<h2>CONFORMING TO</h2>
<p> <code>rename</code>(): 4.3BSD, C89, C99, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>renameat</code>(): POSIX.1-2008. </p>
<p> <code>renameat2</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> On older kernels where <code>renameat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>rename</code>(). When <i>oldpath</i> and <i>newpath</i> are relative pathnames, glibc constructs pathnames based on the symbolic links in <i>/proc/self/fd</i> that correspond to the <i>olddirfd</i> and <i>newdirfd</i> arguments.</p>
<h2>BUGS</h2>
<p> On NFS filesystems, you can not assume that if the operation failed, the file was not renamed. If the server does the rename operation and then crashes, the retransmitted RPC which will be processed when the server is up again causes a failure. The application is expected to deal with this. See <code><a href="/docs/linux/man/2-link/">link</a></code>(2) for a similar problem.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1), <code><a href="/docs/linux/man/1-rename/">rename</a></code>(1), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
