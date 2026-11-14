---
title: "ecore_data_list_remove_item_group(3)"
name: "ecore_data_list_remove_item_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_list_remove_item_group/"
description: "List Item Removing Functions – Functions that remove nodes from an Ecore_List."
---

<p>List Item Removing Functions &#8211; Functions that remove nodes from an Ecore_List. </p>
<h3>Functions</h3>
<p>EAPI void * <code>ecore_list_remove</code> (Ecore_List *list)<br />
 <i>Remove the current item from the list. </i><br />
 EAPI int <code>ecore_list_remove_destroy</code> (Ecore_List *list)<br />
 <i>Remove and free the data in lists current position. </i><br />
 EAPI void * <code>ecore_list_first_remove</code> (Ecore_List *list)<br />
 <i>Remove the first item from the list. </i><br />
 EAPI void * <code>ecore_list_last_remove</code> (Ecore_List *list)<br />
 <i>Remove the last item from the list. </i></p>
<h2>Detailed Description</h2>
<p>Functions that remove nodes from an Ecore_List.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_list_first_remove (Ecore_List * list) [inline]</h3>
<p>Remove the first item from the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to remove the current item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns a pointer to the removed data on success, NULL on failure.</dl>
<p> Referenced by ecore_con_shutdown().</p>
<h3>EAPI void* ecore_list_last_remove (Ecore_List * list) [inline]</h3>
<p>Remove the last item from the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to remove the last node from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the removed data on success, NULL on failure.</dl>
<h3>EAPI void* ecore_list_remove (Ecore_List * list) [inline]</h3>
<p>Remove the current item from the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to remove the current item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the removed data on success, NULL on failure.</dl>
<p> Referenced by ecore_con_client_del(), ecore_con_server_del(), ecore_con_url_destroy(), and ecore_plugin_unload().</p>
<h3>EAPI int ecore_list_remove_destroy (Ecore_List * list)</h3>
<p>Remove and free the data in lists current position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to remove and free the current item.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on error</dl>
<p> Referenced by ecore_path_group_remove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
