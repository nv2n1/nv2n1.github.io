---
title: "hwloc_opencl_get_device_osdev(3)"
name: "hwloc_opencl_get_device_osdev"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_opencl_get_device_osdev/"
description: "hwlocality_opencl – Interoperability with OpenCL"
---

<h2 class="name">NAME</h2>
<p> hwlocality_opencl &#8211; Interoperability with OpenCL </p>
<h3>Functions</h3>
<p> static int <code>hwloc_opencl_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, cl_device_id device, <code>hwloc_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_opencl_get_device_osdev_by_index</code> (<code>hwloc_topology_t</code> topology, unsigned platform_index, unsigned device_index) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_opencl_get_device_osdev</code> (<code>hwloc_topology_t</code> topology, cl_device_id device) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about OpenCL devices. </p>
<p> Only the AMD OpenCL interface currently offers useful locality information about its devices.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_opencl_get_device_cpuset (<code>hwloc_topology_t</code> topology, cl_device_id device, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close to OpenCL device device. Return the CPU set describing the locality of the OpenCL device device. </p>
<p> Topology topology and device device must match the local machine. I/O devices detection and the OpenCL component are not needed in the topology. </p>
<p> The function only returns the locality of the device. If more information about the device is needed, OS objects should be used instead, see <code>hwloc_opencl_get_device_osdev()</code> and <code>hwloc_opencl_get_device_osdev_by_index()</code>. </p>
<p> This function is currently only implemented in a meaningful way for Linux with the AMD OpenCL implementation; other systems will simply get a full cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_opencl_get_device_osdev (<code>hwloc_topology_t</code> topology, cl_device_id device) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to OpenCL device device. Return the hwloc OS device object that describes the given OpenCL device device. Return NULL if there is none. </p>
<p> Topology topology and device device must match the local machine. I/O devices detection and the OpenCL component must be enabled in the topology. If not, the locality of the object may still be found using <code>hwloc_opencl_get_device_cpuset()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding hwloc PCI device may be found by looking at the result parent pointer.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_opencl_get_device_osdev_by_index (<code>hwloc_topology_t</code> topology, unsigned platform_index, unsigned device_index) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the OpenCL device for the given indexes. Return the OS device object describing the OpenCL device whose platform index is platform_index, and whose device index within this platform if device_index. Return NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the OpenCL component must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
