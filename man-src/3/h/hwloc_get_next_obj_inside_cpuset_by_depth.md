---
title: "hwloc_get_next_obj_inside_cpuset_by_depth(3)"
name: "hwloc_get_next_obj_inside_cpuset_by_depth"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_next_obj_inside_cpuset_by_depth/"
description: "hwlocality_helper_find_inside – Finding Objects inside a CPU set"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_find_inside &#8211; Finding Objects inside a CPU set </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_first_largest_obj_inside_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) </p>
<p> int <code>hwloc_get_largest_objs_inside_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> *restrict objs, int max) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_inside_cpuset_by_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_inside_cpuset_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_inside_cpuset_by_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, unsigned idx) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_inside_cpuset_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, unsigned idx) </p>
<p> static unsigned <code>hwloc_get_nbobjs_inside_cpuset_by_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth) </p>
<p> static int <code>hwloc_get_nbobjs_inside_cpuset_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type) </p>
<p> static int <code>hwloc_get_obj_index_inside_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> obj) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static <code>hwloc_obj_t</code> hwloc_get_first_largest_obj_inside_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the first largest object included in the given cpuset set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the first object that is included in set and whose parent is not.</dl>
<p> This is convenient for iterating over all largest objects within a CPU set by doing a loop getting the first largest object and clearing its CPU set from the remaining CPU set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if the root object does not have a CPU set, e.g. if the topology is made of different machines.</dl>
<h3>int hwloc_get_largest_objs_inside_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> *restrict objs, int max)</h3>
<p> Get the set of largest objects covering exactly a given cpuset set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of objects returned in objs.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if the root object does not have a CPU set, e.g. if the topology is made of different machines.</dl>
<h3>static unsigned hwloc_get_nbobjs_inside_cpuset_by_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth) [inline], [static]</h3>
<p> Return the number of objects at depth depth included in CPU set set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects at the given depth do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static int hwloc_get_nbobjs_inside_cpuset_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type) [inline], [static]</h3>
<p> Return the number of objects of type type included in CPU set set. If no object for that type exists inside CPU set set, 0 is returned. If there are several levels with objects of that type inside CPU set set, -1 is returned. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects of the given type do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_inside_cpuset_by_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Return the next object at depth depth included in CPU set set. If prev is NULL, return the first object at depth depth included in set. The next invokation should pass the previous return value in prev so as to obtain the next object in set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects at the given depth do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_inside_cpuset_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Return the next object of type type included in CPU set set. If there are multiple or no depth for given type, return NULL and let the caller fallback to <code>hwloc_get_next_obj_inside_cpuset_by_depth()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects of the given type do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static int hwloc_get_obj_index_inside_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_t</code> obj) [inline], [static]</h3>
<p> Return the logical index among the objects included in CPU set set. Consult all objects in the same level as obj and inside CPU set set in the logical order, and return the index of obj within them. If set covers the entire topology, this is the logical index of obj. Otherwise, this is similar to a logical index within the part of the topology defined by CPU set set.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_inside_cpuset_by_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, unsigned depth, unsigned idx) [inline], [static]</h3>
<p> Return the (logically) idx -th object at depth depth included in CPU set set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects at the given depth do not have CPU sets or if the topology is made of different machines.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_inside_cpuset_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, <code>hwloc_obj_type_t</code> type, unsigned idx) [inline], [static]</h3>
<p> Return the idx -th object of type type included in CPU set set. If there are multiple or no depth for given type, return NULL and let the caller fallback to <code>hwloc_get_obj_inside_cpuset_by_depth()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if objects of the given type do not have CPU sets or if the topology is made of different machines.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
