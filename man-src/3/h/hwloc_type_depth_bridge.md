---
title: "hwloc_type_depth_bridge(3)"
name: "hwloc_type_depth_bridge"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_type_depth_bridge/"
description: "hwlocality_levels – Object levels, depths and types"
---

<p>hwlocality_levels &#8211; Object levels, depths and types </p>
<h3>Enumerations</h3>
<p>enum <code>hwloc_get_type_depth_e</code> { <code>HWLOC_TYPE_DEPTH_UNKNOWN</code>, <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>, <code>HWLOC_TYPE_DEPTH_BRIDGE</code>, <code>HWLOC_TYPE_DEPTH_PCI_DEVICE</code>, <code>HWLOC_TYPE_DEPTH_OS_DEVICE</code> } </p>
<h3>Functions</h3>
<p>unsigned <code>hwloc_topology_get_depth</code> (<code>hwloc_topology_t</code> restrict topology) </p>
<p> int <code>hwloc_get_type_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> static int <code>hwloc_get_type_or_below_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> static int <code>hwloc_get_type_or_above_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> <code>hwloc_obj_type_t</code> <code>hwloc_get_depth_type</code> (<code>hwloc_topology_t</code> topology, unsigned depth) </p>
<p> unsigned <code>hwloc_get_nbobjs_by_depth</code> (<code>hwloc_topology_t</code> topology, unsigned depth) </p>
<p> static int <code>hwloc_get_nbobjs_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_root_obj</code> (<code>hwloc_topology_t</code> topology) </p>
<p> <code>hwloc_obj_t</code> <code>hwloc_get_obj_by_depth</code> (<code>hwloc_topology_t</code> topology, unsigned depth, unsigned idx) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_obj_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, unsigned idx) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_by_depth</code> (<code>hwloc_topology_t</code> topology, unsigned depth, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_obj_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) </p>
<h2>Detailed Description</h2>
<p>Be sure to see the figure in <code>Terms and Definitions</code> that shows a complete topology tree, including depths, child/sibling/cousin relationships, and an example of an asymmetric topology where one package has fewer caches than its peers.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_get_type_depth_e</code></h3>
<p><code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_TYPE_DEPTH_UNKNOWN </i></p>
<dd>No object of given type exists in the topology.</p>
<dt><i>HWLOC_TYPE_DEPTH_MULTIPLE </i></p>
<dd>Objects of given type exist at different depth in the topology.</p>
<dt><i>HWLOC_TYPE_DEPTH_BRIDGE </i></p>
<dd>Virtual depth for bridge object level.</p>
<dt><i>HWLOC_TYPE_DEPTH_PCI_DEVICE </i></p>
<dd>Virtual depth for PCI device object level.</p>
<dt><i>HWLOC_TYPE_DEPTH_OS_DEVICE </i></p>
<dd>Virtual depth for software device object level.</dl>
<h2>Function Documentation</h2>
<h3><code>hwloc_obj_type_t</code> hwloc_get_depth_type (<code>hwloc_topology_t</code> topology, unsigned depth)</h3>
<p>Returns the type of objects at depth depth. depth should between 0 and <code>hwloc_topology_get_depth()</code>-1. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>-1 if depth depth does not exist.</dl>
<h3>unsigned hwloc_get_nbobjs_by_depth (<code>hwloc_topology_t</code> topology, unsigned depth)</h3>
<p>Returns the width of level at depth depth.</p>
<h3>static int hwloc_get_nbobjs_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) [inline], [static]</h3>
<p>Returns the width of level type type. If no object for that type exists, 0 is returned. If there are several levels with objects of that type, -1 is returned.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_by_depth (<code>hwloc_topology_t</code> topology, unsigned depth, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p>Returns the next object at depth depth. If prev is NULL, return the first object at depth depth.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_obj_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p>Returns the next object of type type. If prev is NULL, return the first object at type type. If there are multiple or no depth for given type, return NULL and let the caller fallback to <code>hwloc_get_next_obj_by_depth()</code>.</p>
<h3><code>hwloc_obj_t</code> hwloc_get_obj_by_depth (<code>hwloc_topology_t</code> topology, unsigned depth, unsigned idx)</h3>
<p>Returns the topology object at logical index idx from depth depth.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_obj_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, unsigned idx) [inline], [static]</h3>
<p>Returns the topology object at logical index idx with type type. If no object for that type exists, NULL is returned. If there are several levels with objects of that type, NULL is returned and ther caller may fallback to <code>hwloc_get_obj_by_depth()</code>.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_root_obj (<code>hwloc_topology_t</code> topology) [inline], [static]</h3>
<p>Returns the top-object of the topology-tree. Its type is typically <code>HWLOC_OBJ_MACHINE</code> but it could be different for complex topologies.</p>
<h3>int hwloc_get_type_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type)</h3>
<p>Returns the depth of objects of type type. If no object of this type is present on the underlying architecture, or if the OS doesn&#8217;t provide this kind of information, the function returns <code>HWLOC_TYPE_DEPTH_UNKNOWN</code>. </p>
<p> If type is absent but a similar type is acceptable, see also <code>hwloc_get_type_or_below_depth()</code> and <code>hwloc_get_type_or_above_depth()</code>. </p>
<p> If some objects of the given type exist in different levels, for instance L1 and L2 caches, or L1i and L1d caches, the function returns <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>. See <code>hwloc_get_cache_type_depth()</code> in <code>hwloc/helper.h</code> to better handle this case. </p>
<p> If an I/O object type is given, the function returns a virtual value because I/O objects are stored in special levels that are not CPU-related. This virtual depth may be passed to other hwloc functions such as <code>hwloc_get_obj_by_depth()</code> but it should not be considered as an actual depth by the application. In particular, it should not be compared with any other object depth or with the entire topology depth.</p>
<h3>static int hwloc_get_type_or_above_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) [inline], [static]</h3>
<p>Returns the depth of objects of type type or above. If no object of this type is present on the underlying architecture, the function returns the depth of the first &#8216;present&#8217; object typically containing type. </p>
<p> If some objects of the given type exist in different levels, for instance L1 and L2 caches, the function returns <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>.</p>
<h3>static int hwloc_get_type_or_below_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) [inline], [static]</h3>
<p>Returns the depth of objects of type type or below. If no object of this type is present on the underlying architecture, the function returns the depth of the first &#8216;present&#8217; object typically found inside type. </p>
<p> If some objects of the given type exist in different levels, for instance L1 and L2 caches, the function returns <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>.</p>
<h3>unsigned hwloc_topology_get_depth (<code>hwloc_topology_t</code> restrict topology)</h3>
<p>Get the depth of the hierarchical tree of objects. This is the depth of <code>HWLOC_OBJ_PU</code> objects plus one.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code.</p>
