---
title: "ecore_data_list_creation_group(3)"
name: "ecore_data_list_creation_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_list_creation_group/"
description: "List Creation/Destruction Functions – Functions that create, initialize and destroy Ecore_Lists."
---

<p>List Creation/Destruction Functions &#8211; Functions that create, initialize and destroy Ecore_Lists. </p>
<h3>Functions</h3>
<p>EAPI Ecore_List * <code>ecore_list_new</code> (void)<br />
 <i>Create and initialize a new list. </i><br />
 EAPI int <code>ecore_list_init</code> (Ecore_List *list)<br />
 <i>Initialize a list to some sane starting values. </i><br />
 EAPI void <code>ecore_list_destroy</code> (Ecore_List *list)<br />
 <i>Free a list and all of it&#8217;s nodes. </i></p>
<h2>Detailed Description</h2>
<p>Functions that create, initialize and destroy Ecore_Lists.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_list_destroy (Ecore_List * list)</h3>
<p>Free a list and all of it&#8217;s nodes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to be freed.</dl>
<p> Referenced by ecore_con_shutdown(), ecore_con_url_init(), ecore_con_url_shutdown(), ecore_file_app_list(), ecore_ipc_server_del(), ecore_path_group_del(), and ecore_plugin_unload().</p>
<h3>EAPI int ecore_list_init (Ecore_List * list)</h3>
<p>Initialize a list to some sane starting values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to initialize.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if successful, FALSE if an error occurs.</dl>
<p> Referenced by ecore_ipc_server_add(), ecore_list_append_list(), ecore_list_merge(), ecore_list_new(), and ecore_list_prepend_list().</p>
<h3>EAPI Ecore_List* ecore_list_new (void)</h3>
<p>Create and initialize a new list. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new initialized list on success, NULL on failure.</dl>
<p> References ecore_list_init(). </p>
<p> Referenced by ecore_con_init(), ecore_con_server_add(), ecore_con_server_connect(), ecore_con_url_init(), ecore_file_app_list(), ecore_file_ls(), ecore_hash_keys(), ecore_ipc_server_add(), ecore_path_group_add(), ecore_path_group_available(), and ecore_plugin_load().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
