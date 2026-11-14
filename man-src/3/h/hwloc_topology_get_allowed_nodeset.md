---
title: "hwloc_topology_get_allowed_nodeset(3)"
name: "hwloc_topology_get_allowed_nodeset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_get_allowed_nodeset/"
description: "hwlocality_helper_topology_sets – CPU and node sets of entire topologies"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_topology_sets &#8211; CPU and node sets of entire topologies </p>
<h3>Functions</h3>
<p> static <code>hwloc_const_cpuset_t</code> <code>hwloc_topology_get_complete_cpuset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_cpuset_t</code> <code>hwloc_topology_get_topology_cpuset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_cpuset_t</code> <code>hwloc_topology_get_online_cpuset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_cpuset_t</code> <code>hwloc_topology_get_allowed_cpuset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_nodeset_t</code> <code>hwloc_topology_get_complete_nodeset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_nodeset_t</code> <code>hwloc_topology_get_topology_nodeset</code> (<code>hwloc_topology_t</code> topology) </p>
<p> static <code>hwloc_const_nodeset_t</code> <code>hwloc_topology_get_allowed_nodeset</code> (<code>hwloc_topology_t</code> topology) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static <code>hwloc_const_cpuset_t</code> hwloc_topology_get_allowed_cpuset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get allowed CPU set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the CPU set of allowed logical processors of the system. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned cpuset is not newly allocated and should thus not be changed or freed, <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_nodeset_t</code> hwloc_topology_get_allowed_nodeset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get allowed node set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the node set of allowed memory of the system. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned nodeset is not newly allocated and should thus not be changed or freed, <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_cpuset_t</code> hwloc_topology_get_complete_cpuset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get complete CPU set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the complete CPU set of logical processors of the system. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned cpuset is not newly allocated and should thus not be changed or freed; <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_nodeset_t</code> hwloc_topology_get_complete_nodeset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get complete node set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the complete node set of memory of the system. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned nodeset is not newly allocated and should thus not be changed or freed; <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_cpuset_t</code> hwloc_topology_get_online_cpuset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get online CPU set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the CPU set of online logical processors of the system. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned cpuset is not newly allocated and should thus not be changed or freed; <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_cpuset_t</code> hwloc_topology_get_topology_cpuset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get topology CPU set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the CPU set of logical processors of the system for which hwloc provides topology information. This is equivalent to the cpuset of the system object. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned cpuset is not newly allocated and should thus not be changed or freed; <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h3>static <code>hwloc_const_nodeset_t</code> hwloc_topology_get_topology_nodeset (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p> Get topology node set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the node set of memory of the system for which hwloc provides topology information. This is equivalent to the nodeset of the system object. If the topology is the result of a combination of several systems, NULL is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The returned nodeset is not newly allocated and should thus not be changed or freed; <code>hwloc_bitmap_dup()</code> must be used to obtain a local copy.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
