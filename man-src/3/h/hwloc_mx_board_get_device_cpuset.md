---
title: "hwloc_mx_board_get_device_cpuset(3)"
name: "hwloc_mx_board_get_device_cpuset"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_mx_board_get_device_cpuset/"
description: "hwlocality_myriexpress – Interoperability with Myrinet Express"
---

<h2 class="name">NAME</h2>
<p> hwlocality_myriexpress &#8211; Interoperability with Myrinet Express </p>
<h3>Functions</h3>
<p> static int <code>hwloc_mx_board_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, unsigned id, <code>hwloc_cpuset_t</code> set) </p>
<p> static int <code>hwloc_mx_endpoint_get_device_cpuset</code> (<code>hwloc_topology_t</code> topology, mx_endpoint_t endpoint, <code>hwloc_cpuset_t</code> set) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about Myrinet Express hardware.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_mx_board_get_device_cpuset (<code>hwloc_topology_t</code> topology, unsigned id, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close the MX board id. Return the CPU set describing the locality of the Myrinet Express board whose index is id. </p>
<p> Topology topology and device id must match the local machine. I/O devices detection is not needed in the topology. </p>
<p> The function only returns the locality of the device. No additional information about the device is available.</p>
<h3>static int hwloc_mx_endpoint_get_device_cpuset (<code>hwloc_topology_t</code> topology, mx_endpoint_t endpoint, <code>hwloc_cpuset_t</code> set) [inline], [static]</h3>
<p> Get the CPU set of logical processors that are physically close the MX endpoint endpoint. Return the CPU set describing the locality of the Myrinet Express board that runs the MX endpoint endpoint. </p>
<p> Topology topology and device id must match the local machine. I/O devices detection is not needed in the topology. </p>
<p> The function only returns the locality of the endpoint. No additional information about the endpoint or device is available.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
