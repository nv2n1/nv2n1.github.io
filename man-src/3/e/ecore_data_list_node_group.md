---
title: "ecore_data_list_node_group(3)"
name: "ecore_data_list_node_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_list_node_group/"
description: "List Node Functions – Functions that are used in the creation, maintenance and destruction of Ecore_List nodes."
---

<p>List Node Functions &#8211; Functions that are used in the creation, maintenance and destruction of Ecore_List nodes. </p>
<h3>Functions</h3>
<p>EAPI Ecore_List_Node * <code>ecore_list_node_new</code> ()<br />
 <i>Allocates and initializes a new list node. </i><br />
 EAPI int <code>ecore_list_node_destroy</code> (Ecore_List_Node *node, Ecore_Free_Cb free_func)<br />
 <i>Calls the function to free the data and the node. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used in the creation, maintenance and destruction of Ecore_List nodes.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_list_node_destroy (Ecore_List_Node * node, Ecore_Free_Cb free_func)</h3>
<p>Calls the function to free the data and the node. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>node</i> Node to destroy.<br />
 <i>free_func</i> Function to call if node points to data to free.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE.</dl>
<p> Referenced by ecore_dlist_last_remove().</p>
<h3>EAPI Ecore_List_Node* ecore_list_node_new (void)</h3>
<p>Allocates and initializes a new list node. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Ecore_List_Node on success, NULL otherwise.</dl>
<p> Referenced by ecore_list_append(), ecore_list_insert(), and ecore_list_prepend().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
