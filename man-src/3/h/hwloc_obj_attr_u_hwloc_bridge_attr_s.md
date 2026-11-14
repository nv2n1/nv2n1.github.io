---
title: "hwloc_obj_attr_u_hwloc_bridge_attr_s(3)"
name: "hwloc_obj_attr_u_hwloc_bridge_attr_s"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_attr_u_hwloc_bridge_attr_s/"
description: "hwloc_obj_attr_u::hwloc_bridge_attr_s –"
---

<h2 class="name">NAME</h2>
<p> hwloc_obj_attr_u::hwloc_bridge_attr_s &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> union { </p>
<p> struct <code>hwloc_pcidev_attr_s</code> <code>pci</code> </p>
<p> } <code>upstream</code> </p>
<p> <code>hwloc_obj_bridge_type_t</code> <code>upstream_type</code> </p>
<p> union { </p>
<p> struct { </p>
<p> unsigned short <code>domain</code> </p>
<p> unsigned char <code>secondary_bus</code> </p>
<p> unsigned char <code>subordinate_bus</code> </p>
<p> } <code>pci</code> </p>
<p> } <code>downstream</code> </p>
<p> <code>hwloc_obj_bridge_type_t</code> <code>downstream_type</code> </p>
<p> unsigned <code>depth</code> </p>
<h2>Detailed Description</h2>
<p> Bridge specific Object Attribues.</p>
<h2>Field Documentation</h2>
<h3>unsigned hwloc_obj_attr_u::hwloc_bridge_attr_s::depth</h3>
<h3>unsigned short hwloc_obj_attr_u::hwloc_bridge_attr_s::domain</h3>
<h3>union { &#8230; } hwloc_obj_attr_u::hwloc_bridge_attr_s::downstream</h3>
<h3><code>hwloc_obj_bridge_type_t</code> hwloc_obj_attr_u::hwloc_bridge_attr_s::downstream_type</h3>
<h3>struct { &#8230; } hwloc_obj_attr_u::hwloc_bridge_attr_s::pci</h3>
<h3>struct <code>hwloc_pcidev_attr_s</code> hwloc_obj_attr_u::hwloc_bridge_attr_s::pci</h3>
<h3>unsigned char hwloc_obj_attr_u::hwloc_bridge_attr_s::secondary_bus</h3>
<h3>unsigned char hwloc_obj_attr_u::hwloc_bridge_attr_s::subordinate_bus</h3>
<h3>union { &#8230; } hwloc_obj_attr_u::hwloc_bridge_attr_s::upstream</h3>
<h3><code>hwloc_obj_bridge_type_t</code> hwloc_obj_attr_u::hwloc_bridge_attr_s::upstream_type</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
