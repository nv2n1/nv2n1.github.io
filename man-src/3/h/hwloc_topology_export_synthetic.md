---
title: "hwloc_topology_export_synthetic(3)"
name: "hwloc_topology_export_synthetic"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_export_synthetic/"
description: "hwlocality_syntheticexport – Exporting Topologies to Synthetic"
---

<h2 class="name">NAME</h2>
<p> hwlocality_syntheticexport &#8211; Exporting Topologies to Synthetic </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_topology_export_synthetic_flags_e</code> { <code>HWLOC_TOPOLOGY_EXPORT_SYNTHETIC_FLAG_NO_EXTENDED_TYPES</code>, <code>HWLOC_TOPOLOGY_EXPORT_SYNTHETIC_FLAG_NO_ATTRS</code> } </p>
<h3>Functions</h3>
<p> int <code>hwloc_topology_export_synthetic</code> (<code>hwloc_topology_t</code> topology, char *buffer, size_t buflen, unsigned long flags) </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_topology_export_synthetic_flags_e</code></h3>
<p> Flags for exporting synthetic topologies. Flags to be given as a OR&#8217;ed set to <code>hwloc_topology_export_synthetic()</code>. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_TOPOLOGY_EXPORT_SYNTHETIC_FLAG_NO_EXTENDED_TYPES </i></p>
<dd> Export extended types such as L2dcache as basic types such as Cache. This is required if loading the synthetic description with hwloc &lt; 1.9.</p>
<dt><i>HWLOC_TOPOLOGY_EXPORT_SYNTHETIC_FLAG_NO_ATTRS </i></p>
<dd> Do not export level attributes. Ignore level attributes such as memory/cache sizes or PU indexes. This is required if loading the synthetic description with hwloc &lt; 1.10.</dl>
<h2>Function Documentation</h2>
<h3>int hwloc_topology_export_synthetic (<code>hwloc_topology_t</code> topology, char * buffer, size_t buflen, unsigned long flags)</h3>
<p> Export the topology as a synthetic string. At most buflen characters will be written in buffer, including the terminating 
