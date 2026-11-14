---
title: "fsync(2)"
name: "fsync"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fsync/"
description: "fsync, fdatasync – synchronize a file’s in-core state with storage device"
---

<h2 class="name">NAME</h2>
<p> fsync, fdatasync &#8211; synchronize a file&#8217;s in-core state with storage device </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int fsync(int </code><i>fd</i><code>);</code> </p>
<p> <code>int fdatasync(int </code><i>fd</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fsync</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.16 and later:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;No feature test macros need be defined<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc up to and including 2.15:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;since glibc 2.8:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
 <code>fdatasync</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</p>
<h2>DESCRIPTION</h2>
<p> <code>fsync</code>() transfers (&quot;flushes&quot;) all modified in-core data of (i.e., modified buffer cache pages for) the file referred to by the file descriptor <i>fd</i> to the disk device (or other permanent storage device) so that all changed information can be retrieved even if the system crashes or is rebooted. This includes writing through or flushing a disk cache if present. The call blocks until the device reports that the transfer has completed. </p>
<p> As well as flushing the file data, <code>fsync</code>() also flushes the metadata information associated with the file (see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)). </p>
<p> Calling <code>fsync</code>() does not necessarily ensure that the entry in the directory containing the file has also reached disk. For that an explicit <code>fsync</code>() on a file descriptor for the directory is also needed. </p>
<p> <code>fdatasync</code>() is similar to <code>fsync</code>(), but does not flush modified metadata unless that metadata is needed in order to allow a subsequent data retrieval to be correctly handled. For example, changes to <i>st_atime</i> or <i>st_mtime</i> (respectively, time of last access and time of last modification; see <code><a href="/docs/linux/man/7-inode/">inode</a></code>(7)) do not require flushing because they are not necessary for a subsequent data read to be handled correctly. On the other hand, a change to the file size (<i>st_size</i>, as made by say <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2)), would require a metadata flush. </p>
<p> The aim of <code>fdatasync</code>() is to reduce disk activity for applications that do not require all metadata to be synchronized with the disk.</p>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return zero. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid open file descriptor.</p>
<dt><code>EIO</code></p>
<dd> An error occurred during synchronization. This error may relate to data written to some other file descriptor on the same file. Since Linux 4.13, errors from write-back will be reported to all file descriptors that might have written the data which triggered the error. Some filesystems (e.g., NFS) keep close track of which data came through which file descriptor, and give more precise reporting. Other filesystems (e.g., most local filesystems) will report errors to all file descriptors that were open on the file when the error was recorded.</p>
<dt><code>ENOSPC</code></p>
<dd> Disk space was exhausted while synchronizing.</p>
<dt><code>EROFS</code>, <code>EINVAL</code></p>
<dd> <i>fd</i> is bound to a special file (e.g., a pipe, FIFO, or socket) which does not support synchronization.</p>
<dt><code>ENOSPC</code>, <code>EDQUOT</code></p>
<dd> <i>fd</i> is bound to a file on NFS or another filesystem which does not allocate space at the time of a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call, and some previous write failed due to insufficient storage space.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.3BSD. </p>
<p> On POSIX systems on which <code>fdatasync</code>() is available, <code>_POSIX_SYNCHRONIZED_IO</code> is defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>NOTES</h2>
<p> On some UNIX systems (but not Linux), <i>fd</i> must be a <i>writable</i> file descriptor. </p>
<p> In Linux 2.2 and earlier, <code>fdatasync</code>() is equivalent to <code>fsync</code>(), and so has no performance advantage. </p>
<p> The <code>fsync</code>() implementations in older kernels and lesser used filesystems do not know how to flush disk caches. In these cases disk caches need to be disabled using <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8) or <code><a href="/docs/linux/man/8-sdparm/">sdparm</a></code>(8) to guarantee safe operation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1), <code><a href="/docs/linux/man/2-bdflush/">bdflush</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2), <code><a href="/docs/linux/man/2-pwritev/">pwritev</a></code>(2), <code><a href="/docs/linux/man/2-sync/">sync</a></code>(2), <code><a href="/docs/linux/man/2-sync_file_range/">sync_file_range</a></code>(2), <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-fileno/">fileno</a></code>(3), <code><a href="/docs/linux/man/8-hdparm/">hdparm</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
