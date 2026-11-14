---
title: "symlink(2)"
name: "symlink"
section: "2"
letter: "s"
url: "/docs/linux/man/2-symlink/"
description: "symlink, symlinkat – make a new name for a file"
---

<h2 class="name">NAME</h2>
<p> symlink, symlinkat &#8211; make a new name for a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int symlink(const char *target, const char *linkpath);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
int symlinkat(const char *target, int newdirfd, const char *linkpath);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>symlink</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>symlinkat</code>():</p>
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
<p> <code>symlink</code>() creates a symbolic link named <i>linkpath</i> which contains the string <i>target</i>. </p>
<p> Symbolic links are interpreted at run time as if the contents of the link had been substituted into the path being followed to find a file or directory. </p>
<p> Symbolic links may contain <i>..</i> path components, which (if used at the start of the link) refer to the parent directories of that in which the link resides. </p>
<p> A symbolic link (also known as a soft link) may point to an existing file or to a nonexistent one; the latter case is known as a dangling link. </p>
<p> The permissions of a symbolic link are irrelevant; the ownership is ignored when following the link, but is checked when removal or renaming of the link is requested and the link is in a directory with the sticky bit (<code>S_ISVTX</code>) set. </p>
<p> If <i>linkpath</i> exists, it will <i>not</i> be overwritten.</p>
<h3>symlinkat()</h3>
<p> The <code>symlinkat</code>() system call operates in exactly the same way as <code>symlink</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>linkpath</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>newdirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>symlink</code>() for a relative pathname). </p>
<p> If <i>linkpath</i> is relative and <i>newdirfd</i> is the special value <code>AT_FDCWD</code>, then <i>linkpath</i> is interpreted relative to the current working directory of the calling process (like <code>symlink</code>()). </p>
<p> If <i>linkpath</i> is absolute, then <i>newdirfd</i> is ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write access to the directory containing <i>linkpath</i> is denied, or one of the directories in the path prefix of <i>linkpath</i> did not allow search permission. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of resources on the filesystem has been exhausted. The resources could be inodes or disk blocks, depending on the filesystem implementation.</p>
<dt><code>EEXIST</code></p>
<dd> <i>linkpath</i> already exists.</p>
<dt><code>EFAULT</code></p>
<dd> <i>target</i> or <i>linkpath</i> points outside your accessible address space.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>linkpath</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>target</i> or <i>linkpath</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>linkpath</i> does not exist or is a dangling symbolic link, or <i>target</i> or <i>linkpath</i> is an empty string.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The device containing the file has no room for the new directory entry.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>linkpath</i> is not, in fact, a directory.</p>
<dt><code>EPERM</code></p>
<dd> The filesystem containing <i>linkpath</i> does not support the creation of symbolic links.</p>
<dt><code>EROFS</code></p>
<dd> <i>linkpath</i> is on a read-only filesystem.</dl>
<p> The following additional errors can occur for <code>symlinkat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>newdirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOENT</code></p>
<dd> <i>linkpath</i> is a relative pathname and <i>newdirfd</i> refers to a directory that has been deleted.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>linkpath</i> is relative and <i>newdirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>symlinkat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>symlink</code>(): SVr4, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>symlinkat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> No checking of <i>target</i> is done. </p>
<p> Deleting the name referred to by a symbolic link will actually delete the file (unless it also has other hard links). If this behavior is not desired, use <code><a href="/docs/linux/man/2-link/">link</a></code>(2).</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>symlinkat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>symlink</code>(). When <i>linkpath</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>newdirfd</i> argument.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), <code><a href="/docs/linux/man/1-namei/">namei</a></code>(1), <code><a href="/docs/linux/man/2-lchown/">lchown</a></code>(2), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
