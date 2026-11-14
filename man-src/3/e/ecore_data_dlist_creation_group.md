---
title: "ecore_data_dlist_creation_group(3)"
name: "ecore_data_dlist_creation_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_dlist_creation_group/"
description: "Doubly Linked List Creation/Destruction Functions – Functions used to create, initialize and destroy Ecore_DLists."
---

<p>Doubly Linked List Creation/Destruction Functions &#8211; Functions used to create, initialize and destroy Ecore_DLists. </p>
<h3>Functions</h3>
<p>EAPI Ecore_DList * <code>ecore_dlist_new</code> ()<br />
 <i>Creates and initialises a new doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_init</code> (Ecore_DList *list)<br />
 <i>Initialises a list to some sane starting values. </i><br />
 EAPI void <code>ecore_dlist_destroy</code> (Ecore_DList *list)<br />
 <i>Frees a doubly linked list and all of its nodes. </i><br />
 EAPI int <code>ecore_dlist_free_cb_set</code> (Ecore_DList *list, Ecore_Free_Cb free_func)<br />
 <i>Sets the function used for freeing data stored in a doubly linked list. </i></p>
<h2>Detailed Description</h2>
<p>Functions used to create, initialize and destroy Ecore_DLists.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_dlist_destroy (Ecore_DList * list)</h3>
<p>Frees a doubly linked list and all of its nodes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The doubly linked list to be freed.</dl>
<h3>EAPI int ecore_dlist_free_cb_set (Ecore_DList * list, Ecore_Free_Cb free_func)</h3>
<p>Sets the function used for freeing data stored in a doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The doubly linked list that will use this function when nodes are destroyed.<br />
 <i>free_func</i> The function that will free the key data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on failure.</dl>
<p> References ecore_list_free_cb_set().</p>
<h3>EAPI int ecore_dlist_init (Ecore_DList * list)</h3>
<p>Initialises a list to some sane starting values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The doubly linked list to initialise.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if successful, FALSE if an error occurs.</dl>
<p> Referenced by ecore_dlist_append_list(), ecore_dlist_merge(), ecore_dlist_new(), and ecore_dlist_prepend_list().</p>
<h3>EAPI Ecore_DList* ecore_dlist_new (void)</h3>
<p>Creates and initialises a new doubly linked list. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new initialised doubly linked list on success, NULL on failure.</dl>
<p> References ecore_dlist_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
