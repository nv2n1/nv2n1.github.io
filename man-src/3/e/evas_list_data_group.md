---
title: "evas_list_data_group(3)"
name: "evas_list_data_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_list_data_group/"
description: "Linked List Creation Functions – Functions that add data to an Evas_List."
---

<p>Linked List Creation Functions &#8211; Functions that add data to an Evas_List. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_List</code> * <code>evas_list_append</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Appends the given data to the given linked list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prepend</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Prepends the given data to the given linked list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_append_relative</code> (<code>Evas_List</code> *list, const void *data, const void *relative)<br />
 <i>Inserts the given data into the given linked list after the specified data. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prepend_relative</code> (<code>Evas_List</code> *list, const void *data, const void *relative)<br />
 <i>Prepend a data pointer to a linked list before the memeber specified. </i></p>
<h2>Detailed Description</h2>
<p>Functions that add data to an Evas_List.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_List</code>* evas_list_append (<code>Evas_List</code> * list, const void * data)</h3>
<p>Appends the given data to the given linked list. </p>
<p> The following example code demonstrates how to ensure that the given data has been successfully appended. </p>
<pre> Evas_List *list = NULL;
 extern void *my_data;
 list = evas_list_append(list, my_data);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given list. If NULL is given, then a new list is created.<br />
 <i>data</i> The data to append.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list pointer that should be used in place of the one given to this function if successful. Otherwise, the old pointer is returned.</dl>
<p> References _Evas_List::accounting, _Evas_List::data, _Evas_List::next, and _Evas_List::prev. </p>
<p> Referenced by evas_damage_rectangle_add(), evas_event_feed_mouse_move(), evas_font_path_append(), evas_list_append_relative(), evas_object_clip_set(), evas_object_image_data_update_add(), evas_object_polygon_point_add(), evas_object_smart_members_get(), evas_object_textblock_style_set(), evas_obscured_rectangle_add(), and evas_render_method_list().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_append_relative (<code>Evas_List</code> * list, const void * data, const void * relative)</h3>
<p>Inserts the given data into the given linked list after the specified data. </p>
<p> If relative is not in the list, data is appended to the end of the list. If there are multiple instances of relative in the list, data is inserted after the first instance. </p>
<p> The following example code demonstrates how to ensure that the given data has been successfully inserted. </p>
<pre> Evas_List *list = NULL;
 extern void *my_data;
 extern void *relative_member;
 list = evas_list_append(list, relative_member);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }
 list = evas_list_append_relative(list, my_data, relative_member);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given linked list.<br />
 <i>data</i> The given data.<br />
 <i>relative</i> The data to insert after.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list pointer that should be used in place of the one given to this function if successful. Otherwise, the old pointer is returned.</dl>
<p> References _Evas_List::data, evas_list_append(), and _Evas_List::next.</p>
<h3>EAPI <code>Evas_List</code>* evas_list_prepend (<code>Evas_List</code> * list, const void * data)</h3>
<p>Prepends the given data to the given linked list. </p>
<p> The following example code demonstrates how to ensure that the given data has been successfully prepended. </p>
<p> Example: </p>
<pre> Evas_List *list = NULL;
 extern void *my_data;
 list = evas_list_prepend(list, my_data);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given list.<br />
 <i>data</i> The given data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list pointer that should be used in place of the one given to this function, if successful. Otherwise, the old pointer is returned.</dl>
<p> References _Evas_List::accounting, _Evas_List::data, _Evas_List::next, and _Evas_List::prev. </p>
<p> Referenced by evas_font_path_prepend(), evas_list_prepend_relative(), evas_object_data_set(), evas_object_smart_callback_add(), evas_objects_at_xy_get(), and evas_objects_in_rectangle_get().</p>
<h3>EAPI <code>Evas_List</code>* evas_list_prepend_relative (<code>Evas_List</code> * list, const void * data, const void * relative)</h3>
<p>Prepend a data pointer to a linked list before the memeber specified. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to prepend data too<br />
 <i>data</i> The data pointer to prepend to list list before relative<br />
 <i>relative</i> The data pointer before which to insert data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list handle to replace the old one</dl>
<p> Inserts the given data into the given linked list before the member specified. </p>
<p> If relative is not in the list, data is prepended to the start of the list. If there are multiple instances of relative in the list, data is inserted before the first instance. </p>
<p> The following code example demonstrates how to ensure that the given data has been successfully inserted. </p>
<pre> Evas_List *list = NULL;
 extern void *my_data;
 extern void *relative_member;
 list = evas_list_append(list, relative_member);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }
 list = evas_list_prepend_relative(list, my_data, relative_member);
 if (evas_list_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. List allocation failed.);
 exit(-1);
 }</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given linked list.<br />
 <i>data</i> The given data.<br />
 <i>relative</i> The data to insert before.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list pointer that should be used in place of the one given to this function if successful. Otherwise the old pointer is returned.</dl>
<p> References _Evas_List::data, evas_list_prepend(), and _Evas_List::next.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
