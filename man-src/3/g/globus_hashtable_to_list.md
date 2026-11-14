---
title: "globus_hashtable_to_list(3)"
name: "globus_hashtable_to_list"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_hashtable_to_list/"
description: "globus_hashtable.h –"
---

<h2 class="name">NAME</h2>
<p> globus_hashtable.h &#8211; </p>
<p> Hash Table.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_types.h&#8217;<br />
 #include &#8216;globus_list.h&#8217; </p>
<h3>Typedefs</h3>
<p> typedef int(* <code>globus_hashtable_hash_func_t</code> )(void *key, int limit) </p>
<p> typedef int(* <code>globus_hashtable_keyeq_func_t</code> )(void *key1, void *key2) </p>
<p> typedef void(* <code>globus_hashtable_copy_func_t</code> )(void **dest_key, void **dest_datum, void *src_key, void *src_datum) </p>
<p> typedef void(* <code>globus_hashtable_destructor_func_t</code> )(void *datum) </p>
<h3>Functions</h3>
<p> int <code>globus_hashtable_init</code> (globus_hashtable_t *table, int size, <code>globus_hashtable_hash_func_t</code> hash_func, <code>globus_hashtable_keyeq_func_t</code> keyeq_func)<br />
 <i>Initialize a hash table. </i><br />
 void * <code>globus_hashtable_lookup</code> (globus_hashtable_t *table, void *key)<br />
 <i>Look up a datum in a hash table. </i><br />
 int <code>globus_hashtable_insert</code> (globus_hashtable_t *table, void *key, void *datum)<br />
 <i>Insert a datum into a hash table. </i><br />
 void * <code>globus_hashtable_update</code> (globus_hashtable_t *table, void *key, void *datum)<br />
 <i>Update a hash table mapping. </i><br />
 void * <code>globus_hashtable_remove</code> (globus_hashtable_t *table, void *key)<br />
 <i>Remove a datum from a hash table. </i><br />
 int <code>globus_hashtable_to_list</code> (globus_hashtable_t *table, <code>globus_list_t</code> **list)<br />
 <i>Create a list of all datums in a hash table. </i><br />
 <code>globus_bool_t</code> <code>globus_hashtable_empty</code> (globus_hashtable_t *table)<br />
 <i>Test hash table emptiness. </i><br />
 int <code>globus_hashtable_size</code> (globus_hashtable_t *table)<br />
 <i>Hash table size. </i><br />
 void * <code>globus_hashtable_first</code> (globus_hashtable_t *table)<br />
 <i>Initialize iterator to first hash table entry. </i><br />
 void * <code>globus_hashtable_next</code> (globus_hashtable_t *table)<br />
 <i>Increment hash table iterator. </i><br />
 void * <code>globus_hashtable_last</code> (globus_hashtable_t *table)<br />
 <i>Initialize iterator to last hash table entry. </i><br />
 void * <code>globus_hashtable_prev</code> (globus_hashtable_t *table)<br />
 <i>Decrement hash table iterator. </i><br />
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
<p> Hash Table. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
