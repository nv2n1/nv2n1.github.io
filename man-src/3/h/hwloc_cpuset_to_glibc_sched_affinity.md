---
title: "hwloc_cpuset_to_glibc_sched_affinity(3)"
name: "hwloc_cpuset_to_glibc_sched_affinity"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_cpuset_to_glibc_sched_affinity/"
description: "hwlocality_glibc_sched – Interoperability with glibc sched affinity"
---

<h2 class="name">NAME</h2>
<p> hwlocality_glibc_sched &#8211; Interoperability with glibc sched affinity </p>
<h3>Functions</h3>
<p> static int <code>hwloc_cpuset_to_glibc_sched_affinity</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> hwlocset, cpu_set_t *schedset, size_t schedsetsize) </p>
<p> static int <code>hwloc_cpuset_from_glibc_sched_affinity</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> hwlocset, const cpu_set_t *schedset, size_t schedsetsize) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to convert between hwloc cpusets and glibc cpusets such as those manipulated by sched_getaffinity() or pthread_attr_setaffinity_np(). </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Topology topology must match the current machine.</dl>
<h2>Function Documentation</h2>
<h3>static int hwloc_cpuset_from_glibc_sched_affinity (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> hwlocset, const cpu_set_t * schedset, size_t schedsetsize) [inline], [static]</h3>
<p> Convert glibc sched affinity CPU set schedset into hwloc CPU set. This function may be used before calling sched_setaffinity or any other function that takes a cpu_set_t as input parameter. </p>
<p> schedsetsize should be sizeof(cpu_set_t) unless schedset was dynamically allocated with CPU_ALLOC</p>
<h3>static int hwloc_cpuset_to_glibc_sched_affinity (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> hwlocset, cpu_set_t * schedset, size_t schedsetsize) [inline], [static]</h3>
<p> Convert hwloc CPU set toposet into glibc sched affinity CPU set schedset. This function may be used before calling sched_setaffinity or any other function that takes a cpu_set_t as input parameter. </p>
<p> schedsetsize should be sizeof(cpu_set_t) unless schedset was dynamically allocated with CPU_ALLOC</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
