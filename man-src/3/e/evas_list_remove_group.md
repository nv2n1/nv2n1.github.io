---
title: "evas_list_remove_group(3)"
name: "evas_list_remove_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_remove_group/"
description: "Linked List Remove Functions – Functions that remove data from linked lists."
---

<p>Linked List Remove Functions &#8211; Functions that remove data from linked lists. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_List</code> * <code>evas_list_remove</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Removes the first instance of the specified data from the given list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_remove_list</code> (<code>Evas_List</code> *list, <code>Evas_List</code> *remove_list)<br />
 <i>Removes the specified data. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_free</code> (<code>Evas_List</code> *list)<br />
 <i>Free an entire list and all the nodes, ignoring the data contained. </i></p>
<h2>Detailed Description</h2>
<p>Functions that remove data from linked lists.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_List</code>* evas_list_free (<code>Evas_List</code> * list)</h3>
<p>Free an entire list and all the nodes, ignoring the data contained. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to free</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A NULL pointer</dl>
<p> This function will free all the list nodes in list specified by list. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 list = evas_list_free(list);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, and _Evas_List::next. </p>
<p> Referenced by evas_event_feed_hold(), evas_event_feed_mouse_down(), evas_event_feed_mouse_in(), evas_event_feed_mouse_move(), evas_event_feed_mouse_out(), evas_event_feed_mouse_up(), evas_event_feed_mouse_wheel(), evas_free(), and evas_object_smart_move_children_relative().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_remove (<code>Evas_List</code> * list, const void * data)</h3>
<p>Removes the first instance of the specified data from the given list. </p>
<p> If the specified data is not in the given list, nothing is done. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given list.<br />
 <i>data</i> The specified data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list pointer that should be used in place of the one passed to this functions.</dl>
<p> References _Evas_List::data, evas_list_remove_list(), and _Evas_List::next. </p>
<p> Referenced by evas_event_feed_mouse_move(), evas_font_path_clear(), evas_free(), evas_object_clip_set(), evas_object_clip_unset(), evas_object_hide(), evas_object_polygon_points_clear(), evas_object_textblock_style_set(), evas_obscured_clear(), evas_render_method_list_free(), and evas_render_updates_free().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_remove_list (<code>Evas_List</code> * list, <code>Evas_List</code> * remove_list)</h3>
<p>Removes the specified data. </p>
<p> Remove a specified member from a list </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to remove remove_list from<br />
 <i>remove_list</i> The list node which is to be removed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list handle to replace the old one</dl>
<p> Calling this function takes the list node remove_list and removes it from the list list, freeing the list node structure remove_list. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *l;
 extern void *my_data;
 for (l = list; l; l= l-&gt;next)
 {
 if (l-&gt;data == my_data)
 {
 list = evas_list_remove_list(list, l);
 break;
 }
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, _Evas_List::next, and _Evas_List::prev. </p>
<p> Referenced by evas_list_remove(), and evas_object_data_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
