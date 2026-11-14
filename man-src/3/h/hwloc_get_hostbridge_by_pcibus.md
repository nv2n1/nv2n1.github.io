---
title: "hwloc_get_hostbridge_by_pcibus(3)"
name: "hwloc_get_hostbridge_by_pcibus"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_hostbridge_by_pcibus/"
description: "hwlocality_advanced_io – Finding I/O objects"
---

<h2 class="name">NAME</h2>
<p> hwlocality_advanced_io &#8211; Finding I/O objects </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_non_io_ancestor_obj</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> ioobj) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_pcidev</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_pcidev_by_busid</code> (<code>hwloc_topology_t</code> topology, unsigned domain, unsigned bus, unsigned dev, unsigned func) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_pcidev_by_busidstring</code> (<code>hwloc_topology_t</code> topology, const char *busid) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_osdev</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_next_bridge</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) </p>
<p> static int <code>hwloc_bridge_covers_pcibus</code> (<code>hwloc_obj_t</code> bridge, unsigned domain, unsigned bus) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_get_hostbridge_by_pcibus</code> (<code>hwloc_topology_t</code> topology, unsigned domain, unsigned bus) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>static int hwloc_bridge_covers_pcibus (<code>hwloc_obj_t</code> bridge, unsigned domain, unsigned bus) [inline], [static]</h3>
<h3>static <code>hwloc_obj_t</code> hwloc_get_hostbridge_by_pcibus (<code>hwloc_topology_t</code> topology, unsigned domain, unsigned bus) [inline], [static]</h3>
<p> Find the hostbridge that covers the given PCI bus. This is useful for finding the locality of a bus because it is the hostbridge parent cpuset.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_bridge (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Get the next bridge in the system. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the first bridge if prev is NULL.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_osdev (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Get the next OS device in the system. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the first OS device if prev is NULL.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_next_pcidev (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> prev) [inline], [static]</h3>
<p> Get the next PCI device in the system. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the first PCI device if prev is NULL.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_get_non_io_ancestor_obj (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> ioobj) [inline], [static]</h3>
<p> Get the first non-I/O ancestor object. Given the I/O object ioobj, find the smallest non-I/O ancestor object. This regular object may then be used for binding because its locality is the same as ioobj.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_pcidev_by_busid (<code>hwloc_topology_t</code> topology, unsigned domain, unsigned bus, unsigned dev, unsigned func) [inline], [static]</h3>
<p> Find the PCI device object matching the PCI bus id given domain, bus device and function PCI bus id.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_get_pcidev_by_busidstring (<code>hwloc_topology_t</code> topology, const char * busid) [inline], [static]</h3>
<p> Find the PCI device object matching the PCI bus id given as a string xxxx:yy:zz.t or yy:zz.t.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
