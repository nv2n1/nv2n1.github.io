---
title: "evas_hash_data(3)"
name: "evas_hash_data"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_hash_data/"
description: "Hash Data Functions – Functions that add, access or remove data from hashes."
---

<p>Hash Data Functions &#8211; Functions that add, access or remove data from hashes. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_Hash</code> * <code>evas_hash_add</code> (<code>Evas_Hash</code> *hash, const char *key, const void *data)<br />
 <i>Adds an entry to the given hash table. </i><br />
 EAPI <code>Evas_Hash</code> * <code>evas_hash_direct_add</code> (<code>Evas_Hash</code> *hash, const char *key, const void *data)<br />
 <i>Adds an entry to the given hash table and does not duplicate the string key. </i><br />
 EAPI <code>Evas_Hash</code> * <code>evas_hash_del</code> (<code>Evas_Hash</code> *hash, const char *key, const void *data)<br />
 <i>Removes the entry identified by </i>key or data from the given hash table.<br />
 EAPI void * <code>evas_hash_find</code> (const <code>Evas_Hash</code> *hash, const char *key)<br />
 <i>Retrieves a specific entry in the given hash table. </i><br />
 EAPI void * <code>evas_hash_modify</code> (<code>Evas_Hash</code> *hash, const char *key, const void *data)<br />
 <i>Modifies the entry pointer at the specified key and returns the old entry. </i></p>
<h2>Detailed Description</h2>
<p>Functions that add, access or remove data from hashes. </p>
<p> The following example shows how to add and then access data in a hash table: </p>
<pre> Evas_Hash *hash = NULL;
 extern void *my_data;
 hash = evas_hash_add(hash, 'My Data', my_data);
 if (evas_hash_alloc_error())
 {
 fprintf(stderr, 'ERROR: Memory is low. Hash allocation failed.);
 exit(-1);
 }
 if (evas_hash_find(hash, 'My Data') == my_data)
 {
 printf('My Data inserted and successfully found.);
 }</pre>
<p>What follows is another example, showing how the <code>evas_hash_del</code> function is used: </p>
<pre> extern Evas_Hash *hash;
 extern void *data;
 printf('Insert some data...);
 hash = evas_hash_add(hash, 'My Data', my_data);
 printf('Removing by key...);
 hash = evas_hash_del(hash, 'My Data', NULL);
 printf('Insert some more data as a NULL key...);
 hash = evas_hash_add(hash, NULL, my_data);
 printf('Removing by data as a NULL key...);
 hash = evas_hash_del(hash, NULL, my_data);</pre>
<p>&nbsp;<wbr></p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Hash</code>* evas_hash_add (<code>Evas_Hash</code> * hash, const char * key, const void * data)</h3>
<p>Adds an entry to the given hash table. </p>
<p> key is expected to be a unique string within the hash table. Otherwise, you cannot be sure which inserted data pointer will be accessed with <code>evas_hash_find</code> , and removed with <code>evas_hash_del</code> . </p>
<p> Key strings are case sensitive. </p>
<p> <code>evas_hash_alloc_error</code> should be used to determine if an allocation error occurred during this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table. Can be NULL, in which case a new hash table is allocated and returned.<br />
 <i>key</i> A unique string. Can be NULL.<br />
 <i>data</i> Data to associate with the string given by key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Either the given hash table, or if the given value for hash is NULL, then a new one. NULL will be returned if memory could not be allocated for a new table.</dl>
<p> Referenced by evas_object_name_set().</p>
<h3>EAPI <code>Evas_Hash</code>* evas_hash_del (<code>Evas_Hash</code> * hash, const char * key, const void * data)</h3>
<p>Removes the entry identified by key or data from the given hash table. </p>
<p> If key is NULL, then data is used to find a match to remove. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key string. Can be NULL.<br />
 <i>data</i> The data pointer to remove if key is NULL. Otherwise, not required and can be NULL.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The modified hash table. If there are no entries left, the hash table will be freed and NULL will be returned.</dl>
<p> Referenced by evas_object_name_set().</p>
<h3>EAPI <code>Evas_Hash</code>* evas_hash_direct_add (<code>Evas_Hash</code> * hash, const char * key, const void * data)</h3>
<p>Adds an entry to the given hash table and does not duplicate the string key. </p>
<p> key is expected to be a unique string within the hash table. Otherwise, you cannot be sure which inserted data pointer will be accessed with <code>evas_hash_find</code> , and removed with <code>evas_hash_del</code> . This call does not make a copy of the key so it must be a string constant or stored elsewhere (in the object being added) etc. </p>
<p> Key strings are case sensitive. </p>
<p> <code>evas_hash_alloc_error</code> should be used to determine if an allocation error occurred during this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table. Can be NULL, in which case a new hash table is allocated and returned.<br />
 <i>key</i> A unique string. Can be NULL.<br />
 <i>data</i> Data to associate with the string given by key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Either the given hash table, or if the given value for hash is NULL, then a new one. NULL will be returned if memory could not be allocated for a new table.</dl>
<h3>EAPI void* evas_hash_find (const <code>Evas_Hash</code> * hash, const char * key)</h3>
<p>Retrieves a specific entry in the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key string of the entry to find.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer for the stored entry, or NULL if not found.</dl>
<p> Referenced by evas_object_name_find().</p>
<h3>EAPI void* evas_hash_modify (<code>Evas_Hash</code> * hash, const char * key, const void * data)</h3>
<p>Modifies the entry pointer at the specified key and returns the old entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.<br />
 <i>key</i> The key string of the entry to modify.<br />
 <i>data</i> The data to replace the old entry, if it exists.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer for the old stored entry, or NULL if not found. If an existing entry is not found, nothing is added to the hash.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
