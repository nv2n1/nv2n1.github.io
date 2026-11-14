---
title: "sync(2)"
name: "sync"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sync/"
description: "sync, syncfs – commit filesystem caches to disk"
---

<h2 class="name">NAME</h2>
<p> sync, syncfs &#8211; commit filesystem caches to disk </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>void sync(void);</code> </p>
<p> <code>int syncfs(int </code><i>fd</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sync</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>syncfs</code>():</p>
<dl>
<dt>
<dd> _GNU_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>sync</code>() causes all pending modifications to filesystem metadata and cached file data to be written to the underlying filesystems. </p>
<p> <code>syncfs</code>() is like <code>sync</code>(), but synchronizes just the filesystem containing file referred to by the open file descriptor <i>fd</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>syncfs</code>() returns 0 on success; on error, it returns -1 and sets <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<p> <code>sync</code>() is always successful. </p>
<p> <code>syncfs</code>() can fail for at least the following reasons:</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EIO</code></p>
<dd> An error occurred during synchronization. This error may relate to data written to any file on the filesystem, or on metadata related to the filesystem itself.</p>
<dt><code>ENOSPC</code></p>
<dd> Disk space was exhausted while synchronizing.</p>
<dt><code>ENOSPC</code>, <code>EDQUOT</code></p>
<dd> Data was written to a files on NFS or another filesystem which does not allocate space at the time of a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call, and some previous write failed due to insufficient storage space.</dl>
<h2>VERSIONS</h2>
<p> <code>syncfs</code>() first appeared in Linux 2.6.39; library support was added to glibc in version 2.14.</p>
<h2>CONFORMING TO</h2>
<p> <code>sync</code>(): POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. </p>
<p> <code>syncfs</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> Since glibc 2.2.2, the Linux prototype for <code>sync</code>() is as listed above, following the various standards. In glibc 2.2.1 and earlier, it was &quot;int sync(void)&quot;, and <code>sync</code>() always returned 0. </p>
<p> According to the standard specification (e.g., POSIX.1-2001), <code>sync</code>() schedules the writes, but may return before the actual writing is done. However Linux waits for I/O completions, and thus <code>sync</code>() or <code>syncfs</code>() provide the same guarantees as <code>fsync</code>() called on every file in the system or filesystem respectively. </p>
<p> In mainline kernel versions prior to 5.8, <code>syncfs</code>() will fail only when passed a bad file descriptor (<code>EBADF</code>). Since Linux 5.8, <code>syncfs</code>() will also report an error if one or more inodes failed to be written back since the last <code>syncfs</code>() call.</p>
<h2>BUGS</h2>
<p> Before version 1.3.20 Linux did not wait for I/O to complete before returning.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1), <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
