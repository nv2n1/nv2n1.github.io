---
title: "hwloc_get_obj_below_by_type(3)"
name: "hwloc_get_obj_below_by_type"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_obj_below_by_type/"
description: "hwlocality_helper_find_misc – Finding objects, miscellaneous helpers"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_find_misc &#8211; Finding objects, miscellaneous helpers </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_pu_obj_by_os_index</code> (<code>hwloc_topology_t</code> topology, unsigned os_index) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_numanode_obj_by_os_index</code> (<code>hwloc_topology_t</code> topology, unsigned os_index) </p>
<p> unsigned <code>hwloc_get_closest_objs</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> src, <code>hwloc_obj_t</code> *restrict objs, unsigned max) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_below_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type1, unsigned idx1, <code>hwloc_obj_type_t</code> type2, unsigned idx2) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_below_array_by_type</code> (<code>hwloc_topology_t</code> topology, int nr, <code>hwloc_obj_type_t</code> *typev, unsigned *idxv) </p>
<h2>Detailed Description</h2>
<p> Be sure to see the figure in <code>Terms and Definitions</code> that shows a complete topology tree, including depths, child/sibling/cousin relationships, and an example of an asymmetric topology where one package has fewer caches than its peers.</p>
<h2>Function Documentation</h2>
<h3>unsigned hwloc_get_closest_objs (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> src, <code>hwloc_obj_t</code> *restrict objs, unsigned max)</h3>
<p> Do a depth-first traversal of the topology to find and sort. all objects that are at the same depth than src. Report in objs up to max physically closest ones to src. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of objects returned in objs. </p>
<p> 0 if src is an I/O object.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function requires the src object to have a CPU set.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_numanode_obj_by_os_index (<code>hwloc_topology_t</code> topology, unsigned os_index) [inline], [static]</h3>
<p> Returns the object of type <code>HWLOC_OBJ_NUMANODE</code> with os_index. This function is useful for converting a nodeset into the NUMA node objects it contains. When retrieving the current binding (e.g. with <code>hwloc_get_membind_nodeset()</code>), one may iterate over the bits of the resulting nodeset with <code>hwloc_bitmap_foreach_begin()</code>, and find the corresponding NUMA nodes with this function.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_below_array_by_type (<code>hwloc_topology_t</code> topology, int nr, <code>hwloc_obj_type_t</code> * typev, unsigned * idxv) [inline], [static]</h3>
<p> Find an object below a chain of objects specified by types and indexes. This is a generalized version of <code>hwloc_get_obj_below_by_type()</code>. </p>
<p> Arrays typev and idxv must contain nr types and indexes. </p>
<p> Start from the top system object and walk the arrays typev and idxv. For each type and logical index couple in the arrays, look under the previously found object to find the index-th object of the given type. Indexes are specified within the parent, not withing the entire system. </p>
<p> For instance, if nr is 3, typev contains NODE, PACKAGE and CORE, and idxv contains 0, 1 and 2, return the third core object below the second package below the first NUMA node. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function requires all these objects and the root object to have a CPU set.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_below_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type1, unsigned idx1, <code>hwloc_obj_type_t</code> type2, unsigned idx2) [inline], [static]</h3>
<p> Find an object below another object, both specified by types and indexes. Start from the top system object and find object of type type1 and logical index idx1. Then look below this object and find another object of type type2 and logical index idx2. Indexes are specified within the parent, not withing the entire system. </p>
<p> For instance, if type1 is PACKAGE, idx1 is 2, type2 is CORE and idx2 is 3, return the fourth core object below the third package. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function requires these objects to have a CPU set.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_pu_obj_by_os_index (<code>hwloc_topology_t</code> topology, unsigned os_index) [inline], [static]</h3>
<p> Returns the object of type <code>HWLOC_OBJ_PU</code> with os_index. This function is useful for converting a CPU set into the PU objects it contains. When retrieving the current binding (e.g. with <code>hwloc_get_cpubind()</code>), one may iterate over the bits of the resulting CPU set with <code>hwloc_bitmap_foreach_begin()</code>, and find the corresponding PUs with this function.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
