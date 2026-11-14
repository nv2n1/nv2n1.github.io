---
title: "evas_list_ordering_group(3)"
name: "evas_list_ordering_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_ordering_group/"
description: "Linked List Ordering Functions – Functions that change the ordering of data in a linked list."
---

<p>Linked List Ordering Functions &#8211; Functions that change the ordering of data in a linked list. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_List</code> * <code>evas_list_reverse</code> (<code>Evas_List</code> *list)<br />
 <i>Reverse all the elements in the list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_sort</code> (<code>Evas_List</code> *list, int size, int(*func)(void *, void *))<br />
 <i>Sort a list according to the ordering func will return. </i></p>
<h2>Detailed Description</h2>
<p>Functions that change the ordering of data in a linked list.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_List</code>* evas_list_reverse (<code>Evas_List</code> * list)</h3>
<p>Reverse all the elements in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to reverse</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The list after it has been reversed</dl>
<p> This takes a list list, and reverses the order of all elements in the list, so the last member is now first, and so on. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 list = evas_list_reverse(list);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, _Evas_List::data, _Evas_List::next, and _Evas_List::prev.</p>
<h3>EAPI <code>Evas_List</code>* evas_list_sort (<code>Evas_List</code> * list, int size, int(*)(void *, void *) func)</h3>
<p>Sort a list according to the ordering func will return. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to sort<br />
 <i>size</i> The length of the list to sort<br />
 <i>func</i> A function pointer that can handle comparing the list data nodes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new sorted list</dl>
<p> This function sorts your list. The data in your nodes can be arbitrary, you just have to be smart enough to know what kind of data is in your lists </p>
<p> Example: </p>
<pre> int
 sort_cb(void *d1, void *d2)
 {
 const char *txt = NULL;
 const char *txt2 = NULL;
 if(!d1) <a href="//www.systutorials.com/docs/linux/man/1-return/">return</a>(1);
 if(!d2) return(-1);
 return(strcmp((const char*)d1, (const char*)d2));
 }
 extern Evas_List *list;
 list = evas_list_sort(list, evas_list_count(list), sort_cb);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List Sorting failed.);
 exit(-1);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, _Evas_List::data, evas_list_next(), evas_list_prev(), _Evas_List::next, and _Evas_List::prev.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
