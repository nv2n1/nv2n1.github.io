---
title: "hwloc_obj(3)"
name: "hwloc_obj"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj/"
description: "hwloc_obj –"
---

<h2 class="name">NAME</h2>
<p> hwloc_obj &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>hwloc_obj_type_t</code> <code>type</code> </p>
<p> unsigned <code>os_index</code> </p>
<p> char * <code>name</code> </p>
<p> struct <code>hwloc_obj_memory_s</code> <code>memory</code> </p>
<p> union <code>hwloc_obj_attr_u</code> * <code>attr</code> </p>
<p> unsigned <code>depth</code> </p>
<p> unsigned <code>logical_index</code> </p>
<p> signed <code>os_level</code> </p>
<p> struct <code>hwloc_obj</code> * <code>next_cousin</code> </p>
<p> struct <code>hwloc_obj</code> * <code>prev_cousin</code> </p>
<p> struct <code>hwloc_obj</code> * <code>parent</code> </p>
<p> unsigned <code>sibling_rank</code> </p>
<p> struct <code>hwloc_obj</code> * <code>next_sibling</code> </p>
<p> struct <code>hwloc_obj</code> * <code>prev_sibling</code> </p>
<p> unsigned <code>arity</code> </p>
<p> struct <code>hwloc_obj</code> ** <code>children</code> </p>
<p> struct <code>hwloc_obj</code> * <code>first_child</code> </p>
<p> struct <code>hwloc_obj</code> * <code>last_child</code> </p>
<p> void * <code>userdata</code> </p>
<p> <code>hwloc_cpuset_t</code> <code>cpuset</code> </p>
<p> <code>hwloc_cpuset_t</code> <code>complete_cpuset</code> </p>
<p> <code>hwloc_cpuset_t</code> <code>online_cpuset</code> </p>
<p> <code>hwloc_cpuset_t</code> <code>allowed_cpuset</code> </p>
<p> <code>hwloc_nodeset_t</code> <code>nodeset</code> </p>
<p> <code>hwloc_nodeset_t</code> <code>complete_nodeset</code> </p>
<p> <code>hwloc_nodeset_t</code> <code>allowed_nodeset</code> </p>
<p> struct <code>hwloc_distances_s</code> ** <code>distances</code> </p>
<p> unsigned <code>distances_count</code> </p>
<p> struct <code>hwloc_obj_info_s</code> * <code>infos</code> </p>
<p> unsigned <code>infos_count</code> </p>
<p> int <code>symmetric_subtree</code> </p>
<h2>Detailed Description</h2>
<p> Structure of a topology object. </p>
<p> Applications must not modify any field except <code>hwloc_obj.userdata</code>.</p>
<h2>Field Documentation</h2>
<h3><code>hwloc_cpuset_t</code> hwloc_obj::allowed_cpuset</h3>
<p> The CPU set of allowed logical processors. This includes the CPUs contained in this object which are allowed for binding, i.e. passing them to the hwloc binding functions should not return permission errors. This is usually restricted by administration rules. Some of them may however be offline so binding to them may still not be possible, see online_cpuset. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3><code>hwloc_nodeset_t</code> hwloc_obj::allowed_nodeset</h3>
<p> The set of allowed NUMA memory nodes. This includes the NUMA memory nodes contained in this object which are allowed for memory allocation, i.e. passing them to NUMA node-directed memory allocation should not return permission errors. This is usually restricted by administration rules. </p>
<p> If there are no NUMA nodes in the machine, all the memory is close to this object, so allowed_nodeset is full. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3>unsigned hwloc_obj::arity</h3>
<p> Number of children.</p>
<h3>union <code>hwloc_obj_attr_u</code>* hwloc_obj::attr</h3>
<p> Object type-specific Attributes, may be NULL if no attribute value was found.</p>
<h3>struct <code>hwloc_obj</code>** hwloc_obj::children</h3>
<p> Children, children[0 .. arity -1].</p>
<h3><code>hwloc_cpuset_t</code> hwloc_obj::complete_cpuset</h3>
<p> The complete CPU set of logical processors of this object,. This includes not only the same as the cpuset field, but also the CPUs for which topology information is unknown or incomplete, and the CPUs that are ignored when the <code>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM</code> flag is not set. Thus no corresponding PU object may be found in the topology, because the precise position is undefined. It is however known that it would be somewhere under this object. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3><code>hwloc_nodeset_t</code> hwloc_obj::complete_nodeset</h3>
<p> The complete NUMA node set of this object,. This includes not only the same as the nodeset field, but also the NUMA nodes for which topology information is unknown or incomplete, and the nodes that are ignored when the <code>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM</code> flag is not set. Thus no corresponding NODE object may be found in the topology, because the precise position is undefined. It is however known that it would be somewhere under this object. </p>
<p> If there are no NUMA nodes in the machine, all the memory is close to this object, so complete_nodeset is full. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3><code>hwloc_cpuset_t</code> hwloc_obj::cpuset</h3>
<p> CPUs covered by this object. This is the set of CPUs for which there are PU objects in the topology under this object, i.e. which are known to be physically contained in this object and known how (the children path between this object and the PU objects). </p>
<p> If the <code>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM</code> configuration flag is set, some of these CPUs may be offline, or not allowed for binding, see online_cpuset and allowed_cpuset. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3>unsigned hwloc_obj::depth</h3>
<p> Vertical index in the hierarchy. If the topology is symmetric, this is equal to the parent depth plus one, and also equal to the number of parent/child links from the root object to here.</p>
<h3>struct <code>hwloc_distances_s</code>** hwloc_obj::distances</h3>
<p> Distances between all objects at same depth below this object.</p>
<h3>unsigned hwloc_obj::distances_count</h3>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::first_child</h3>
<p> First child.</p>
<h3>struct <code>hwloc_obj_info_s</code>* hwloc_obj::infos</h3>
<p> Array of stringified info type=name.</p>
<h3>unsigned hwloc_obj::infos_count</h3>
<p> Size of infos array.</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::last_child</h3>
<p> Last child.</p>
<h3>unsigned hwloc_obj::logical_index</h3>
<p> Horizontal index in the whole list of similar objects, hence guaranteed unique across the entire machine. Could be a &#8216;cousin_rank&#8217; since it&#8217;s the rank within the &#8216;cousin&#8217; list below.</p>
<h3>struct <code>hwloc_obj_memory_s</code> hwloc_obj::memory</h3>
<p> Memory attributes.</p>
<h3>char* hwloc_obj::name</h3>
<p> Object description if any.</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::next_cousin</h3>
<p> Next object of same type and depth.</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::next_sibling</h3>
<p> Next object below the same parent.</p>
<h3><code>hwloc_nodeset_t</code> hwloc_obj::nodeset</h3>
<p> NUMA nodes covered by this object or containing this object. This is the set of NUMA nodes for which there are NODE objects in the topology under or above this object, i.e. which are known to be physically contained in this object or containing it and known how (the children path between this object and the NODE objects). </p>
<p> In the end, these nodes are those that are close to the current object. </p>
<p> If the <code>HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM</code> configuration flag is set, some of these nodes may not be allowed for allocation, see allowed_nodeset. </p>
<p> If there are no NUMA nodes in the machine, all the memory is close to this object, so nodeset is full. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3><code>hwloc_cpuset_t</code> hwloc_obj::online_cpuset</h3>
<p> The CPU set of online logical processors. This includes the CPUs contained in this object that are online, i.e. draw power and can execute threads. It may however not be allowed to bind to them due to administration rules, see allowed_cpuset. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Its value must not be changed, <code>hwloc_bitmap_dup()</code> must be used instead.</dl>
<h3>unsigned hwloc_obj::os_index</h3>
<p> OS-provided physical index number. It is not guaranteed unique across the entire machine, except for PUs and NUMA nodes.</p>
<h3>signed hwloc_obj::os_level</h3>
<p> OS-provided physical level, -1 if unknown or meaningless.</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::parent</h3>
<p> Parent, NULL if root (system object)</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::prev_cousin</h3>
<p> Previous object of same type and depth.</p>
<h3>struct <code>hwloc_obj</code>* hwloc_obj::prev_sibling</h3>
<p> Previous object below the same parent.</p>
<h3>unsigned hwloc_obj::sibling_rank</h3>
<p> Index in parent&#8217;s children[] array.</p>
<h3>int hwloc_obj::symmetric_subtree</h3>
<p> Set if the subtree of objects below this object is symmetric, which means all children and their children have identical subtrees. If set in the topology root object, lstopo may export the topology as a synthetic string.</p>
<h3><code>hwloc_obj_type_t</code> hwloc_obj::type</h3>
<p> Type of object.</p>
<h3>void* hwloc_obj::userdata</h3>
<p> Application-given private data pointer, initialized to NULL, use it as you wish. See <code>hwloc_topology_set_userdata_export_callback()</code> if you wish to export this field to XML. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBL">Author</a></p>
<dd></dl>
