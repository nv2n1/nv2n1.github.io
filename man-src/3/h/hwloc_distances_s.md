---
title: "hwloc_distances_s(3)"
name: "hwloc_distances_s"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_distances_s/"
description: "hwloc_distances_s –"
---

<h2 class="name">NAME</h2>
<p> hwloc_distances_s &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned <code>relative_depth</code> </p>
<p> unsigned <code>nbobjs</code> </p>
<p> float * <code>latency</code> </p>
<p> float <code>latency_max</code> </p>
<p> float <code>latency_base</code> </p>
<h2>Detailed Description</h2>
<p> Distances between objects. </p>
<p> One object may contain a distance structure describing distances between all its descendants at a given relative depth. If the containing object is the root object of the topology, then the distances are available for all objects in the machine. </p>
<p> If the latency pointer is not NULL, the pointed array contains memory latencies (non-zero values), see below. </p>
<p> In the future, some other types of distances may be considered. In these cases, latency may be NULL.</p>
<h2>Field Documentation</h2>
<h3>float* hwloc_distances_s::latency</h3>
<p> Matrix of latencies between objects, stored as a one-dimension array. May be NULL if the distances considered here are not latencies. Unless defined by the user, this currently contains latencies between NUMA nodes (as reported in the System Locality Distance Information Table (SLIT) in the ACPI specification), which may or may not be accurate. It corresponds to the latency for accessing the memory of one node from a core in another node. </p>
<p> Values are normalized to get 1.0 as the minimal value in the matrix. Latency from i-th to j-th object is stored in slot i*nbobjs+j.</p>
<h3>float hwloc_distances_s::latency_base</h3>
<p> The multiplier that should be applied to latency matrix to retrieve the original OS-provided latencies. Usually 10 on Linux since ACPI SLIT uses 10 for local latency.</p>
<h3>float hwloc_distances_s::latency_max</h3>
<p> The maximal value in the latency matrix.</p>
<h3>unsigned hwloc_distances_s::nbobjs</h3>
<p> Number of objects considered in the matrix. It is the number of descendant objects at relative_depth below the containing object. It corresponds to the result of <code>hwloc_get_nbobjs_inside_cpuset_by_depth()</code>.</p>
<h3>unsigned hwloc_distances_s::relative_depth</h3>
<p> Relative depth of the considered objects below the object containing this distance information. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
