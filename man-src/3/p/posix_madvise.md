---
title: "posix_madvise(3)"
name: "posix_madvise"
section: "3"
letter: "p"
url: "/docs/linux/man/3-posix_madvise/"
description: "posix_madvise – give advice about patterns of memory usage"
---

<p>posix_madvise &#8211; give advice about patterns of memory usage</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/mman.h&gt;

int posix_madvise(void *addr, size_t len, int advice);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>posix_madvise</code>(): </p>
<dl>
<dd>_POSIX_C_SOURCE &gt;= 200112L</dl>
<h2>Description</h2>
<p>The <code>posix_madvise</code>() function allows an application to advise the system about its expected patterns of usage of memory in the address range starting at <i>addr</i> and continuing for <i>len</i> bytes. The system is free to use this advice in order to improve the performance of memory accesses (or to ignore the advice altogether), but calling <code>posix_madvise</code>() shall not affect the semantics of access to memory in the specified range. </p>
<p> The <i>advice</i> argument is one of the following:</p>
<dl>
<dt><code>POSIX_MADV_NORMAL</code></p>
<dd>The application has no special advice regarding its memory usage patterns for the specified address range. This is the default behavior.</p>
<dt><code>POSIX_MADV_SEQUENTIAL</code></p>
<dd>The application expects to access the specified address range sequentially, running from lower addresses to higher addresses. Hence, pages in this region can be aggressively read ahead, and may be freed soon after they are accessed.</p>
<dt><code>POSIX_MADV_RANDOM</code></p>
<dd>The application expects to access the specified address range randomly. Thus, read ahead may be less useful than normally.</p>
<dt><code>POSIX_MADV_WILLNEED</code></p>
<dd>The application expects to access the specified address range in the near future. Thus, read ahead may be beneficial.</p>
<dt><code>POSIX_MADV_DONTNEED</code></p>
<dd>The application expects that it will not access the specified address range in the near future.</dl>
<h2>Return Value</h2>
<p>On success, <code>posix_madvise</code>() returns 0. On failure, it returns a positive error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>addr</i> is not a multiple of the system page size or <i>len</i> is negative.</p>
<dt><code>EINVAL</code></p>
<dd><i>advice</i> is invalid.</p>
<dt><code>ENOMEM</code></p>
<dd>Addresses in the specified range are partially or completely outside the caller&#8217;s address space.</dl>
<h2>Versions</h2>
<p>Support for <code>posix_madvise</code>() first appeared in glibc version 2.2.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001.</p>
<h2>Notes</h2>
<p>POSIX.1 permits an implementation to generate an error if <i>len</i> is 0. On Linux, specifying <i>len</i> as 0 is permitted (as a successful no-op). </p>
<p> In glibc, this function is implemented using <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2). However, since glibc 2.6, <code>POSIX_MADV_DONTNEED</code> is treated as a no-op, because the corresponding <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) value, <code>MADV_DONTNEED</code>, has destructive semantics.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
