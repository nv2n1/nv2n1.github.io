---
title: "mbind(2)"
name: "mbind"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mbind/"
description: "mbind – set memory policy for a memory range"
---

<h2 class="name">NAME</h2>
<p> mbind &#8211; set memory policy for a memory range </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;numaif.h&gt;
long mbind(void *addr, unsigned long len, int mode,
           const unsigned long *nodemask, unsigned long maxnode,
           unsigned flags);
Link with - lnuma.
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mbind</code>() sets the NUMA memory policy, which consists of a policy mode and zero or more nodes, for the memory range starting with <i>addr</i> and continuing for <i>len</i> bytes. The memory policy defines from which node memory is allocated. </p>
<p> If the memory range specified by the <i>addr</i> and <i>len</i> arguments includes an &quot;anonymous&quot; region of memory&#8212;that is a region of memory created using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call with the <code>MAP_ANONYMOUS</code>&#8212;or a memory-mapped file, mapped using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call with the <code>MAP_PRIVATE</code> flag, pages will be allocated only according to the specified policy when the application writes (stores) to the page. For anonymous regions, an initial read access will use a shared page in the kernel containing all zeros. For a file mapped with <code>MAP_PRIVATE</code>, an initial read access will allocate pages according to the memory policy of the thread that causes the page to be allocated. This may not be the thread that called <code>mbind</code>(). </p>
<p> The specified policy will be ignored for any <code>MAP_SHARED</code> mappings in the specified memory range. Rather the pages will be allocated according to the memory policy of the thread that caused the page to be allocated. Again, this may not be the thread that called <code>mbind</code>(). </p>
<p> If the specified memory range includes a shared memory region created using the <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2) system call and attached using the <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) system call, pages allocated for the anonymous or shared memory region will be allocated according to the policy specified, regardless of which process attached to the shared memory segment causes the allocation. If, however, the shared memory region was created with the <code>SHM_HUGETLB</code> flag, the huge pages will be allocated according to the policy specified only if the page allocation is caused by the process that calls <code>mbind</code>() for that region. </p>
<p> By default, <code>mbind</code>() has an effect only for new allocations; if the pages inside the range have been already touched before setting the policy, then the policy has no effect. This default behavior may be overridden by the <code>MPOL_MF_MOVE</code> and <code>MPOL_MF_MOVE_ALL</code> flags described below. </p>
<p> The <i>mode</i> argument must specify one of <code>MPOL_DEFAULT</code>, <code>MPOL_BIND</code>, <code>MPOL_INTERLEAVE</code>, <code>MPOL_PREFERRED</code>, or <code>MPOL_LOCAL</code> (which are described in detail below). All policy modes except <code>MPOL_DEFAULT</code> require the caller to specify the node or nodes to which the mode applies, via the <i>nodemask</i> argument. </p>
<p> The <i>mode</i> argument may also include an optional <i>mode flag</i>. The supported <i>mode flags</i> are:</p>
<dl>
<dt><code>MPOL_F_STATIC_NODES</code> (since Linux-2.6.26)</p>
<dd> A nonempty <i>nodemask</i> specifies physical node IDs. Linux does not remap the <i>nodemask</i> when the thread moves to a different cpuset context, nor when the set of nodes allowed by the thread&#8217;s current cpuset context changes.</p>
<dt><code>MPOL_F_RELATIVE_NODES</code> (since Linux-2.6.26)</p>
<dd> A nonempty <i>nodemask</i> specifies node IDs that are relative to the set of node IDs allowed by the thread&#8217;s current cpuset.</dl>
<p> <i>nodemask</i> points to a bit mask of nodes containing up to <i>maxnode</i> bits. The bit mask size is rounded to the next multiple of <i>sizeof(unsigned long)</i>, but the kernel will use bits only up to <i>maxnode</i>. A NULL value of <i>nodemask</i> or a <i>maxnode</i> value of zero specifies the empty set of nodes. If the value of <i>maxnode</i> is zero, the <i>nodemask</i> argument is ignored. Where a <i>nodemask</i> is required, it must contain at least one node that is on-line, allowed by the thread&#8217;s current cpuset context (unless the <code>MPOL_F_STATIC_NODES</code> mode flag is specified), and contains memory. </p>
<p> The <i>mode</i> argument must include one of the following values:</p>
<dl>
<dt><code>MPOL_DEFAULT</code></p>
<dd> This mode requests that any nondefault policy be removed, restoring default behavior. When applied to a range of memory via <code>mbind</code>(), this means to use the thread memory policy, which may have been set with <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). If the mode of the thread memory policy is also <code>MPOL_DEFAULT</code>, the system-wide default policy will be used. The system-wide default policy allocates pages on the node of the CPU that triggers the allocation. For <code>MPOL_DEFAULT</code>, the <i>nodemask</i> and <i>maxnode</i> arguments must be specify the empty set of nodes.</p>
<dt><code>MPOL_BIND</code></p>
<dd> This mode specifies a strict policy that restricts memory allocation to the nodes specified in <i>nodemask</i>. If <i>nodemask</i> specifies more than one node, page allocations will come from the node with sufficient free memory that is closest to the node where the allocation takes place. Pages will not be allocated from any node not specified in the IR nodemask . (Before Linux 2.6.26, page allocations came from the node with the lowest numeric node ID first, until that node contained no free memory. Allocations then came from the node with the next highest node ID specified in <i>nodemask</i> and so forth, until none of the specified nodes contained free memory.)</p>
<dt><code>MPOL_INTERLEAVE</code></p>
<dd> This mode specifies that page allocations be interleaved across the set of nodes specified in <i>nodemask</i>. This optimizes for bandwidth instead of latency by spreading out pages and memory accesses to those pages across multiple nodes. To be effective the memory area should be fairly large, at least 1 MB or bigger with a fairly uniform access pattern. Accesses to a single page of the area will still be limited to the memory bandwidth of a single node.</p>
<dt><code>MPOL_PREFERRED</code></p>
<dd> This mode sets the preferred node for allocation. The kernel will try to allocate pages from this node first and fall back to other nodes if the preferred nodes is low on free memory. If <i>nodemask</i> specifies more than one node ID, the first node in the mask will be selected as the preferred node. If the <i>nodemask</i> and <i>maxnode</i> arguments specify the empty set, then the memory is allocated on the node of the CPU that triggered the allocation.</p>
<dt><code>MPOL_LOCAL</code> (since Linux 3.8)</p>
<dd> This mode specifies &quot;local allocation&quot;; the memory is allocated on the node of the CPU that triggered the allocation (the &quot;local node&quot;). The <i>nodemask</i> and <i>maxnode</i> arguments must specify the empty set. If the &quot;local node&quot; is low on free memory, the kernel will try to allocate memory from other nodes. The kernel will allocate memory from the &quot;local node&quot; whenever memory for this node is available. If the &quot;local node&quot; is not allowed by the thread&#8217;s current cpuset context, the kernel will try to allocate memory from other nodes. The kernel will allocate memory from the &quot;local node&quot; whenever it becomes allowed by the thread&#8217;s current cpuset context. By contrast, <code>MPOL_DEFAULT</code> reverts to the memory policy of the thread (which may be set via <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2)); that policy may be something other than &quot;local allocation&quot;.</dl>
<p> If <code>MPOL_MF_STRICT</code> is passed in <i>flags</i> and <i>mode</i> is not <code>MPOL_DEFAULT</code>, then the call fails with the error <code>EIO</code> if the existing pages in the memory range don&#8217;t follow the policy. </p>
<p> If <code>MPOL_MF_MOVE</code> is specified in <i>flags</i>, then the kernel will attempt to move all the existing pages in the memory range so that they follow the policy. Pages that are shared with other processes will not be moved. If <code>MPOL_MF_STRICT</code> is also specified, then the call fails with the error <code>EIO</code> if some pages could not be moved. </p>
<p> If <code>MPOL_MF_MOVE_ALL</code> is passed in <i>flags</i>, then the kernel will attempt to move all existing pages in the memory range regardless of whether other processes use the pages. The calling thread must be privileged (<code>CAP_SYS_NICE</code>) to use this flag. If <code>MPOL_MF_STRICT</code> is also specified, then the call fails with the error <code>EIO</code> if some pages could not be moved.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>mbind</code>() returns 0; on error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Part or all of the memory range specified by <i>nodemask</i> and <i>maxnode</i> points outside your accessible address space. Or, there was an unmapped hole in the specified memory range specified by <i>addr</i> and <i>len</i>.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid value was specified for <i>flags</i> or <i>mode</i>; or <i>addr + len</i> was less than <i>addr</i>; or <i>addr</i> is not a multiple of the system page size. Or, <i>mode</i> is <code>MPOL_DEFAULT</code> and <i>nodemask</i> specified a nonempty set; or <i>mode</i> is <code>MPOL_BIND</code> or <code>MPOL_INTERLEAVE</code> and <i>nodemask</i> is empty. Or, <i>maxnode</i> exceeds a kernel-imposed limit. Or, <i>nodemask</i> specifies one or more node IDs that are greater than the maximum supported node ID. Or, none of the node IDs specified by <i>nodemask</i> are on-line and allowed by the thread&#8217;s current cpuset context, or none of the specified nodes contain memory. Or, the <i>mode</i> argument specified both <code>MPOL_F_STATIC_NODES</code> and <code>MPOL_F_RELATIVE_NODES</code>.</p>
<dt><code>EIO</code></p>
<dd> <code>MPOL_MF_STRICT</code> was specified and an existing page was already on a node that does not follow the policy; or <code>MPOL_MF_MOVE</code> or <code>MPOL_MF_MOVE_ALL</code> was specified and the kernel was unable to move all existing pages in the range.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>EPERM</code></p>
<dd> The <i>flags</i> argument included the <code>MPOL_MF_MOVE_ALL</code> flag and the caller does not have the <code>CAP_SYS_NICE</code> privilege.</dl>
<h2>VERSIONS</h2>
<p> The <code>mbind</code>() system call was added to the Linux kernel in version 2.6.7.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> For information on library support, see <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7). </p>
<p> NUMA policy is not supported on a memory-mapped file range that was mapped with the <code>MAP_SHARED</code> flag. </p>
<p> The <code>MPOL_DEFAULT</code> mode can have different effects for <code>mbind</code>() and <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). When <code>MPOL_DEFAULT</code> is specified for <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), the thread&#8217;s memory policy reverts to the system default policy or local allocation. When <code>MPOL_DEFAULT</code> is specified for a range of memory using <code>mbind</code>(), any pages subsequently allocated for that range will use the thread&#8217;s memory policy, as set by <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). This effectively removes the explicit policy from the specified range, &quot;falling back&quot; to a possibly nondefault policy. To select explicit &quot;local allocation&quot; for a memory range, specify a <i>mode</i> of <code>MPOL_LOCAL</code> or <code>MPOL_PREFERRED</code> with an empty set of nodes. This method will work for <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), as well. </p>
<p> Support for huge page policy was added with 2.6.16. For interleave policy to be effective on huge page mappings the policied memory needs to be tens of megabytes or larger. </p>
<p> Before Linux 5.7. <code>MPOL_MF_STRICT</code> was ignored on huge page mappings. </p>
<p> <code>MPOL_MF_MOVE</code> and <code>MPOL_MF_MOVE_ALL</code> are available only on Linux 2.6.16 and later.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
