---
title: "ecore_data_hash_adt_destruction_group(3)"
name: "ecore_data_hash_adt_destruction_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_hash_adt_destruction_group/"
description: "Hash Destruction Functions – Functions that destroy hash tables and their contents."
---

<p>Hash Destruction Functions &#8211; Functions that destroy hash tables and their contents. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_hash_free_key_cb_set</code> (Ecore_Hash *hash, Ecore_Free_Cb function)<br />
 <i>Sets the function to destroy the keys of the given hash. </i><br />
 EAPI int <code>ecore_hash_free_value_cb_set</code> (Ecore_Hash *hash, Ecore_Free_Cb function)<br />
 <i>Sets the function to destroy the values in the given hash. </i><br />
 EAPI void <code>ecore_hash_destroy</code> (Ecore_Hash *hash)<br />
 <i>Frees the hash table and the data contained inside it. </i><br />
 EAPI int <code>ecore_hash_count</code> (Ecore_Hash *hash)<br />
 <i>Counts the number of nodes in a hash table. </i></p>
<h2>Detailed Description</h2>
<p>Functions that destroy hash tables and their contents.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_hash_count (Ecore_Hash * hash)</h3>
<p>Counts the number of nodes in a hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The hash table to count current nodes.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of nodes in the hash.</dl>
<h3>EAPI void ecore_hash_destroy (Ecore_Hash * hash)</h3>
<p>Frees the hash table and the data contained inside it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The hash table to destroy.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on error.</dl>
<p> Referenced by ecore_plugin_available_get(), ecore_string_shutdown(), and ecore_x_netwm_shutdown().</p>
<h3>EAPI int ecore_hash_free_key_cb_set (Ecore_Hash * hash, Ecore_Free_Cb function)</h3>
<p>Sets the function to destroy the keys of the given hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash.<br />
 <i>function</i> The function used to free the node keys. NULL is a valid value and means that no function will be called.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on error.</dl>
<p> Referenced by ecore_plugin_available_get().</p>
<h3>EAPI int ecore_hash_free_value_cb_set (Ecore_Hash * hash, Ecore_Free_Cb function)</h3>
<p>Sets the function to destroy the values in the given hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash.<br />
 <i>function</i> The function that will free the node values. NULL is a valid value and means that no function will be called.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on error</dl>
<p> Referenced by ecore_string_init(), and ecore_x_netwm_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
