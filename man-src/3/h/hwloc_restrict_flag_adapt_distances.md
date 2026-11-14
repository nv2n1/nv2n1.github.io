---
title: "hwloc_restrict_flag_adapt_distances(3)"
name: "hwloc_restrict_flag_adapt_distances"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_restrict_flag_adapt_distances/"
description: "hwlocality_tinker – Modifying a loaded Topology"
---

<p>hwlocality_tinker &#8211; Modifying a loaded Topology </p>
<h3>Enumerations</h3>
<p>enum <code>hwloc_restrict_flags_e</code> { <code>HWLOC_RESTRICT_FLAG_ADAPT_DISTANCES</code>, <code>HWLOC_RESTRICT_FLAG_ADAPT_MISC</code>, <code>HWLOC_RESTRICT_FLAG_ADAPT_IO</code> } </p>
<h3>Functions</h3>
<p><code>hwloc_obj_t</code> <code>hwloc_topology_insert_misc_object_by_cpuset</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, const char *name) </p>
<p> <code>hwloc_obj_t</code> <code>hwloc_topology_insert_misc_object_by_parent</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, const char *name) </p>
<p> int <code>hwloc_topology_restrict</code> (<code>hwloc_topology_t</code> restrict topology, <code>hwloc_const_cpuset_t</code> cpuset, unsigned long flags) </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_restrict_flags_e</code></h3>
<p>Flags to be given to <code>hwloc_topology_restrict()</code>. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_RESTRICT_FLAG_ADAPT_DISTANCES </i></p>
<dd>Adapt distance matrices according to objects being removed during restriction. If this flag is not set, distance matrices are removed.</p>
<dt><i>HWLOC_RESTRICT_FLAG_ADAPT_MISC </i></p>
<dd>Move Misc objects to ancestors if their parents are removed during restriction. If this flag is not set, Misc objects are removed when their parents are removed.</p>
<dt><i>HWLOC_RESTRICT_FLAG_ADAPT_IO </i></p>
<dd>Move I/O objects to ancestors if their parents are removed during restriction. If this flag is not set, I/O devices and bridges are removed when their parents are removed.</dl>
<h2>Function Documentation</h2>
<h3><code>hwloc_obj_t</code> hwloc_topology_insert_misc_object_by_cpuset (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> cpuset, const char * name)</h3>
<p>Add a MISC object to the topology. A new MISC object will be created and inserted into the topology at the position given by bitmap cpuset. This offers a way to add new intermediate levels to the topology hierarchy. </p>
<p> cpuset and name will be copied to setup the new object attributes. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the newly-created object. </p>
<p> NULL if the insertion conflicts with the existing topology tree.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If name contains some non-printable characters, they will be dropped when exporting to XML, see <code>hwloc_topology_export_xml()</code>.</dl>
<h3><code>hwloc_obj_t</code> hwloc_topology_insert_misc_object_by_parent (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> parent, const char * name)</h3>
<p>Add a MISC object as a leaf of the topology. A new MISC object will be created and inserted into the topology at the position given by parent. It is appended to the list of existing children, without ever adding any intermediate hierarchy level. This is useful for annotating the topology without actually changing the hierarchy. </p>
<p> name will be copied to the setup the new object attributes. However, the new leaf object will not have any cpuset. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the newly-created object</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If name contains some non-printable characters, they will be dropped when exporting to XML, see <code>hwloc_topology_export_xml()</code>.</dl>
<h3>int hwloc_topology_restrict (<code>hwloc_topology_t</code> restrict topology, <code>hwloc_const_cpuset_t</code> cpuset, unsigned long flags)</h3>
<p>Restrict the topology to the given CPU set. Topology topology is modified so as to remove all objects that are not included (or partially included) in the CPU set cpuset. All objects CPU and node sets are restricted accordingly. </p>
<p> flags is a OR&#8217;ed set of <code>hwloc_restrict_flags_e</code>. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This call may not be reverted by restricting back to a larger cpuset. Once dropped during restriction, objects may not be brought back, except by loading another topology with <code>hwloc_topology_load()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success. </p>
<p> -1 with errno set to EINVAL if the input cpuset is invalid. The topology is not modified in this case. </p>
<p> -1 with errno set to ENOMEM on failure to allocate internal data. The topology is reinitialized in this case. It should be either destroyed with <code>hwloc_topology_destroy()</code> or configured and loaded again.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code.</p>
