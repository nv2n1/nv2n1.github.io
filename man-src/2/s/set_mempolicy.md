---
title: "set_mempolicy(2)"
name: "set_mempolicy"
section: "2"
letter: "s"
url: "/docs/linux/man/2-set_mempolicy/"
description: "set_mempolicy – set default NUMA memory policy for a thread and its children"
---

<h2 class="name">NAME</h2>
<p> set_mempolicy &#8211; set default NUMA memory policy for a thread and its children </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;numaif.h&gt;
long set_mempolicy(int mode, const unsigned long *nodemask,
                   unsigned long maxnode);
Link with - lnuma.
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>set_mempolicy</code>() sets the NUMA memory policy of the calling thread, which consists of a policy mode and zero or more nodes, to the values specified by the <i>mode</i>, <i>nodemask</i>, and <i>maxnode</i> arguments. </p>
<p> A NUMA machine has different memory controllers with different distances to specific CPUs. The memory policy defines from which node memory is allocated for the thread. </p>
<p> This system call defines the default policy for the thread. The thread policy governs allocation of pages in the process&#8217;s address space outside of memory ranges controlled by a more specific policy set by <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2). The thread default policy also controls allocation of any pages for memory-mapped files mapped using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) call with the <code>MAP_PRIVATE</code> flag and that are only read (loaded) from by the thread and of memory-mapped files mapped using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) call with the <code>MAP_SHARED</code> flag, regardless of the access type. The policy is applied only when a new page is allocated for the thread. For anonymous memory this is when the page is first touched by the thread. </p>
<p> The <i>mode</i> argument must specify one of <code>MPOL_DEFAULT</code>, <code>MPOL_BIND</code>, <code>MPOL_INTERLEAVE</code>, <code>MPOL_PREFERRED</code>, or <code>MPOL_LOCAL</code> (which are described in detail below). All modes except <code>MPOL_DEFAULT</code> require the caller to specify the node or nodes to which the mode applies, via the <i>nodemask</i> argument. </p>
<p> The <i>mode</i> argument may also include an optional <i>mode flag</i>. The supported <i>mode flags</i> are:</p>
<dl>
<dt><code>MPOL_F_STATIC_NODES</code> (since Linux 2.6.26)</p>
<dd> A nonempty <i>nodemask</i> specifies physical node IDs. Linux will not remap the <i>nodemask</i> when the process moves to a different cpuset context, nor when the set of nodes allowed by the process&#8217;s current cpuset context changes.</p>
<dt><code>MPOL_F_RELATIVE_NODES</code> (since Linux 2.6.26)</p>
<dd> A nonempty <i>nodemask</i> specifies node IDs that are relative to the set of node IDs allowed by the process&#8217;s current cpuset.</dl>
<p> <i>nodemask</i> points to a bit mask of node IDs that contains up to <i>maxnode</i> bits. The bit mask size is rounded to the next multiple of <i>sizeof(unsigned long)</i>, but the kernel will use bits only up to <i>maxnode</i>. A NULL value of <i>nodemask</i> or a <i>maxnode</i> value of zero specifies the empty set of nodes. If the value of <i>maxnode</i> is zero, the <i>nodemask</i> argument is ignored. </p>
<p> Where a <i>nodemask</i> is required, it must contain at least one node that is on-line, allowed by the process&#8217;s current cpuset context, (unless the <code>MPOL_F_STATIC_NODES</code> mode flag is specified), and contains memory. If the <code>MPOL_F_STATIC_NODES</code> is set in <i>mode</i> and a required <i>nodemask</i> contains no nodes that are allowed by the process&#8217;s current cpuset context, the memory policy reverts to <i>local allocation</i>. This effectively overrides the specified policy until the process&#8217;s cpuset context includes one or more of the nodes specified by <i>nodemask</i>. </p>
<p> The <i>mode</i> argument must include one of the following values:</p>
<dl>
<dt><code>MPOL_DEFAULT</code></p>
<dd> This mode specifies that any nondefault thread memory policy be removed, so that the memory policy &quot;falls back&quot; to the system default policy. The system default policy is &quot;local allocation&quot;&#8212;that is, allocate memory on the node of the CPU that triggered the allocation. <i>nodemask</i> must be specified as NULL. If the &quot;local node&quot; contains no free memory, the system will attempt to allocate memory from a &quot;near by&quot; node.</p>
<dt><code>MPOL_BIND</code></p>
<dd> This mode defines a strict policy that restricts memory allocation to the nodes specified in <i>nodemask</i>. If <i>nodemask</i> specifies more than one node, page allocations will come from the node with the lowest numeric node ID first, until that node contains no free memory. Allocations will then come from the node with the next highest node ID specified in <i>nodemask</i> and so forth, until none of the specified nodes contain free memory. Pages will not be allocated from any node not specified in the <i>nodemask</i>.</p>
<dt><code>MPOL_INTERLEAVE</code></p>
<dd> This mode interleaves page allocations across the nodes specified in <i>nodemask</i> in numeric node ID order. This optimizes for bandwidth instead of latency by spreading out pages and memory accesses to those pages across multiple nodes. However, accesses to a single page will still be limited to the memory bandwidth of a single node.</p>
<dt><code>MPOL_PREFERRED</code></p>
<dd> This mode sets the preferred node for allocation. The kernel will try to allocate pages from this node first and fall back to &quot;near by&quot; nodes if the preferred node is low on free memory. If <i>nodemask</i> specifies more than one node ID, the first node in the mask will be selected as the preferred node. If the <i>nodemask</i> and <i>maxnode</i> arguments specify the empty set, then the policy specifies &quot;local allocation&quot; (like the system default policy discussed above).</p>
<dt><code>MPOL_LOCAL</code> (since Linux 3.8)</p>
<dd> This mode specifies &quot;local allocation&quot;; the memory is allocated on the node of the CPU that triggered the allocation (the &quot;local node&quot;). The <i>nodemask</i> and <i>maxnode</i> arguments must specify the empty set. If the &quot;local node&quot; is low on free memory, the kernel will try to allocate memory from other nodes. The kernel will allocate memory from the &quot;local node&quot; whenever memory for this node is available. If the &quot;local node&quot; is not allowed by the process&#8217;s current cpuset context, the kernel will try to allocate memory from other nodes. The kernel will allocate memory from the &quot;local node&quot; whenever it becomes allowed by the process&#8217;s current cpuset context.</dl>
<p> The thread memory policy is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and is inherited by child threads created using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>set_mempolicy</code>() returns 0; on error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Part of all of the memory range specified by <i>nodemask</i> and <i>maxnode</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is invalid. Or, <i>mode</i> is <code>MPOL_DEFAULT</code> and <i>nodemask</i> is nonempty, or <i>mode</i> is <code>MPOL_BIND</code> or <code>MPOL_INTERLEAVE</code> and <i>nodemask</i> is empty. Or, <i>maxnode</i> specifies more than a page worth of bits. Or, <i>nodemask</i> specifies one or more node IDs that are greater than the maximum supported node ID. Or, none of the node IDs specified by <i>nodemask</i> are on-line and allowed by the process&#8217;s current cpuset context, or none of the specified nodes contain memory. Or, the <i>mode</i> argument specified both <code>MPOL_F_STATIC_NODES</code> and <code>MPOL_F_RELATIVE_NODES</code>.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</dl>
<h2>VERSIONS</h2>
<p> The <code>set_mempolicy</code>() system call was added to the Linux kernel in version 2.6.7.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Memory policy is not remembered if the page is swapped out. When such a page is paged back in, it will use the policy of the thread or memory range that is in effect at the time the page is allocated. </p>
<p> For information on library support, see <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
