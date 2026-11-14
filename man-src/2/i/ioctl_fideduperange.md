---
title: "ioctl_fideduperange(2)"
name: "ioctl_fideduperange"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_fideduperange/"
description: "ioctl_fideduperange – share some the data of one file with another file"
---

<h2 class="name">NAME</h2>
<p> ioctl_fideduperange &#8211; share some the data of one file with another file </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ioctl.h&gt;</code><br />
 <code>#include &lt;linux/fs.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>src_fd</i><code>, FIDEDUPERANGE, struct file_dedupe_range *</code><i>arg</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> If a filesystem supports files sharing physical storage between multiple files, this <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation can be used to make some of the data in the <code>src_fd</code> file appear in the <code>dest_fd</code> file by sharing the underlying storage if the file data is identical (&quot;deduplication&quot;). Both files must reside within the same filesystem. This reduces storage consumption by allowing the filesystem to store one shared copy of the data. If a file write should occur to a shared region, the filesystem must ensure that the changes remain private to the file being written. This behavior is commonly referred to as &quot;copy on write&quot;. </p>
<p> This ioctl performs the &quot;compare and share if identical&quot; operation on up to <i>src_length</i> bytes from file descriptor <i>src_fd</i> at offset <i>src_offset</i>. This information is conveyed in a structure of the following form: </p>
<p> struct file_dedupe_range {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 src_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 src_length;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 dest_count;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 reserved1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 reserved2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct file_dedupe_range_info info[0]; }; </p>
<p> Deduplication is atomic with regards to concurrent writes, so no locks need to be taken to obtain a consistent deduplicated copy. </p>
<p> The fields <i>reserved1</i> and <i>reserved2</i> must be zero. </p>
<p> Destinations for the deduplication operation are conveyed in the array at the end of the structure. The number of destinations is given in <i>dest_count</i>, and the destination information is conveyed in the following form: </p>
<p> struct file_dedupe_range_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 dest_fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 dest_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 bytes_deduped;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s32 status;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 reserved; }; </p>
<p> Each deduplication operation targets <i>src_length</i> bytes in file descriptor <i>dest_fd</i> at offset <i>dest_offset</i>. The field <i>reserved</i> must be zero. During the call, <i>src_fd</i> must be open for reading and <i>dest_fd</i> must be open for writing. The combined size of the struct <i>file_dedupe_range</i> and the struct <i>file_dedupe_range_info</i> array must not exceed the system page size. The maximum size of <i>src_length</i> is filesystem dependent and is typically 16 MiB. This limit will be enforced silently by the filesystem. By convention, the storage used by <i>src_fd</i> is mapped into <i>dest_fd</i> and the previous contents in <i>dest_fd</i> are freed. </p>
<p> Upon successful completion of this ioctl, the number of bytes successfully deduplicated is returned in <i>bytes_deduped</i> and a status code for the deduplication operation is returned in <i>status</i>. If even a single byte in the range does not match, the deduplication request will be ignored and <i>status</i> set to <code>FILE_DEDUPE_RANGE_DIFFERS</code>. The <i>status</i> code is set to <code>FILE_DEDUPE_RANGE_SAME</code> for success, a negative error code in case of error, or <code>FILE_DEDUPE_RANGE_DIFFERS</code> if the data did not match.</p>
<h2>RETURN VALUE</h2>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> Error codes can be one of, but are not limited to, the following:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>src_fd</i> is not open for reading; <i>dest_fd</i> is not open for writing or is open for append-only writes; or the filesystem which <i>src_fd</i> resides on does not support deduplication.</p>
<dt><code>EINVAL</code></p>
<dd> The filesystem does not support deduplicating the ranges of the given files. This error can also appear if either file descriptor represents a device, FIFO, or socket. Disk filesystems generally require the offset and length arguments to be aligned to the fundamental block size. Neither Btrfs nor XFS support overlapping deduplication ranges in the same file.</p>
<dt><code>EISDIR</code></p>
<dd> One of the files is a directory and the filesystem does not support shared regions in directories.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel was unable to allocate sufficient memory to perform the operation or <i>dest_count</i> is so large that the input argument description spans more than a single page of memory.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> This can appear if the filesystem does not support deduplicating either file descriptor, or if either file descriptor refers to special inodes.</p>
<dt><code>EPERM</code></p>
<dd> <i>dest_fd</i> is immutable.</p>
<dt><code>ETXTBSY</code></p>
<dd> One of the files is a swap file. Swap files cannot share storage.</p>
<dt><code>EXDEV</code></p>
<dd> <i>dest_fd</i> and <i>src_fd</i> are not on the same mounted filesystem.</dl>
<h2>VERSIONS</h2>
<p> This ioctl operation first appeared in Linux 4.5. It was previously known as <code>BTRFS_IOC_FILE_EXTENT_SAME</code> and was private to Btrfs.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific.</p>
<h2>NOTES</h2>
<p> Because a copy-on-write operation requires the allocation of new storage, the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) operation may unshare shared blocks to guarantee that subsequent writes will not fail because of lack of disk space. </p>
<p> Some filesystems may limit the amount of data that can be deduplicated in a single call.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
