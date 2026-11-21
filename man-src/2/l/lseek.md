---
title: "lseek(2)"
name: "lseek"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lseek/"
description: "lseek – reposition read/write file offset"
---

<h2 class="name">NAME</h2>
<p> lseek &#8211; reposition read/write file offset </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>off_t lseek(int </code><i>fd</i><code>, off_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>lseek</code>() repositions the file offset of the open file description associated with the file descriptor <i>fd</i> to the argument <i>offset</i> according to the directive <i>whence</i> as follows:</p>
<dl>
<dt><code>SEEK_SET</code></dt>
<dd> The file offset is set to <i>offset</i> bytes.</dd>
<dt><code>SEEK_CUR</code></dt>
<dd> The file offset is set to its current location plus <i>offset</i> bytes.</dd>
<dt><code>SEEK_END</code></dt>
<dd> The file offset is set to the size of the file plus <i>offset</i> bytes.</dd></dl>
<p> <code>lseek</code>() allows the file offset to be set beyond the end of the file (but this does not change the size of the file). If data is later written at this point, subsequent reads of the data in the gap (a &quot;hole&quot;) return null bytes (&#8216;\0&#8217;) until data is actually written into the gap.  </p>
<h3>Seeking file data and holes</h3>
<p> Since version 3.1, Linux supports the following additional values for <i>whence</i>: </p>
<dl>
<dt><code>SEEK_DATA</code></dt>
<dd> <p> Adjust the file offset to the next location in the file greater than or equal to <i>offset</i> containing data. If <i>offset</i> points to data, then the file offset is set to <i>offset</i>. </p>
 </dd>
<dt><code>SEEK_HOLE</code></dt>
<dd> <p> Adjust the file offset to the next hole in the file greater than or equal to <i>offset</i>. If <i>offset</i> points into the middle of a hole, then the file offset is set to <i>offset</i>. If there is no hole past <i>offset</i>, then the file offset is adjusted to the end of the file (i.e., there is an implicit hole at the end of any file). </p>
 </dd></dl>
<p> In both of the above cases, <code>lseek</code>() fails if <i>offset</i> points past the end of the file. </p>
<p> These operations allow applications to map holes in a sparsely allocated file. This can be useful for applications such as file backup tools, which can save space when creating backups and preserve holes, if they have a mechanism for discovering holes. </p>
<p> For the purposes of these operations, a hole is a sequence of zeros that (normally) has not been allocated in the underlying file storage. However, a filesystem is not obliged to report holes, so these operations are not a guaranteed mechanism for mapping the storage space actually allocated to a file. (Furthermore, a sequence of zeros that actually has been written to the underlying storage may not be reported as a hole.) In the simplest implementation, a filesystem can support the operations by making <code>SEEK_HOLE</code> always return the offset of the end of the file, and making <code>SEEK_DATA</code> always return <i>offset</i> (i.e., even if the location referred to by <i>offset</i> is a hole, it can be considered to consist of data that is a sequence of zeros). </p>
<p> The <code>_GNU_SOURCE</code> feature test macro must be defined in order to obtain the definitions of <code>SEEK_DATA</code> and <code>SEEK_HOLE</code> from <i>&lt;unistd.h&gt;</i>. </p>
<p> The <code>SEEK_HOLE</code> and <code>SEEK_DATA</code> operations are supported for the following filesystems: </p>
<dl>
<dt>*</dt>
<dd> <p> Btrfs (since Linux 3.1) </p>
 </dd>
<dt>*</dt>
<dd> <p> OCFS (since Linux 3.2) </p>
 </dd>
<dt>*</dt>
<dd> <p> XFS (since Linux 3.5) </p>
 </dd>
<dt>*</dt>
<dd> <p> ext4 (since Linux 3.8) </p>
 </dd>
<dt>*</dt>
<dd> <p> <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) (since Linux 3.8) </p>
 </dd>
<dt>*</dt>
<dd> <p> NFS (since Linux 3.18) </p>
 </dd>
<dt>*</dt>
<dd> <p> FUSE (since Linux 4.5) </p>
 </dd>
<dt>*</dt>
<dd> <p> GFS2 (since Linux 4.15) </p>
 </dd></dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>lseek</code>() returns the resulting offset location as measured in bytes from the beginning of the file. On error, the value <i>(off_t)&nbsp;-1</i> is returned and <i>errno</i> is set to indicate the error.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></dt>
<dd> <p> <i>fd</i> is not an open file descriptor. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> <i>whence</i> is not valid. Or: the resulting file offset would be negative, or beyond the end of a seekable device. </p>
 </dd>
<dt><code>ENXIO</code></dt>
<dd> <p> <i>whence</i> is <code>SEEK_DATA</code> or <code>SEEK_HOLE</code>, and <i>offset</i> is beyond the end of the file, or <i>whence</i> is <code>SEEK_DATA</code> and <i>offset</i> is within a hole at the end of the file. </p>
 </dd>
<dt><code>EOVERFLOW</code></dt>
<dd> <p> The resulting file offset cannot be represented in an <i>off_t</i>. </p>
 </dd>
<dt><code>ESPIPE</code></dt>
<dd> <p> <i>fd</i> is associated with a pipe, socket, or FIFO. </p>
 </dd></dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. </p>
<p> <code>SEEK_DATA</code> and <code>SEEK_HOLE</code> are nonstandard extensions also present in Solaris, FreeBSD, and DragonFly BSD; they are proposed for inclusion in the next POSIX revision (Issue 8).  </p>
<h2>NOTES</h2>
<p> See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for a discussion of the relationship between file descriptors, open file descriptions, and files. </p>
<p> If the <code>O_APPEND</code> file status flag is set on the open file description, then a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) <i>always</i> moves the file offset to the end of the file, regardless of the use of <code>lseek</code>(). </p>
<p> The <i>off_t</i> data type is a signed integer data type specified by POSIX.1. </p>
<p> Some devices are incapable of seeking and POSIX does not specify which devices must support <code>lseek</code>(). </p>
<p> On Linux, using <code>lseek</code>() on a terminal device fails with the error <code>ESPIPE</code>.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3), <code><a href="/docs/linux/man/3-lseek64/">lseek64</a></code>(3), <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
