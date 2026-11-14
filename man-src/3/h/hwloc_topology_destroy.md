---
title: "hwloc_topology_destroy(3)"
name: "hwloc_topology_destroy"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_destroy/"
description: "hwlocality_creation – Topology Creation and Destruction"
---

<h2 class="name">NAME</h2>
<p> hwlocality_creation &#8211; Topology Creation and Destruction </p>
<h3>Typedefs</h3>
<p> typedef struct hwloc_topology * <code>hwloc_topology_t</code> </p>
<h3>Functions</h3>
<p> int <code>hwloc_topology_init</code> (<code>hwloc_topology_t</code> *topologyp) </p>
<p> int <code>hwloc_topology_load</code> (<code>hwloc_topology_t</code> topology) </p>
<p> void <code>hwloc_topology_destroy</code> (<code>hwloc_topology_t</code> topology) </p>
<p> int <code>hwloc_topology_dup</code> (<code>hwloc_topology_t</code> *newtopology, <code>hwloc_topology_t</code> oldtopology) </p>
<p> void <code>hwloc_topology_check</code> (<code>hwloc_topology_t</code> topology) </p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef struct hwloc_topology* <code>hwloc_topology_t</code></h3>
<p> Topology context. To be initialized with <code>hwloc_topology_init()</code> and built with <code>hwloc_topology_load()</code>.</p>
<h2>Function Documentation</h2>
<h3>void hwloc_topology_check (<code>hwloc_topology_t</code> topology)</h3>
<p> Run internal checks on a topology structure. The program aborts if an inconsistency is detected in the given topology. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>topology</i> is the topology to be checked</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This routine is only useful to developers. </p>
<p> The input topology should have been previously loaded with <code>hwloc_topology_load()</code>.</dl>
<h3>void hwloc_topology_destroy (<code>hwloc_topology_t</code> topology)</h3>
<p> Terminate and free a topology context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>topology</i> is the topology to be freed</dl>
<h3>int hwloc_topology_dup (<code>hwloc_topology_t</code> * newtopology, <code>hwloc_topology_t</code> oldtopology)</h3>
<p> Duplicate a topology. The entire topology structure as well as its objects are duplicated into a new one. </p>
<p> This is useful for keeping a backup while modifying a topology.</p>
<h3>int hwloc_topology_init (<code>hwloc_topology_t</code> * topologyp)</h3>
<p> Allocate a topology context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>topologyp</i> is assigned a pointer to the new allocated context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<h3>int hwloc_topology_load (<code>hwloc_topology_t</code> topology)</h3>
<p> Build the actual topology. Build the actual topology once initialized with <code>hwloc_topology_init()</code> and tuned with <code>Topology Detection Configuration and Query</code> routines. No other routine may be called earlier using this topology context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>topology</i> is the topology to be loaded with objects.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> On failure, the topology is reinitialized. It should be either destroyed with <code>hwloc_topology_destroy()</code> or configured and loaded again. </p>
<p> This function may be called only once per topology.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>Topology Detection Configuration and Query</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
