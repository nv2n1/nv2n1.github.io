---
title: "ecore_data_dlist_add_item_group(3)"
name: "ecore_data_dlist_add_item_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_dlist_add_item_group/"
description: "Doubly Linked List Adding Functions – Functions that are used to add nodes to an Ecore_DList."
---

<p>Doubly Linked List Adding Functions &#8211; Functions that are used to add nodes to an Ecore_DList. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_dlist_append</code> (Ecore_DList *list, void *data)<br />
 <i>Appends data to the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_prepend</code> (Ecore_DList *list, void *data)<br />
 <i>Adds data to the very beginning of the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_insert</code> (Ecore_DList *list, void *data)<br />
 <i>Inserts data at the current point in the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_append_list</code> (Ecore_DList *list, Ecore_DList *append)<br />
 <i>Appends a list to the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_prepend_list</code> (Ecore_DList *list, Ecore_DList *prepend)<br />
 <i>Adds a list to the very beginning of the given doubly linked list. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to add nodes to an Ecore_DList.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_dlist_append (Ecore_DList * list, void * data)</h3>
<p>Appends data to the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>data</i> The data to append.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if the data is successfully appended, FALSE otherwise.</dl>
<p> Referenced by ecore_dlist_insert().</p>
<h3>EAPI int ecore_dlist_append_list (Ecore_DList * list, Ecore_DList * append)</h3>
<p>Appends a list to the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>append</i> The list to append.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if the data is successfully appended, FALSE otherwise.</dl>
<p> References ecore_dlist_empty_is(), and ecore_dlist_init(). </p>
<p> Referenced by ecore_dlist_merge().</p>
<h3>EAPI int ecore_dlist_insert (Ecore_DList * list, void * data)</h3>
<p>Inserts data at the current point in the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>data</i> The data to be inserted.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE otherwise.</dl>
<p> References ecore_dlist_append(), and ecore_dlist_prepend().</p>
<h3>EAPI int ecore_dlist_prepend (Ecore_DList * list, void * data)</h3>
<p>Adds data to the very beginning of the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>data</i> The data to prepend.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if the data is successfully prepended, FALSE otherwise.</dl>
<p> Referenced by ecore_dlist_insert().</p>
<h3>EAPI int ecore_dlist_prepend_list (Ecore_DList * list, Ecore_DList * prepend)</h3>
<p>Adds a list to the very beginning of the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>prepend</i> The list to prepend.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if the data is successfully prepended, FALSE otherwise.</dl>
<p> References ecore_dlist_empty_is(), and ecore_dlist_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
