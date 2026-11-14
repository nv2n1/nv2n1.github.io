---
title: "msync(2)"
name: "msync"
section: "2"
letter: "m"
url: "/docs/linux/man/2-msync/"
description: "msync – synchronize a file with a memory map"
---

<h2 class="name">NAME</h2>
<p> msync &#8211; synchronize a file with a memory map </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/mman.h&gt;</code> </p>
<p> <code>int msync(void *</code><i>addr</i><code>, size_t </code><i>length</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>msync</code>() flushes changes made to the in-core copy of a file that was mapped into memory using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) back to the filesystem. Without use of this call, there is no guarantee that changes are written back before <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) is called. To be more precise, the part of the file that corresponds to the memory area starting at <i>addr</i> and having length <i>length</i> is updated. </p>
<p> The <i>flags</i> argument should specify exactly one of <code>MS_ASYNC</code> and <code>MS_SYNC</code>, and may additionally include the <code>MS_INVALIDATE</code> bit. These bits have the following meanings:</p>
<dl>
<dt><code>MS_ASYNC</code></p>
<dd> Specifies that an update be scheduled, but the call returns immediately.</p>
<dt><code>MS_SYNC</code></p>
<dd> Requests an update and waits for it to complete.</p>
<dt><code>MS_INVALIDATE</code></p>
<dd> Asks to invalidate other mappings of the same file (so that they can be updated with the fresh values just written).</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBUSY</code></p>
<dd> <code>MS_INVALIDATE</code> was specified in <i>flags</i>, and a memory lock exists for the specified address range.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i> is not a multiple of PAGESIZE; or any bit other than <code>MS_ASYNC</code> | <code>MS_INVALIDATE</code> | <code>MS_SYNC</code> is set in <i>flags</i>; or both <code>MS_SYNC</code> and <code>MS_ASYNC</code> are set in <i>flags</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> The indicated memory (or part of it) was not mapped.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008. </p>
<p> This call was introduced in Linux 1.3.21, and then used <code>EFAULT</code> instead of <code>ENOMEM</code>. In Linux 2.4.19, this was changed to the POSIX value <code>ENOMEM</code>. </p>
<p> On POSIX systems on which <code>msync</code>() is available, both <code>_POSIX_MAPPED_FILES</code> and <code>_POSIX_SYNCHRONIZED_IO</code> are defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>NOTES</h2>
<p> According to POSIX, either <code>MS_SYNC</code> or <code>MS_ASYNC</code> must be specified in <i>flags</i>, and indeed failure to include one of these flags will cause <code>msync</code>() to fail on some systems. However, Linux permits a call to <code>msync</code>() that specifies neither of these flags, with semantics that are (currently) equivalent to specifying <code>MS_ASYNC</code>. (Since Linux 2.6.19, <code>MS_ASYNC</code> is in fact a no-op, since the kernel properly tracks dirty pages and flushes them to storage as necessary.) Notwithstanding the Linux behavior, portable, future-proof applications should ensure that they specify either <code>MS_SYNC</code> or <code>MS_ASYNC</code> in <i>flags</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<p> B.O. Gallmeister, POSIX.4, O&#8217;Reilly, pp. 128-129 and 389-391.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
