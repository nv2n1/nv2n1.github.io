---
title: "ecore_data_list_add_item_group(3)"
name: "ecore_data_list_add_item_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_list_add_item_group/"
description: "List Item Adding Functions – Functions that are used to add nodes to an Ecore_List."
---

<p>List Item Adding Functions &#8211; Functions that are used to add nodes to an Ecore_List. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_list_append</code> (Ecore_List *list, void *data)<br />
 <i>Append data to the list. </i><br />
 EAPI int <code>ecore_list_prepend</code> (Ecore_List *list, void *data)<br />
 <i>Prepend data to the beginning of the list. </i><br />
 EAPI int <code>ecore_list_insert</code> (Ecore_List *list, void *data)<br />
 <i>Insert data in front of the current point in the list. </i><br />
 EAPI int <code>ecore_list_append_list</code> (Ecore_List *list, Ecore_List *append)<br />
 <i>Append a list to the list. </i><br />
 EAPI int <code>ecore_list_prepend_list</code> (Ecore_List *list, Ecore_List *prepend)<br />
 <i>Prepend a list to the beginning of the list. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to add nodes to an Ecore_List.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_list_append (Ecore_List * list, void * data) [inline]</h3>
<p>Append data to the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>data</i> The data to append.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FALSE if an error occurs, TRUE if appended successfully</dl>
<p> References ecore_list_node_new(). </p>
<p> Referenced by ecore_con_server_add(), ecore_con_server_connect(), ecore_file_app_list(), ecore_file_ls(), ecore_hash_keys(), ecore_path_group_add(), ecore_path_group_available(), and ecore_plugin_load().</p>
<h3>EAPI int ecore_list_append_list (Ecore_List * list, Ecore_List * append)</h3>
<p>Append a list to the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>append</i> The list to append.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FALSE if an error occurs, TRUE if appended successfully</dl>
<p> References ecore_list_empty_is(), and ecore_list_init(). </p>
<p> Referenced by ecore_list_merge().</p>
<h3>EAPI int ecore_list_insert (Ecore_List * list, void * data) [inline]</h3>
<p>Insert data in front of the current point in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to hold the inserted data.<br />
 <i>data</i> The data to insert into list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FALSE if there is an error, TRUE on success</dl>
<p> References ecore_list_node_new().</p>
<h3>EAPI int ecore_list_prepend (Ecore_List * list, void * data) [inline]</h3>
<p>Prepend data to the beginning of the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>data</i> The data to prepend.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FALSE if an error occurs, TRUE if prepended successfully.</dl>
<p> References ecore_list_node_new().</p>
<h3>EAPI int ecore_list_prepend_list (Ecore_List * list, Ecore_List * prepend)</h3>
<p>Prepend a list to the beginning of the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>prepend</i> The list to prepend.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>FALSE if an error occurs, TRUE if prepended successfully.</dl>
<p> References ecore_list_empty_is(), and ecore_list_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
