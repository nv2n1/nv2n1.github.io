---
title: "fallocate(2)"
name: "fallocate"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fallocate/"
description: "fallocate – manipulate file space"
---

<h2 class="name">NAME</h2>
<p> fallocate &#8211; manipulate file space </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
int fallocate(int fd, int mode, off_t offset, off_t len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a nonportable, Linux-specific system call. For the portable, POSIX.1-specified method of ensuring that space is allocated for a file, see <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3). </p>
<p> <code>fallocate</code>() allows the caller to directly manipulate the allocated disk space for the file referred to by <i>fd</i> for the byte range starting at <i>offset</i> and continuing for <i>len</i> bytes. </p>
<p> The <i>mode</i> argument determines the operation to be performed on the given range. Details of the supported operations are given in the subsections below.</p>
<h3>Allocating disk space</h3>
<p> The default operation (i.e., <i>mode</i> is zero) of <code>fallocate</code>() allocates the disk space within the range specified by <i>offset</i> and <i>len</i>. The file size (as reported by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)) will be changed if <i>offset</i>+<i>len</i> is greater than the file size. Any subregion within the range specified by <i>offset</i> and <i>len</i> that did not contain data before the call will be initialized to zero. This default behavior closely resembles the behavior of the <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3) library function, and is intended as a method of optimally implementing that function. </p>
<p> After a successful call, subsequent writes into the range specified by <i>offset</i> and <i>len</i> are guaranteed not to fail because of lack of disk space. </p>
<p> If the <code>FALLOC_FL_KEEP_SIZE</code> flag is specified in <i>mode</i>, the behavior of the call is similar, but the file size will not be changed even if <i>offset</i>+<i>len</i> is greater than the file size. Preallocating zeroed blocks beyond the end of the file in this manner is useful for optimizing append workloads. </p>
<p> If the <code>FALLOC_FL_UNSHARE</code> flag is specified in <i>mode</i>, shared file data extents will be made private to the file to guarantee that a subsequent write will not fail due to lack of space. Typically, this will be done by performing a copy-on-write operation on all shared data in the file. This flag may not be supported by all filesystems. </p>
<p> Because allocation is done in block size chunks, <code>fallocate</code>() may allocate a larger range of disk space than was specified.</p>
<h3>Deallocating file space</h3>
<p> Specifying the <code>FALLOC_FL_PUNCH_HOLE</code> flag (available since Linux 2.6.38) in <i>mode</i> deallocates space (i.e., creates a hole) in the byte range starting at <i>offset</i> and continuing for <i>len</i> bytes. Within the specified range, partial filesystem blocks are zeroed, and whole filesystem blocks are removed from the file. After a successful call, subsequent reads from this range will return zeros. </p>
<p> The <code>FALLOC_FL_PUNCH_HOLE</code> flag must be ORed with <code>FALLOC_FL_KEEP_SIZE</code> in <i>mode</i>; in other words, even when punching off the end of the file, the file size (as reported by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)) does not change. </p>
<p> Not all filesystems support <code>FALLOC_FL_PUNCH_HOLE</code>; if a filesystem doesn&#8217;t support the operation, an error is returned. The operation is supported on at least the following filesystems:</p>
<dl>
<dt>*</p>
<dd> XFS (since Linux 2.6.38)</p>
<dt>*</p>
<dd> ext4 (since Linux 3.0)</p>
<dt>*</p>
<dd> Btrfs (since Linux 3.7)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) (since Linux 3.5)</p>
<dt>*</p>
<dd> <code><a href="/docs/linux/man/5-gfs2/">gfs2</a></code>(5) (since Linux 4.16)</dl>
<h3>Collapsing file space</h3>
<p> Specifying the <code>FALLOC_FL_COLLAPSE_RANGE</code> flag (available since Linux 3.15) in <i>mode</i> removes a byte range from a file, without leaving a hole. The byte range to be collapsed starts at <i>offset</i> and continues for <i>len</i> bytes. At the completion of the operation, the contents of the file starting at the location <i>offset+len</i> will be appended at the location <i>offset</i>, and the file will be <i>len</i> bytes smaller. </p>
<p> A filesystem may place limitations on the granularity of the operation, in order to ensure efficient implementation. Typically, <i>offset</i> and <i>len</i> must be a multiple of the filesystem logical block size, which varies according to the filesystem type and configuration. If a filesystem has such a requirement, <code>fallocate</code>() fails with the error <code>EINVAL</code> if this requirement is violated. </p>
<p> If the region specified by <i>offset</i> plus <i>len</i> reaches or passes the end of file, an error is returned; instead, use <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2) to truncate a file. </p>
<p> No other flags may be specified in <i>mode</i> in conjunction with <code>FALLOC_FL_COLLAPSE_RANGE</code>. </p>
<p> As at Linux 3.15, <code>FALLOC_FL_COLLAPSE_RANGE</code> is supported by ext4 (only for extent-based files) and XFS.</p>
<h3>Zeroing file space</h3>
<p> Specifying the <code>FALLOC_FL_ZERO_RANGE</code> flag (available since Linux 3.15) in <i>mode</i> zeros space in the byte range starting at <i>offset</i> and continuing for <i>len</i> bytes. Within the specified range, blocks are preallocated for the regions that span the holes in the file. After a successful call, subsequent reads from this range will return zeros. </p>
<p> Zeroing is done within the filesystem preferably by converting the range into unwritten extents. This approach means that the specified range will not be physically zeroed out on the device (except for partial blocks at the either end of the range), and I/O is (otherwise) required only to update metadata. </p>
<p> If the <code>FALLOC_FL_KEEP_SIZE</code> flag is additionally specified in <i>mode</i>, the behavior of the call is similar, but the file size will not be changed even if <i>offset</i>+<i>len</i> is greater than the file size. This behavior is the same as when preallocating space with <code>FALLOC_FL_KEEP_SIZE</code> specified. </p>
<p> Not all filesystems support <code>FALLOC_FL_ZERO_RANGE</code>; if a filesystem doesn&#8217;t support the operation, an error is returned. The operation is supported on at least the following filesystems:</p>
<dl>
<dt>*</p>
<dd> XFS (since Linux 3.15)</p>
<dt>*</p>
<dd> ext4, for extent-based files (since Linux 3.15)</p>
<dt>*</p>
<dd> SMB3 (since Linux 3.17)</p>
<dt>*</p>
<dd> Btrfs (since Linux 4.16)</dl>
<h3>Increasing file space</h3>
<p> Specifying the <code>FALLOC_FL_INSERT_RANGE</code> flag (available since Linux 4.1) in <i>mode</i> increases the file space by inserting a hole within the file size without overwriting any existing data. The hole will start at <i>offset</i> and continue for <i>len</i> bytes. When inserting the hole inside file, the contents of the file starting at <i>offset</i> will be shifted upward (i.e., to a higher file offset) by <i>len</i> bytes. Inserting a hole inside a file increases the file size by <i>len</i> bytes. </p>
<p> This mode has the same limitations as <code>FALLOC_FL_COLLAPSE_RANGE</code> regarding the granularity of the operation. If the granularity requirements are not met, <code>fallocate</code>() fails with the error <code>EINVAL</code>. If the <i>offset</i> is equal to or greater than the end of file, an error is returned. For such operations (i.e., inserting a hole at the end of file), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2) should be used. </p>
<p> No other flags may be specified in <i>mode</i> in conjunction with <code>FALLOC_FL_INSERT_RANGE</code>. </p>
<p> <code>FALLOC_FL_INSERT_RANGE</code> requires filesystem support. Filesystems that support this operation include XFS (since Linux 4.1) and ext4 (since Linux 4.2).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>fallocate</code>() returns zero. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor, or is not opened for writing.</p>
<dt><code>EFBIG</code></p>
<dd> <i>offset</i>+<i>len</i> exceeds the maximum file size.</p>
<dt><code>EFBIG</code></p>
<dd> <i>mode</i> is <code>FALLOC_FL_INSERT_RANGE</code>, and the current file size+<i>len</i> exceeds the maximum file size.</p>
<dt><code>EINTR</code></p>
<dd> A signal was caught during execution; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>offset</i> was less than 0, or <i>len</i> was less than or equal to 0.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is <code>FALLOC_FL_COLLAPSE_RANGE</code> and the range specified by <i>offset</i> plus <i>len</i> reaches or passes the end of the file.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is <code>FALLOC_FL_INSERT_RANGE</code> and the range specified by <i>offset</i> reaches or passes the end of the file.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code>, but either <i>offset</i> or <i>len</i> is not a multiple of the filesystem block size.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> contains one of <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code> and also other flags; no other flags are permitted with <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_ZERO_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code>, but the file referred to by <i>fd</i> is not a regular file.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred while reading from or writing to a filesystem.</p>
<dt><code>ENODEV</code></p>
<dd> <i>fd</i> does not refer to a regular file or a directory. (If <i>fd</i> is a pipe or FIFO, a different error results.)</p>
<dt><code>ENOSPC</code></p>
<dd> There is not enough space left on the device containing the file referred to by <i>fd</i>.</p>
<dt><code>ENOSYS</code></p>
<dd> This kernel does not implement <code>fallocate</code>().</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The filesystem containing the file referred to by <i>fd</i> does not support this operation; or the <i>mode</i> is not supported by the filesystem containing the file referred to by <i>fd</i>.</p>
<dt><code>EPERM</code></p>
<dd> The file referred to by <i>fd</i> is marked immutable (see <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)).</p>
<dt><code>EPERM</code></p>
<dd> <i>mode</i> specifies <code>FALLOC_FL_PUNCH_HOLE</code> or <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code> and the file referred to by <i>fd</i> is marked append-only (see <code><a href="/docs/linux/man/1-chattr/">chattr</a></code>(1)).</p>
<dt><code>EPERM</code></p>
<dd> The operation was prevented by a file seal; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>ESPIPE</code></p>
<dd> <i>fd</i> refers to a pipe or FIFO.</p>
<dt><code>ETXTBSY</code></p>
<dd> <i>mode</i> specifies <code>FALLOC_FL_COLLAPSE_RANGE</code> or <code>FALLOC_FL_INSERT_RANGE</code>, but the file referred to by <i>fd</i> is currently being executed.</dl>
<h2>VERSIONS</h2>
<p> <code>fallocate</code>() is available on Linux since kernel 2.6.23. Support is provided by glibc since version 2.10. The <code>FALLOC_FL_*</code> flags are defined in glibc headers only since version 2.18.</p>
<h2>CONFORMING TO</h2>
<p> <code>fallocate</code>() is Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fallocate/">fallocate</a></code>(1), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/3-posix_fadvise/">posix_fadvise</a></code>(3), <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
