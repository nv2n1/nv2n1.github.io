---
title: "globus_handle_table-h(3)"
name: "globus_handle_table-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_handle_table-h/"
description: "globus_handle_table.h –"
---

<p>globus_handle_table.h &#8211; </p>
<p> Handle Table for Reference Counting Data.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_types.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_NULL_HANDLE</code> </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_l_handle_table_s * <code>globus_handle_table_t</code>&quot;<br />
 <i>Handle table abstract type. </i><br />
 typedef int <code>globus_handle_t</code><br />
 <i>Handle abstract type. </i><br />
 typedef void(* <code>globus_handle_destructor_t</code> )(void *datum)<br />
 <i>Handle datum destructor. </i></p>
<h3>Functions</h3>
<p>int <code>globus_handle_table_init</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_destructor_t</code> destructor) </p>
<p> int <code>globus_handle_table_destroy</code> (<code>globus_handle_table_t</code> *handle_table)<br />
 <i>Destroy a handle table. </i><br />
 <code>globus_handle_t</code> <code>globus_handle_table_insert</code> (<code>globus_handle_table_t</code> *handle_table, void *datum, int initial_refs) </p>
<p> <code>globus_bool_t</code> <code>globus_handle_table_increment_reference</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Add a reference to a handle table entry. </i><br />
 <code>globus_bool_t</code> <code>globus_handle_table_increment_reference_by</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle, unsigned int inc)<br />
 <i>Increment the reference count for handle. </i><br />
 <code>globus_bool_t</code> <code>globus_handle_table_decrement_reference</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Remove a reference to a handle. </i><br />
 void * <code>globus_handle_table_lookup</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Resolve a handle its datum. </i></p>
<h2>Detailed Description</h2>
<p>Handle Table for Reference Counting Data. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
