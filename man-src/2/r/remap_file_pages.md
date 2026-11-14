---
title: "remap_file_pages(2)"
name: "remap_file_pages"
section: "2"
letter: "r"
url: "/docs/linux/man/2-remap_file_pages/"
description: "remap_file_pages – create a nonlinear file mapping"
---

<h2 class="name">NAME</h2>
<p> remap_file_pages &#8211; create a nonlinear file mapping </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/mman.h&gt;
int remap_file_pages(void *addr, size_t size, int prot,
                     size_t pgoff, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Note</code>: this system call was marked as deprecated starting with Linux 3.16. In Linux 4.0, the implementation was replaced by a slower in-kernel emulation. Those few applications that use this system call should consider migrating to alternatives. This change was made because the kernel code for this system call was complex, and it is believed to be little used or perhaps even completely unused. While it had some use cases in database applications on 32-bit systems, those use cases don&#8217;t exist on 64-bit systems. </p>
<p> The <code>remap_file_pages</code>() system call is used to create a nonlinear mapping, that is, a mapping in which the pages of the file are mapped into a nonsequential order in memory. The advantage of using <code>remap_file_pages</code>() over using repeated calls to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) is that the former approach does not require the kernel to create additional VMA (Virtual Memory Area) data structures. </p>
<p> To create a nonlinear mapping we perform the following steps:</p>
<dl>
<dt>1.</p>
<dd> Use <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) to create a mapping (which is initially linear). This mapping must be created with the <code>MAP_SHARED</code> flag.</p>
<dt>2.</p>
<dd> Use one or more calls to <code>remap_file_pages</code>() to rearrange the correspondence between the pages of the mapping and the pages of the file. It is possible to map the same page of a file into multiple locations within the mapped region.</dl>
<p> The <i>pgoff</i> and <i>size</i> arguments specify the region of the file that is to be relocated within the mapping: <i>pgoff</i> is a file offset in units of the system page size; <i>size</i> is the length of the region in bytes. </p>
<p> The <i>addr</i> argument serves two purposes. First, it identifies the mapping whose pages we want to rearrange. Thus, <i>addr</i> must be an address that falls within a region previously mapped by a call to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). Second, <i>addr</i> specifies the address at which the file pages identified by <i>pgoff</i> and <i>size</i> will be placed. </p>
<p> The values specified in <i>addr</i> and <i>size</i> should be multiples of the system page size. If they are not, then the kernel rounds <i>both</i> values <i>down</i> to the nearest multiple of the page size. </p>
<p> The <i>prot</i> argument must be specified as 0. </p>
<p> The <i>flags</i> argument has the same meaning as for <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), but all flags other than <code>MAP_NONBLOCK</code> are ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>remap_file_pages</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i> does not refer to a valid mapping created with the <code>MAP_SHARED</code> flag.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i>, <i>size</i>, <i>prot</i>, or <i>pgoff</i> is invalid.</dl>
<h2>VERSIONS</h2>
<p> The <code>remap_file_pages</code>() system call appeared in Linux 2.5.46; glibc support was added in version 2.3.3.</p>
<h2>CONFORMING TO</h2>
<p> The <code>remap_file_pages</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Since Linux 2.6.23, <code>remap_file_pages</code>() creates non-linear mappings only on in-memory filesystems such as <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5), hugetlbfs or ramfs. On filesystems with a backing store, <code>remap_file_pages</code>() is not much more efficient than using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) to adjust which parts of the file are mapped to which addresses.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mmap2/">mmap2</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
