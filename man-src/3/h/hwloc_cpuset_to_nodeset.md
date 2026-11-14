---
title: "hwloc_cpuset_to_nodeset(3)"
name: "hwloc_cpuset_to_nodeset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_cpuset_to_nodeset/"
description: "hwlocality_helper_nodeset_convert – Converting between CPU sets and node sets"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_nodeset_convert &#8211; Converting between CPU sets and node sets </p>
<h3>Functions</h3>
<p> static void <code>hwloc_cpuset_to_nodeset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> _cpuset, <code>hwloc_nodeset_t</code> nodeset) </p>
<p> static void <code>hwloc_cpuset_to_nodeset_strict</code> (struct hwloc_topology *topology, <code>hwloc_const_cpuset_t</code> _cpuset, <code>hwloc_nodeset_t</code> nodeset) </p>
<p> static void <code>hwloc_cpuset_from_nodeset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> _cpuset, <code>hwloc_const_nodeset_t</code> nodeset) </p>
<p> static void <code>hwloc_cpuset_from_nodeset_strict</code> (struct hwloc_topology *topology, <code>hwloc_cpuset_t</code> _cpuset, <code>hwloc_const_nodeset_t</code> nodeset) </p>
<h2>Detailed Description</h2>
<p> There are two semantics for converting cpusets to nodesets depending on how non-NUMA machines are handled. </p>
<p> When manipulating nodesets for memory binding, non-NUMA machines should be considered as having a single NUMA node. The standard conversion routines below should be used so that marking the first bit of the nodeset means that memory should be bound to a non-NUMA whole machine. </p>
<p> When manipulating nodesets as an actual list of NUMA nodes without any need to handle memory binding on non-NUMA machines, the strict conversion routines may be used instead.</p>
<h2>Function Documentation</h2>
<h3>static void hwloc_cpuset_from_nodeset (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> _cpuset, <code>hwloc_const_nodeset_t</code> nodeset) [inline], [static]</h3>
<p> Convert a NUMA node set into a CPU set and handle non-NUMA cases. If the topology contains no NUMA nodes, the machine is considered as a single memory node, and the following behavior is used: If nodeset is empty, cpuset will be emptied as well. Otherwise cpuset will be entirely filled. This is useful for manipulating memory binding sets.</p>
<h3>static void hwloc_cpuset_from_nodeset_strict (struct hwloc_topology * topology, <code>hwloc_cpuset_t</code> _cpuset, <code>hwloc_const_nodeset_t</code> nodeset) [inline], [static]</h3>
<p> Convert a NUMA node set into a CPU set without handling non-NUMA cases. This is the strict variant of <code>hwloc_cpuset_from_nodeset()</code>. It does not fix non-NUMA cases. If the topology contains some NUMA nodes, behave exactly the same. However, if the topology contains no NUMA nodes, return an empty cpuset.</p>
<h3>static void hwloc_cpuset_to_nodeset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> _cpuset, <code>hwloc_nodeset_t</code> nodeset) [inline], [static]</h3>
<p> Convert a CPU set into a NUMA node set and handle non-NUMA cases. If some NUMA nodes have no CPUs at all, this function never sets their indexes in the output node set, even if a full CPU set is given in input. </p>
<p> If the topology contains no NUMA nodes, the machine is considered as a single memory node, and the following behavior is used: If cpuset is empty, nodeset will be emptied as well. Otherwise nodeset will be entirely filled.</p>
<h3>static void hwloc_cpuset_to_nodeset_strict (struct hwloc_topology * topology, <code>hwloc_const_cpuset_t</code> _cpuset, <code>hwloc_nodeset_t</code> nodeset) [inline], [static]</h3>
<p> Convert a CPU set into a NUMA node set without handling non-NUMA cases. This is the strict variant of <code>hwloc_cpuset_to_nodeset()</code>. It does not fix non-NUMA cases. If the topology contains some NUMA nodes, behave exactly the same. However, if the topology contains no NUMA nodes, return an empty nodeset.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
