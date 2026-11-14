---
title: "globus_rsl_list(3)"
name: "globus_rsl_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_list/"
description: "List Functions –"
---

<h2 class="name">NAME</h2>
<p> List Functions &#8211; </p>
<h3>Functions</h3>
<p> globus_list_t * <code>globus_list_copy_reverse</code> (globus_list_t *orig)<br />
 <i>Create a reverse-order copy of a list. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>globus_list_t* globus_list_copy_reverse (globus_list_t *orig)</h3>
<p> Create a reverse-order copy of a list. The <code>globus_list_copy_reverse()</code> function creates and returns a copy of its input parameter, with the order of the list elements reversed. This copy is a shallow copy of list nodes, so both the list pointed to by <i>orig</i> and the returned list point to the same list element data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>orig</i> A pointer to the list to copy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_list_copy_reverse()</code> returns a new list containing the same elements as the list pointed to by <i>orig</i> in reverse order. If an error occurs, <code>globus_list_copy_reverse()</code> returns NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
