---
title: "splice(2)"
name: "splice"
section: "2"
letter: "s"
url: "/docs/linux/man/2-splice/"
description: "splice – splice data to/from a pipe"
---

<h2 class="name">NAME</h2>
<p> splice &#8211; splice data to/from a pipe </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
ssize_t splice(int fd_in, loff_t *off_in, int fd_out,
               loff_t *off_out, size_t len, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>splice</code>() moves data between two file descriptors without copying between kernel address space and user address space. It transfers up to <i>len</i> bytes of data from the file descriptor <i>fd_in</i> to the file descriptor <i>fd_out</i>, where one of the file descriptors must refer to a pipe. </p>
<p> The following semantics apply for <i>fd_in</i> and <i>off_in</i>:</p>
<dl>
<dt>*</p>
<dd> If <i>fd_in</i> refers to a pipe, then <i>off_in</i> must be NULL.</p>
<dt>*</p>
<dd> If <i>fd_in</i> does not refer to a pipe and <i>off_in</i> is NULL, then bytes are read from <i>fd_in</i> starting from the file offset, and the file offset is adjusted appropriately.</p>
<dt>*</p>
<dd> If <i>fd_in</i> does not refer to a pipe and <i>off_in</i> is not NULL, then <i>off_in</i> must point to a buffer which specifies the starting offset from which bytes will be read from <i>fd_in</i>; in this case, the file offset of <i>fd_in</i> is not changed.</dl>
<p> Analogous statements apply for <i>fd_out</i> and <i>off_out</i>. </p>
<p> The <i>flags</i> argument is a bit mask that is composed by ORing together zero or more of the following values:</p>
<dl>
<dt><code>SPLICE_F_MOVE</code></p>
<dd> Attempt to move pages instead of copying. This is only a hint to the kernel: pages may still be copied if the kernel cannot move the pages from the pipe, or if the pipe buffers don&#8217;t refer to full pages. The initial implementation of this flag was buggy: therefore starting in Linux 2.6.21 it is a no-op (but is still permitted in a <code>splice</code>() call); in the future, a correct implementation may be restored.</p>
<dt><code>SPLICE_F_NONBLOCK</code></p>
<dd> Do not block on I/O. This makes the splice pipe operations nonblocking, but <code>splice</code>() may nevertheless block because the file descriptors that are spliced to/from may block (unless they have the <code>O_NONBLOCK</code> flag set).</p>
<dt><code>SPLICE_F_MORE</code></p>
<dd> More data will be coming in a subsequent splice. This is a helpful hint when the <i>fd_out</i> refers to a socket (see also the description of <code>MSG_MORE</code> in <code><a href="/docs/linux/man/2-send/">send</a></code>(2), and the description of <code>TCP_CORK</code> in <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)).</p>
<dt><code>SPLICE_F_GIFT</code></p>
<dd> Unused for <code>splice</code>(); see <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2).</dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>splice</code>() returns the number of bytes spliced to or from the pipe. </p>
<p> A return value of 0 means end of input. If <i>fd_in</i> refers to a pipe, then this means that there was no data to transfer, and it would not make sense to block because there are no writers connected to the write end of the pipe. </p>
<p> On error, <code>splice</code>() returns -1 and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> <code>SPLICE_F_NONBLOCK</code> was specified in <i>flags</i> or one of the file descriptors had been marked as nonblocking (<code>O_NONBLOCK</code>)<code>,</code> and the operation would block.</p>
<dt><code>EBADF</code></p>
<dd> One or both file descriptors are not valid, or do not have proper read-write mode.</p>
<dt><code>EINVAL</code></p>
<dd> The target filesystem doesn&#8217;t support splicing.</p>
<dt><code>EINVAL</code></p>
<dd> The target file is opened in append mode.</p>
<dt><code>EINVAL</code></p>
<dd> Neither of the file descriptors refers to a pipe.</p>
<dt><code>EINVAL</code></p>
<dd> An offset was given for nonseekable device (e.g., a pipe).</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd_in</i> and <i>fd_out</i> refer to the same pipe.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ESPIPE</code></p>
<dd> Either <i>off_in</i> or <i>off_out</i> was not NULL, but the corresponding file descriptor refers to a pipe.</dl>
<h2>VERSIONS</h2>
<p> The <code>splice</code>() system call first appeared in Linux 2.6.17; library support was added to glibc in version 2.5.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> The three system calls <code>splice</code>(), <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2), and <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2), provide user-space programs with full control over an arbitrary kernel buffer, implemented within the kernel using the same type of buffer that is used for a pipe. In overview, these system calls perform the following tasks:</p>
<dl>
<dt>&bull;</p>
<dd> <code>splice</code>() moves data from the buffer to an arbitrary file descriptor, or vice versa, or from one buffer to another.</p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2) &quot;copies&quot; the data from one buffer to another.</p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2) &quot;copies&quot; data from user space into the buffer.</dl>
<p> Though we talk of copying, actual copies are generally avoided. The kernel does this by implementing a pipe buffer as a set of reference-counted pointers to pages of kernel memory. The kernel creates &quot;copies&quot; of pages in a buffer by creating new pointers (for the output buffer) referring to the pages, and increasing the reference counts for the pages: only pointers are copied, not the pages of the buffer. </p>
<p> In Linux 2.6.30 and earlier, exactly one of <i>fd_in</i> and <i>fd_out</i> was required to be a pipe. Since Linux 2.6.31, both arguments may refer to pipes.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-copy_file_range/">copy_file_range</a></code>(2), <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2), <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
