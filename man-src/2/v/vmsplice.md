---
title: "vmsplice(2)"
name: "vmsplice"
section: "2"
letter: "v"
url: "/docs/linux/man/2-vmsplice/"
description: "vmsplice – splice user pages to/from a pipe"
---

<h2 class="name">NAME</h2>
<p> vmsplice &#8211; splice user pages to/from a pipe </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;
#include &lt;sys/uio.h&gt;
ssize_t vmsplice(int fd, const struct iovec *iov,
                 unsigned long nr_segs, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>fd</i> is opened for writing, the <code>vmsplice</code>() system call maps <i>nr_segs</i> ranges of user memory described by <i>iov</i> into a pipe. If <i>fd</i> is opened for reading, the <code>vmsplice</code>() system call fills <i>nr_segs</i> ranges of user memory described by <i>iov</i> from a pipe. The file descriptor <i>fd</i> must refer to a pipe. </p>
<p> The pointer <i>iov</i> points to an array of <i>iovec</i> structures as defined in <i>&lt;sys/uio.h&gt;</i>: </p>
<p> struct iovec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*iov_base;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t iov_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes&nbsp;*/ }; </p>
<p> The <i>flags</i> argument is a bit mask that is composed by ORing together zero or more of the following values:</p>
<dl>
<dt><code>SPLICE_F_MOVE</code></p>
<dd> Unused for <code>vmsplice</code>(); see <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2).</p>
<dt><code>SPLICE_F_NONBLOCK</code></p>
<dd> Do not block on I/O; see <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) for further details.</p>
<dt><code>SPLICE_F_MORE</code></p>
<dd> Currently has no effect for <code>vmsplice</code>(), but may be implemented in the future; see <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2).</p>
<dt><code>SPLICE_F_GIFT</code></p>
<dd> The user pages are a gift to the kernel. The application may not modify this memory ever, otherwise the page cache and on-disk data may differ. Gifting pages to the kernel means that a subsequent <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) <code>SPLICE_F_MOVE</code> can successfully move the pages; if this flag is not specified, then a subsequent <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) <code>SPLICE_F_MOVE</code> must copy the pages. Data must also be properly page aligned, both in memory and length.</dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>vmsplice</code>() returns the number of bytes transferred to the pipe. On error, <code>vmsplice</code>() returns -1 and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> <code>SPLICE_F_NONBLOCK</code> was specified in <i>flags</i>, and the operation would block.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> either not valid, or doesn&#8217;t refer to a pipe.</p>
<dt><code>EINVAL</code></p>
<dd> <i>nr_segs</i> is greater than <code>IOV_MAX</code>; or memory not aligned if <code>SPLICE_F_GIFT</code> set.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</dl>
<h2>VERSIONS</h2>
<p> The <code>vmsplice</code>() system call first appeared in Linux 2.6.17; library support was added to glibc in version 2.5.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> <code>vmsplice</code>() follows the other vectorized read/write type functions when it comes to limitations on the number of segments being passed in. This limit is <code>IOV_MAX</code> as defined in <i>&lt;limits.h&gt;</i>. Currently, this limit is 1024. </p>
<p> <code>vmsplice</code>() really supports true splicing only from user memory to a pipe. In the opposite direction, it actually just copies the data to userspace. But this makes the interface nice and symmetric and enables people to build on <code>vmsplice</code>() with room for future improvement in performance.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
