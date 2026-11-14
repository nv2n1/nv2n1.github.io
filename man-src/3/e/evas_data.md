---
title: "evas_data(3)"
name: "evas_data"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_data/"
description: "Evas_Data.h – These routines are used for Evas data types."
---

<p>Evas_Data.h &#8211; These routines are used for Evas data types. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>_Evas_Array</code><br />
 <i>An array of data. </i><br />
 struct <code>_Evas_List</code><br />
 <i>A linked list node. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>_Evas_Array</code> <code>Evas_Array</code><br />
 <i>A generic vector. </i><br />
 typedef struct _Evas_Hash <code>Evas_Hash</code><br />
 <i>A Hash table handle. </i><br />
 typedef struct <code>_Evas_List</code> <code>Evas_List</code><br />
 <i>A generic linked list node handle. </i></p>
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
 <i>Modifies the entry pointer at the specified key and returns the old entry. </i><br />
 EAPI int <code>evas_hash_size</code> (const <code>Evas_Hash</code> *hash)<br />
 <i>Retrieves the number of buckets available in the given hash table. </i><br />
 EAPI void <code>evas_hash_free</code> (<code>Evas_Hash</code> *hash)<br />
 <i>Free an entire hash table. </i><br />
 EAPI void <code>evas_hash_foreach</code> (const <code>Evas_Hash</code> *hash, Evas_Bool(*func)(const <code>Evas_Hash</code> *hash, const char *key, void *data, void *fdata), const void *fdata)<br />
 <i>Call a function on every member stored in the hash table. </i><br />
 EAPI int <code>evas_hash_alloc_error</code> (void)<br />
 <i>Return memory allocation failure flag after an function requiring allocation. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_append</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Appends the given data to the given linked list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prepend</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Prepends the given data to the given linked list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_append_relative</code> (<code>Evas_List</code> *list, const void *data, const void *relative)<br />
 <i>Inserts the given data into the given linked list after the specified data. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prepend_relative</code> (<code>Evas_List</code> *list, const void *data, const void *relative)<br />
 <i>Prepend a data pointer to a linked list before the memeber specified. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_remove</code> (<code>Evas_List</code> *list, const void *data)<br />
 <i>Removes the first instance of the specified data from the given list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_remove_list</code> (<code>Evas_List</code> *list, <code>Evas_List</code> *remove_list)<br />
 <i>Removes the specified data. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_promote_list</code> (<code>Evas_List</code> *list, <code>Evas_List</code> *move_list)<br />
 <i>Moves the specified data to the head of the list. </i><br />
 EAPI void * <code>evas_list_find</code> (const <code>Evas_List</code> *list, const void *data)<br />
 <i>Find a member of a list and return the member. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_find_list</code> (const <code>Evas_List</code> *list, const void *data)<br />
 <i>Find a member of a list and return the list node containing that member. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_free</code> (<code>Evas_List</code> *list)<br />
 <i>Free an entire list and all the nodes, ignoring the data contained. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_last</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the last list node in the list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_next</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the next list node after the specified list node. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_prev</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the previous list node before the specified list node. </i><br />
 EAPI void * <code>evas_list_data</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the list node data member. </i><br />
 EAPI int <code>evas_list_count</code> (const <code>Evas_List</code> *list)<br />
 <i>Get the count of the number of items in a list. </i><br />
 EAPI void * <code>evas_list_nth</code> (const <code>Evas_List</code> *list, int n)<br />
 <i>Get the nth member&#8217;s data pointer in a list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_nth_list</code> (const <code>Evas_List</code> *list, int n)<br />
 <i>Get the nth member&#8217;s list node in a list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_reverse</code> (<code>Evas_List</code> *list)<br />
 <i>Reverse all the elements in the list. </i><br />
 EAPI <code>Evas_List</code> * <code>evas_list_sort</code> (<code>Evas_List</code> *list, int size, int(*func)(void *, void *))<br />
 <i>Sort a list according to the ordering func will return. </i><br />
 EAPI int <code>evas_list_alloc_error</code> (void)<br />
 <i>Return the memory allocation failure flag after any operation needin allocation. </i></p>
<h2>Detailed Description</h2>
<p>These routines are used for Evas data types. </p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_List</code>* evas_list_promote_list (<code>Evas_List</code> * list, <code>Evas_List</code> * move_list)</h3>
<p>Moves the specified data to the head of the list. </p>
<p> Move a specified member to the head of the list </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list handle to move inside<br />
 <i>move_list</i> The list node which is to be moved</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new list handle to replace the old one</dl>
<p> Calling this function takes the list node move_list and moves it to the front of the list. </p>
<p> Example: </p>
<pre> extern Evas_List *list;
 Evas_List *l;
 extern void *my_data;
 for (l = list; l; l= l-&gt;next)
 {
 if (l-&gt;data == my_data)
 {
 list = evas_list_promote_list(list, l);
 break;
 }
 }</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::accounting, _Evas_List::next, and _Evas_List::prev.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
