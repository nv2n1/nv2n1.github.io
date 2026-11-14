---
title: "ecore_data_hash_adt_data_group(3)"
name: "ecore_data_hash_adt_data_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_hash_adt_data_group/"
description: "Hash Data Functions – Functions that set, access and delete values from the hash tables."
---

<p>Hash Data Functions &#8211; Functions that set, access and delete values from the hash tables. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_hash_set</code> (Ecore_Hash *hash, void *key, void *value)<br />
 <i>Sets a key-value pair in the given hash table. </i><br />
 EAPI int <code>ecore_hash_hash_set</code> (Ecore_Hash *hash, Ecore_Hash *set)<br />
 <i>Sets all key-value pairs from set in the given hash table. </i><br />
 EAPI void * <code>ecore_hash_get</code> (Ecore_Hash *hash, const void *key)<br />
 <i>Retrieves the value associated with the given key from the given hash table. </i><br />
 EAPI void * <code>ecore_hash_remove</code> (Ecore_Hash *hash, const void *key)<br />
 <i>Removes the value associated with the given key in the given hash table. </i><br />
 EAPI void * <code>ecore_hash_find</code> (Ecore_Hash *hash, Ecore_Compare_Cb compare, const void *value)<br />
 <i>Retrieves the first value that matches table. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set, access and delete values from the hash tables.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* ecore_hash_find (Ecore_Hash * hash, Ecore_Compare_Cb compare, const void * value)</h3>
<p>Retrieves the first value that matches table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key to search for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value corresponding to key on success, NULL otherwise.</dl>
<h3>EAPI void* ecore_hash_get (Ecore_Hash * hash, const void * key)</h3>
<p>Retrieves the value associated with the given key from the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key to search for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value corresponding to key on success, NULL otherwise.</dl>
<p> Referenced by ecore_plugin_available_get(), ecore_string_instance(), and ecore_string_release().</p>
<h3>EAPI int ecore_hash_hash_set (Ecore_Hash * hash, Ecore_Hash * set)</h3>
<p>Sets all key-value pairs from set in the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>set</i> The hash table to import.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if successful, FALSE if not.</dl>
<p> References ecore_hash_init().</p>
<h3>EAPI void* ecore_hash_remove (Ecore_Hash * hash, const void * key)</h3>
<p>Removes the value associated with the given key in the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key to search for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value corresponding to the key on success. NULL is returned if there is an error.</dl>
<p> Referenced by ecore_string_release().</p>
<h3>EAPI int ecore_hash_set (Ecore_Hash * hash, void * key, void * value)</h3>
<p>Sets a key-value pair in the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key.<br />
 <i>value</i> The value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if successful, FALSE if not.</dl>
<p> Referenced by ecore_plugin_available_get(), and ecore_string_instance().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
