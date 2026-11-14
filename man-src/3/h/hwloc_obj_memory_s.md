---
title: "hwloc_obj_memory_s(3)"
name: "hwloc_obj_memory_s"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_memory_s/"
description: "hwloc_obj_memory_s –"
---

<h2 class="name">NAME</h2>
<p> hwloc_obj_memory_s &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;hwloc.h&gt;</p>
<h3>Data Structures</h3>
<p> struct <code>hwloc_obj_memory_page_type_s</code> </p>
<h3>Data Fields</h3>
<p> hwloc_uint64_t <code>total_memory</code> </p>
<p> hwloc_uint64_t <code>local_memory</code> </p>
<p> unsigned <code>page_types_len</code> </p>
<p> struct <code>hwloc_obj_memory_s::hwloc_obj_memory_page_type_s</code> * <code>page_types</code> </p>
<h2>Detailed Description</h2>
<p> Object memory.</p>
<h2>Field Documentation</h2>
<h3>hwloc_uint64_t hwloc_obj_memory_s::local_memory</h3>
<p> Local memory (in bytes)</p>
<h3>struct <code>hwloc_obj_memory_s::hwloc_obj_memory_page_type_s</code> * hwloc_obj_memory_s::page_types</h3>
<h3>unsigned hwloc_obj_memory_s::page_types_len</h3>
<p> Size of array page_types.</p>
<h3>hwloc_uint64_t hwloc_obj_memory_s::total_memory</h3>
<p> Total memory (in bytes) in this object and its children. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
