---
title: "globus_handle_table_insert(3)"
name: "globus_handle_table_insert"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_handle_table_insert/"
description: "Handle Table for Reference Counting Data –"
---

<h2 class="name">NAME</h2>
<p> Handle Table for Reference Counting Data &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_NULL_HANDLE</code> </p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_handle_table_s * <code>globus_handle_table_t</code>&quot;<br />
 <i>Handle table abstract type. </i><br />
 typedef int <code>globus_handle_t</code><br />
 <i>Handle abstract type. </i><br />
 typedef void(* <code>globus_handle_destructor_t</code> )(void *datum)<br />
 <i>Handle datum destructor. </i></p>
<h3>Functions</h3>
<p> int <code>globus_handle_table_init</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_destructor_t</code> destructor) </p>
<p> int <code>globus_handle_table_destroy</code> (<code>globus_handle_table_t</code> *handle_table)<br />
 <i>Destroy a handle table. </i><br />
 <code>globus_handle_t</code> <code>globus_handle_table_insert</code> (<code>globus_handle_table_t</code> *handle_table, void *value, int initial_refs) </p>
<p> <code>globus_bool_t</code> <code>globus_handle_table_increment_reference_by</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle, unsigned int inc)<br />
 <i>Increment the reference count for handle. </i><br />
 <code>globus_bool_t</code> <code>globus_handle_table_decrement_reference</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Remove a reference to a handle. </i><br />
 <code>globus_bool_t</code> <code>globus_handle_table_increment_reference</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Add a reference to a handle table entry. </i><br />
 void * <code>globus_handle_table_lookup</code> (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code> handle)<br />
 <i>Resolve a handle its datum. </i></p>
<h2>Detailed Description</h2>
<p> The globus_handle_table_t abstraction provides a reference-counting handle table to automatically free data when there are no more references to it. Each datum in the globus_handle_table_t container has a count associated with it which may be incremented and decremented in single steps or by an increment. While a handle has any references to it, the <code>globus_handle_table_lookup()</code> will return the datum associated with the handle, otherwise it will return NULL. The value of a globus_handle_t is not reused until INT_MAX data have been inserted into the handle table.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_NULL_HANDLE</h3>
<p> Invalid handle value</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_handle_destructor_t)(void *datum)</h3>
<p> Handle datum destructor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>datum</i> Datum to destroy</dl>
<h2>Function Documentation</h2>
<h3><code>globus_bool_t</code> globus_handle_table_decrement_reference (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code>handle)</h3>
<p> Remove a reference to a handle. Remove a reference to a handle table entry, calling its destructor if no more references exist for the handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> The table that the handle was created in.<br />
 <i>handle</i> The handle to a datum to decrement the reference count for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_handle_table_decrement_reference()</code> function returns a boolean value indicating whether the handle still references a valid datum.</dl>
<h3>int globus_handle_table_destroy (<code>globus_handle_table_t</code> *handle_table)</h3>
<p> Destroy a handle table. Destroy a handle table and call the destructor for all objects associated with it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> Pointer to the handle table to destroy</dl>
<h3><code>globus_bool_t</code> globus_handle_table_increment_reference (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code>handle)</h3>
<p> Add a reference to a handle table entry. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> The table that the handle was created in.<br />
 <i>handle</i> The handle to a datum to increment the reference count for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_handle_table_increment_reference()</code> function returns a boolean value indicating whether the handle still references a valid datum.</dl>
<h3><code>globus_bool_t</code> globus_handle_table_increment_reference_by (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code>handle, unsigned intinc)</h3>
<p> Increment the reference count for handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> The table that the handle was created in.<br />
 <i>handle</i> The handle to a datum to increment the reference count for.<br />
 <i>inc</i> The number of references to add the handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_handle_table_increment_reference_by()</code> function returns a boolean value indicating whether the handle still references a valid datum.</dl>
<h3>int globus_handle_table_init (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_destructor_t</code>destructor)</h3>
<p> Initialize a table of unique reference counted handles. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> the table of unique handles we want to use.<br />
 <i>destructor</i> Function to call to free the data associated with a handle when the handle&#8217;s reference count reaches 0 or the handle table is destroyed.</dl>
<h3><code>globus_handle_t</code> globus_handle_table_insert (<code>globus_handle_table_t</code> *handle_table, void *value, intinitial_refs)</h3>
<p> Insert a datum into a handle table </p>
<p> Insert a value into the handle table, and return a unique handle to it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> Handle table to add the value to<br />
 <i>value</i> The value to insert into the table<br />
 <i>initial_refs</i> The initial reference count of this value in the table</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_handle_table_insert()</code> function returns a unique handle to value.</dl>
<h3>void* globus_handle_table_lookup (<code>globus_handle_table_t</code> *handle_table, <code>globus_handle_t</code>handle)</h3>
<p> Resolve a handle its datum. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_table</i> The table that the handle was created in.<br />
 <i>handle</i> The handle to a datum to resolve</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_handle_table_lookup()</code> function returns the datum associated with the handle in the handle table, or NULL if the handle does not reference valid data.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
