---
title: "globus_hashtable_destructor_func_t(3)"
name: "globus_hashtable_destructor_func_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_hashtable_destructor_func_t/"
description: "Hash Table –"
---

<h2 class="name">NAME</h2>
<p> Hash Table &#8211; </p>
<h3>Modules</h3>
<p> <code>Iterators</code> </p>
<h3>Typedefs</h3>
<p> typedef int(* <code>globus_hashtable_hash_func_t</code> )(void *key, int limit) </p>
<p> typedef int(* <code>globus_hashtable_keyeq_func_t</code> )(void *key1, void *key2) </p>
<p> typedef void(* <code>globus_hashtable_copy_func_t</code> )(void **dest_key, void **dest_datum, void *src_key, void *src_datum) </p>
<p> typedef void(* <code>globus_hashtable_destructor_func_t</code> )(void *datum) </p>
<h3>Functions</h3>
<p> int <code>globus_hashtable_init</code> (globus_hashtable_t *table, int size, <code>globus_hashtable_hash_func_t</code> hash_func, <code>globus_hashtable_keyeq_func_t</code> keyeq_func)<br />
 <i>Initialize a hash table. </i><br />
 int <code>globus_hashtable_insert</code> (globus_hashtable_t *table, void *key, void *datum)<br />
 <i>Insert a datum into a hash table. </i><br />
 void * <code>globus_hashtable_update</code> (globus_hashtable_t *table, void *key, void *datum)<br />
 <i>Update a hash table mapping. </i><br />
 void * <code>globus_hashtable_lookup</code> (globus_hashtable_t *table, void *key)<br />
 <i>Look up a datum in a hash table. </i><br />
 void * <code>globus_hashtable_remove</code> (globus_hashtable_t *table, void *key)<br />
 <i>Remove a datum from a hash table. </i><br />
 int <code>globus_hashtable_to_list</code> (globus_hashtable_t *table, <code>globus_list_t</code> **list)<br />
 <i>Create a list of all datums in a hash table. </i><br />
 <code>globus_bool_t</code> <code>globus_hashtable_empty</code> (globus_hashtable_t *table)<br />
 <i>Test hash table emptiness. </i><br />
 int <code>globus_hashtable_size</code> (globus_hashtable_t *table)<br />
 <i>Hash table size. </i><br />
 int <code>globus_hashtable_destroy</code> (globus_hashtable_t *table)<br />
 <i>Destroy a hash table</i> </p>
<p> Destroys a hashtable representation, releasing any resources used to represent the mappings (abandoning any data in the queue). After this call, a hashtable is no longer considered initialized. &quot;<br />
 int <code>globus_hashtable_string_hash</code> (void *string, int limit)<br />
 <i>Null-terminated string hash function. </i><br />
 int <code>globus_hashtable_string_keyeq</code> (void *string1, void *string2)<br />
 <i>Null-terminated string equality predicate. </i><br />
 int <code>globus_hashtable_voidp_hash</code> (void *voidp, int limit)<br />
 <i>Void pointer hash function. </i><br />
 int <code>globus_hashtable_voidp_keyeq</code> (void *voidp1, void *voidp2)<br />
 <i>Void pointer equality predicate. </i><br />
 int <code>globus_hashtable_int_hash</code> (void *integer, int limit)<br />
 <i>Integer hash function. </i><br />
 int <code>globus_hashtable_int_keyeq</code> (void *integer1, void *integer2)<br />
 <i>Integer equality predicate. </i></p>
<h2>Detailed Description</h2>
<p> The globus_hashtable data type provides an abstract hashtable mapping representation and operations on such mappings. These queues can contain arbitrary data in the form of a void pointer for each key and a void pointer for each datum. It is the user&#8217;s responsibility to provide and interpret keys and data of the correct type.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_hashtable_copy_func_t)(void **dest_key, void **dest_datum, void *src_key, void *src_datum)</h3>
<p> datum copy func</p>
<h3>typedef void(* globus_hashtable_destructor_func_t)(void *datum)</h3>
<p> Destructor callback for use with globus_hashtable_destroy_all</p>
<h3>typedef int(* globus_hashtable_hash_func_t)(void *key, int limit)</h3>
<p> An anonymous hash function providing an onto mapping of (key, limit) pairs to integers, where the result integer is in the range [ 0, limit &#8211; 1 ] .</p>
<dl>
<dt>&bull;</p>
<dd> Note that as a proper function, such hash routines must always compute the same result given the same key and limit value.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Value to map<br />
 <i>limit</i> Map range limit</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Integer hash value of key</dl>
<h3>typedef int(* globus_hashtable_keyeq_func_t)(void *key1, void *key2)</h3>
<p> An anonymous predicate that returns true when the keys are equal and false otherwise. Truth and falsity are represented by non-zero and zero (0) integers for use directly in C language conditionals.</p>
<h2>Function Documentation</h2>
<h3>int globus_hashtable_destroy (globus_hashtable_t *table)</h3>
<p> Destroy a hash table </p>
<p> Destroys a hashtable representation, releasing any resources used to represent the mappings (abandoning any data in the queue). After this call, a hashtable is no longer considered initialized. It is an error to destroy a hashtable that is not initialized. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>table</i> Hash table to destroy.</dl>
<h3><code>globus_bool_t</code> globus_hashtable_empty (globus_hashtable_t *table)</h3>
<p> Test hash table emptiness. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_TRUE if hashtable is empty, GLOBUS_FALSE otherwise</dl>
<h3>int globus_hashtable_init (globus_hashtable_t *table, intsize, <code>globus_hashtable_hash_func_t</code>hash_func, <code>globus_hashtable_keyeq_func_t</code>keyeq_func)</h3>
<p> Initialize a hash table. Initializes a generic chaining hashtable to represent an empty mapping and returns zero, or returns non-zero on failure. The size parameter specifies the number of chains with which to represent the mapping. This defines the maximum possible number of mappings that can be represented without conflict given a perfect hash, and therefore affects performance as hash conflicts will be resolved by linear chains. </p>
<p> The hash_func and keyeq_func anonymous functions will be used by the table to manipulate the user&#8217;s keys.</p>
<h3>int globus_hashtable_insert (globus_hashtable_t *table, void *key, void *datum)</h3>
<p> Insert a datum into a hash table. The routine globus_hashtable_insert adds a new mapping to the table, returning zero on success or non-zero on failure. Any previous mapping for the same key (where equality is defined by the keyeq_func provided at table initialization) is lost. </p>
<p> It is an error to call this routine on an uninitialized table.</p>
<h3>int globus_hashtable_int_hash (void *integer, intlimit)</h3>
<p> Integer hash function. A pathetic hash function for integers, calculating the index as the remainder of dividing the integer by the table size. </p>
<p> Your pet gerbil could probably design a better hash function for your integer keys, but you might as well use this one if you were going to use modular division anyway.</p>
<h3>void* globus_hashtable_lookup (globus_hashtable_t *table, void *key)</h3>
<p> Look up a datum in a hash table. The globus_hashtable_lookup routine returns the datum mapped to the given key in the table, or NULL if the key is not mapped. </p>
<p> It is an error to call this routine on an uninitialized or empty table.</p>
<h3>void* globus_hashtable_remove (globus_hashtable_t *table, void *key)</h3>
<p> Remove a datum from a hash table. The <code>globus_hashtable_remove()</code> function removes the mapping of key in the table, or does nothing if no such mapping exists. </p>
<p> It is an error to call this routine on an uninitialized or empty table.</p>
<h3>int globus_hashtable_size (globus_hashtable_t *table)</h3>
<p> Hash table size. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Number of entries in hashtable</dl>
<h3>int globus_hashtable_string_hash (void *string, intlimit)</h3>
<p> Null-terminated string hash function. A decent hash function for null-terminated character arrays.</p>
<h3>void* globus_hashtable_update (globus_hashtable_t *table, void *key, void *datum)</h3>
<p> Update a hash table mapping. Update an existing key -&gt; datum association with new values for both, key and datum. The old datum is returned. If key is non-scalar (eg, string), it should be part of datum so its resources may be recovered. If old key does not exist, NULL is returned.</p>
<h3>int globus_hashtable_voidp_hash (void *voidp, intlimit)</h3>
<p> Void pointer hash function. A decent hash function for void pointers. This routine goes to some effort to distribute the information from the address into the hash index by XORing the upper and lower halves of the pointer into one accumulator and calculating the index as the remainder of dividing the accumulator by the table size.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAX">Author</a></p>
<dd></dl>
