---
title: "hwloc_distrib_flags_e(3)"
name: "hwloc_distrib_flags_e"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_distrib_flags_e/"
description: "hwlocality_helper_distribute – Distributing items over a topology"
---

<h2 class="name">NAME</h2>
<p> hwlocality_helper_distribute &#8211; Distributing items over a topology </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_distrib_flags_e</code> { <code>HWLOC_DISTRIB_FLAG_REVERSE</code> } </p>
<h3>Functions</h3>
<p> static int <code>hwloc_distrib</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> *roots, unsigned n_roots, <code>hwloc_cpuset_t</code> *set, unsigned n, unsigned until, unsigned long flags) </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_distrib_flags_e</code></h3>
<p> Flags to be given to <code>hwloc_distrib()</code>. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_DISTRIB_FLAG_REVERSE </i></p>
<dd> Distrib in reverse order, starting from the last objects.</dl>
<h2>Function Documentation</h2>
<h3>static int hwloc_distrib (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> * roots, unsigned n_roots, <code>hwloc_cpuset_t</code> * set, unsigned n, unsigned until, unsigned long flags) [inline], [static]</h3>
<p> Distribute n items over the topology under roots. Array set will be filled with n cpusets recursively distributed linearly over the topology under objects roots, down to depth until (which can be INT_MAX to distribute down to the finest level). </p>
<p> n_roots is usually 1 and roots only contains the topology root object so as to distribute over the entire topology. </p>
<p> This is typically useful when an application wants to distribute n threads over a machine, giving each of them as much private cache as possible and keeping them locally in number order. </p>
<p> The caller may typically want to also call <code>hwloc_bitmap_singlify()</code> before binding a thread so that it does not move at all. </p>
<p> flags should be 0 or a OR&#8217;ed set of <code>hwloc_distrib_flags_e</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function requires the roots objects to have a CPU set. </p>
<p> This function replaces the now deprecated hwloc_distribute() and hwloc_distributev() functions.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
