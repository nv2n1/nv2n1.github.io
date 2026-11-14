---
title: "ecore_data_hash_adt_traverse_group(3)"
name: "ecore_data_hash_adt_traverse_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_hash_adt_traverse_group/"
description: "Hash Traverse Functions – Functions that iterate through hash tables."
---

<p>Hash Traverse Functions &#8211; Functions that iterate through hash tables. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_hash_for_each_node</code> (Ecore_Hash *hash, Ecore_For_Each for_each_func, void *user_data)<br />
 <i>Runs the </i>for_each_func function on each entry in the given hash.<br />
 EAPI Ecore_List * <code>ecore_hash_keys</code> (Ecore_Hash *hash)<br />
 <i>Retrieves an ecore_list of all keys in the given hash. </i></p>
<h2>Detailed Description</h2>
<p>Functions that iterate through hash tables.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_hash_for_each_node (Ecore_Hash * hash, Ecore_For_Each for_each_func, void * user_data)</h3>
<p>Runs the for_each_func function on each entry in the given hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash.<br />
 <i>for_each_func</i> The function that each entry is passed to.<br />
 <i>user_data</i> a pointer passed to calls of for_each_func</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE otherwise.</dl>
<h3>EAPI Ecore_List* ecore_hash_keys (Ecore_Hash * hash)</h3>
<p>Retrieves an ecore_list of all keys in the given hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>new ecore_list on success, NULL otherwise</dl>
<p> References ecore_list_append(), ecore_list_first_goto(), and ecore_list_new(). </p>
<p> Referenced by ecore_plugin_available_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
