---
title: "migrate_pages(2)"
name: "migrate_pages"
section: "2"
letter: "m"
url: "/docs/linux/man/2-migrate_pages/"
description: "migrate_pages – move all pages in a process to another set of nodes"
---

<h2 class="name">NAME</h2>
<p> migrate_pages &#8211; move all pages in a process to another set of nodes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;numaif.h&gt;
long migrate_pages(int pid, unsigned long maxnode,
                   const unsigned long *old_nodes,
                   const unsigned long *new_nodes);
</code></pre>
<p> Link with <i>-lnuma</i>.</p>
<h2>DESCRIPTION</h2>
<p> <code>migrate_pages</code>() attempts to move all pages of the process <i>pid</i> that are in memory nodes <i>old_nodes</i> to the memory nodes in <i>new_nodes</i>. Pages not located in any node in <i>old_nodes</i> will not be migrated. As far as possible, the kernel maintains the relative topology relationship inside <i>old_nodes</i> during the migration to <i>new_nodes</i>. </p>
<p> The <i>old_nodes</i> and <i>new_nodes</i> arguments are pointers to bit masks of node numbers, with up to <i>maxnode</i> bits in each mask. These masks are maintained as arrays of unsigned <i>long</i> integers (in the last <i>long</i> integer, the bits beyond those specified by <i>maxnode</i> are ignored). The <i>maxnode</i> argument is the maximum node number in the bit mask plus one (this is the same as in <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), but different from <code><a href="/docs/linux/man/2-select/">select</a></code>(2)). </p>
<p> The <i>pid</i> argument is the ID of the process whose pages are to be moved. To move pages in another process, the caller must be privileged (<code>CAP_SYS_NICE</code>) or the real or effective user ID of the calling process must match the real or saved-set user ID of the target process. If <i>pid</i> is 0, then <code>migrate_pages</code>() moves pages of the calling process. </p>
<p> Pages shared with another process will be moved only if the initiating process has the <code>CAP_SYS_NICE</code> privilege.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>migrate_pages</code>() returns the number of pages that could not be moved (i.e., a return of zero means that all pages were successfully moved). On error, it returns -1, and sets <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Part or all of the memory range specified by <i>old_nodes</i>/<i>new_nodes</i> and <i>maxnode</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified by <i>maxnode</i> exceeds a kernel-imposed limit. Or, <i>old_nodes</i> or <i>new_nodes</i> specifies one or more node IDs that are greater than the maximum supported node ID. Or, none of the node IDs specified by <i>new_nodes</i> are on-line and allowed by the process&#8217;s current cpuset context, or none of the specified nodes contain memory.</p>
<dt><code>EPERM</code></p>
<dd> Insufficient privilege (<code>CAP_SYS_NICE</code>) to move pages of the process specified by <i>pid</i>, or insufficient privilege (<code>CAP_SYS_NICE</code>) to access the specified target nodes.</p>
<dt><code>ESRCH</code></p>
<dd> No process matching <i>pid</i> could be found.</dl>
<h2>VERSIONS</h2>
<p> The <code>migrate_pages</code>() system call first appeared on Linux in version 2.6.16.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> For information on library support, see <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7). </p>
<p> Use <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2) with the <code>MPOL_F_MEMS_ALLOWED</code> flag to obtain the set of nodes that are allowed by the calling process&#8217;s cpuset. Note that this information is subject to change at any time by manual or automatic reconfiguration of the cpuset. </p>
<p> Use of <code>migrate_pages</code>() may result in pages whose location (node) violates the memory policy established for the specified addresses (see <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2)) and/or the specified process (see <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2)). That is, memory policy does not constrain the destination nodes used by <code>migrate_pages</code>(). </p>
<p> The <i>&lt;numaif.h&gt;</i> header is not included with glibc, but requires installing <i>libnuma-devel</i> or a similar package.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/5-numa_maps/">numa_maps</a></code>(5), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7), <code><a href="/docs/linux/man/8-migratepages/">migratepages</a></code>(8), <code><a href="/docs/linux/man/8-numastat/">numastat</a></code>(8) </p>
<p> <i>Documentation/vm/page_migration.rst</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
