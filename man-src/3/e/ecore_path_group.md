---
title: "ecore_path_group(3)"
name: "ecore_path_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_path_group/"
description: "Path Group Functions – Functions that make it easier to find a file in a set of search paths."
---

<p>Path Group Functions &#8211; Functions that make it easier to find a file in a set of search paths. </p>
<h3>Functions</h3>
<p>EAPI Ecore_Path_Group * <code>ecore_path_group_new</code> (void)<br />
 <i>Creates a new path group. </i><br />
 EAPI void <code>ecore_path_group_del</code> (Ecore_Path_Group *group)<br />
 <i>Destroys a previously created path group. </i><br />
 EAPI void <code>ecore_path_group_add</code> (Ecore_Path_Group *group, const char *path)<br />
 <i>Adds a directory to be searched for files. </i><br />
 EAPI void <code>ecore_path_group_remove</code> (Ecore_Path_Group *group, const char *path)<br />
 <i>Removes the given directory from the given group. </i><br />
 EAPI char * <code>ecore_path_group_find</code> (Ecore_Path_Group *group, const char *name)<br />
 <i>Finds a file in a group of paths. </i><br />
 EAPI Ecore_List * <code>ecore_path_group_available</code> (Ecore_Path_Group *group)<br />
 <i>Retrieves a list of all available files in the given path. </i></p>
<h2>Detailed Description</h2>
<p>Functions that make it easier to find a file in a set of search paths. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Give this a better description.</dl>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_path_group_add (Ecore_Path_Group * group, const char * path)</h3>
<p>Adds a directory to be searched for files. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group</i> The group to add the path.<br />
 <i>path</i> The new path to be added to the group.</dl>
<p> References ecore_list_append(), ecore_list_free_cb_set(), and ecore_list_new().</p>
<h3>EAPI Ecore_List* ecore_path_group_available (Ecore_Path_Group * group)</h3>
<p>Retrieves a list of all available files in the given path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group_id</i> The identifier for the given path.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a newly allocated list of all files found in the paths identified by group_id. NULL otherwise.</dl>
<p> References ecore_list_append(), ecore_list_empty_is(), ecore_list_first_goto(), ecore_list_new(), and ecore_list_next().</p>
<h3>EAPI void ecore_path_group_del (Ecore_Path_Group * group)</h3>
<p>Destroys a previously created path group. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group</i> The group to delete.</dl>
<p> References ecore_list_destroy().</p>
<h3>EAPI char* ecore_path_group_find (Ecore_Path_Group * group, const char * name)</h3>
<p>Finds a file in a group of paths. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group</i> The group to search.<br />
 <i>name</i> The name of the file to find.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a newly allocated path location of the found file on success. NULL on failure.</dl>
<p> References ecore_list_first_goto(), and ecore_list_next(). </p>
<p> Referenced by ecore_plugin_load().</p>
<h3>EAPI Ecore_Path_Group* ecore_path_group_new (void)</h3>
<p>Creates a new path group. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group_name</i> The name of the new group.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on error, the handle of the new group on success.</dl>
<h3>EAPI void ecore_path_group_remove (Ecore_Path_Group * group, const char * path)</h3>
<p>Removes the given directory from the given group. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>group</i> The group to remove the path from.<br />
 <i>path</i> The path of the directory to be removed.</dl>
<p> References ecore_list_current(), ecore_list_first_goto(), ecore_list_next(), and ecore_list_remove_destroy().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
