---
title: "hwloc_obj_is_in_subtree(3)"
name: "hwloc_obj_is_in_subtree"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_is_in_subtree/"
description: "hwlocality_helper_ancestors – Looking at Ancestor and Child Objects"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_ancestors &#8211; Looking at Ancestor and Child Objects </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_ancestor_obj_by_depth</code> (<code>hwloc_topology_t</code> topology, unsigned depth, <code>hwloc_obj_t</code> obj) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_ancestor_obj_by_type</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> obj) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_common_ancestor_obj</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj1, <code>hwloc_obj_t</code> obj2) </p>
<p> static int <code>hwloc_obj_is_in_subtree</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, <code>hwloc_obj_t</code> subtree_root) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_child</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, <code>hwloc_obj_t</code> prev) </p>
<h2>Detailed Description</h2>
<p> Be sure to see the figure in <code>Terms and Definitions</code> that shows a complete topology tree, including depths, child/sibling/cousin relationships, and an example of an asymmetric topology where one package has fewer caches than its peers.</p>
<h2>Function Documentation</h2>
<h3>static <code>hwloc_obj_t</code> hwloc_get_ancestor_obj_by_depth (<code>hwloc_topology_t</code> topology, unsigned depth, <code>hwloc_obj_t</code> obj) [inline], [static]</h3>
<p> Returns the ancestor object of obj at depth depth.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_ancestor_obj_by_type (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_type_t</code> type, <code>hwloc_obj_t</code> obj) [inline], [static]</h3>
<p> Returns the ancestor object of obj with type type.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_common_ancestor_obj (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj1, <code>hwloc_obj_t</code> obj2) [inline], [static]</h3>
<p> Returns the common parent object to objects obj1 and obj2.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_child (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Return the next child. If prev is NULL, return the first child.</p>
<h3>static int hwloc_obj_is_in_subtree (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, <code>hwloc_obj_t</code> subtree_root) [inline], [static]</h3>
<p> Returns true if obj is inside the subtree beginning with ancestor object subtree_root. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function assumes that both obj and subtree_root have a cpuset.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
