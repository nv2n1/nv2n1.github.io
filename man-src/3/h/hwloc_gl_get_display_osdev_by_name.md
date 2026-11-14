---
title: "hwloc_gl_get_display_osdev_by_name(3)"
name: "hwloc_gl_get_display_osdev_by_name"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_gl_get_display_osdev_by_name/"
description: "hwlocality_gl – Interoperability with OpenGL displays"
---

<h2 class="name">NAME</h2>
<p> hwlocality_gl &#8211; Interoperability with OpenGL displays </p>
<h3>Functions</h3>
<p> static <code>hwloc_obj_t</code> <code>hwloc_gl_get_display_osdev_by_port_device</code> (<code>hwloc_topology_t</code> topology, unsigned port, unsigned device) </p>
<p> static <code>hwloc_obj_t</code> <code>hwloc_gl_get_display_osdev_by_name</code> (<code>hwloc_topology_t</code> topology, const char *name) </p>
<p> static int <code>hwloc_gl_get_display_by_osdev</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> osdev, unsigned *port, unsigned *device) </p>
<h2>Detailed Description</h2>
<p> This interface offers ways to retrieve topology information about OpenGL displays. </p>
<p> Only the NVIDIA display locality information is currently available, using the NV-CONTROL X11 extension and the NVCtrl library.</p>
<h2>Function Documentation</h2>
<h3>static int hwloc_gl_get_display_by_osdev (<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> osdev, unsigned * port, unsigned * device) [inline], [static]</h3>
<p> Get the OpenGL display port and device corresponding to the given hwloc OS object. Return the OpenGL display port (server) in port and device (screen) in screen that correspond to the given hwloc OS device object. Return -1 if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the GL component must be enabled in the topology.</p>
<h3>static <code>hwloc_obj_t</code> hwloc_gl_get_display_osdev_by_name (<code>hwloc_topology_t</code> topology, const char * name) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the OpenGL display given by name. Return the OS device object describing the OpenGL display whose name is name, built as &#8216;:port.device&#8217; such as &#8216;:0.0&#8217; . Return NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the GL component must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h3>static <code>hwloc_obj_t</code> hwloc_gl_get_display_osdev_by_port_device (<code>hwloc_topology_t</code> topology, unsigned port, unsigned device) [inline], [static]</h3>
<p> Get the hwloc OS device object corresponding to the OpenGL display given by port and device index. Return the OS device object describing the OpenGL display whose port (server) is port and device (screen) is device. Return NULL if there is none. </p>
<p> The topology topology does not necessarily have to match the current machine. For instance the topology may be an XML import of a remote host. I/O devices detection and the GL component must be enabled in the topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The corresponding PCI device object can be obtained by looking at the OS device parent object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
