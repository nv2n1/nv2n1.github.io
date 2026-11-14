---
title: "lstat64(2)"
name: "lstat64"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lstat64/"
description: "stat, fstat, lstat, fstatat – get file status"
---

<h2 class="name">NAME</h2>
<p> stat, fstat, lstat, fstatat &#8211; get file status </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
int stat(const char *pathname, struct stat *statbuf);
int fstat(int fd, struct stat *statbuf);
int lstat(const char *pathname, struct stat *statbuf);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int fstatat(int dirfd, const char *pathname, struct stat *statbuf,
            int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>lstat</code>():</p>
<dl>
<dt>
<dd> /* glibc 2.19 and earlier */ _BSD_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.20&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.10:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<p> <code>fstatat</code>():</p>
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
<p> These functions return information about a file, in the buffer pointed to by <i>statbuf</i>. No permissions are required on the file itself, but&#8212;in the case of <code>stat</code>(), <code>fstatat</code>(), and <code>lstat</code>()&#8212;execute (search) permission is required on all of the directories in <i>pathname</i> that lead to the file. </p>
<p> <code>stat</code>() and <code>fstatat</code>() retrieve information about the file pointed to by <i>pathname</i>; the differences for <code>fstatat</code>() are described below. </p>
<p> <code>lstat</code>() is identical to <code>stat</code>(), except that if <i>pathname</i> is a symbolic link, then it returns information about the link itself, not the file that the link refers to. </p>
<p> <code>fstat</code>() is identical to <code>stat</code>(), except that the file about which information is to be retrieved is specified by the file descriptor <i>fd</i>.</p>
<h3>The stat structure</h3>
<p> All of these system calls return a <i>stat</i> structure, which contains the following fields: </p>
<p> struct stat {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_dev;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ID of device containing file&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ino_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File type and mode&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nlink_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_nlink;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of hard links&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User ID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Group ID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_rdev;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Device ID&nbsp;(if special file)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Total size, in bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blksize_t st_blksize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Block size for filesystem I/O&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blkcnt_t&nbsp;<wbr>&nbsp;st_blocks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of 512B blocks allocated&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Since Linux 2.6, the kernel supports nanosecond<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;precision for the following timestamp fields.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;For the details before Linux 2.6, see NOTES.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec st_atim;&nbsp;<wbr>&nbsp;/*&nbsp;Time of last access&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec st_mtim;&nbsp;<wbr>&nbsp;/*&nbsp;Time of last modification&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec st_ctim;&nbsp;<wbr>&nbsp;/*&nbsp;Time of last status change&nbsp;*/ </p>
<p> #define st_atime st_atim.tv_sec /* Backward compatibility */ #define st_mtime st_mtim.tv_sec #define st_ctime st_ctim.tv_sec }; </p>
<p> <i>Note</i>: the order of fields in the <i>stat</i> structure varies somewhat across architectures. In addition, the definition above does not show the padding bytes that may be present between some fields on various architectures. Consult the glibc and kernel source code if you need to know the details. </p>
<p> <i>Note</i>: for performance and simplicity reasons, different fields in the <i>stat</i> structure may contain state information from different moments during the execution of the system call. For example, if <i>st_mode</i> or <i>st_uid</i> is changed by another process by calling <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2) or <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code>stat</code>() might return the old <i>st_mode</i> together with the new <i>st_uid</i>, or the old <i>st_uid</i> together with the new <i>st_mode</i>. </p>
<p> The fields in the <i>stat</i> structure are as follows:</p>
<dl>
<dt><i>st_dev</i></p>
<dd> This field describes the device on which this file resides. (The <code><a href="/docs/linux/man/3-major/">major</a></code>(3) and <code><a href="/docs/linux/man/3-minor/">minor</a></code>(3) macros may be useful to decompose the device ID in this field.)</p>
<dt><i>st_ino</i></p>
<dd> This field contains the file&#8217;s inode number.</p>
<dt><i>st_mode</i></p>
<dd> This field contains the file type and mode. See <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7) for further information.</p>
<dt><i>st_nlink</i></p>
<dd> This field contains the number of hard links to the file.</p>
<dt><i>st_uid</i></p>
<dd> This field contains the user ID of the owner of the file.</p>
<dt><i>st_gid</i></p>
<dd> This field contains the ID of the group owner of the file.</p>
<dt><i>st_rdev</i></p>
<dd> This field describes the device that this file (inode) represents.</p>
<dt><i>st_size</i></p>
<dd> This field gives the size of the file (if it is a regular file or a symbolic link) in bytes. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.</p>
<dt><i>st_blksize</i></p>
<dd> This field gives the &quot;preferred&quot; block size for efficient filesystem I/O.</p>
<dt><i>st_blocks</i></p>
<dd> This field indicates the number of blocks allocated to the file, in 512-byte units. (This may be smaller than <i>st_size</i>/512 when the file has holes.)</p>
<dt><i>st_atime</i></p>
<dd> This is the time of the last access of file data.</p>
<dt><i>st_mtime</i></p>
<dd> This is the time of last modification of file data.</p>
<dt><i>st_ctime</i></p>
<dd> This is the file&#8217;s last status change timestamp (time of last change to the inode).</dl>
<p> For further information on the above fields, see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7).</p>
<h3>fstatat()</h3>
<p> The <code>fstatat</code>() system call is a more general interface for accessing file information which can still provide exactly the behavior of each of <code>stat</code>(), <code>lstat</code>(), and <code>fstat</code>(). </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>stat</code>() and <code>lstat</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>stat</code>() and <code>lstat</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> <i>flags</i> can either be 0, or include one or more of the following flags ORed:</p>
<dl>
<dt><code>AT_EMPTY_PATH</code> (since Linux 2.6.39)</p>
<dd> If <i>pathname</i> is an empty string, operate on the file referred to by <i>dirfd</i> (which may have been obtained using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_PATH</code> flag). In this case, <i>dirfd</i> can refer to any type of file, not just a directory, and the behavior of <code>fstatat</code>() is similar to that of <code>fstat</code>(). If <i>dirfd</i> is <code>AT_FDCWD</code>, the call operates on the current working directory. This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_NO_AUTOMOUNT</code> (since Linux 2.6.38)</p>
<dd> Don&#8217;t automount the terminal (&quot;basename&quot;) component of <i>pathname</i> if it is a directory that is an automount point. This allows the caller to gather attributes of an automount point (rather than the location it would mount). Since Linux 4.14, also don&#8217;t instantiate a nonexistent name in an on-demand directory such as used for automounter indirect maps. This flag has no effect if the mount point has already been mounted over.</p>
<dt>
<dd> Both <code>stat</code>() and <code>lstat</code>() act as though <code>AT_NO_AUTOMOUNT</code> was set.</p>
<dt>
<dd> The <code>AT_NO_AUTOMOUNT</code> can be used in tools that scan directories to prevent mass-automounting of a directory of automount points.</p>
<dt>
<dd> This flag is Linux-specific; define <code>_GNU_SOURCE</code> to obtain its definition.</p>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If <i>pathname</i> is a symbolic link, do not dereference it: instead return information about the link itself, like <code>lstat</code>(). (By default, <code>fstatat</code>() dereferences symbolic links, like <code>stat</code>().)</dl>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>fstatat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied for one of the directories in the path prefix of <i>pathname</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> Bad address.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links encountered while traversing the path.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> A component of <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOENT</code></p>
<dd> <i>pathname</i> is an empty string and <code>AT_EMPTY_PATH</code> was not specified in <i>flags</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory (i.e., kernel memory).</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix of <i>pathname</i> is not a directory.</p>
<dt><code>EOVERFLOW</code></p>
<dd> <i>pathname</i> or <i>fd</i> refers to a file whose size, inode number, or number of blocks cannot be represented in, respectively, the types <i>off_t</i>, <i>ino_t</i>, or <i>blkcnt_t</i>. This error can occur when, for example, an application compiled on a 32-bit platform without <i>-D_FILE_OFFSET_BITS=64</i> calls <code>stat</code>() on a file whose size exceeds <i>(1&lt;&lt;31)-1</i> bytes.</dl>
<p> The following additional errors can occur for <code>fstatat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>fstatat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>stat</code>(), <code>fstat</code>(), <code>lstat</code>(): SVr4, 4.3BSD, POSIX.1-2001, POSIX.1.2008. </p>
<p> <code>fstatat</code>(): POSIX.1-2008. </p>
<p> According to POSIX.1-2001, <code>lstat</code>() on a symbolic link need return valid information only in the <i>st_size</i> field and the file type of the <i>st_mode</i> field of the <i>stat</i> structure. POSIX.1-2008 tightens the specification, requiring <code>lstat</code>() to return valid information in all fields except the mode bits in <i>st_mode</i>. </p>
<p> Use of the <i>st_blocks</i> and <i>st_blksize</i> fields may be less portable. (They were introduced in BSD. The interpretation differs between systems, and possibly on a single system when NFS mounts are involved.)</p>
<h2>NOTES</h2>
<h3>Timestamp fields</h3>
<p> Older kernels and older standards did not support nanosecond timestamp fields. Instead, there were three timestamp fields&#8212;<i>st_atime</i>, <i>st_mtime</i>, and <i>st_ctime</i>&#8212;typed as <i>time_t</i> that recorded timestamps with one-second precision. </p>
<p> Since kernel 2.5.48, the <i>stat</i> structure supports nanosecond resolution for the three file timestamp fields. The nanosecond components of each timestamp are available via names of the form <i>st_atim.tv_nsec</i>, if suitable feature test macros are defined. Nanosecond timestamps were standardized in POSIX.1-2008, and, starting with version 2.12, glibc exposes the nanosecond component names if <code>_POSIX_C_SOURCE</code> is defined with the value 200809L or greater, or <code>_XOPEN_SOURCE</code> is defined with the value 700 or greater. Up to and including glibc 2.19, the definitions of the nanoseconds components are also defined if <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> is defined. If none of the aforementioned macros are defined, then the nanosecond values are exposed with names of the form <i>st_atimensec</i>.</p>
<h3>C library/kernel differences</h3>
<p> Over time, increases in the size of the <i>stat</i> structure have led to three successive versions of <code>stat</code>(): <i>sys_stat</i>() (slot <i>__NR_oldstat</i>), <i>sys_newstat</i>() (slot <i>__NR_stat</i>), and <i>sys_stat64()</i> (slot <i>__NR_stat64</i>) on 32-bit platforms such as i386. The first two versions were already present in Linux 1.0 (albeit with different names); the last was added in Linux 2.4. Similar remarks apply for <code>fstat</code>() and <code>lstat</code>(). </p>
<p> The kernel-internal versions of the <i>stat</i> structure dealt with by the different versions are, respectively:</p>
<dl>
<dt><i>__old_kernel_stat</i></p>
<dd> The original structure, with rather narrow fields, and no padding.</p>
<dt><i>stat</i></p>
<dd> Larger <i>st_ino</i> field and padding added to various parts of the structure to allow for future expansion.</p>
<dt><i>stat64</i></p>
<dd> Even larger <i>st_ino</i> field, larger <i>st_uid</i> and <i>st_gid</i> fields to accommodate the Linux-2.4 expansion of UIDs and GIDs to 32 bits, and various other enlarged fields and further padding in the structure. (Various padding bytes were eventually consumed in Linux 2.6, with the advent of 32-bit device IDs and nanosecond components for the timestamp fields.)</dl>
<p> The glibc <code>stat</code>() wrapper function hides these details from applications, invoking the most recent version of the system call provided by the kernel, and repacking the returned information if required for old binaries. </p>
<p> On modern 64-bit systems, life is simpler: there is a single <code>stat</code>() system call and the kernel deals with a <i>stat</i> structure that contains fields of a sufficient size. </p>
<p> The underlying system call employed by the glibc <code>fstatat</code>() wrapper function is actually called <code>fstatat64</code>() or, on some architectures, <code>newfstatat</code>().</p>
<h2>EXAMPLES</h2>
<p> The following program calls <code>lstat</code>() and displays selected fields in the returned <i>stat</i> structure. </p>
<p> #include &lt;sys/types.h&gt; #include &lt;sys/stat.h&gt; #include &lt;stdint.h&gt; #include &lt;time.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/sysmacros.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat sb; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;pathname&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(lstat(argv[1],&nbsp;&amp;sb)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;lstat&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;ID of containing device:&nbsp;<wbr>&nbsp;[%jx,%jx]
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;major(sb.st_dev),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;minor(sb.st_dev)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;File type:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(sb.st_mode&nbsp;&amp;&nbsp;S_IFMT)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFBLK:&nbsp;<wbr>&nbsp;printf(&quot;block device
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFCHR:&nbsp;<wbr>&nbsp;printf(&quot;character device
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFDIR:&nbsp;<wbr>&nbsp;printf(&quot;directory
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFIFO:&nbsp;<wbr>&nbsp;printf(&quot;FIFO/pipe
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFLNK:&nbsp;<wbr>&nbsp;printf(&quot;symlink
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFREG:&nbsp;<wbr>&nbsp;printf(&quot;regular file
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case S_IFSOCK: printf(&quot;socket
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;unknown?
&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;I-node number:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%ju
&quot;,&nbsp;(uintmax_t)&nbsp;sb.st_ino); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Mode:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jo&nbsp;(octal)
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;sb.st_mode); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Link count:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%ju
&quot;,&nbsp;(uintmax_t)&nbsp;sb.st_nlink);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Ownership:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UID=%ju&nbsp;<wbr>&nbsp;<wbr>&nbsp;GID=%ju
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;sb.st_uid,&nbsp;(uintmax_t)&nbsp;sb.st_gid); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Preferred I/O block size:&nbsp;%jd bytes
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;sb.st_blksize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;File size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jd bytes
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;sb.st_size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Blocks allocated:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jd
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(intmax_t)&nbsp;sb.st_blocks); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Last status change:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s&quot;, ctime(&amp;sb.st_ctime));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Last file access:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s&quot;, ctime(&amp;sb.st_atime));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Last file modification:&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s&quot;, ctime(&amp;sb.st_mtime)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-stat/">stat</a></code>(1), <code><a href="/docs/linux/man/2-access/">access</a></code>(2), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/2-statx/">statx</a></code>(2), <code><a href="/docs/linux/man/2-utime/">utime</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
