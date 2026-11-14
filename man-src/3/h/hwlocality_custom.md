---
title: "hwlocality_custom(3)"
name: "hwlocality_custom"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwlocality_custom/"
description: "hwlocality_custom – Building Custom Topologies"
---

<h2 class="name">NAME</h2>
<p> hwlocality_custom &#8211; Building Custom Topologies </p>
<h3>Functions</h3>
<p> int <code>hwloc_custom_insert_topology</code> (<code>hwloc_topology_t</code> newtopology, <code>hwloc_obj_t</code> newparent, <code>hwloc_topology_t</code> oldtopology, <code>hwloc_obj_t</code> oldroot) </p>
<p> <code>hwloc_obj_t</code> <code>hwloc_custom_insert_group_object_by_parent</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, int groupdepth) </p>
<h2>Detailed Description</h2>
<p> A custom topology may be initialized by calling <code>hwloc_topology_set_custom()</code> after <code>hwloc_topology_init()</code>. It may then be modified by inserting objects or entire topologies. Once done assembling, <code>hwloc_topology_load()</code> should be invoked as usual to finalize the topology.</p>
<h2>Function Documentation</h2>
<h3><code>hwloc_obj_t</code> hwloc_custom_insert_group_object_by_parent (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, int groupdepth)</h3>
<p> Insert a new group object inside a custom topology. An object with type <code>HWLOC_OBJ_GROUP</code> is inserted as a new child of object parent. </p>
<p> groupdepth is the depth attribute to be given to the new object. It may for instance be 0 for top-level groups, 1 for their children, and so on. </p>
<p> The custom topology newtopology must have been prepared with <code>hwloc_topology_set_custom()</code> and not loaded with <code>hwloc_topology_load()</code> yet. </p>
<p> parent may be either the root of topology or an object that was added earlier through <code>hwloc_custom_insert_group_object_by_parent()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The cpuset and nodeset of the new group object are NULL because these sets are meaningless when assembling multiple topologies. </p>
<p> The cpuset and nodeset of the parent object are not modified.</dl>
<h3>int hwloc_custom_insert_topology (<code>hwloc_topology_t</code> newtopology, <code>hwloc_obj_t</code> newparent, <code>hwloc_topology_t</code> oldtopology, <code>hwloc_obj_t</code> oldroot)</h3>
<p> Insert an existing topology inside a custom topology. Duplicate the existing topology oldtopology inside a new custom topology newtopology as a leaf of object newparent. </p>
<p> If oldroot is not NULL, duplicate oldroot and all its children instead of the entire oldtopology. Passing the root object of oldtopology in oldroot is equivalent to passing NULL. </p>
<p> The custom topology newtopology must have been prepared with <code>hwloc_topology_set_custom()</code> and not loaded with <code>hwloc_topology_load()</code> yet. </p>
<p> newparent may be either the root of newtopology or an object that was added through <code>hwloc_custom_insert_group_object_by_parent()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The cpuset and nodeset of the newparent object are not modified based on the contents of oldtopology.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
