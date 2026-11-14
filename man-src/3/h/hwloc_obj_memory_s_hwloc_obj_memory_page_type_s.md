---
title: "hwloc_obj_memory_s_hwloc_obj_memory_page_type_s(3)"
name: "hwloc_obj_memory_s_hwloc_obj_memory_page_type_s"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_memory_s_hwloc_obj_memory_page_type_s/"
description: "hwloc_obj_memory_s::hwloc_obj_memory_page_type_s –"
---

<h2 class="name">NAME</h2>
<p> hwloc_obj_memory_s::hwloc_obj_memory_page_type_s &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Fields</h3>
<p> hwloc_uint64_t <code>size</code> </p>
<p> hwloc_uint64_t <code>count</code> </p>
<h2>Detailed Description</h2>
<p> Array of local memory page types, NULL if no local memory and page_types is 0. </p>
<p> The array is sorted by increasing size fields. It contains page_types_len slots.</p>
<h2>Field Documentation</h2>
<h3>hwloc_uint64_t hwloc_obj_memory_s::hwloc_obj_memory_page_type_s::count</h3>
<p> Number of pages of this size.</p>
<h3>hwloc_uint64_t hwloc_obj_memory_s::hwloc_obj_memory_page_type_s::size</h3>
<p> Size of pages. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
