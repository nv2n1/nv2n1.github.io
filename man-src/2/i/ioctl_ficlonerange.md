---
title: "ioctl_ficlonerange(2)"
name: "ioctl_ficlonerange"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_ficlonerange/"
description: "ioctl_ficlonerange, ioctl_ficlone – share some the data of one file with another file"
---

<h2 class="name">NAME</h2>
<p> ioctl_ficlonerange, ioctl_ficlone &#8211; share some the data of one file with another file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ioctl.h&gt;</code><br />
 <code>#include &lt;linux/fs.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>dest_fd</i><code>, FICLONERANGE, struct file_clone_range *</code><i>arg</i><code>);</code><br />
 <code>int ioctl(int </code><i>dest_fd</i><code>, FICLONE, int </code><i>src_fd</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> If a filesystem supports files sharing physical storage between multiple files (&quot;reflink&quot;), this <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation can be used to make some of the data in the <i>src_fd</i> file appear in the <i>dest_fd</i> file by sharing the underlying storage, which is faster than making a separate physical copy of the data. Both files must reside within the same filesystem. If a file write should occur to a shared region, the filesystem must ensure that the changes remain private to the file being written. This behavior is commonly referred to as &quot;copy on write&quot;. </p>
<p> This ioctl reflinks up to <i>src_length</i> bytes from file descriptor <i>src_fd</i> at offset <i>src_offset</i> into the file <i>dest_fd</i> at offset <i>dest_offset</i>, provided that both are files. If <i>src_length</i> is zero, the ioctl reflinks to the end of the source file. This information is conveyed in a structure of the following form: </p>
<p> struct file_clone_range {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 src_fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 src_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 src_length;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 dest_offset; }; </p>
<p> Clones are atomic with regards to concurrent writes, so no locks need to be taken to obtain a consistent cloned copy. </p>
<p> The <code>FICLONE</code> ioctl clones entire files.</p>
<h2>RETURN VALUE</h2>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> Error codes can be one of, but are not limited to, the following:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>src_fd</i> is not open for reading; <i>dest_fd</i> is not open for writing or is open for append-only writes; or the filesystem which <i>src_fd</i> resides on does not support reflink.</p>
<dt><code>EINVAL</code></p>
<dd> The filesystem does not support reflinking the ranges of the given files. This error can also appear if either file descriptor represents a device, FIFO, or socket. Disk filesystems generally require the offset and length arguments to be aligned to the fundamental block size. XFS and Btrfs do not support overlapping reflink ranges in the same file.</p>
<dt><code>EISDIR</code></p>
<dd> One of the files is a directory and the filesystem does not support shared regions in directories.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> This can appear if the filesystem does not support reflinking either file descriptor, or if either file descriptor refers to special inodes.</p>
<dt><code>EPERM</code></p>
<dd> <i>dest_fd</i> is immutable.</p>
<dt><code>ETXTBSY</code></p>
<dd> One of the files is a swap file. Swap files cannot share storage.</p>
<dt><code>EXDEV</code></p>
<dd> <i>dest_fd</i> and <i>src_fd</i> are not on the same mounted filesystem.</dl>
<h2>VERSIONS</h2>
<p> These ioctl operations first appeared in Linux 4.5. They were previously known as <code>BTRFS_IOC_CLONE</code> and <code>BTRFS_IOC_CLONE_RANGE</code>, and were private to Btrfs.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific.</p>
<h2>NOTES</h2>
<p> Because a copy-on-write operation requires the allocation of new storage, the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) operation may unshare shared blocks to guarantee that subsequent writes will not fail because of lack of disk space.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
