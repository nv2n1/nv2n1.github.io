---
title: "hwloc_topology_membind_support(3)"
name: "hwloc_topology_membind_support"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_membind_support/"
description: "hwloc_topology_membind_support –"
---

<h2 class="name">NAME</h2>
<p> hwloc_topology_membind_support &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned char <code>set_thisproc_membind</code> </p>
<p> unsigned char <code>get_thisproc_membind</code> </p>
<p> unsigned char <code>set_proc_membind</code> </p>
<p> unsigned char <code>get_proc_membind</code> </p>
<p> unsigned char <code>set_thisthread_membind</code> </p>
<p> unsigned char <code>get_thisthread_membind</code> </p>
<p> unsigned char <code>set_area_membind</code> </p>
<p> unsigned char <code>get_area_membind</code> </p>
<p> unsigned char <code>alloc_membind</code> </p>
<p> unsigned char <code>firsttouch_membind</code> </p>
<p> unsigned char <code>bind_membind</code> </p>
<p> unsigned char <code>interleave_membind</code> </p>
<p> unsigned char <code>replicate_membind</code> </p>
<p> unsigned char <code>nexttouch_membind</code> </p>
<p> unsigned char <code>migrate_membind</code> </p>
<h2>Detailed Description</h2>
<p> Flags describing actual memory binding support for this topology.</p>
<h2>Field Documentation</h2>
<h3>unsigned char hwloc_topology_membind_support::alloc_membind</h3>
<p> Allocating a bound memory area is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::bind_membind</h3>
<p> Bind policy is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::firsttouch_membind</h3>
<p> First-touch policy is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::get_area_membind</h3>
<p> Getting the binding of a given memory area is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::get_proc_membind</h3>
<p> Getting the binding of a whole given process is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::get_thisproc_membind</h3>
<p> Getting the binding of the whole current process is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::get_thisthread_membind</h3>
<p> Getting the binding of the current thread only is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::interleave_membind</h3>
<p> Interleave policy is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::migrate_membind</h3>
<p> Migration flags is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::nexttouch_membind</h3>
<p> Next-touch migration policy is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::replicate_membind</h3>
<p> Replication policy is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::set_area_membind</h3>
<p> Binding a given memory area is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::set_proc_membind</h3>
<p> Binding a whole given process is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::set_thisproc_membind</h3>
<p> Binding the whole current process is supported.</p>
<h3>unsigned char hwloc_topology_membind_support::set_thisthread_membind</h3>
<p> Binding the current thread only is supported. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
