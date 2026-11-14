---
title: "hwloc_get_next_obj_covering_cpuset_by_type(3)"
name: "hwloc_get_next_obj_covering_cpuset_by_type"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_next_obj_covering_cpuset_by_type/"
description: "hwlocality_helper_find_covering – Finding Objects covering at least CPU set"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_find_covering &#8211; Finding Objects covering at least CPU set </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_child_covering_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> parent) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_covering_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_covering_cpuset_by_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_covering_cpuset_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static <code>hwloc_obj_t</code> hwloc_get_child_covering_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> parent) [inline], [static]</h3>
<p> Get the child covering at least CPU set set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no child matches or if set is empty.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if parent does not have a CPU set.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_covering_cpuset_by_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Iterate through same-depth objects covering at least CPU set set. If object prev is NULL, return the first object at depth depth covering at least part of CPU set set. The next invokation should pass the previous return value in prev so as to obtain the next object covering at least another part of set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects at the given depth do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_covering_cpuset_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Iterate through same-type objects covering at least CPU set set. If object prev is NULL, return the first object of type type covering at least part of CPU set set. The next invokation should pass the previous return value in prev so as to obtain the next object of type type covering at least another part of set. </p>
<p> If there are no or multiple depths for type type, NULL is returned. The caller may fallback to <code>hwloc_get_next_obj_covering_cpuset_by_depth()</code> for each depth. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects of the given type do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_covering_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the lowest object covering at least CPU set set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no object matches or if set is empty.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if the root object does not have a CPU set, e.g. if the topology is made of different machines.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
