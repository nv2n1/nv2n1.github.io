---
title: "mincore(2)"
name: "mincore"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mincore/"
description: "mincore – determine whether pages are resident in memory"
---

<h2 class="name">NAME</h2>
<p> mincore &#8211; determine whether pages are resident in memory </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/mman.h&gt;</code> </p>
<p> <code>int mincore(void *</code><i>addr</i><code>, size_t </code><i>length</i><code>, unsigned char *</code><i>vec</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mincore</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>mincore</code>() returns a vector that indicates whether pages of the calling process&#8217;s virtual memory are resident in core (RAM), and so will not cause a disk access (page fault) if referenced. The kernel returns residency information about the pages starting at the address <i>addr</i>, and continuing for <i>length</i> bytes. </p>
<p> The <i>addr</i> argument must be a multiple of the system page size. The <i>length</i> argument need not be a multiple of the page size, but since residency information is returned for whole pages, <i>length</i> is effectively rounded up to the next multiple of the page size. One may obtain the page size (<code>PAGE_SIZE</code>) using <i>sysconf(_SC_PAGESIZE)</i>. </p>
<p> The <i>vec</i> argument must point to an array containing at least <i>(length+PAGE_SIZE-1) / PAGE_SIZE</i> bytes. On return, the least significant bit of each byte will be set if the corresponding page is currently resident in memory, and be clear otherwise. (The settings of the other bits in each byte are undefined; these bits are reserved for possible later use.) Of course the information returned in <i>vec</i> is only a snapshot: pages that are not locked in memory can come and go at any moment, and the contents of <i>vec</i> may already be stale by the time this call returns.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>mincore</code>() returns zero. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>EAGAIN</code> kernel is temporarily out of resources.</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>vec</i> points to an invalid address.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i> is not a multiple of the page size.</p>
<dt><code>ENOMEM</code></p>
<dd> <i>length</i> is greater than (<i>TASK_SIZE</i> &#8211; <i>addr</i>). (This could occur if a negative value is specified for <i>length</i>, since that value will be interpreted as a large unsigned integer.) In Linux 2.6.11 and earlier, the error <code>EINVAL</code> was returned for this condition.</p>
<dt><code>ENOMEM</code></p>
<dd> <i>addr</i> to <i>addr</i> + <i>length</i> contained unmapped memory.</dl>
<h2>VERSIONS</h2>
<p> Available since Linux 2.3.99pre1 and glibc 2.2.</p>
<h2>CONFORMING TO</h2>
<p> <code>mincore</code>() is not specified in POSIX.1, and it is not available on all UNIX implementations.</p>
<h2>BUGS</h2>
<p> Before kernel 2.6.21, <code>mincore</code>() did not return correct information for <code>MAP_PRIVATE</code> mappings, or for nonlinear mappings (established using <code><a href="/docs/linux/man/2-remap_file_pages/">remap_file_pages</a></code>(2)).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fincore/">fincore</a></code>(1), <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-posix_fadvise/">posix_fadvise</a></code>(2), <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
