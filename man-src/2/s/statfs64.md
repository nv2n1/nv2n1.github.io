---
title: "statfs64(2)"
name: "statfs64"
section: "2"
letter: "s"
url: "/docs/linux/man/2-statfs64/"
description: "statfs, fstatfs – get filesystem statistics"
---

<h2 class="name">NAME</h2>
<p> statfs, fstatfs &#8211; get filesystem statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/vfs.h&gt; </code>/* or &lt;sys/statfs.h&gt; */ </p>
<p> <code>int statfs(const char *</code><i>path</i><code>, struct statfs *</code><i>buf</i><code>);</code><br />
 <code>int fstatfs(int </code><i>fd</i><code>, struct statfs *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>statfs</code>() system call returns information about a mounted filesystem. <i>path</i> is the pathname of any file within the mounted filesystem. <i>buf</i> is a pointer to a <i>statfs</i> structure defined approximately as follows: </p>
<p> struct statfs {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type of filesystem&nbsp;(see below)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_bsize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Optimal transfer block size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t f_blocks;&nbsp;<wbr>&nbsp;/*&nbsp;Total data blocks in filesystem&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t f_bfree;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Free blocks in filesystem&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsblkcnt_t f_bavail;&nbsp;<wbr>&nbsp;/*&nbsp;Free blocks available to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unprivileged user&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsfilcnt_t f_files;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Total inodes in filesystem&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsfilcnt_t f_ffree;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Free inodes in filesystem&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fsid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f_fsid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Filesystem ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_namelen;&nbsp;/*&nbsp;Maximum length of filenames&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_frsize;&nbsp;<wbr>&nbsp;/*&nbsp;Fragment size&nbsp;(since Linux 2.6)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Mount flags of filesystem<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(since Linux 2.6.36)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__fsword_t f_spare[xxx];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Padding bytes reserved for future use&nbsp;*/ }; </p>
<p> The following filesystem types may appear in <i>f_type</i>: </p>
<p> ADFS_SUPER_MAGIC 0xadf5 AFFS_SUPER_MAGIC 0xadff AFS_SUPER_MAGIC 0x5346414f ANON_INODE_FS_MAGIC 0x09041934 /* Anonymous inode FS (for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pseudofiles that have no name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e.g., epoll, signalfd, bpf)&nbsp;*/ AUTOFS_SUPER_MAGIC 0x0187 BDEVFS_MAGIC 0x62646576 BEFS_SUPER_MAGIC 0x42465331 BFS_MAGIC 0x1badface BINFMTFS_MAGIC 0x42494e4d BPF_FS_MAGIC 0xcafe4a11 BTRFS_SUPER_MAGIC 0x9123683e BTRFS_TEST_MAGIC 0x73727279 CGROUP_SUPER_MAGIC 0x27e0eb /* Cgroup pseudo FS */ CGROUP2_SUPER_MAGIC 0x63677270 /* Cgroup v2 pseudo FS */ CIFS_MAGIC_NUMBER 0xff534d42 CODA_SUPER_MAGIC 0x73757245 COH_SUPER_MAGIC 0x012ff7b7 CRAMFS_MAGIC 0x28cd3d45 DEBUGFS_MAGIC 0x64626720 DEVFS_SUPER_MAGIC 0x1373 /* Linux 2.6.17 and earlier */ DEVPTS_SUPER_MAGIC 0x1cd1 ECRYPTFS_SUPER_MAGIC 0xf15f EFIVARFS_MAGIC 0xde5e81e4 EFS_SUPER_MAGIC 0x00414a53 EXT_SUPER_MAGIC 0x137d /* Linux 2.0 and earlier */ EXT2_OLD_SUPER_MAGIC 0xef51 EXT2_SUPER_MAGIC 0xef53 EXT3_SUPER_MAGIC 0xef53 EXT4_SUPER_MAGIC 0xef53 F2FS_SUPER_MAGIC 0xf2f52010 FUSE_SUPER_MAGIC 0x65735546 FUTEXFS_SUPER_MAGIC 0xbad1dea /* Unused */ HFS_SUPER_MAGIC 0x4244 HOSTFS_SUPER_MAGIC 0x00c0ffee HPFS_SUPER_MAGIC 0xf995e849 HUGETLBFS_MAGIC 0x958458f6 ISOFS_SUPER_MAGIC 0x9660 JFFS2_SUPER_MAGIC 0x72b6 JFS_SUPER_MAGIC 0x3153464a MINIX_SUPER_MAGIC 0x137f /* original minix FS */ MINIX_SUPER_MAGIC2 0x138f /* 30 char minix FS */ MINIX2_SUPER_MAGIC 0x2468 /* minix V2 FS */ MINIX2_SUPER_MAGIC2 0x2478 /* minix V2 FS, 30 char names */ MINIX3_SUPER_MAGIC 0x4d5a /* minix V3 FS, 60 char names */ MQUEUE_MAGIC 0x19800202 /* POSIX message queue FS */ MSDOS_SUPER_MAGIC 0x4d44 MTD_INODE_FS_MAGIC 0x11307854 NCP_SUPER_MAGIC 0x564c NFS_SUPER_MAGIC 0x6969 NILFS_SUPER_MAGIC 0x3434 NSFS_MAGIC 0x6e736673 NTFS_SB_MAGIC 0x5346544e OCFS2_SUPER_MAGIC 0x7461636f OPENPROM_SUPER_MAGIC 0x9fa1 OVERLAYFS_SUPER_MAGIC 0x794c7630 PIPEFS_MAGIC 0x50495045 PROC_SUPER_MAGIC 0x9fa0 /* /proc FS */ PSTOREFS_MAGIC 0x6165676c QNX4_SUPER_MAGIC 0x002f QNX6_SUPER_MAGIC 0x68191122 RAMFS_MAGIC 0x858458f6 REISERFS_SUPER_MAGIC 0x52654973 ROMFS_MAGIC 0x7275 SECURITYFS_MAGIC 0x73636673 SELINUX_MAGIC 0xf97cff8c SMACK_MAGIC 0x43415d53 SMB_SUPER_MAGIC 0x517b SMB2_MAGIC_NUMBER 0xfe534d42 SOCKFS_MAGIC 0x534f434b SQUASHFS_MAGIC 0x73717368 SYSFS_MAGIC 0x62656572 SYSV2_SUPER_MAGIC 0x012ff7b6 SYSV4_SUPER_MAGIC 0x012ff7b5 TMPFS_MAGIC 0x01021994 TRACEFS_MAGIC 0x74726163 UDF_SUPER_MAGIC 0x15013346 UFS_MAGIC 0x00011954 USBDEVICE_SUPER_MAGIC 0x9fa2 V9FS_MAGIC 0x01021997 VXFS_SUPER_MAGIC 0xa501fcf5 XENFS_SUPER_MAGIC 0xabba1974 XENIX_SUPER_MAGIC 0x012ff7b4 XFS_SUPER_MAGIC 0x58465342 _XIAFS_SUPER_MAGIC 0x012fd16d /* Linux 2.0 and earlier */ </p>
<p> Most of these MAGIC constants are defined in <i>/usr/include/linux/magic.h</i>, and some are hardcoded in kernel sources. </p>
<p> The <i>f_flags</i> field is a bit mask indicating mount options for the filesystem. It contains zero or more of the following bits:</p>
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
<dd> Writes are synched to the filesystem immediately (see the description of <code>O_SYNC</code> in <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<dt><code>ST_NOSYMFOLLOW</code> (since Linux 5.10)</p>
<dd> Symbolic links are not followed when resolving paths; see <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2).</dl>
<p> Nobody knows what <i>f_fsid</i> is supposed to contain (but see below). </p>
<p> Fields that are undefined for a particular filesystem are set to 0. </p>
<p> <code>fstatfs</code>() returns the same information about an open file referenced by descriptor <i>fd</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> (<code>statfs</code>()) Search permission is denied for a component of the path prefix of <i>path</i>. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EBADF</code></p>
<dd> (<code>fstatfs</code>()) <i>fd</i> is not a valid open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> or <i>path</i> points to an invalid address.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred while reading from the filesystem.</p>
<dt><code>ELOOP</code></p>
<dd> (<code>statfs</code>()) Too many symbolic links were encountered in translating <i>path</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> (<code>statfs</code>()) <i>path</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> (<code>statfs</code>()) The file referred to by <i>path</i> does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSYS</code></p>
<dd> The filesystem does not support this call.</p>
<dt><code>ENOTDIR</code></p>
<dd> (<code>statfs</code>()) A component of the path prefix of <i>path</i> is not a directory.</p>
<dt><code>EOVERFLOW</code></p>
<dd> Some values were too large to be represented in the returned struct.</dl>
<h2>CONFORMING TO</h2>
<p> Linux-specific. The Linux <code>statfs</code>() was inspired by the 4.4BSD one (but they do not use the same structure).</p>
<h2>NOTES</h2>
<p> The <i>__fsword_t</i> type used for various fields in the <i>statfs</i> structure definition is a glibc internal type, not intended for public use. This leaves the programmer in a bit of a conundrum when trying to copy or compare these fields to local variables in a program. Using <i>unsigned int</i> for such variables suffices on most systems. </p>
<p> The original Linux <code>statfs</code>() and <code>fstatfs</code>() system calls were not designed with extremely large file sizes in mind. Subsequently, Linux 2.6 added new <code>statfs64</code>() and <code>fstatfs64</code>() system calls that employ a new structure, <i>statfs64</i>. The new structure contains the same fields as the original <i>statfs</i> structure, but the sizes of various fields are increased, to accommodate large file sizes. The glibc <code>statfs</code>() and <code>fstatfs</code>() wrapper functions transparently deal with the kernel differences. </p>
<p> Some systems have only <i>&lt;sys/vfs.h&gt;</i>, other systems also have <i>&lt;sys/statfs.h&gt;</i>, where the former includes the latter. So it seems including the former is the best choice. </p>
<p> LSB has deprecated the library calls <code>statfs</code>() and <code>fstatfs</code>() and tells us to use <code><a href="/docs/linux/man/2-statvfs/">statvfs</a></code>(2) and <code><a href="/docs/linux/man/2-fstatvfs/">fstatvfs</a></code>(2) instead.</p>
<h3>The f_fsid field</h3>
<p> Solaris, Irix and POSIX have a system call <code><a href="/docs/linux/man/2-statvfs/">statvfs</a></code>(2) that returns a <i>struct statvfs</i> (defined in <i>&lt;sys/statvfs.h&gt;</i>) containing an <i>unsigned long</i> <i>f_fsid</i>. Linux, SunOS, HP-UX, 4.4BSD have a system call <code>statfs</code>() that returns a <i>struct statfs</i> (defined in <i>&lt;sys/vfs.h&gt;</i>) containing a <i>fsid_t</i> <i>f_fsid</i>, where <i>fsid_t</i> is defined as <i>struct { int val[2]; }</i>. The same holds for FreeBSD, except that it uses the include file <i>&lt;sys/mount.h&gt;</i>. </p>
<p> The general idea is that <i>f_fsid</i> contains some random stuff such that the pair (<i>f_fsid</i>,<i>ino</i>) uniquely determines a file. Some operating systems use (a variation on) the device number, or the device number combined with the filesystem type. Several operating systems restrict giving out the <i>f_fsid</i> field to the superuser only (and zero it for unprivileged users), because this field is used in the filehandle of the filesystem when NFS-exported, and giving it out is a security concern. </p>
<p> Under some operating systems, the <i>fsid</i> can be used as the second argument to the <code><a href="/docs/linux/man/2-sysfs/">sysfs</a></code>(2) system call.</p>
<h2>BUGS</h2>
<p> From Linux 2.6.38 up to and including Linux 3.1, <code>fstatfs</code>() failed with the error <code>ENOSYS</code> for file descriptors created by <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-statvfs/">statvfs</a></code>(3), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
