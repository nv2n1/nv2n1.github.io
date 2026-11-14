---
title: "hwloc_get_cache_covering_cpuset(3)"
name: "hwloc_get_cache_covering_cpuset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_cache_covering_cpuset/"
description: "hwlocality_helper_find_cache – Looking at Cache Objects"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_find_cache &#8211; Looking at Cache Objects </p>
<h3>Functions</h3>
<p> static int <code>hwloc_get_cache_type_depth</code> (<code>hwloc_topology_t</code> topology, unsigned cachelevel, <code>hwloc_obj_cache_type_t</code> cachetype) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_cache_covering_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_shared_cache_covering_obj</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static <code>hwloc_obj_t</code> hwloc_get_cache_covering_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the first cache covering a cpuset set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no cache matches.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function cannot work if the root object does not have a CPU set, e.g. if the topology is made of different machines.</dl>
<h3>static int hwloc_get_cache_type_depth (<code>hwloc_topology_t</code> topology, unsigned cachelevel, <code>hwloc_obj_cache_type_t</code> cachetype) [inline], [static]</h3>
<p> Find the depth of cache objects matching cache depth and type. Return the depth of the topology level that contains cache objects whose attributes match cachedepth and cachetype. This function intends to disambiguate the case where <code>hwloc_get_type_depth()</code> returns <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>. </p>
<p> If no cache level matches, <code>HWLOC_TYPE_DEPTH_UNKNOWN</code> is returned. </p>
<p> If cachetype is <code>HWLOC_OBJ_CACHE_UNIFIED</code>, the depth of the unique matching unified cache level is returned. </p>
<p> If cachetype is <code>HWLOC_OBJ_CACHE_DATA</code> or <code>HWLOC_OBJ_CACHE_INSTRUCTION</code>, either a matching cache, or a unified cache is returned. </p>
<p> If cachetype is -1, it is ignored and multiple levels may match. The function returns either the depth of a uniquely matching level or <code>HWLOC_TYPE_DEPTH_MULTIPLE</code>.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_shared_cache_covering_obj (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj) [inline], [static]</h3>
<p> Get the first cache shared between an object and somebody else. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if no cache matches or if an invalid object is given.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
