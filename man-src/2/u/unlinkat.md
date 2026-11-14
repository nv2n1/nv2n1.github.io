---
title: "unlinkat(2)"
name: "unlinkat"
section: "2"
letter: "u"
url: "/docs/linux/man/2-unlinkat/"
description: "unlink, unlinkat – delete a name and possibly the file it refers to"
---

<h2 class="name">NAME</h2>
<p> unlink, unlinkat &#8211; delete a name and possibly the file it refers to </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int unlink(const char *pathname);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
int unlinkat(int dirfd, const char *pathname, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>unlinkat</code>():</p>
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
<p> <code>unlink</code>() deletes a name from the filesystem. If that name was the last link to a file and no processes have the file open, the file is deleted and the space it was using is made available for reuse. </p>
<p> If the name was the last link to a file but any processes still have the file open, the file will remain in existence until the last file descriptor referring to it is closed. </p>
<p> If the name referred to a symbolic link, the link is removed. </p>
<p> If the name referred to a socket, FIFO, or device, the name for it is removed but processes which have the object open may continue to use it.</p>
<h3>unlinkat()</h3>
<p> The <code>unlinkat</code>() system call operates in exactly the same way as either <code>unlink</code>() or <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) (depending on whether or not <i>flags</i> includes the <code>AT_REMOVEDIR</code> flag) except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>unlink</code>() and <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) for a relative pathname). </p>
<p> If the pathname given in <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>unlink</code>() and <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2)). </p>
<p> If the pathname given in <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> <i>flags</i> is a bit mask that can either be specified as 0, or by ORing together flag values that control the operation of <code>unlinkat</code>(). Currently, only one such flag is defined:</p>
<dl>
<dt><code>AT_REMOVEDIR</code></p>
<dd> By default, <code>unlinkat</code>() performs the equivalent of <code>unlink</code>() on <i>pathname</i>. If the <code>AT_REMOVEDIR</code> flag is specified, then performs the equivalent of <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) on <i>pathname</i>.</dl>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>unlinkat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write access to the directory containing <i>pathname</i> is not allowed for the process&#8217;s effective UID, or one of the directories in <i>pathname</i> did not allow search permission. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBUSY</code></p>
<dd> The file <i>pathname</i> cannot be unlinked because it is being used by the system or another process; for example, it is a mount point or the NFS client software created it to represent an active but otherwise nameless inode (&quot;NFS silly renamed&quot;).</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>EISDIR</code></p>
<dd> <i>pathname</i> refers to a directory. (This is the non-POSIX value returned by Linux since 2.1.132.)</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in translating <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A component in <i>pathname</i> does not exist or is a dangling symbolic link, or <i>pathname</i> is empty.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory.</p>
<dt><code>EPERM</code></p>
<dd> The system does not allow unlinking of directories, or unlinking of directories requires privileges that the calling process doesn&#8217;t have. (This is the POSIX prescribed error return; as noted above, Linux returns <code>EISDIR</code> for this case.)</p>
<dt><code>EPERM</code> (Linux only)</p>
<dd> The filesystem does not allow unlinking of files.</p>
<dt><code>EPERM</code> or <code>EACCES</code></p>
<dd> The directory containing <i>pathname</i> has the sticky bit (<code>S_ISVTX</code>) set and the process&#8217;s effective UID is neither the UID of the file to be deleted nor that of the directory containing it, and the process is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability).</p>
<dt><code>EPERM</code></p>
<dd> The file to be unlinked is marked immutable or append-only. (See <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2).)</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a file on a read-only filesystem.</dl>
<p> The same errors that occur for <code>unlink</code>() and <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) can also occur for <code>unlinkat</code>(). The following additional errors can occur for <code>unlinkat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid flag value was specified in <i>flags</i>.</p>
<dt><code>EISDIR</code></p>
<dd> <i>pathname</i> refers to a directory, and <code>AT_REMOVEDIR</code> was not specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>unlinkat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>unlink</code>(): SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>unlinkat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<h3>Glibc notes</h3>
<p> On older kernels where <code>unlinkat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>unlink</code>() or <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h2>BUGS</h2>
<p> Infelicities in the protocol underlying NFS can cause the unexpected disappearance of files which are still being used.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1), <code><a href="/docs/linux/man/1-unlink/">unlink</a></code>(1), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2), <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/3-remove/">remove</a></code>(3), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
