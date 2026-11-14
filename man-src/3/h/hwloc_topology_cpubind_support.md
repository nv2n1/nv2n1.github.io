---
title: "hwloc_topology_cpubind_support(3)"
name: "hwloc_topology_cpubind_support"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_cpubind_support/"
description: "hwloc_topology_cpubind_support –"
---

<h2 class="name">NAME</h2>
<p> hwloc_topology_cpubind_support &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned char <code>set_thisproc_cpubind</code> </p>
<p> unsigned char <code>get_thisproc_cpubind</code> </p>
<p> unsigned char <code>set_proc_cpubind</code> </p>
<p> unsigned char <code>get_proc_cpubind</code> </p>
<p> unsigned char <code>set_thisthread_cpubind</code> </p>
<p> unsigned char <code>get_thisthread_cpubind</code> </p>
<p> unsigned char <code>set_thread_cpubind</code> </p>
<p> unsigned char <code>get_thread_cpubind</code> </p>
<p> unsigned char <code>get_thisproc_last_cpu_location</code> </p>
<p> unsigned char <code>get_proc_last_cpu_location</code> </p>
<p> unsigned char <code>get_thisthread_last_cpu_location</code> </p>
<h2>Detailed Description</h2>
<p> Flags describing actual PU binding support for this topology.</p>
<h2>Field Documentation</h2>
<h3>unsigned char hwloc_topology_cpubind_support::get_proc_cpubind</h3>
<p> Getting the binding of a whole given process is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_proc_last_cpu_location</h3>
<p> Getting the last processors where a whole process ran is supported</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_thisproc_cpubind</h3>
<p> Getting the binding of the whole current process is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_thisproc_last_cpu_location</h3>
<p> Getting the last processors where the whole current process ran is supported</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_thisthread_cpubind</h3>
<p> Getting the binding of the current thread only is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_thisthread_last_cpu_location</h3>
<p> Getting the last processors where the current thread ran is supported</p>
<h3>unsigned char hwloc_topology_cpubind_support::get_thread_cpubind</h3>
<p> Getting the binding of a given thread only is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::set_proc_cpubind</h3>
<p> Binding a whole given process is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::set_thisproc_cpubind</h3>
<p> Binding the whole current process is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::set_thisthread_cpubind</h3>
<p> Binding the current thread only is supported.</p>
<h3>unsigned char hwloc_topology_cpubind_support::set_thread_cpubind</h3>
<p> Binding a given thread only is supported. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
