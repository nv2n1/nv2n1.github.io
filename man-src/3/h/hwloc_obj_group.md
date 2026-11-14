---
title: "hwloc_obj_group(3)"
name: "hwloc_obj_group"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_group/"
description: "hwlocality_object_types – Object Types"
---

<p>hwlocality_object_types &#8211; Object Types </p>
<h3>Typedefs</h3>
<p>typedef enum <code>hwloc_obj_cache_type_e</code> <code>hwloc_obj_cache_type_t</code> </p>
<p> typedef enum <code>hwloc_obj_bridge_type_e</code> <code>hwloc_obj_bridge_type_t</code> </p>
<p> typedef enum <code>hwloc_obj_osdev_type_e</code> <code>hwloc_obj_osdev_type_t</code> </p>
<h3>Enumerations</h3>
<p>enum <code>hwloc_obj_type_t</code> { <code>HWLOC_OBJ_SYSTEM</code>, <code>HWLOC_OBJ_MACHINE</code>, <code>HWLOC_OBJ_NUMANODE</code>, <code>HWLOC_OBJ_PACKAGE</code>, <code>HWLOC_OBJ_CACHE</code>, <code>HWLOC_OBJ_CORE</code>, <code>HWLOC_OBJ_PU</code>, <code>HWLOC_OBJ_GROUP</code>, <code>HWLOC_OBJ_MISC</code>, <code>HWLOC_OBJ_BRIDGE</code>, <code>HWLOC_OBJ_PCI_DEVICE</code>, <code>HWLOC_OBJ_OS_DEVICE</code>, <code>HWLOC_OBJ_TYPE_MAX</code> } </p>
<p> enum <code>hwloc_obj_cache_type_e</code> { <code>HWLOC_OBJ_CACHE_UNIFIED</code>, <code>HWLOC_OBJ_CACHE_DATA</code>, <code>HWLOC_OBJ_CACHE_INSTRUCTION</code> } </p>
<p> enum <code>hwloc_obj_bridge_type_e</code> { <code>HWLOC_OBJ_BRIDGE_HOST</code>, <code>HWLOC_OBJ_BRIDGE_PCI</code> } </p>
<p> enum <code>hwloc_obj_osdev_type_e</code> { <code>HWLOC_OBJ_OSDEV_BLOCK</code>, <code>HWLOC_OBJ_OSDEV_GPU</code>, <code>HWLOC_OBJ_OSDEV_NETWORK</code>, <code>HWLOC_OBJ_OSDEV_OPENFABRICS</code>, <code>HWLOC_OBJ_OSDEV_DMA</code>, <code>HWLOC_OBJ_OSDEV_COPROC</code> } </p>
<p> enum <code>hwloc_compare_types_e</code> { <code>HWLOC_TYPE_UNORDERED</code> } </p>
<h3>Functions</h3>
<p>int <code>hwloc_compare_types</code> (<code>hwloc_obj_type_t</code> type1, <code>hwloc_obj_type_t</code> type2) </p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef enum <code>hwloc_obj_bridge_type_e</code> <code>hwloc_obj_bridge_type_t</code></h3>
<p>Type of one side (upstream or downstream) of an I/O bridge.</p>
<h3>typedef enum <code>hwloc_obj_cache_type_e</code> <code>hwloc_obj_cache_type_t</code></h3>
<p>Cache type.</p>
<h3>typedef enum <code>hwloc_obj_osdev_type_e</code> <code>hwloc_obj_osdev_type_t</code></h3>
<p>Type of a OS device.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_compare_types_e</code></h3>
<p><code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_TYPE_UNORDERED </i></p>
<dd>Value returned by <code>hwloc_compare_types()</code> when types can not be compared.</dl>
<h3>enum <code>hwloc_obj_bridge_type_e</code></h3>
<p>Type of one side (upstream or downstream) of an I/O bridge. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_OBJ_BRIDGE_HOST </i></p>
<dd>Host-side of a bridge, only possible upstream.</p>
<dt><i>HWLOC_OBJ_BRIDGE_PCI </i></p>
<dd>PCI-side of a bridge.</dl>
<h3>enum <code>hwloc_obj_cache_type_e</code></h3>
<p>Cache type. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_OBJ_CACHE_UNIFIED </i></p>
<dd>Unified cache.</p>
<dt><i>HWLOC_OBJ_CACHE_DATA </i></p>
<dd>Data cache.</p>
<dt><i>HWLOC_OBJ_CACHE_INSTRUCTION </i></p>
<dd>Instruction cache. Only used when the <code>HWLOC_TOPOLOGY_FLAG_ICACHES</code> topology flag is set.</dl>
<h3>enum <code>hwloc_obj_osdev_type_e</code></h3>
<p>Type of a OS device. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_OBJ_OSDEV_BLOCK </i></p>
<dd>Operating system block device. For instance &#8216;sda&#8217; on Linux.</p>
<dt><i>HWLOC_OBJ_OSDEV_GPU </i></p>
<dd>Operating system GPU device. For instance &#8216;:0.0&#8217; for a GL display, &#8216;card0&#8217; for a Linux DRM device.</p>
<dt><i>HWLOC_OBJ_OSDEV_NETWORK </i></p>
<dd>Operating system network device. For instance the &#8216;eth0&#8217; interface on Linux.</p>
<dt><i>HWLOC_OBJ_OSDEV_OPENFABRICS </i></p>
<dd>Operating system openfabrics device. For instance the &#8216;mlx4_0&#8217; InfiniBand HCA device on Linux.</p>
<dt><i>HWLOC_OBJ_OSDEV_DMA </i></p>
<dd>Operating system dma engine device. For instance the &#8216;dma0chan0&#8217; DMA channel on Linux.</p>
<dt><i>HWLOC_OBJ_OSDEV_COPROC </i></p>
<dd>Operating system co-processor device. For instance &#8216;mic0&#8217; for a Xeon Phi (MIC) on Linux, &#8216;opencl0d0&#8217; for a OpenCL device, &#8216;cuda0&#8217; for a CUDA device.</dl>
<h3>enum <code>hwloc_obj_type_t</code></h3>
<p>Type of topology object. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Do not rely on the ordering or completeness of the values as new ones may be defined in the future! If you need to compare types, use <code>hwloc_compare_types()</code> instead.</dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>HWLOC_OBJ_SYSTEM </i></p>
<dd>Whole system (may be a cluster of machines). The whole system that is accessible to hwloc. That may comprise several machines in SSI systems like Kerrighed.</p>
<dt><i>HWLOC_OBJ_MACHINE </i></p>
<dd>Machine. The typical root object type. A set of processors and memory with cache coherency.</p>
<dt><i>HWLOC_OBJ_NUMANODE </i></p>
<dd>NUMA node. A set of processors around memory which the processors can directly access.</p>
<dt><i>HWLOC_OBJ_PACKAGE </i></p>
<dd>Physical package, what goes into a socket. In the physical meaning, i.e. that you can add or remove physically.</p>
<dt><i>HWLOC_OBJ_CACHE </i></p>
<dd>Cache. Can be L1i, L1d, L2, L3, &#8230;</p>
<dt><i>HWLOC_OBJ_CORE </i></p>
<dd>Core. A computation unit (may be shared by several logical processors).</p>
<dt><i>HWLOC_OBJ_PU </i></p>
<dd>Processing Unit, or (Logical) Processor. An execution unit (may share a core with some other logical processors, e.g. in the case of an SMT core). Objects of this kind are always reported and can thus be used as fallback when others are not.</p>
<dt><i>HWLOC_OBJ_GROUP </i></p>
<dd>Group objects. Objects which do not fit in the above but are detected by hwloc and are useful to take into account for affinity. For instance, some operating systems expose their arbitrary processors aggregation this way. And hwloc may insert such objects to group NUMA nodes according to their distances. See also <code>What are these Group objects in my topology?</code>. These objects are ignored when they do not bring any structure.</p>
<dt><i>HWLOC_OBJ_MISC </i></p>
<dd>Miscellaneous objects. Objects without particular meaning, that can e.g. be added by the application for its own use, or by hwloc for miscellaneous objects such as MemoryModule (DIMMs).</p>
<dt><i>HWLOC_OBJ_BRIDGE </i></p>
<dd>Bridge. Any bridge that connects the host or an I/O bus, to another I/O bus. Bridge objects have neither CPU sets nor node sets. They are not added to the topology unless I/O discovery is enabled with <code>hwloc_topology_set_flags()</code>.</p>
<dt><i>HWLOC_OBJ_PCI_DEVICE </i></p>
<dd>PCI device. These objects have neither CPU sets nor node sets. They are not added to the topology unless I/O discovery is enabled with <code>hwloc_topology_set_flags()</code>.</p>
<dt><i>HWLOC_OBJ_OS_DEVICE </i></p>
<dd>Operating system device. These objects have neither CPU sets nor node sets. They are not added to the topology unless I/O discovery is enabled with <code>hwloc_topology_set_flags()</code>.</p>
<dt><i>HWLOC_OBJ_TYPE_MAX </i></p>
<dd>Sentinel value</dl>
<h2>Function Documentation</h2>
<h3>int hwloc_compare_types (<code>hwloc_obj_type_t</code> type1, <code>hwloc_obj_type_t</code> type2)</h3>
<p>Compare the depth of two object types. Types shouldn&#8217;t be compared as they are, since newer ones may be added in the future. This function returns less than, equal to, or greater than zero respectively if type1 objects usually include type2 objects, are the same as type2 objects, or are included in type2 objects. If the types can not be compared (because neither is usually contained in the other), <code>HWLOC_TYPE_UNORDERED</code> is returned. Object types containing CPUs can always be compared (usually, a system contains machines which contain nodes which contain packages which contain caches, which contain cores, which contain processors). </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd><code>HWLOC_OBJ_PU</code> will always be the deepest. </p>
<p> This does not mean that the actual topology will respect that order: e.g. as of today cores may also contain caches, and packages may also contain nodes. This is thus just to be seen as a fallback comparison method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code.</p>
