---
title: "hwloc_cudart_get_device_cpuset(3)"
name: "hwloc_cudart_get_device_cpuset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_cudart_get_device_cpuset/"
description: "hwlocality_cudart – Interoperability with the CUDA Runtime API"
---

<h2 class="name">NAME</h2>
<p> hwlocality_cudart &#8211; Interoperability with the CUDA Runtime API </p>
<h3>Functions</h3>
<p> static int <code>hwloc_cudart_get_device_pci_ids</code> (<code>hwloc_topology_t</code> topology, int idx, int *domain, int *bus, int *dev) </p>
<p> static int <code>hwloc_cudart_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, int idx, <code>hwloc_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_cudart_get_device_pcidev</code> (<code>hwloc_topology_t</code> topology, int idx) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_cudart_get_device_osdev_by_index</code> (<code>hwloc_topology_t</code> topology, unsigned idx) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about CUDA devices when using the CUDA Runtime API.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_cudart_get_device_cpuset (<code>hwloc_topology_t</code> topology, int idx, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close to device idx. Return the CPU set describing the locality of the CUDA device whose index is idx. </p>
<p> Topology topology and device idx must match the local machine. I/O devices detection and the CUDA component are not needed in the topology. </p>
<p> The function only returns the locality of the device. If more information about the device is needed, OS objects should be used instead, see <code>hwloc_cudart_get_device_osdev_by_index()</code>. </p>
<p> This function is currently only implemented in a meaningful way for Linux; other systems will simply get a full cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_cudart_get_device_osdev_by_index (<code>hwloc_topology_t</code> topology, unsigned idx) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the CUDA device whose index is idx. Return the OS device object describing the CUDA device whose index is idx. Return NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the CUDA component must be enabled in the topology. If not, the locality of the object may still be found using <code>hwloc_cudart_get_device_cpuset()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object. </p>
<p> This function is identical to <code>hwloc_cuda_get_device_osdev_by_index()</code>.</dl>
<h3>static int hwloc_cudart_get_device_pci_ids (<code>hwloc_topology_t</code> topology, int idx, int * domain, int * bus, int * dev) [inline], [static]</h3>
<p> Return the domain, bus and device IDs of the CUDA device whose index is idx. Device index idx must match the local machine.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_cudart_get_device_pcidev (<code>hwloc_topology_t</code> topology, int idx) [inline], [static]</h3>
<p> Get the hwloc PCI device object corresponding to the CUDA device whose index is idx. Return the PCI device object describing the CUDA device whose index is idx. Return NULL if there is none. </p>
<p> Topology topology and device idx must match the local machine. I/O devices detection must be enabled in topology topology. The CUDA component is not needed in the topology.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
