---
title: "ecore_data_list_traverse_group(3)"
name: "ecore_data_list_traverse_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_list_traverse_group/"
description: "List Traversal Functions – Functions that can be used to traverse an Ecore_List."
---

<p>List Traversal Functions &#8211; Functions that can be used to traverse an Ecore_List. </p>
<h3>Functions</h3>
<p>EAPI void * <code>ecore_list_index_goto</code> (Ecore_List *list, int index)<br />
 <i>Make the current item the item with the given index number. </i><br />
 EAPI void * <code>ecore_list_goto</code> (Ecore_List *list, const void *data)<br />
 <i>Make the current item the node that contains </i>data.<br />
 EAPI void * <code>ecore_list_first_goto</code> (Ecore_List *list)<br />
 <i>Make the current item the first item in the list. </i><br />
 EAPI void * <code>ecore_list_last_goto</code> (Ecore_List *list)<br />
 <i>Make the current item the last item in the list. </i><br />
 EAPI int <code>ecore_list_for_each</code> (Ecore_List *list, Ecore_For_Each function, void *user_data)<br />
 <i>Execute function for each node in </i>list.</p>
<h2>Detailed Description</h2>
<p>Functions that can be used to traverse an Ecore_List.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_list_first_goto (Ecore_List * list) [inline]</h3>
<p>Make the current item the first item in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the first item on success, NULL on failure</dl>
<p> Referenced by ecore_file_app_installed(), ecore_file_app_list(), ecore_file_ls(), ecore_file_path_dir_exists(), ecore_hash_keys(), ecore_path_group_available(), ecore_path_group_find(), ecore_path_group_remove(), and ecore_plugin_available_get().</p>
<h3>EAPI int ecore_list_for_each (Ecore_List * list, Ecore_For_Each function, void * user_data)</h3>
<p>Execute function for each node in list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>function</i> The function to pass each node from list to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on success, FALSE on failure.</dl>
<h3>EAPI void* ecore_list_goto (Ecore_List * list, const void * data) [inline]</h3>
<p>Make the current item the node that contains data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>data</i> The data to find.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to data on success, NULL on failure.</dl>
<p> Referenced by ecore_con_client_del(), ecore_con_server_del(), and ecore_plugin_unload().</p>
<h3>EAPI void* ecore_list_index_goto (Ecore_List * list, int index) [inline]</h3>
<p>Make the current item the item with the given index number. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>index</i> The position to move the current item.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to new current item on success, NULL on failure.</dl>
<h3>EAPI void* ecore_list_last_goto (Ecore_List * list) [inline]</h3>
<p>Make the current item the last item in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the last item on success, NULL on failure.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
