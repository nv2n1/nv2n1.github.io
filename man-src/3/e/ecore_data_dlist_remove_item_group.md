---
title: "ecore_data_dlist_remove_item_group(3)"
name: "ecore_data_dlist_remove_item_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_dlist_remove_item_group/"
description: "Doubly Linked List Removing Functions – Functions that remove nodes from an Ecore_DList."
---

<p>Doubly Linked List Removing Functions &#8211; Functions that remove nodes from an Ecore_DList. </p>
<h3>Functions</h3>
<p>EAPI void * <code>ecore_dlist_remove</code> (Ecore_DList *list)<br />
 <i>Removes the current item from the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_first_remove</code> (Ecore_DList *list)<br />
 <i>Removes the first item from the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_remove_destroy</code> (Ecore_DList *list)<br />
 <i>Removes and frees the data at the current position in the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_last_remove</code> (Ecore_DList *list)<br />
 <i>Removes the last item from the given doubly linked list. </i></p>
<h2>Detailed Description</h2>
<p>Functions that remove nodes from an Ecore_DList.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_dlist_first_remove (Ecore_DList * list)</h3>
<p>Removes the first item from the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the removed data on success, NULL on failure.</dl>
<h3>EAPI void* ecore_dlist_last_remove (Ecore_DList * list)</h3>
<p>Removes the last item from the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the removed data on success, NULL otherwise.</dl>
<p> References ecore_list_empty_is(), and ecore_list_node_destroy().</p>
<h3>EAPI void* ecore_dlist_remove (Ecore_DList * list)</h3>
<p>Removes the current item from the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the removed data on success, NULL otherwise.</dl>
<p> Referenced by ecore_dlist_remove_destroy().</p>
<h3>EAPI int ecore_dlist_remove_destroy (Ecore_DList * list)</h3>
<p>Removes and frees the data at the current position in the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE otherwise.</dl>
<p> References ecore_dlist_remove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
