---
title: "hwloc_topology_support(3)"
name: "hwloc_topology_support"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_support/"
description: "hwloc_topology_support –"
---

<h2 class="name">NAME</h2>
<p> hwloc_topology_support &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> struct <code>hwloc_topology_discovery_support</code> * <code>discovery</code> </p>
<p> struct <code>hwloc_topology_cpubind_support</code> * <code>cpubind</code> </p>
<p> struct <code>hwloc_topology_membind_support</code> * <code>membind</code> </p>
<h2>Detailed Description</h2>
<p> Set of flags describing actual support for this topology. </p>
<p> This is retrieved with <code>hwloc_topology_get_support()</code> and will be valid until the topology object is destroyed. Note: the values are correct only after discovery.</p>
<h2>Field Documentation</h2>
<h3>struct <code>hwloc_topology_cpubind_support</code>* hwloc_topology_support::cpubind</h3>
<h3>struct <code>hwloc_topology_discovery_support</code>* hwloc_topology_support::discovery</h3>
<h3>struct <code>hwloc_topology_membind_support</code>* hwloc_topology_support::membind</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
