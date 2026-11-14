---
title: "hwloc_cpuset_t(3)"
name: "hwloc_cpuset_t"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_cpuset_t/"
description: "hwlocality_object_sets – Object Sets (hwloc_cpuset_t and hwloc_nodeset_t)"
---

<h2 class="name">NAME</h2>
<p> hwlocality_object_sets &#8211; Object Sets (hwloc_cpuset_t and hwloc_nodeset_t) </p>
<h3>Typedefs</h3>
<p> typedef <code>hwloc_bitmap_t</code> <code>hwloc_cpuset_t</code> </p>
<p> typedef <code>hwloc_const_bitmap_t</code> <code>hwloc_const_cpuset_t</code> </p>
<p> typedef <code>hwloc_bitmap_t</code> <code>hwloc_nodeset_t</code> </p>
<p> typedef <code>hwloc_const_bitmap_t</code> <code>hwloc_const_nodeset_t</code> </p>
<h2>Detailed Description</h2>
<p> Hwloc uses bitmaps to represent two distinct kinds of object sets: CPU sets (<code>hwloc_cpuset_t</code>) and NUMA node sets (<code>hwloc_nodeset_t</code>). These types are both typedefs to a common back end type (<code>hwloc_bitmap_t</code>), and therefore all the hwloc bitmap functions are applicable to both <code>hwloc_cpuset_t</code> and <code>hwloc_nodeset_t</code> (see <code>The bitmap API</code>). </p>
<p> The rationale for having two different types is that even though the actions one wants to perform on these types are the same (e.g., enable and disable individual items in the set/mask), they&#8217;re used in very different contexts: one for specifying which processors to use and one for specifying which NUMA nodes to use. Hence, the name difference is really just to reflect the intent of where the type is used.</p>
<h2>Typedef Documentation</h2>
<h3>typedef <code>hwloc_const_bitmap_t</code> <code>hwloc_const_cpuset_t</code></h3>
<p> A non-modifiable <code>hwloc_cpuset_t</code>.</p>
<h3>typedef <code>hwloc_const_bitmap_t</code> <code>hwloc_const_nodeset_t</code></h3>
<p> A non-modifiable <code>hwloc_nodeset_t</code>.</p>
<h3>typedef <code>hwloc_bitmap_t</code> <code>hwloc_cpuset_t</code></h3>
<p> A CPU set is a bitmap whose bits are set according to CPU physical OS indexes. It may be consulted and modified with the bitmap API as any <code>hwloc_bitmap_t</code> (see <code>hwloc/bitmap.h</code>). </p>
<p> Each bit may be converted into a PU object using <code>hwloc_get_pu_obj_by_os_index()</code>.</p>
<h3>typedef <code>hwloc_bitmap_t</code> <code>hwloc_nodeset_t</code></h3>
<p> A node set is a bitmap whose bits are set according to NUMA memory node physical OS indexes. It may be consulted and modified with the bitmap API as any <code>hwloc_bitmap_t</code> (see <code>hwloc/bitmap.h</code>). Each bit may be converted into a NUMA node object using <code>hwloc_get_numanode_obj_by_os_index()</code>. </p>
<p> When binding memory on a system without any NUMA node (when the whole memory is considered as a single memory bank), the nodeset may be either empty (no memory selected) or full (whole system memory selected). </p>
<p> See also <code>Converting between CPU sets and node sets</code>.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
