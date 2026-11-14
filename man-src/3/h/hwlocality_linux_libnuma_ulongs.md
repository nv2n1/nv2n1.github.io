---
title: "hwlocality_linux_libnuma_ulongs(3)"
name: "hwlocality_linux_libnuma_ulongs"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwlocality_linux_libnuma_ulongs/"
description: "hwlocality_linux_libnuma_ulongs – Interoperability with Linux libnuma unsigned long masks"
---

<h2 class="name">NAME</h2>
<p> hwlocality_linux_libnuma_ulongs &#8211; Interoperability with Linux libnuma unsigned long masks </p>
<h3>Functions</h3>
<p> static int <code>hwloc_cpuset_to_linux_libnuma_ulongs</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, unsigned long *mask, unsigned long *maxnode) </p>
<p> static int <code>hwloc_nodeset_to_linux_libnuma_ulongs</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset, unsigned long *mask, unsigned long *maxnode) </p>
<p> static int <code>hwloc_cpuset_from_linux_libnuma_ulongs</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, const unsigned long *mask, unsigned long maxnode) </p>
<p> static int <code>hwloc_nodeset_from_linux_libnuma_ulongs</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, const unsigned long *mask, unsigned long maxnode) </p>
<h2>Detailed Description</h2>
<p> This interface helps converting between Linux libnuma unsigned long masks and hwloc cpusets and nodesets. </p>
<p> It also offers a consistent behavior on non-NUMA machines or non-NUMA-aware kernels by assuming that the machines have a single NUMA node. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Topology topology must match the current machine. </p>
<p> The behavior of libnuma is undefined if the kernel is not NUMA-aware. (when CONFIG_NUMA is not set in the kernel configuration). This helper and libnuma may thus not be strictly compatible in this case, which may be detected by checking whether numa_available() returns -1.</dl>
<h2>Function Documentation</h2>
<h3>static int hwloc_cpuset_from_linux_libnuma_ulongs (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, const unsigned long * mask, unsigned long maxnode) [inline], [static]</h3>
<p> Convert the array of unsigned long mask into hwloc CPU set. mask is a array of unsigned long that will be read. maxnode contains the maximal node number that may be read in mask. </p>
<p> This function may be used after calling get_mempolicy or any other function that takes an array of unsigned long as output parameter (and possibly a maximal node number as input parameter).</p>
<h3>static int hwloc_cpuset_to_linux_libnuma_ulongs (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, unsigned long * mask, unsigned long * maxnode) [inline], [static]</h3>
<p> Convert hwloc CPU set cpuset into the array of unsigned long mask. mask is the array of unsigned long that will be filled. maxnode contains the maximal node number that may be stored in mask. maxnode will be set to the maximal node number that was found, plus one. </p>
<p> This function may be used before calling set_mempolicy, mbind, migrate_pages or any other function that takes an array of unsigned long and a maximal node number as input parameter.</p>
<h3>static int hwloc_nodeset_from_linux_libnuma_ulongs (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, const unsigned long * mask, unsigned long maxnode) [inline], [static]</h3>
<p> Convert the array of unsigned long mask into hwloc NUMA node set. mask is a array of unsigned long that will be read. maxnode contains the maximal node number that may be read in mask. </p>
<p> This function may be used after calling get_mempolicy or any other function that takes an array of unsigned long as output parameter (and possibly a maximal node number as input parameter).</p>
<h3>static int hwloc_nodeset_to_linux_libnuma_ulongs (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset, unsigned long * mask, unsigned long * maxnode) [inline], [static]</h3>
<p> Convert hwloc NUMA node set nodeset into the array of unsigned long mask. mask is the array of unsigned long that will be filled. maxnode contains the maximal node number that may be stored in mask. maxnode will be set to the maximal node number that was found, plus one. </p>
<p> This function may be used before calling set_mempolicy, mbind, migrate_pages or any other function that takes an array of unsigned long and a maximal node number as input parameter.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
