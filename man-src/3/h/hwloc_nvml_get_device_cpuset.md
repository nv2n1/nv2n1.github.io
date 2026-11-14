---
title: "hwloc_nvml_get_device_cpuset(3)"
name: "hwloc_nvml_get_device_cpuset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_nvml_get_device_cpuset/"
description: "hwlocality_nvml – Interoperability with the NVIDIA Management Library"
---

<h2 class="name">NAME</h2>
<p> hwlocality_nvml &#8211; Interoperability with the NVIDIA Management Library </p>
<h3>Functions</h3>
<p> static int <code>hwloc_nvml_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, nvmlDevice_t device, <code>hwloc_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_nvml_get_device_osdev_by_index</code> (<code>hwloc_topology_t</code> topology, unsigned idx) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_nvml_get_device_osdev</code> (<code>hwloc_topology_t</code> topology, nvmlDevice_t device) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about devices managed by the NVIDIA Management Library (NVML).</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_nvml_get_device_cpuset (<code>hwloc_topology_t</code> topology, nvmlDevice_t device, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close to NVML device device. Return the CPU set describing the locality of the NVML device device. </p>
<p> Topology topology and device device must match the local machine. I/O devices detection and the NVML component are not needed in the topology. </p>
<p> The function only returns the locality of the device. If more information about the device is needed, OS objects should be used instead, see <code>hwloc_nvml_get_device_osdev()</code> and <code>hwloc_nvml_get_device_osdev_by_index()</code>. </p>
<p> This function is currently only implemented in a meaningful way for Linux; other systems will simply get a full cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_nvml_get_device_osdev (<code>hwloc_topology_t</code> topology, nvmlDevice_t device) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to NVML device device. Return the hwloc OS device object that describes the given NVML device device. Return NULL if there is none. </p>
<p> Topology topology and device device must match the local machine. I/O devices detection and the NVML component must be enabled in the topology. If not, the locality of the object may still be found using <code>hwloc_nvml_get_device_cpuset()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding hwloc PCI device may be found by looking at the result parent pointer.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_nvml_get_device_osdev_by_index (<code>hwloc_topology_t</code> topology, unsigned idx) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the NVML device whose index is idx. Return the OS device object describing the NVML device whose index is idx. Returns NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the NVML component must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
