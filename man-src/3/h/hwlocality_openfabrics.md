---
title: "hwlocality_openfabrics(3)"
name: "hwlocality_openfabrics"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwlocality_openfabrics/"
description: "hwlocality_openfabrics – Interoperability with OpenFabrics"
---

<h2 class="name">NAME</h2>
<p> hwlocality_openfabrics &#8211; Interoperability with OpenFabrics </p>
<h3>Functions</h3>
<p> static int <code>hwloc_ibv_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, struct ibv_device *ibdev, <code>hwloc_cpuset_t</code> set) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_ibv_get_device_osdev_by_name</code> (<code>hwloc_topology_t</code> topology, const char *ibname) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_ibv_get_device_osdev</code> (<code>hwloc_topology_t</code> topology, struct ibv_device *ibdev) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about OpenFabrics devices.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_ibv_get_device_cpuset (<code>hwloc_topology_t</code> topology, struct ibv_device * ibdev, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close to device ibdev. Return the CPU set describing the locality of the OpenFabrics device ibdev. </p>
<p> Topology topology and device ibdev must match the local machine. I/O devices detection is not needed in the topology. </p>
<p> The function only returns the locality of the device. If more information about the device is needed, OS objects should be used instead, see <code>hwloc_ibv_get_device_osdev()</code> and <code>hwloc_ibv_get_device_osdev_by_name()</code>. </p>
<p> This function is currently only implemented in a meaningful way for Linux; other systems will simply get a full cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_ibv_get_device_osdev (<code>hwloc_topology_t</code> topology, struct ibv_device * ibdev) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the OpenFabrics device ibdev. Return the OS device object describing the OpenFabrics device ibdev. Returns NULL if there is none. </p>
<p> Topology topology and device ibdev must match the local machine. I/O devices detection must be enabled in the topology. If not, the locality of the object may still be found using <code>hwloc_ibv_get_device_cpuset()</code>. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_ibv_get_device_osdev_by_name (<code>hwloc_topology_t</code> topology, const char * ibname) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the OpenFabrics device named ibname. Return the OS device object describing the OpenFabrics device whose name is ibname. Returns NULL if there is none. The name ibname is usually obtained from ibv_get_device_name(). </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
