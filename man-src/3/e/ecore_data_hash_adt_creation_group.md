---
title: "ecore_data_hash_adt_creation_group(3)"
name: "ecore_data_hash_adt_creation_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data_hash_adt_creation_group/"
description: "Hash Creation Functions – Functions that create hash tables."
---

<p>Hash Creation Functions &#8211; Functions that create hash tables. </p>
<h3>Functions</h3>
<p>EAPI Ecore_Hash * <code>ecore_hash_new</code> (Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)<br />
 <i>Creates and initializes a new hash. </i><br />
 EAPI int <code>ecore_hash_init</code> (Ecore_Hash *hash, Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)<br />
 <i>Initializes the given hash. </i></p>
<h2>Detailed Description</h2>
<p>Functions that create hash tables.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_hash_init (Ecore_Hash * hash, Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)</h3>
<p>Initializes the given hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash.<br />
 <i>hash_func</i> The function used for hashing node keys.<br />
 <i>compare</i> The function used for comparing node keys.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on an error.</dl>
<p> Referenced by ecore_hash_hash_set(), and ecore_hash_new().</p>
<h3>EAPI Ecore_Hash* ecore_hash_new (Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)</h3>
<p>Creates and initializes a new hash. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash_func</i> The function for determining hash position.<br />
 <i>compare</i> The function for comparing node keys.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on error, a new hash on success.</dl>
<p> References ecore_hash_init(). </p>
<p> Referenced by ecore_plugin_available_get(), ecore_string_init(), and ecore_x_netwm_init().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
