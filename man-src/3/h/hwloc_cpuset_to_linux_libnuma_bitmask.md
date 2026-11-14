---
title: "hwloc_cpuset_to_linux_libnuma_bitmask(3)"
name: "hwloc_cpuset_to_linux_libnuma_bitmask"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_cpuset_to_linux_libnuma_bitmask/"
description: "hwlocality_linux_libnuma_bitmask – Interoperability with Linux libnuma bitmask"
---

<h2 class="name">NAME</h2>
<p> hwlocality_linux_libnuma_bitmask &#8211; Interoperability with Linux libnuma bitmask </p>
<h3>Functions</h3>
<p> static struct bitmask * <code>hwloc_cpuset_to_linux_libnuma_bitmask</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset) </p>
<p> static struct bitmask * <code>hwloc_nodeset_to_linux_libnuma_bitmask</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset) </p>
<p> static int <code>hwloc_cpuset_from_linux_libnuma_bitmask</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, const struct bitmask *bitmask) </p>
<p> static int <code>hwloc_nodeset_from_linux_libnuma_bitmask</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, const struct bitmask *bitmask) </p>
<h2>Detailed Description</h2>
<p> This interface helps converting between Linux libnuma bitmasks and hwloc cpusets and nodesets. </p>
<p> It also offers a consistent behavior on non-NUMA machines or non-NUMA-aware kernels by assuming that the machines have a single NUMA node. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Topology topology must match the current machine. </p>
<p> The behavior of libnuma is undefined if the kernel is not NUMA-aware. (when CONFIG_NUMA is not set in the kernel configuration). This helper and libnuma may thus not be strictly compatible in this case, which may be detected by checking whether numa_available() returns -1.</dl>
<h2>Function Documentation</h2>
<h3>static int hwloc_cpuset_from_linux_libnuma_bitmask (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> cpuset, const struct bitmask * bitmask) [inline], [static]</h3>
<p> Convert libnuma bitmask bitmask into hwloc CPU set cpuset. This function may be used after calling many numa_ functions that use a struct bitmask as an output parameter.</p>
<h3>static struct bitmask * hwloc_cpuset_to_linux_libnuma_bitmask (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset) [static]</h3>
<p> Convert hwloc CPU set cpuset into the returned libnuma bitmask. The returned bitmask should later be freed with numa_bitmask_free. </p>
<p> This function may be used before calling many numa_ functions that use a struct bitmask as an input parameter. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> newly allocated struct bitmask.</dl>
<h3>static int hwloc_nodeset_from_linux_libnuma_bitmask (<code>hwloc_topology_t</code> topology, <code>hwloc_nodeset_t</code> nodeset, const struct bitmask * bitmask) [inline], [static]</h3>
<p> Convert libnuma bitmask bitmask into hwloc NUMA node set nodeset. This function may be used after calling many numa_ functions that use a struct bitmask as an output parameter.</p>
<h3>static struct bitmask * hwloc_nodeset_to_linux_libnuma_bitmask (<code>hwloc_topology_t</code> topology, <code>hwloc_const_nodeset_t</code> nodeset) [static]</h3>
<p> Convert hwloc NUMA node set nodeset into the returned libnuma bitmask. The returned bitmask should later be freed with numa_bitmask_free. </p>
<p> This function may be used before calling many numa_ functions that use a struct bitmask as an input parameter. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> newly allocated struct bitmask.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
