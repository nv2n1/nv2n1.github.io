---
title: "ioctl_iflags(2)"
name: "ioctl_iflags"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_iflags/"
description: "ioctl_iflags – ioctl() operations for inode flags"
---

<h2 class="name">NAME</h2>
<p> ioctl_iflags &#8211; ioctl() operations for inode flags </p>
<h2>DESCRIPTION</h2>
<p> Various Linux filesystems support the notion of <i>inode flags</i>&#8212;attributes that modify the semantics of files and directories. These flags can be retrieved and modified using two <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations: </p>
<p> int attr; fd = open(&quot;pathname&quot;, &#8230;); </p>
<p> ioctl(fd, FS_IOC_GETFLAGS, &amp;attr); /* Place current flags<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in&nbsp;&#8216;attr&#8217;&nbsp;*/ attr |= FS_NOATIME_FL; /* Tweak returned bit mask */ ioctl(fd, FS_IOC_SETFLAGS, &amp;attr); /* Update flags for inode<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;referred to by&nbsp;&#8216;fd&#8217;&nbsp;*/ </p>
<p> The <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1) and <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) shell commands provide interfaces to these two operations, allowing a user to view and modify the inode flags associated with a file. </p>
<p> The following flags are supported (shown along with the corresponding letter used to indicate the flag by <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1) and <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)):</p>
<dl>
<dt><code>FS_APPEND_FL</code> &#8216;a&#8217;</p>
<dd> The file can be opened only with the <code>O_APPEND</code> flag. (This restriction applies even to the superuser.) Only a privileged process (<code>CAP_LINUX_IMMUTABLE</code>) can set or clear this attribute.</p>
<dt><code>FS_COMPR_FL</code> &#8216;c&#8217;</p>
<dd> Store the file in a compressed format on disk. This flag is <i>not</i> supported by most of the mainstream filesystem implementations; one exception is <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5).</p>
<dt><code>FS_DIRSYNC_FL</code> &#8216;D&#8217; (since Linux 2.6.0)</p>
<dd> Write directory changes synchronously to disk. This flag provides semantics equivalent to the <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) <code>MS_DIRSYNC</code> option, but on a per-directory basis. This flag can be applied only to directories.</p>
<dt><code>FS_IMMUTABLE_FL</code> &#8216;i&#8217;</p>
<dd> The file is immutable: no changes are permitted to the file contents or metadata (permissions, timestamps, ownership, link count and so on). (This restriction applies even to the superuser.) Only a privileged process (<code>CAP_LINUX_IMMUTABLE</code>) can set or clear this attribute.</p>
<dt><code>FS_JOURNAL_DATA_FL</code> &#8216;j&#8217;</p>
<dd> Enable journaling of file data on <code><a href="/docs/linux/man/5-ext3/">ext3</a></code>(5) and <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5) filesystems. On a filesystem that is journaling in <i>ordered</i> or <i>writeback</i> mode, a privileged (<code>CAP_SYS_RESOURCE</code>) process can set this flag to enable journaling of data updates on a per-file basis.</p>
<dt><code>FS_NOATIME_FL</code> &#8216;A&#8217;</p>
<dd> Don&#8217;t update the file last access time when the file is accessed. This can provide I/O performance benefits for applications that do not care about the accuracy of this timestamp. This flag provides functionality similar to the <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) <code>MS_NOATIME</code> flag, but on a per-file basis.</p>
<dt><code>FS_NOCOW_FL</code> &#8216;C&#8217; (since Linux 2.6.39)</p>
<dd> The file will not be subject to copy-on-write updates. This flag has an effect only on filesystems that support copy-on-write semantics, such as Btrfs. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) and <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5).</p>
<dt><code>FS_NODUMP_FL</code> &#8216;d&#8217;</p>
<dd> Don&#8217;t include this file in backups made using <code><a href="/docs/linux/man/8-dump/">dump</a></code>(8).</p>
<dt><code>FS_NOTAIL_FL</code> &#8216;t&#8217;</p>
<dd> This flag is supported only on Reiserfs. It disables the Reiserfs tail-packing feature, which tries to pack small files (and the final fragment of larger files) into the same disk block as the file metadata.</p>
<dt><code>FS_PROJINHERIT_FL</code> &#8216;P&#8217; (since Linux 4.5)</p>
<dd> Inherit the quota project ID. Files and subdirectories will inherit the project ID of the directory. This flag can be applied only to directories.</p>
<dt><code>FS_SECRM_FL</code> &#8216;s&#8217;</p>
<dd> Mark the file for secure deletion. This feature is not implemented by any filesystem, since the task of securely erasing a file from a recording medium is surprisingly difficult.</p>
<dt><code>FS_SYNC_FL</code> &#8216;S&#8217;</p>
<dd> Make file updates synchronous. For files, this makes all writes synchronous (as though all opens of the file were with the <code>O_SYNC</code> flag). For directories, this has the same effect as the <code>FS_DIRSYNC_FL</code> flag.</p>
<dt><code>FS_TOPDIR_FL</code> &#8216;T&#8217;</p>
<dd> Mark a directory for special treatment under the Orlov block-allocation strategy. See <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1) for details. This flag can be applied only to directories and has an effect only for ext2, ext3, and ext4.</p>
<dt><code>FS_UNRM_FL</code> &#8216;u&#8217;</p>
<dd> Allow the file to be undeleted if it is deleted. This feature is not implemented by any filesystem, since it is possible to implement file-recovery mechanisms outside the kernel.</dl>
<p> In most cases, when any of the above flags is set on a directory, the flag is inherited by files and subdirectories created inside that directory. Exceptions include <code>FS_TOPDIR_FL</code>, which is not inheritable, and <code>FS_DIRSYNC_FL</code>, which is inherited only by subdirectories.</p>
<h2>CONFORMING TO</h2>
<p> Inode flags are a nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> In order to change the inode flags of a file using the <code>FS_IOC_SETFLAGS</code> operation, the effective user ID of the caller must match the owner of the file, or the caller must have the <code>CAP_FOWNER</code> capability. </p>
<p> The type of the argument given to the <code>FS_IOC_GETFLAGS</code> and <code>FS_IOC_SETFLAGS</code> operations is <i>int&nbsp;*</i>, notwithstanding the implication in the kernel source file <i>include/uapi/linux/fs.h</i> that the argument is <i>long&nbsp;*</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1), <code><a href="/docs/linux/man/1-lsattr/">lsattr</a></code>(1), <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2), <code><a href="/docs/linux/man/5-btrfs/">btrfs</a></code>(5), <code><a href="/docs/linux/man/5-ext4/">ext4</a></code>(5), <code><a href="/docs/linux/man/5-xfs/">xfs</a></code>(5), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
