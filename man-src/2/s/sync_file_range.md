---
title: "sync_file_range(2)"
name: "sync_file_range"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sync_file_range/"
description: "sync_file_range – sync a file segment with disk"
---

<h2 class="name">NAME</h2>
<p> sync_file_range &#8211; sync a file segment with disk </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
int sync_file_range(int fd, off64_t offset, off64_t nbytes,
                    unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>sync_file_range</code>() permits fine control when synchronizing the open file referred to by the file descriptor <i>fd</i> with disk. </p>
<p> <i>offset</i> is the starting byte of the file range to be synchronized. <i>nbytes</i> specifies the length of the range to be synchronized, in bytes; if <i>nbytes</i> is zero, then all bytes from <i>offset</i> through to the end of file are synchronized. Synchronization is in units of the system page size: <i>offset</i> is rounded down to a page boundary; <i>(offset+nbytes-1)</i> is rounded up to a page boundary. </p>
<p> The <i>flags</i> bit-mask argument can include any of the following values:</p>
<dl>
<dt><code>SYNC_FILE_RANGE_WAIT_BEFORE</code></p>
<dd> Wait upon write-out of all pages in the specified range that have already been submitted to the device driver for write-out before performing any write.</p>
<dt><code>SYNC_FILE_RANGE_WRITE</code></p>
<dd> Initiate write-out of all dirty pages in the specified range which are not presently submitted write-out. Note that even this may block if you attempt to write more than request queue size.</p>
<dt><code>SYNC_FILE_RANGE_WAIT_AFTER</code></p>
<dd> Wait upon write-out of all pages in the range after performing any write.</dl>
<p> Specifying <i>flags</i> as 0 is permitted, as a no-op.</p>
<h3>Warning</h3>
<p> This system call is extremely dangerous and should not be used in portable programs. None of these operations writes out the file&#8217;s metadata. Therefore, unless the application is strictly performing overwrites of already-instantiated disk blocks, there are no guarantees that the data will be available after a crash. There is no user interface to know if a write is purely an overwrite. On filesystems using copy-on-write semantics (e.g., <i>btrfs</i>) an overwrite of existing allocated blocks is impossible. When writing into preallocated space, many filesystems also require calls into the block allocator, which this system call does not sync out to disk. This system call does not flush disk write caches and thus does not provide any data integrity on systems with volatile disk write caches.</p>
<h3>Some details</h3>
<p> <code>SYNC_FILE_RANGE_WAIT_BEFORE</code> and <code>SYNC_FILE_RANGE_WAIT_AFTER</code> will detect any I/O errors or <code>ENOSPC</code> conditions and will return these to the caller. </p>
<p> Useful combinations of the <i>flags</i> bits are:</p>
<dl>
<dt><code>SYNC_FILE_RANGE_WAIT_BEFORE | SYNC_FILE_RANGE_WRITE</code></p>
<dd> Ensures that all pages in the specified range which were dirty when <code>sync_file_range</code>() was called are placed under write-out. This is a start-write-for-data-integrity operation.</p>
<dt><code>SYNC_FILE_RANGE_WRITE</code></p>
<dd> Start write-out of all dirty pages in the specified range which are not presently under write-out. This is an asynchronous flush-to-disk operation. This is not suitable for data integrity operations.</p>
<dt><code>SYNC_FILE_RANGE_WAIT_BEFORE</code> (or <code>SYNC_FILE_RANGE_WAIT_AFTER</code>)</p>
<dd> Wait for completion of write-out of all pages in the specified range. This can be used after an earlier <code>SYNC_FILE_RANGE_WAIT_BEFORE | SYNC_FILE_RANGE_WRITE</code> operation to wait for completion of that operation, and obtain its result.</p>
<dt><code>SYNC_FILE_RANGE_WAIT_BEFORE | SYNC_FILE_RANGE_WRITE | SYNC_FILE_RANGE_WAIT_AFTER</code></p>
<dd> This is a write-for-data-integrity operation that will ensure that all pages in the specified range which were dirty when <code>sync_file_range</code>() was called are committed to disk.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>sync_file_range</code>() returns 0; on failure -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> specifies an invalid bit; or <i>offset</i> or <i>nbytes</i> is invalid.</p>
<dt><code>EIO</code></p>
<dd> I/O error.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ENOSPC</code></p>
<dd> Out of disk space.</p>
<dt><code>ESPIPE</code></p>
<dd> <i>fd</i> refers to something other than a regular file, a block device, or a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>sync_file_range</code>() appeared on Linux in kernel 2.6.17.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific, and should be avoided in portable programs.</p>
<h2>NOTES</h2>
<h3>sync_file_range2()</h3>
<p> Some architectures (e.g., PowerPC, ARM) need 64-bit arguments to be aligned in a suitable pair of registers. On such architectures, the call signature of <code>sync_file_range</code>() shown in the SYNOPSIS would force a register to be wasted as padding between the <i>fd</i> and <i>offset</i> arguments. (See <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for details.) Therefore, these architectures define a different system call that orders the arguments suitably: </p>
<p> <code>int sync_file_range2(int </code><i>fd</i><code>, unsigned int </code><i>flags</i><code>,</code> <code> off64_t </code><i>offset</i><code>, off64_t </code><i>nbytes</i><code>);</code> </p>
<p> The behavior of this system call is otherwise exactly the same as <code>sync_file_range</code>(). </p>
<p> A system call with this signature first appeared on the ARM architecture in Linux 2.6.20, with the name <code>arm_sync_file_range</code>(). It was renamed in Linux 2.6.22, when the analogous system call was added for PowerPC. On architectures where glibc support is provided, glibc transparently wraps <code>sync_file_range2</code>() under the name <code>sync_file_range</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
