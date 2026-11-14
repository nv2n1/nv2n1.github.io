---
title: "fstatvfs(3)"
name: "fstatvfs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fstatvfs/"
description: "statvfs, fstatvfs – get filesystem statistics"
---

<h2 class="name">NAME</h2>
<p> statvfs, fstatvfs &#8211; get filesystem statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/statvfs.h&gt;</code> </p>
<p> <code>int statvfs(const char *</code><i>path</i><code>, struct statvfs *</code><i>buf</i><code>);</code><br />
 <code>int fstatvfs(int </code><i>fd</i><code>, struct statvfs *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The function <code>statvfs</code>() returns information about a mounted filesystem. <i>path</i> is the pathname of any file within the mounted filesystem. <i>buf</i> is a pointer to a <i>statvfs</i> structure defined approximately as follows: </p>
<p> struct statvfs {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;f_bsize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Filesystem block size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;f_frsize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Fragment size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_blocks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of fs in f_frsize units&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_bfree;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_bavail;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free blocks for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unprivileged users&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsfilcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_files;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsfilcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_ffree;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsfilcnt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_favail;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of free inodes for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unprivileged users&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;f_fsid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Filesystem ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;f_flag;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mount flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;f_namemax;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum filename length&nbsp;*/ }; </p>
<p> Here the types <i>fsblkcnt_t</i> and <i>fsfilcnt_t</i> are defined in <i>&lt;sys/types.h&gt;</i>. Both used to be <i>unsigned long</i>. </p>
<p> The field <i>f_flag</i> is a bit mask indicating various options that were employed when mounting this filesystem. It contains zero or more of the following flags:</p>
<dl>
<dt><code>ST_MANDLOCK</code></p>
<dd> Mandatory locking is permitted on the filesystem (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</p>
<dt><code>ST_NOATIME</code></p>
<dd> Do not update access times; see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).</p>
<dt><code>ST_NODEV</code></p>
<dd> Disallow access to device special files on this filesystem.</p>
<dt><code>ST_NODIRATIME</code></p>
<dd> Do not update directory access times; see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).</p>
<dt><code>ST_NOEXEC</code></p>
<dd> Execution of programs is disallowed on this filesystem.</p>
<dt><code>ST_NOSUID</code></p>
<dd> The set-user-ID and set-group-ID bits are ignored by <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) for executable files on this filesystem</p>
<dt><code>ST_RDONLY</code></p>
<dd> This filesystem is mounted read-only.</p>
<dt><code>ST_RELATIME</code></p>
<dd> Update atime relative to mtime/ctime; see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).</p>
<dt><code>ST_SYNCHRONOUS</code></p>
<dd> Writes are synched to the filesystem immediately (see the description of <code>O_SYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</dl>
<p> It is unspecified whether all members of the returned struct have meaningful values on all filesystems. </p>
<p> <code>fstatvfs</code>() returns the same information about an open file referenced by descriptor <i>fd</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> (<code>statvfs</code>()) Search permission is denied for a component of the path prefix of <i>path</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBADF</code></p>
<dd> (<code>fstatvfs</code>()) <i>fd</i> is not a valid open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>Buf</i> or <i>path</i> points to an invalid address.</p>
<dt><code>EINTR</code></p>
<dd> This call was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred while reading from the filesystem.</p>
<dt><code>ELOOP</code></p>
<dd> (<code>statvfs</code>()) Too many symbolic links were encountered in translating <i>path</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> (<code>statvfs</code>()) <i>path</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> (<code>statvfs</code>()) The file referred to by <i>path</i> does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSYS</code></p>
<dd> The filesystem does not support this call.</p>
<dt><code>ENOTDIR</code></p>
<dd> (<code>statvfs</code>()) A component of the path prefix of <i>path</i> is not a directory.</p>
<dt><code>EOVERFLOW</code></p>
<dd> Some values were too large to be represented in the returned struct.</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>statvfs</code>(), <code>fstatvfs</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> Only the <code>ST_NOSUID</code> and <code>ST_RDONLY</code> flags of the <i>f_flag</i> field are specified in POSIX.1. To obtain definitions of the remaining flags, one must define <code>_GNU_SOURCE</code>.</p>
<h2>NOTES</h2>
<p> The Linux kernel has system calls <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) and <code><a href="/docs/linux/man/2-fstatfs/">fstatfs</a></code>(2) to support this library call. </p>
<p> In glibc versions before 2.13, <code>statvfs</code>() populated the bits of the <i>f_flag</i> field by scanning the mount options shown in <i>/proc/mounts</i>. However, starting with Linux 2.6.36, the underlying <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) system call provides the necessary information via the <i>f_flags</i> field, and since glibc version 2.13, the <code>statvfs</code>() function will use information from that field rather than scanning <i>/proc/mounts</i>. </p>
<p> The glibc implementations of </p>
<p> pathconf(path, _PC_REC_XFER_ALIGN); pathconf(path, _PC_ALLOC_SIZE_MIN); pathconf(path, _PC_REC_MIN_XFER_SIZE); </p>
<p> respectively use the <i>f_frsize</i>, <i>f_frsize</i>, and <i>f_bsize</i> fields returned by a call to <code>statvfs</code>() with the argument <i>path</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
