---
title: "evas_list_find_group(3)"
name: "evas_list_find_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_find_group/"
description: "Linked List Find Functions – Functions that find specified data in a linked list."
---

<p>Linked List Find Functions &#8211; Functions that find specified data in a linked list. </p>
<h3>Functions</h3>
<p>EAPI void * <code>evas_list_find</code> (const <code>Evas_List</code> *list, const void *data)<br />
 <i>Find a member of a list and return the member. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_find_list</code> (const <code>Evas_List</code> *list, const void *data)<br />
 <i>Find a member of a list and return the list node containing that member. </i><br />
 EAPI void * <code>evas_list_nth</code> (const <code>Evas_List</code> *list, int n)<br />
 <i>Get the nth member&#8217;s data pointer in a list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_nth_list</code> (const <code>Evas_List</code> *list, int n)<br />
 <i>Get the nth member&#8217;s list node in a list. </i></p>
<h2>Detailed Description</h2>
<p>Functions that find specified data in a linked list.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* evas_list_find (const <code>Evas_List</code> * list, const void * data)</h3>
<p>Find a member of a list and return the member. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to search for data<br />
 <i>data</i> The data pointer to find in the list list</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The found member data pointer</dl>
<p> A call to this function will search the list list from beginning to end for the first member whose data pointer is data. If it is found, data will be returned, otherwise NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 extern void *my_data;
 if (evas_list_find(list, my_data) == my_data)
 {
 printf('Found member %p, my_data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, and _Evas_List::next. </p>
<p> Referenced by evas_event_feed_mouse_in(), evas_event_feed_mouse_move(), evas_event_feed_mouse_up(), and evas_object_layer_set().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_find_list (const <code>Evas_List</code> * list, const void * data)</h3>
<p>Find a member of a list and return the list node containing that member. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to search for data<br />
 <i>data</i> The data pointer to find in the list list</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The found members list node</dl>
<p> A call to this function will search the list list from beginning to end for the first member whose data pointer is data. If it is found, the list node containing the specified member will be returned, otherwise NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 extern void *my_data;
 Evas_List *found_node;
 found_node = evas_list_find_list(list, my_data);
 if (found_node)
 {
 printf('Found member %p, found_node-&gt;data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI void* evas_list_nth (const <code>Evas_List</code> * list, int n)</h3>
<p>Get the nth member&#8217;s data pointer in a list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to get member number n from<br />
 <i>n</i> The number of the element (0 being the first)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer stored in the specified element</dl>
<p> This function returns the data pointer of element number n, in the list list. The first element in the array is element number 0. If the element number n does not exist, NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 extern int number;
 void *data;
 data = evas_list_nth(list, number);
 if (data)
 printf('Element number %i has data %p, number, data);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, and evas_list_nth_list().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_nth_list (const <code>Evas_List</code> * list, int n)</h3>
<p>Get the nth member&#8217;s list node in a list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to get member number n from<br />
 <i>n</i> The number of the element (0 being the first)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The list node stored in the numbered element</dl>
<p> This function returns the list node of element number n, in the list list. The first element in the array is element number 0. If the element number n does not exist, NULL will be returned. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 extern int number;
 Evas_List *nth_list;
 nth_list = evas_list_nth_list(list, number);
 if (nth_list)
 printf('Element number %i has data %p, number, nth_list-&gt;data);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, _Evas_List::next, and _Evas_List::prev. </p>
<p> Referenced by evas_list_nth().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
