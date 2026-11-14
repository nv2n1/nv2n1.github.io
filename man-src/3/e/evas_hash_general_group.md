---
title: "evas_hash_general_group(3)"
name: "evas_hash_general_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_hash_general_group/"
description: "Hash General Functions – Miscellaneous functions that operate on hash objects."
---

<p>Hash General Functions &#8211; Miscellaneous functions that operate on hash objects. </p>
<h3>Functions</h3>
<p>EAPI int <code>evas_hash_size</code> (const <code>Evas_Hash</code> *hash)<br />
 <i>Retrieves the number of buckets available in the given hash table. </i><br />
 EAPI void <code>evas_hash_free</code> (<code>Evas_Hash</code> *hash)<br />
 <i>Free an entire hash table. </i><br />
 EAPI void <code>evas_hash_foreach</code> (const <code>Evas_Hash</code> *hash, Evas_Bool(*func)(const <code>Evas_Hash</code> *hash, const char *key, void *data, void *fdata), const void *fdata)<br />
 <i>Call a function on every member stored in the hash table. </i><br />
 EAPI int <code>evas_hash_alloc_error</code> (void)<br />
 <i>Return memory allocation failure flag after an function requiring allocation. </i></p>
<h2>Detailed Description</h2>
<p>Miscellaneous functions that operate on hash objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI int evas_hash_alloc_error (void)</h3>
<p>Return memory allocation failure flag after an function requiring allocation. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The state of the allocation flag</dl>
<p> This function returns the state of the memory allocation flag. This flag is set if memory allocations fail during <code>evas_hash_add()</code> calls. If they do, 1 will be returned, otherwise 0 will be returned. The flag will remain in its current state until the next call that requires allocation is called, and is then reset. </p>
<p> Example: </p>
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
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_hash_foreach (const <code>Evas_Hash</code> * hash, Evas_Bool(*)(const <code>Evas_Hash</code> *hash, const char *key, void *data, void *fdata) func, const void * fdata)</h3>
<p>Call a function on every member stored in the hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The hash table whose members will be walked<br />
 <i>func</i> The function to call on each parameter<br />
 <i>fdata</i> The data pointer to pass to the function being called</dl>
<p> This function goes through every entry in the hash table hash and calls the function func on each member. The function should NOT modify the hash table contents if it returns 1. IF the hash table contents are modified by this function or the function wishes to stop processing it must return 0, otherwise return 1 to keep processing. </p>
<p> Example: </p>
<pre> extern Evas_Hash *hash;
 Evas_Bool hash_fn(Evas_Hash *hash, const char *key, void *data, void *fdata)
 {
 printf('Func data: %s, Hash entry: %s / %p, fdata, key, data);
 return 1;
 }
 int main(int argc, char **argv)
 {
 char *hash_fn_data;
 hash_fn_data = strdup('Hello World');
 evas_hash_foreach(hash, hash_fn, hash_fn_data);
 free(hash_fn_data);
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_hash_size().</p>
<h3>EAPI void evas_hash_free (<code>Evas_Hash</code> * hash)</h3>
<p>Free an entire hash table. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Complete polishing documentation for evas_hash.c. The functions&#8217; docs may be grouped, but they need some simplification.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The hash table to be freed</dl>
<p> This function frees up all the memory allocated to storing the specified hash tale pointed to by hash. Any entries in the table that the program has no more pointers for elsewhere may now be lost, so this should only be called if the program has lready freed any allocated data in the hash table or has the pointers for data in teh table stored elswehere as well. </p>
<p> Example: </p>
<pre> extern Evas_Hash *hash;
 evas_hash_free(hash);
 hash = NULL;</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_hash_size(). </p>
<p> Referenced by evas_free().</p>
<h3>EAPI int evas_hash_size (const <code>Evas_Hash</code> * hash)</h3>
<p>Retrieves the number of buckets available in the given hash table. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>256 if hash is not NULL. 0 otherwise.</dl>
<p> Referenced by evas_hash_foreach(), and evas_hash_free().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
