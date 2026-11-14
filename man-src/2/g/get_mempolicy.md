---
title: "get_mempolicy(2)"
name: "get_mempolicy"
section: "2"
letter: "g"
url: "/docs/linux/man/2-get_mempolicy/"
description: "get_mempolicy – retrieve NUMA memory policy for a thread"
---

<h2 class="name">NAME</h2>
<p> get_mempolicy &#8211; retrieve NUMA memory policy for a thread </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;numaif.h&gt;</code> </p>
<pre><code>
long get_mempolicy(int *mode, unsigned long *nodemask,
                   unsigned long maxnode, void *addr,
                   unsigned long flags);
Link with - lnuma.
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>get_mempolicy</code>() retrieves the NUMA policy of the calling thread or of a memory address, depending on the setting of <i>flags</i>. </p>
<p> A NUMA machine has different memory controllers with different distances to specific CPUs. The memory policy defines from which node memory is allocated for the thread. </p>
<p> If <i>flags</i> is specified as 0, then information about the calling thread&#8217;s default policy (as set by <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2)) is returned, in the buffers pointed to by <i>mode</i> and <i>nodemask</i>. The value returned in these arguments may be used to restore the thread&#8217;s policy to its state at the time of the call to <code>get_mempolicy</code>() using <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2). When <i>flags</i> is 0, <i>addr</i> must be specified as NULL. </p>
<p> If <i>flags</i> specifies <code>MPOL_F_MEMS_ALLOWED</code> (available since Linux 2.6.24), the <i>mode</i> argument is ignored and the set of nodes (memories) that the thread is allowed to specify in subsequent calls to <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) or <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2) (in the absence of any <i>mode flags</i>) is returned in <i>nodemask</i>. It is not permitted to combine <code>MPOL_F_MEMS_ALLOWED</code> with either <code>MPOL_F_ADDR</code> or <code>MPOL_F_NODE</code>. </p>
<p> If <i>flags</i> specifies <code>MPOL_F_ADDR</code>, then information is returned about the policy governing the memory address given in <i>addr</i>. This policy may be different from the thread&#8217;s default policy if <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) or one of the helper functions described in <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) has been used to establish a policy for the memory range containing <i>addr</i>. </p>
<p> If the <i>mode</i> argument is not NULL, then <code>get_mempolicy</code>() will store the policy mode and any optional <i>mode flags</i> of the requested NUMA policy in the location pointed to by this argument. If <i>nodemask</i> is not NULL, then the nodemask associated with the policy will be stored in the location pointed to by this argument. <i>maxnode</i> specifies the number of node IDs that can be stored into <i>nodemask</i>&#8212;that is, the maximum node ID plus one. The value specified by <i>maxnode</i> is always rounded to a multiple of <i>sizeof(unsigned long)*8</i>. </p>
<p> If <i>flags</i> specifies both <code>MPOL_F_NODE</code> and <code>MPOL_F_ADDR</code>, <code>get_mempolicy</code>() will return the node ID of the node on which the address <i>addr</i> is allocated into the location pointed to by <i>mode</i>. If no page has yet been allocated for the specified address, <code>get_mempolicy</code>() will allocate a page as if the thread had performed a read (load) access to that address, and return the ID of the node where that page was allocated. </p>
<p> If <i>flags</i> specifies <code>MPOL_F_NODE</code>, but not <code>MPOL_F_ADDR</code>, and the thread&#8217;s current policy is <code>MPOL_INTERLEAVE</code>, then <code>get_mempolicy</code>() will return in the location pointed to by a non-NULL <i>mode</i> argument, the node ID of the next node that will be used for interleaving of internal kernel pages allocated on behalf of the thread. These allocations include pages for memory-mapped files in process memory ranges mapped using the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) call with the <code>MAP_PRIVATE</code> flag for read accesses, and in memory ranges mapped with the <code>MAP_SHARED</code> flag for all accesses. </p>
<p> Other flag values are reserved. </p>
<p> For an overview of the possible policies see <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>get_mempolicy</code>() returns 0; on error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Part of all of the memory range specified by <i>nodemask</i> and <i>maxnode</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified by <i>maxnode</i> is less than the number of node IDs supported by the system. Or <i>flags</i> specified values other than <code>MPOL_F_NODE</code> or <code>MPOL_F_ADDR</code>; or <i>flags</i> specified <code>MPOL_F_ADDR</code> and <i>addr</i> is NULL, or <i>flags</i> did not specify <code>MPOL_F_ADDR</code> and <i>addr</i> is not NULL. Or, <i>flags</i> specified <code>MPOL_F_NODE</code> but not <code>MPOL_F_ADDR</code> and the current thread policy is not <code>MPOL_INTERLEAVE</code>. Or, <i>flags</i> specified <code>MPOL_F_MEMS_ALLOWED</code> with either <code>MPOL_F_ADDR</code> or <code>MPOL_F_NODE</code>. (And there are other <code>EINVAL</code> cases.)</dl>
<h2>VERSIONS</h2>
<p> The <code>get_mempolicy</code>() system call was added to the Linux kernel in version 2.6.7.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> For information on library support, see <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
