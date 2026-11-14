---
title: "hwloc_obj_attr_u_hwloc_cache_attr_s(3)"
name: "hwloc_obj_attr_u_hwloc_cache_attr_s"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_attr_u_hwloc_cache_attr_s/"
description: "hwloc_obj_attr_u::hwloc_cache_attr_s –"
---

<h2 class="name">NAME</h2>
<p> hwloc_obj_attr_u::hwloc_cache_attr_s &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> hwloc_uint64_t <code>size</code> </p>
<p> unsigned <code>depth</code> </p>
<p> unsigned <code>linesize</code> </p>
<p> int <code>associativity</code> </p>
<p> <code>hwloc_obj_cache_type_t</code> <code>type</code> </p>
<h2>Detailed Description</h2>
<p> Cache-specific Object Attributes.</p>
<h2>Field Documentation</h2>
<h3>int hwloc_obj_attr_u::hwloc_cache_attr_s::associativity</h3>
<p> Ways of associativity, -1 if fully associative, 0 if unknown.</p>
<h3>unsigned hwloc_obj_attr_u::hwloc_cache_attr_s::depth</h3>
<p> Depth of cache (e.g., L1, L2, &#8230;etc.)</p>
<h3>unsigned hwloc_obj_attr_u::hwloc_cache_attr_s::linesize</h3>
<p> Cache-line size in bytes. 0 if unknown.</p>
<h3>hwloc_uint64_t hwloc_obj_attr_u::hwloc_cache_attr_s::size</h3>
<p> Size of cache in bytes.</p>
<h3><code>hwloc_obj_cache_type_t</code> hwloc_obj_attr_u::hwloc_cache_attr_s::type</h3>
<p> Cache type. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
