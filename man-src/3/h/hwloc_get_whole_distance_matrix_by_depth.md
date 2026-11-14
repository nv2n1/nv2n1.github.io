---
title: "hwloc_get_whole_distance_matrix_by_depth(3)"
name: "hwloc_get_whole_distance_matrix_by_depth"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_whole_distance_matrix_by_depth/"
description: "hwlocality_distances – Manipulating Distances"
---

<h2 class="name">NAME</h2>
<p> hwlocality_distances &#8211; Manipulating Distances </p>
<h3>Functions</h3>
<p> static const struct <code>hwloc_distances_s</code> * <code>hwloc_get_whole_distance_matrix_by_depth</code> (<code>hwloc_topology_t</code> topology, unsigned depth) </p>
<p> static const struct <code>hwloc_distances_s</code> * <code>hwloc_get_whole_distance_matrix_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) </p>
<p> static const struct <code>hwloc_distances_s</code> * <code>hwloc_get_distance_matrix_covering_obj_by_depth</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, unsigned depth, unsigned *firstp) </p>
<p> static int <code>hwloc_get_latency</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj1, <code>hwloc_obj_t</code> obj2, float *latency, float *reverse_latency) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static const struct <code>hwloc_distances_s</code>* hwloc_get_distance_matrix_covering_obj_by_depth (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, unsigned depth, unsigned * firstp) [static]</h3>
<p> Get distances for the given depth and covering some objects. Return a distance matrix that describes depth depth and covers at least object obj and all its children. </p>
<p> When looking for the distance between some objects, a common ancestor should be passed in obj. </p>
<p> firstp is set to logical index of the first object described by the matrix. </p>
<p> The returned structure belongs to the hwloc library. The caller should not modify or free it.</p>
<h3>static int hwloc_get_latency (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj1, <code>hwloc_obj_t</code> obj2, float * latency, float * reverse_latency) [inline], [static]</h3>
<p> Get the latency in both directions between two objects. Look at ancestor objects from the bottom to the top until one of them contains a distance matrix that matches the objects exactly. </p>
<p> latency gets the value from object obj1 to obj2, while reverse_latency gets the reverse-direction value, which may be different on some architectures. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 if no ancestor contains a matching latency matrix.</dl>
<h3>static const struct <code>hwloc_distances_s</code>* hwloc_get_whole_distance_matrix_by_depth (<code>hwloc_topology_t</code> topology, unsigned depth) [static]</h3>
<p> Get the distances between all objects at the given depth. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a distances structure containing a matrix with all distances between all objects at the given depth.</dl>
<p> Slot i+nbobjs*j contains the distance from the object of logical index i the object of logical index j. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function only returns matrices covering the whole topology, without any unknown distance value. Those matrices are available in top-level object of the hierarchy. Matrices of lower objects are not reported here since they cover only part of the machine.</dl>
<p> The returned structure belongs to the hwloc library. The caller should not modify or free it. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no such distance matrix exists.</dl>
<h3>static const struct <code>hwloc_distances_s</code>* hwloc_get_whole_distance_matrix_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type) [static]</h3>
<p> Get the distances between all objects of a given type. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a distances structure containing a matrix with all distances between all objects of the given type.</dl>
<p> Slot i+nbobjs*j contains the distance from the object of logical index i the object of logical index j. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function only returns matrices covering the whole topology, without any unknown distance value. Those matrices are available in top-level object of the hierarchy. Matrices of lower objects are not reported here since they cover only part of the machine.</dl>
<p> The returned structure belongs to the hwloc library. The caller should not modify or free it. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no such distance matrix exists.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
