---
title: "evas_list_general_group(3)"
name: "evas_list_general_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_general_group/"
description: "Linked List General Functions – Miscellaneous functions that work on linked lists."
---

<p>Linked List General Functions &#8211; Miscellaneous functions that work on linked lists. </p>
<h3>Functions</h3>
<p>EAPI void * <code>evas_list_data</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the list node data member. </i><br />
 EAPI int <code>evas_list_count</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the count of the number of items in a list. </i><br />
 EAPI int <code>evas_list_alloc_error</code> (void)<br />
 <i>Return the memory allocation failure flag after any operation needin allocation. </i></p>
<h2>Detailed Description</h2>
<p>Miscellaneous functions that work on linked lists.</p>
<h2>Function Documentation</h2>
<h3>EAPI int evas_list_alloc_error (void)</h3>
<p>Return the memory allocation failure flag after any operation needin allocation. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The state of the allocation flag</dl>
<p> This function returns the state of the memory allocation flag. This flag is set if memory allocations during <code>evas_list_append()</code>, <code>evas_list_prepend()</code>, <code>evas_list_append_relative()</code>, or <code>evas_list_prepend_relative()</code> fail. If they do fail, 1 will be returned, otherwise 0 will be returned. The flag will remain in its current state until the next call that requires allocation is called, and is then reset. </p>
<p> Example: </p>
<pre> Evas_List *list = NULL;
 extern void *my_data;
 list = evas_list_append(list, my_data);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI int evas_list_count (const <code>Evas_List</code> * list)</h3>
<p>Get the count of the number of items in a list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list whose count to return</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of members in the list list</dl>
<p> This function returns how many members in the specified list: list. If the list is empty (NULL), 0 is returned. </p>
<p> NB: This is an order-1 operation and takes the same tiem regardless of the length of the list. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 printf('The list has %i members, evas_list_count(list));</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting.</p>
<h3>EAPI void* evas_list_data (const <code>Evas_List</code> * list)</h3>
<p>Get the list node data member. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list node to get the data member of</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data member from the list node list</dl>
<p> This function returns the data member of the specified list node list. It is equivalent to list-&gt;data. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *l;
 printf('The list:);
 for (l = list; l; l = <a href="//www.systutorials.com/docs/linux/man/l-evas_list_next/">evas_list_next</a>(l))
 {
 printf('%p, <a href="//www.systutorials.com/docs/linux/man/l-evas_list_data/">evas_list_data</a>(l));
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
