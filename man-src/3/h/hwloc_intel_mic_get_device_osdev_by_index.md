---
title: "hwloc_intel_mic_get_device_osdev_by_index(3)"
name: "hwloc_intel_mic_get_device_osdev_by_index"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_intel_mic_get_device_osdev_by_index/"
description: "hwlocality_intel_mic – Interoperability with Intel Xeon Phi (MIC)"
---

<h2 class="name">NAME</h2>
<p> hwlocality_intel_mic &#8211; Interoperability with Intel Xeon Phi (MIC) </p>
<h3>Functions</h3>
<p> static int <code>hwloc_intel_mic_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, int idx, <code>hwloc_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_intel_mic_get_device_osdev_by_index</code> (<code>hwloc_topology_t</code> topology, unsigned idx) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about Intel Xeon Phi (MIC) devices.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_intel_mic_get_device_cpuset (<code>hwloc_topology_t</code> topology, int idx, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close to MIC device whose index is idx. Return the CPU set describing the locality of the MIC device whose index is idx. </p>
<p> Topology topology and device index idx must match the local machine. I/O devices detection is not needed in the topology. </p>
<p> The function only returns the locality of the device. If more information about the device is needed, OS objects should be used instead, see <code>hwloc_intel_mic_get_device_osdev_by_index()</code>. </p>
<p> This function is currently only implemented in a meaningful way for Linux; other systems will simply get a full cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_intel_mic_get_device_osdev_by_index (<code>hwloc_topology_t</code> topology, unsigned idx) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the MIC device for the given index. Return the OS device object describing the MIC device whose index is idx. Return NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
