---
title: "ecore_plugin(3)"
name: "ecore_plugin"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_plugin/"
description: "Plugin Functions – Functions that load modules of compiled code into memory."
---

<p>Plugin Functions &#8211; Functions that load modules of compiled code into memory. </p>
<h3>Functions</h3>
<p>EAPI Ecore_Plugin * <code>ecore_plugin_load</code> (Ecore_Path_Group *group, const char *plugin_name, const char *version)<br />
 <i>Loads the specified plugin from the specified path group. </i><br />
 EAPI void <code>ecore_plugin_unload</code> (Ecore_Plugin *plugin)<br />
 <i>Unloads the given plugin from memory. </i><br />
 EAPI Ecore_List * <code>ecore_plugin_available_get</code> (Ecore_Path_Group *group)<br />
 <i>Retrieves a list of all available plugins in the given path. </i></p>
<h2>Detailed Description</h2>
<p>Functions that load modules of compiled code into memory.</p>
<h2>Function Documentation</h2>
<h3>EAPI Ecore_List* ecore_plugin_available_get (Ecore_Path_Group * group)</h3>
<p>Retrieves a list of all available plugins in the given path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group_id</i> The identifier for the given path.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a newly allocated list of all plugins found in the paths identified by group_id. NULL otherwise.</dl>
<p> References ecore_hash_destroy(), ecore_hash_free_key_cb_set(), ecore_hash_get(), ecore_hash_keys(), ecore_hash_new(), ecore_hash_set(), ecore_list_empty_is(), ecore_list_first_goto(), ecore_list_free_cb_set(), ecore_list_next(), ecore_str_compare(), and ecore_str_hash().</p>
<h3>EAPI Ecore_Plugin* ecore_plugin_load (Ecore_Path_Group * group, const char * plugin_name, const char * version)</h3>
<p>Loads the specified plugin from the specified path group. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group</i> The path group to search for the plugin to load<br />
 <i>plugin_name</i> The name of the plugin to load.<br />
 <i>version</i> The interface version of the plugin. With version equal to NULL the default will be loaded.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the newly loaded plugin on success, NULL on failure.</dl>
<p> References ecore_list_append(), ecore_list_new(), and ecore_path_group_find().</p>
<h3>EAPI void ecore_plugin_unload (Ecore_Plugin * plugin)</h3>
<p>Unloads the given plugin from memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plugin</i> The given plugin.</dl>
<p> References ecore_list_destroy(), ecore_list_empty_is(), ecore_list_goto(), and ecore_list_remove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
