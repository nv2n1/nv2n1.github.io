---
title: "ecore_data(3)"
name: "ecore_data"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_data/"
description: "Ecore_Data.h – Contains threading, list, hash, debugging and tree functions."
---

<p>Ecore_Data.h &#8211; Contains threading, list, hash, debugging and tree functions. </p>
<h2>Synopsis</h2>
<h3>Functions</h3>
<p>EAPI int <code>ecore_direct_compare</code> (const void *key1, const void *key2)<br />
 <i>Perform a direct comparison of two keys&#8217; values. </i><br />
 EAPI int <code>ecore_str_compare</code> (const void *key1, const void *key2)<br />
 <i>Perform a string comparison of two keys values. </i><br />
 EAPI unsigned int <code>ecore_direct_hash</code> (const void *key)<br />
 <i>Just casts the key to an unsigned int. </i><br />
 EAPI unsigned int <code>ecore_str_hash</code> (const void *key)<br />
 <i>Compute the hash value of a string. </i><br />
 EAPI Ecore_List * <code>ecore_list_new</code> (void)<br />
 <i>Create and initialize a new list. </i><br />
 EAPI int <code>ecore_list_init</code> (Ecore_List *list)<br />
 <i>Initialize a list to some sane starting values. </i><br />
 EAPI int <code>ecore_list_append</code> (Ecore_List *list, void *_data)<br />
 <i>Append data to the list. </i><br />
 EAPI int <code>ecore_list_prepend</code> (Ecore_List *list, void *_data)<br />
 <i>Prepend data to the beginning of the list. </i><br />
 EAPI int <code>ecore_list_insert</code> (Ecore_List *list, void *_data)<br />
 <i>Insert data in front of the current point in the list. </i><br />
 EAPI int <code>ecore_list_append_list</code> (Ecore_List *list, Ecore_List *append)<br />
 <i>Append a list to the list. </i><br />
 EAPI int <code>ecore_list_prepend_list</code> (Ecore_List *list, Ecore_List *prepend)<br />
 <i>Prepend a list to the beginning of the list. </i><br />
 EAPI int <code>ecore_list_remove_destroy</code> (Ecore_List *list)<br />
 <i>Remove and free the data in lists current position. </i><br />
 EAPI void * <code>ecore_list_remove</code> (Ecore_List *list)<br />
 <i>Remove the current item from the list. </i><br />
 EAPI void * <code>ecore_list_first_remove</code> (Ecore_List *list)<br />
 <i>Remove the first item from the list. </i><br />
 EAPI void * <code>ecore_list_last_remove</code> (Ecore_List *list)<br />
 <i>Remove the last item from the list. </i><br />
 EAPI void * <code>ecore_list_current</code> (Ecore_List *list)<br />
 <i>Retrieve the data pointed to by the current item in </i>list.<br />
 EAPI void * <code>ecore_list_first</code> (Ecore_List *list)<br />
 <i>Retrieve the data pointed to by the first item in </i>list.<br />
 EAPI void * <code>ecore_list_last</code> (Ecore_List *list)<br />
 <i>Retrieve the data pointed to by the last item in </i>list.<br />
 EAPI int <code>ecore_list_index</code> (Ecore_List *list)<br />
 <i>Returns the number of the current node. </i><br />
 EAPI int <code>ecore_list_count</code> (Ecore_List *list)<br />
 <i>Find the number of nodes in the list. </i><br />
 EAPI int <code>ecore_list_for_each</code> (Ecore_List *list, Ecore_For_Each function, void *user_data)<br />
 <i>Execute function for each node in </i>list.<br />
 EAPI void * <code>ecore_list_first_goto</code> (Ecore_List *list)<br />
 <i>Make the current item the first item in the list. </i><br />
 EAPI void * <code>ecore_list_last_goto</code> (Ecore_List *list)<br />
 <i>Make the current item the last item in the list. </i><br />
 EAPI void * <code>ecore_list_index_goto</code> (Ecore_List *list, int index)<br />
 <i>Make the current item the item with the given index number. </i><br />
 EAPI void * <code>ecore_list_goto</code> (Ecore_List *list, const void *_data)<br />
 <i>Make the current item the node that contains </i>data.<br />
 EAPI void * <code>ecore_list_next</code> (Ecore_List *list)<br />
 <i>Retrieve the data pointed to by the current item, and make the next item the current item. </i><br />
 EAPI void * <code>ecore_list_find</code> (Ecore_List *list, Ecore_Compare_Cb function, const void *user_data)<br />
 <i>Find data in </i>list using the compare function func.<br />
 EAPI int <code>ecore_list_sort</code> (Ecore_List *list, Ecore_Compare_Cb compare, char order)<br />
 <i>Sort data in </i>list using the compare function compare.<br />
 EAPI int <code>ecore_list_mergesort</code> (Ecore_List *list, Ecore_Compare_Cb compare, char order)<br />
 <i>Sort data in </i>list using the compare function compare.<br />
 EAPI int <code>ecore_list_heapsort</code> (Ecore_List *list, Ecore_Compare_Cb compare, char order)<br />
 <i>Sort data in </i>list using the compare function compare.<br />
 EAPI void <code>ecore_list_merge</code> (Ecore_List *list, Ecore_List *l2, Ecore_Compare_Cb, char order)<br />
 <i>Merge the </i>l2 into the list using the compare function compare.<br />
 EAPI int <code>ecore_list_empty_is</code> (Ecore_List *list)<br />
 <i>Checks the list for any nodes. </i><br />
 EAPI int <code>ecore_list_clear</code> (Ecore_List *list)<br />
 <i>Remove all nodes from </i>list.<br />
 EAPI void <code>ecore_list_destroy</code> (Ecore_List *list)<br />
 <i>Free a list and all of it&#8217;s nodes. </i><br />
 EAPI Ecore_List_Node * <code>ecore_list_node_new</code> (void)<br />
 <i>Allocates and initializes a new list node. </i><br />
 EAPI int <code>ecore_list_node_destroy</code> (Ecore_List_Node *_e_node, Ecore_Free_Cb free_func)<br />
 <i>Calls the function to free the data and the node. </i><br />
 EAPI int <code>ecore_list_free_cb_set</code> (Ecore_List *list, Ecore_Free_Cb free_func)<br />
 <i>Set the function for freeing data. </i><br />
 EAPI Ecore_DList * <code>ecore_dlist_new</code> (void)<br />
 <i>Creates and initialises a new doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_init</code> (Ecore_DList *list)<br />
 <i>Initialises a list to some sane starting values. </i><br />
 EAPI void <code>ecore_dlist_destroy</code> (Ecore_DList *list)<br />
 <i>Frees a doubly linked list and all of its nodes. </i><br />
 EAPI int <code>ecore_dlist_append</code> (Ecore_DList *_e_dlist, void *_data)<br />
 <i>Appends data to the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_prepend</code> (Ecore_DList *_e_dlist, void *_data)<br />
 <i>Adds data to the very beginning of the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_insert</code> (Ecore_DList *_e_dlist, void *_data)<br />
 <i>Inserts data at the current point in the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_append_list</code> (Ecore_DList *_e_dlist, Ecore_DList *append)<br />
 <i>Appends a list to the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_prepend_list</code> (Ecore_DList *_e_dlist, Ecore_DList *prepend)<br />
 <i>Adds a list to the very beginning of the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_current</code> (Ecore_DList *list)<br />
 <i>Return the data in the current list item. </i><br />
 EAPI int <code>ecore_dlist_index</code> (Ecore_DList *list)<br />
 <i>Retrieves the index of the current node of the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_remove</code> (Ecore_DList *_e_dlist)<br />
 <i>Removes the current item from the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_first_remove</code> (Ecore_DList *_e_dlist)<br />
 <i>Removes the first item from the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_remove_destroy</code> (Ecore_DList *list)<br />
 <i>Removes and frees the data at the current position in the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_last_remove</code> (Ecore_DList *_e_dlist)<br />
 <i>Removes the last item from the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_first_goto</code> (Ecore_DList *_e_dlist)<br />
 <i>Move the current pointer to the first item in the list. </i><br />
 EAPI void * <code>ecore_dlist_last_goto</code> (Ecore_DList *_e_dlist)<br />
 <i>Move the pointer to the current item to the last item. </i><br />
 EAPI void * <code>ecore_dlist_index_goto</code> (Ecore_DList *_e_dlist, int index)<br />
 <i>Moves the current item to the index number in the given doubly linked list. </i><br />
 EAPI void * <code>ecore_dlist_goto</code> (Ecore_DList *_e_dlist, void *_data)<br />
 <i>Move the current item to the node that contains data. </i><br />
 EAPI void * <code>ecore_dlist_next</code> (Ecore_DList *list)<br />
 <i>Move to the next item in the list and return current item. </i><br />
 EAPI void * <code>ecore_dlist_previous</code> (Ecore_DList *list)<br />
 <i>Move to the previous item and return current item. </i><br />
 EAPI int <code>ecore_dlist_sort</code> (Ecore_DList *list, Ecore_Compare_Cb compare, char order)<br />
 <i>Sort data in </i>list using the compare function compare.<br />
 EAPI int <code>ecore_dlist_mergesort</code> (Ecore_DList *list, Ecore_Compare_Cb compare, char order)<br />
 <i>Sort data in </i>list using the compare function compare.<br />
 EAPI void <code>ecore_dlist_merge</code> (Ecore_DList *list, Ecore_DList *l2, Ecore_Compare_Cb, char order)<br />
 <i>Merge the </i>l2 into the list using the compare function compare.<br />
 EAPI int <code>ecore_dlist_empty_is</code> (Ecore_DList *_e_dlist)<br />
 <i>Returns whether there is anything in the given doubly linked list. </i><br />
 EAPI int <code>ecore_dlist_clear</code> (Ecore_DList *_e_dlist)<br />
 <i>Remove all nodes from the list. </i><br />
 EAPI int <code>ecore_dlist_free_cb_set</code> (Ecore_DList *dlist, Ecore_Free_Cb free_func)<br />
 <i>Sets the function used for freeing data stored in a doubly linked list. </i><br />
 EAPI Ecore_Hash * <code>ecore_hash_new</code> (Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)<br />
 <i>Creates and initializes a new hash. </i><br />
 EAPI int <code>ecore_hash_init</code> (Ecore_Hash *hash, Ecore_Hash_Cb hash_func, Ecore_Compare_Cb compare)<br />
 <i>Initializes the given hash. </i><br />
 EAPI int <code>ecore_hash_free_key_cb_set</code> (Ecore_Hash *hash, Ecore_Free_Cb function)<br />
 <i>Sets the function to destroy the keys of the given hash. </i><br />
 EAPI int <code>ecore_hash_free_value_cb_set</code> (Ecore_Hash *hash, Ecore_Free_Cb function)<br />
 <i>Sets the function to destroy the values in the given hash. </i><br />
 EAPI void <code>ecore_hash_destroy</code> (Ecore_Hash *hash)<br />
 <i>Frees the hash table and the data contained inside it. </i><br />
 EAPI int <code>ecore_hash_count</code> (Ecore_Hash *hash)<br />
 <i>Counts the number of nodes in a hash table. </i><br />
 EAPI int <code>ecore_hash_for_each_node</code> (Ecore_Hash *hash, Ecore_For_Each for_each_func, void *user_data)<br />
 <i>Runs the </i>for_each_func function on each entry in the given hash.<br />
 EAPI Ecore_List * <code>ecore_hash_keys</code> (Ecore_Hash *hash)<br />
 <i>Retrieves an ecore_list of all keys in the given hash. </i><br />
 EAPI void * <code>ecore_hash_get</code> (Ecore_Hash *hash, const void *key)<br />
 <i>Retrieves the value associated with the given key from the given hash table. </i><br />
 EAPI int <code>ecore_hash_set</code> (Ecore_Hash *hash, void *key, void *value)<br />
 <i>Sets a key-value pair in the given hash table. </i><br />
 EAPI int <code>ecore_hash_hash_set</code> (Ecore_Hash *hash, Ecore_Hash *set)<br />
 <i>Sets all key-value pairs from set in the given hash table. </i><br />
 EAPI void * <code>ecore_hash_remove</code> (Ecore_Hash *hash, const void *key)<br />
 <i>Removes the value associated with the given key in the given hash table. </i><br />
 EAPI void * <code>ecore_hash_find</code> (Ecore_Hash *hash, Ecore_Compare_Cb compare, const void *value)<br />
 <i>Retrieves the first value that matches table. </i><br />
 EAPI void <code>ecore_hash_dump_graph</code> (Ecore_Hash *hash)<br />
 <i>Prints the distribution of the given hash table for graphing. </i><br />
 EAPI void <code>ecore_hash_dump_stats</code> (Ecore_Hash *hash)<br />
 <i>Prints the distribution of the given hash table for graphing. </i><br />
 EAPI Ecore_Path_Group * <code>ecore_path_group_new</code> (void)<br />
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
 <i>Retrieves a list of all available files in the given path. </i><br />
 EAPI Ecore_Plugin * <code>ecore_plugin_load</code> (Ecore_Path_Group *group, const char *plugin, const char *version)<br />
 <i>Loads the specified plugin from the specified path group. </i><br />
 EAPI void <code>ecore_plugin_unload</code> (Ecore_Plugin *plugin)<br />
 <i>Unloads the given plugin from memory. </i><br />
 EAPI Ecore_List * <code>ecore_plugin_available_get</code> (Ecore_Path_Group *group)<br />
 <i>Retrieves a list of all available plugins in the given path. </i><br />
 EAPI Ecore_Sheap * <code>ecore_sheap_new</code> (Ecore_Compare_Cb compare, int size)<br />
 <i>Allocate and initialize a new binary heap. </i><br />
 EAPI void <code>ecore_sheap_destroy</code> (Ecore_Sheap *heap)<br />
 <i>Free up the memory used by the heap. </i><br />
 EAPI int <code>ecore_sheap_init</code> (Ecore_Sheap *heap, Ecore_Compare_Cb compare, int size)<br />
 <i>Initialize a binary heap to default values. </i><br />
 EAPI int <code>ecore_sheap_free_cb_set</code> (Ecore_Sheap *heap, Ecore_Free_Cb free_func)<br />
 <i>Set the function for freeing data. </i><br />
 EAPI int <code>ecore_sheap_insert</code> (Ecore_Sheap *heap, void *data)<br />
 <i>Insert new data into the heap. </i><br />
 EAPI void * <code>ecore_sheap_extract</code> (Ecore_Sheap *heap)<br />
 <i>Extract the item at the top of the heap. </i><br />
 EAPI void * <code>ecore_sheap_extreme</code> (Ecore_Sheap *heap)<br />
 <i>Examine the item at the top of the heap. </i><br />
 EAPI int <code>ecore_sheap_change</code> (Ecore_Sheap *heap, void *item, void *newval)<br />
 <i>Change the value of the specified item in the heap. </i><br />
 EAPI int <code>ecore_sheap_compare_set</code> (Ecore_Sheap *heap, Ecore_Compare_Cb compare)<br />
 <i>Change the comparison function for the heap. </i><br />
 EAPI void <code>ecore_sheap_order_set</code> (Ecore_Sheap *heap, char order)<br />
 <i>Change the order of the heap. </i><br />
 EAPI void <code>ecore_sheap_sort</code> (Ecore_Sheap *heap)<br />
 <i>Sort the data in the heap. </i><br />
 EAPI int <code>ecore_string_init</code> (void)<br />
 <i>Initialize the ecore string internal structure. </i><br />
 EAPI void <code>ecore_string_shutdown</code> (void)<br />
 <i>Shutdown the ecore string internal structures. </i><br />
 EAPI const char * <code>ecore_string_instance</code> (const char *string)<br />
 <i>Retrieves an instance of a string for use in an ecore program. </i><br />
 EAPI void <code>ecore_string_release</code> (const char *string)<br />
 <i>Notes that the given string has lost an instance. </i><br />
 EAPI Ecore_Tree * <code>ecore_tree_new</code> (Ecore_Compare_Cb compare_func)<br />
 <i>Allocate a new tree structure. </i><br />
 EAPI int <code>ecore_tree_init</code> (Ecore_Tree *tree, Ecore_Compare_Cb compare_func)<br />
 <i>Initialize a tree structure to some sane initial values. </i><br />
 EAPI int <code>ecore_tree_destroy</code> (Ecore_Tree *tree)<br />
 <i>Free the tree and it&#8217;s stored data. </i><br />
 EAPI int <code>ecore_tree_empty_is</code> (Ecore_Tree *tree)<br />
 <i>Test to see if the tree has any nodes. </i><br />
 EAPI void * <code>ecore_tree_get</code> (Ecore_Tree *tree, const void *key)<br />
 <i>Return the value corresponding to key. </i><br />
 EAPI Ecore_Tree_Node * <code>ecore_tree_get_node</code> (Ecore_Tree *tree, const void *key)<br />
 <i>Return the node corresponding to key. </i><br />
 EAPI void * <code>ecore_tree_closest_larger_get</code> (Ecore_Tree *tree, const void *key)<br />
 <i>Find the closest value greater than or equal to the key. </i><br />
 EAPI void * <code>ecore_tree_closest_smaller_get</code> (Ecore_Tree *tree, const void *key)<br />
 <i>Find the closest value &lt;= key. </i><br />
 EAPI int <code>ecore_tree_set</code> (Ecore_Tree *tree, void *key, void *value)<br />
 <i>Set the value associated with key to value</i>.<br />
 EAPI int <code>ecore_tree_remove</code> (Ecore_Tree *tree, const void *key)<br />
 <i>Remove the key from the tree. </i><br />
 EAPI int <code>ecore_tree_node_add</code> (Ecore_Tree *tree, Ecore_Tree_Node *node)<br />
 <i>Place a node in the tree. </i><br />
 EAPI int <code>ecore_tree_node_remove</code> (Ecore_Tree *tree, Ecore_Tree_Node *node)<br />
 <i>Remove the node from the tree. </i><br />
 EAPI int <code>ecore_tree_for_each_node</code> (Ecore_Tree *tree, Ecore_For_Each for_each_func, void *user_data)<br />
 <i>Execute the function for each node in the tree. </i><br />
 EAPI int <code>ecore_tree_for_each_node_value</code> (Ecore_Tree *tree, Ecore_For_Each for_each_func, void *user_data)<br />
 <i>Execute function for each value in the tree. </i><br />
 EAPI Ecore_Strbuf * <code>ecore_strbuf_new</code> (void)<br />
 <i>Create a new string buffer. </i><br />
 EAPI void <code>ecore_strbuf_free</code> (Ecore_Strbuf *buf)<br />
 <i>Free a string buffer. </i><br />
 EAPI void <code>ecore_strbuf_append</code> (Ecore_Strbuf *buf, const char *str)<br />
 <i>Append a string to a buffer, reallocating as necessary. </i><br />
 EAPI void <code>ecore_strbuf_append_char</code> (Ecore_Strbuf *buf, char c)<br />
 <i>Append a character to a string buffer, reallocating as necessary. </i><br />
 EAPI void <code>ecore_strbuf_insert</code> (Ecore_Strbuf *buf, const char *str, size_t pos)<br />
 <i>Insert a string to a buffer, reallocating as necessary. </i><br />
 EAPI const char * <code>ecore_strbuf_string_get</code> (Ecore_Strbuf *buf)<br />
 <i>Retrieve a pointer to the contents of a string buffer. </i><br />
 EAPI size_t <code>ecore_strbuf_length_get</code> (Ecore_Strbuf *buf)<br />
 <i>Retrieve the length of the string buffer content. </i><br />
 EAPI int <code>ecore_strbuf_replace</code> (Ecore_Strbuf *buf, const char *str, const char *with, unsigned int n)<br />
 <i>Replace the n-th string with an other string. </i><br />
 EAPI int <code>ecore_strbuf_replace_all</code> (Ecore_Strbuf *buf, const char *str, const char *with)<br />
 <i>Replace all strings with an other string. </i></p>
<h2>Detailed Description</h2>
<p>Contains threading, list, hash, debugging and tree functions. </p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_direct_compare (const void * key1, const void * key2)</h3>
<p>Perform a direct comparison of two keys&#8217; values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key1</i> The first key to compare<br />
 <i>key2</i> The second key to compare</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A strcmp style value to indicate the larger key</dl>
<p> References ecore_direct_compare(). </p>
<p> Referenced by ecore_con_url_destroy(), ecore_direct_compare(), ecore_sheap_compare_set(), ecore_sheap_init(), ecore_str_compare(), ecore_tree_init(), and ecore_x_netwm_init().</p>
<h3>EAPI unsigned int ecore_direct_hash (const void * key)</h3>
<p>Just casts the key to an unsigned int. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key to return compute a hash value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The key cast to an unsigned int.</dl>
<p> References ecore_direct_hash(). </p>
<p> Referenced by ecore_direct_hash(), and ecore_x_netwm_init().</p>
<h3>EAPI int ecore_dlist_clear (Ecore_DList * list)</h3>
<p>Remove all nodes from the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to remove all nodes from</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on success, FALSE on errors</dl>
<p> References ecore_dlist_clear(), and ecore_list_clear(). </p>
<p> Referenced by ecore_dlist_clear().</p>
<h3>EAPI void* ecore_dlist_current (Ecore_DList * list)</h3>
<p>Return the data in the current list item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to the return the current data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns value of the current data item, NULL if no current item</dl>
<p> References ecore_dlist_current(). </p>
<p> Referenced by ecore_dlist_current().</p>
<h3>EAPI int ecore_dlist_empty_is (Ecore_DList * list)</h3>
<p>Returns whether there is anything in the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if there are nodes, FALSE otherwise.</dl>
<p> References ecore_dlist_empty_is(), and ecore_list_empty_is(). </p>
<p> Referenced by ecore_dlist_append_list(), ecore_dlist_empty_is(), ecore_dlist_merge(), and ecore_dlist_prepend_list().</p>
<h3>EAPI void* ecore_dlist_first_goto (Ecore_DList * list)</h3>
<p>Move the current pointer to the first item in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to change the current to the first item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns a pointer to the first item on success, NULL on failure.</dl>
<p> References ecore_dlist_first_goto(). </p>
<p> Referenced by ecore_dlist_first_goto().</p>
<h3>EAPI void* ecore_dlist_goto (Ecore_DList * list, void * data)</h3>
<p>Move the current item to the node that contains data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to move the current item in<br />
 <i>data,:</i> the data to find and set the current item to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns specified data on success, NULL on error</dl>
<p> References ecore_dlist_goto(). </p>
<p> Referenced by ecore_dlist_goto().</p>
<h3>EAPI int ecore_dlist_index (Ecore_DList * list) [inline]</h3>
<p>Retrieves the index of the current node of the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The index of the current node.</dl>
<p> References ecore_dlist_index(), and ecore_list_index(). </p>
<p> Referenced by ecore_dlist_index().</p>
<h3>EAPI void* ecore_dlist_index_goto (Ecore_DList * list, int index)</h3>
<p>Moves the current item to the index number in the given doubly linked list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The given doubly linked list.<br />
 <i>index</i> The position to move the current item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The node at specified index on success, NULL on error.</dl>
<p> References ecore_dlist_index_goto(). </p>
<p> Referenced by ecore_dlist_index_goto().</p>
<h3>EAPI void* ecore_dlist_last_goto (Ecore_DList * list)</h3>
<p>Move the pointer to the current item to the last item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to move the current item pointer to the last</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns a pointer to the last item in the list , NULL if empty.</dl>
<p> References ecore_dlist_last_goto(). </p>
<p> Referenced by ecore_dlist_last_goto().</p>
<h3>EAPI void ecore_dlist_merge (Ecore_DList * list, Ecore_DList * l2, Ecore_Compare_Cb compare, char order)</h3>
<p>Merge the l2 into the list using the compare function compare. </p>
<p> Both lists need to be sorted else a corrupt list could be the result. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>l2</i> The second list, this list will be empty after the merge<br />
 <i>compare</i> The function to compare the data of list and l2<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> References ecore_dlist_append_list(), ecore_dlist_empty_is(), ecore_dlist_init(), and ecore_dlist_merge(). </p>
<p> Referenced by ecore_dlist_merge().</p>
<h3>EAPI int ecore_dlist_mergesort (Ecore_DList * list, Ecore_Compare_Cb compare, char order)</h3>
<p>Sort data in list using the compare function compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>compare</i> The function to compare the data of list<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> Mergesort is a stable, in-place sorting algorithm </p>
<p> References ecore_dlist_mergesort(). </p>
<p> Referenced by ecore_dlist_mergesort(), and ecore_dlist_sort().</p>
<h3>EAPI void* ecore_dlist_next (Ecore_DList * list)</h3>
<p>Move to the next item in the list and return current item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to move to the next item in.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns data in the current list node, or NULL on error</dl>
<p> References ecore_dlist_next(). </p>
<p> Referenced by ecore_dlist_next().</p>
<h3>EAPI void* ecore_dlist_previous (Ecore_DList * list)</h3>
<p>Move to the previous item and return current item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list,:</i> the list to move to the previous item in.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns data in the current list node, or NULL on error</dl>
<p> References ecore_dlist_previous(). </p>
<p> Referenced by ecore_dlist_previous().</p>
<h3>EAPI int ecore_dlist_sort (Ecore_List * list, Ecore_Compare_Cb compare, char order)</h3>
<p>Sort data in list using the compare function compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>compare</i> The function to compare the data of list<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> This is a wrapper function for mergesort and heapsort. It tries to choose the fastest algorithm depending on the number of notes. Note: The sort may be unstable. </p>
<p> References ecore_dlist_mergesort(), and ecore_dlist_sort(). </p>
<p> Referenced by ecore_dlist_sort().</p>
<h3>EAPI void ecore_hash_dump_graph (Ecore_Hash * hash)</h3>
<p>Prints the distribution of the given hash table for graphing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.</dl>
<p> References ecore_hash_dump_graph(). </p>
<p> Referenced by ecore_hash_dump_graph().</p>
<h3>EAPI void ecore_hash_dump_stats (Ecore_Hash * hash)</h3>
<p>Prints the distribution of the given hash table for graphing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hash</i> The given hash table.</dl>
<p> References ecore_hash_dump_stats(). </p>
<p> Referenced by ecore_hash_dump_stats().</p>
<h3>EAPI int ecore_list_clear (Ecore_List * list)</h3>
<p>Remove all nodes from list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on success, FALSE on error.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The data for each item on the list is not freed by <code>ecore_list_clear()</code>.</dl>
<p> References ecore_list_clear(), and ecore_list_empty_is(). </p>
<p> Referenced by ecore_dlist_clear(), and ecore_list_clear().</p>
<h3>EAPI int ecore_list_count (Ecore_List * list)</h3>
<p>Find the number of nodes in the list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to find the number of nodes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of nodes in the list.</dl>
<p> References ecore_list_count(). </p>
<p> Referenced by ecore_list_count().</p>
<h3>EAPI void* ecore_list_current (Ecore_List * list) [inline]</h3>
<p>Retrieve the data pointed to by the current item in list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the data at current position, can be NULL.</dl>
<p> References ecore_list_current(). </p>
<p> Referenced by ecore_list_current(), and ecore_path_group_remove().</p>
<h3>EAPI int ecore_list_empty_is (Ecore_List * list)</h3>
<p>Checks the list for any nodes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to check for nodes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if no nodes in list, FALSE if the list contains nodes</dl>
<p> References ecore_list_empty_is(). </p>
<p> Referenced by ecore_con_shutdown(), ecore_con_url_shutdown(), ecore_dlist_empty_is(), ecore_dlist_last_remove(), ecore_list_append_list(), ecore_list_clear(), ecore_list_empty_is(), ecore_list_merge(), ecore_list_prepend_list(), ecore_path_group_available(), ecore_plugin_available_get(), and ecore_plugin_unload().</p>
<h3>EAPI void* ecore_list_find (Ecore_List * list, Ecore_Compare_Cb function, const void * user_data)</h3>
<p>Find data in list using the compare function func. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>function</i> The function to test each node of list with<br />
 <i>user_data</i> Data to match against (used by function)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the first matching data node, or NULL if none match</dl>
<p> References ecore_list_find(). </p>
<p> Referenced by ecore_con_url_destroy(), and ecore_list_find().</p>
<h3>EAPI void* ecore_list_first (Ecore_List * list) [inline]</h3>
<p>Retrieve the data pointed to by the first item in list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the data at current position, can be NULL.</dl>
<p> References ecore_list_first(). </p>
<p> Referenced by ecore_con_url_shutdown(), and ecore_list_first().</p>
<h3>EAPI int ecore_list_free_cb_set (Ecore_List * list, Ecore_Free_Cb free_func)</h3>
<p>Set the function for freeing data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list that will use this function when nodes are destroyed.<br />
 <i>free_func</i> The function that will free the key data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on successful set, FALSE otherwise.</dl>
<p> References ecore_list_free_cb_set(). </p>
<p> Referenced by ecore_dlist_free_cb_set(), ecore_file_app_list(), ecore_file_ls(), ecore_list_free_cb_set(), ecore_path_group_add(), and ecore_plugin_available_get().</p>
<h3>EAPI int ecore_list_heapsort (Ecore_List * list, Ecore_Compare_Cb compare, char order)</h3>
<p>Sort data in list using the compare function compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>compare</i> The function to compare the data of list<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> Heapsort is a unstable sorting algorithm, it needs to allocate extra memomry, but there for it is for a great number of nodes faster than mergesort </p>
<p> References ecore_list_heapsort(), ecore_sheap_destroy(), ecore_sheap_extract(), ecore_sheap_insert(), ecore_sheap_new(), and ecore_sheap_order_set(). </p>
<p> Referenced by ecore_list_heapsort(), and ecore_list_sort().</p>
<h3>EAPI int ecore_list_index (Ecore_List * list)</h3>
<p>Returns the number of the current node. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to return the number of the current node.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of the current node in the list.</dl>
<p> References ecore_list_index(). </p>
<p> Referenced by ecore_dlist_index(), and ecore_list_index().</p>
<h3>EAPI void* ecore_list_last (Ecore_List * list) [inline]</h3>
<p>Retrieve the data pointed to by the last item in list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the data at current position, can be NULL.</dl>
<p> References ecore_list_last(). </p>
<p> Referenced by ecore_list_last().</p>
<h3>EAPI void ecore_list_merge (Ecore_List * list, Ecore_List * l2, Ecore_Compare_Cb compare, char order)</h3>
<p>Merge the l2 into the list using the compare function compare. </p>
<p> Both lists need to be sorted else a corrupt list could be the result. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>l2</i> The second list, this list will be empty after the merge<br />
 <i>compare</i> The function to compare the data of list and l2<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> References ecore_list_append_list(), ecore_list_empty_is(), ecore_list_init(), and ecore_list_merge(). </p>
<p> Referenced by ecore_list_merge().</p>
<h3>EAPI int ecore_list_mergesort (Ecore_List * list, Ecore_Compare_Cb compare, char order)</h3>
<p>Sort data in list using the compare function compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>compare</i> The function to compare the data of list<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> Mergesort is a stable, in-place sorting algorithm </p>
<p> References ecore_list_mergesort(). </p>
<p> Referenced by ecore_list_mergesort(), and ecore_list_sort().</p>
<h3>EAPI void* ecore_list_next (Ecore_List * list) [inline]</h3>
<p>Retrieve the data pointed to by the current item, and make the next item the current item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list to retrieve data from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current item in the list on success, NULL on failure.</dl>
<p> References ecore_list_next(). </p>
<p> Referenced by ecore_file_app_installed(), ecore_file_app_list(), ecore_file_path_dir_exists(), ecore_list_next(), ecore_path_group_available(), ecore_path_group_find(), ecore_path_group_remove(), and ecore_plugin_available_get().</p>
<h3>EAPI int ecore_list_sort (Ecore_List * list, Ecore_Compare_Cb compare, char order)</h3>
<p>Sort data in list using the compare function compare. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>list</i> The list.<br />
 <i>compare</i> The function to compare the data of list<br />
 <i>order</i> The sort direction, possible values are ECORE_SORT_MIN and ECORE_SORT_MAX</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> This is a wrapper function for mergesort and heapsort. It tries to choose the fastest algorithm depending on the number of notes. Note: The sort may be unstable. </p>
<p> References ecore_list_heapsort(), ecore_list_mergesort(), and ecore_list_sort(). </p>
<p> Referenced by ecore_file_ls(), and ecore_list_sort().</p>
<h3>EAPI int ecore_sheap_change (Ecore_Sheap * heap, void * item, void * newval)</h3>
<p>Change the value of the specified item in the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to search for the item to change<br />
 <i>item</i> The item in the heap to change<br />
 <i>newval</i> The new value assigned to the item in the heap</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on failure.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The heap does not free the old data since it must be passed in, so the caller can perform the free if desired.</dl>
<p> References ecore_sheap_change(). </p>
<p> Referenced by ecore_sheap_change().</p>
<h3>EAPI int ecore_sheap_compare_set (Ecore_Sheap * heap, Ecore_Compare_Cb compare)</h3>
<p>Change the comparison function for the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to change comparison function<br />
 <i>compare</i> The new function for comparing nodes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on failure.</dl>
<p> The comparison function is changed to and the heap is heapified by the new comparison. </p>
<p> References ecore_direct_compare(), and ecore_sheap_compare_set(). </p>
<p> Referenced by ecore_sheap_compare_set().</p>
<h3>EAPI void ecore_sheap_destroy (Ecore_Sheap * heap)</h3>
<p>Free up the memory used by the heap. </p>
<p> Frees the memory used by <i>heap</i>, calls the destroy function on each data item if necessary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to be freed</dl>
<p> References ecore_sheap_destroy(). </p>
<p> Referenced by ecore_list_heapsort(), and ecore_sheap_destroy().</p>
<h3>EAPI void* ecore_sheap_extract (Ecore_Sheap * heap)</h3>
<p>Extract the item at the top of the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to remove the top item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The top item of the heap on success, NULL on failure.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The extract function maintains the heap properties after the extract.</dl>
<p> References ecore_sheap_extract(). </p>
<p> Referenced by ecore_list_heapsort(), ecore_sheap_extract(), and ecore_sheap_sort().</p>
<h3>EAPI void* ecore_sheap_extreme (Ecore_Sheap * heap)</h3>
<p>Examine the item at the top of the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to examine the top item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The top item of the heap on success, NULL on failure.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The function does not alter the heap.</dl>
<p> References ecore_sheap_extreme(). </p>
<p> Referenced by ecore_sheap_extreme().</p>
<h3>EAPI int ecore_sheap_free_cb_set (Ecore_Sheap * heap, Ecore_Free_Cb free_func)</h3>
<p>Set the function for freeing data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap that will use this function when nodes are destroyed.<br />
 <i>free_func</i> The function that will free the key data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on successful set, FALSE otherwise.</dl>
<p> References ecore_sheap_free_cb_set(). </p>
<p> Referenced by ecore_sheap_free_cb_set().</p>
<h3>EAPI int ecore_sheap_init (Ecore_Sheap * heap, Ecore_Compare_Cb compare, int size)</h3>
<p>Initialize a binary heap to default values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to initialize<br />
 <i>compare</i> The function for comparing keys, NULL for direct comparison<br />
 <i>size</i> The number of elements to allow in the heap</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, FALSE on failure</dl>
<p> References ecore_direct_compare(), and ecore_sheap_init(). </p>
<p> Referenced by ecore_sheap_init(), and ecore_sheap_new().</p>
<h3>EAPI int ecore_sheap_insert (Ecore_Sheap * heap, void * data)</h3>
<p>Insert new data into the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to insert <i>data</i>.<br />
 <i>data</i> The data to add to <i>heap</i>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on success, NULL on failure. Increases the size of the heap if it becomes larger than available space.</dl>
<p> References ecore_sheap_insert(). </p>
<p> Referenced by ecore_list_heapsort(), and ecore_sheap_insert().</p>
<h3>EAPI Ecore_Sheap* ecore_sheap_new (Ecore_Compare_Cb compare, int size)</h3>
<p>Allocate and initialize a new binary heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compare</i> The function for comparing keys, NULL for direct comparison<br />
 <i>size</i> The number of elements to allow in the heap</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the newly allocated binary heap on success, NULL on failure.</dl>
<p> References ecore_sheap_init(), and ecore_sheap_new(). </p>
<p> Referenced by ecore_list_heapsort(), and ecore_sheap_new().</p>
<h3>EAPI void ecore_sheap_order_set (Ecore_Sheap * heap, char order)</h3>
<p>Change the order of the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to change the order<br />
 <i>order</i> The new order of the heap</dl>
<p> Changes the heap order of and re-heapifies the data to this new order. The default order is a min heap. </p>
<p> References ecore_sheap_order_set(). </p>
<p> Referenced by ecore_list_heapsort(), and ecore_sheap_order_set().</p>
<h3>EAPI void ecore_sheap_sort (Ecore_Sheap * heap)</h3>
<p>Sort the data in the heap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>heap</i> The heap to be sorted</dl>
<p> Sorts the data in the heap into the order that is used for the heap&#8217;s data. </p>
<p> References ecore_sheap_extract(), and ecore_sheap_sort(). </p>
<p> Referenced by ecore_sheap_sort().</p>
<h3>EAPI int ecore_str_compare (const void * key1, const void * key2)</h3>
<p>Perform a string comparison of two keys values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key1</i> The first key to compare<br />
 <i>key2</i> The second key to compare</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A strcmp style value to indicate the larger key</dl>
<p> References ecore_direct_compare(), and ecore_str_compare(). </p>
<p> Referenced by ecore_plugin_available_get(), ecore_str_compare(), and ecore_string_init().</p>
<h3>EAPI unsigned int ecore_str_hash (const void * key)</h3>
<p>Compute the hash value of a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> A pointer to the string to compute a hash value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A computed hash value for <i>key</i>.</dl>
<p> References ecore_str_hash(). </p>
<p> Referenced by ecore_plugin_available_get(), ecore_str_hash(), and ecore_string_init().</p>
<h3>EAPI void ecore_strbuf_append (Ecore_Strbuf * buf, const char * str)</h3>
<p>Append a string to a buffer, reallocating as necessary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the Ecore_Strbuf to append to<br />
 <i>str</i> the string to append</dl>
<p> References ecore_strbuf_append(). </p>
<p> Referenced by ecore_strbuf_append(), and ecore_strbuf_insert().</p>
<h3>EAPI void ecore_strbuf_append_char (Ecore_Strbuf * buf, char c)</h3>
<p>Append a character to a string buffer, reallocating as necessary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the Ecore_Strbuf to append to<br />
 <i>c</i> the char to append</dl>
<p> References ecore_strbuf_append_char(). </p>
<p> Referenced by ecore_strbuf_append_char().</p>
<h3>EAPI void ecore_strbuf_free (Ecore_Strbuf * buf)</h3>
<p>Free a string buffer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the buffer to free</dl>
<p> References ecore_strbuf_free(). </p>
<p> Referenced by ecore_strbuf_free().</p>
<h3>EAPI void ecore_strbuf_insert (Ecore_Strbuf * buf, const char * str, size_t pos)</h3>
<p>Insert a string to a buffer, reallocating as necessary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the Ecore_Strbuf to insert<br />
 <i>str</i> the string to insert<br />
 <i>pos</i> the position to insert the string</dl>
<p> References ecore_strbuf_append(), and ecore_strbuf_insert(). </p>
<p> Referenced by ecore_strbuf_insert().</p>
<h3>EAPI size_t ecore_strbuf_length_get (Ecore_Strbuf * buf)</h3>
<p>Retrieve the length of the string buffer content. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the buffer</dl>
<p> References ecore_strbuf_length_get(). </p>
<p> Referenced by ecore_strbuf_length_get().</p>
<h3>EAPI int ecore_strbuf_replace (Ecore_Strbuf * buf, const char * str, const char * with, unsigned int n)</h3>
<p>Replace the n-th string with an other string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the Ecore_Strbuf to work with<br />
 <i>str</i> the string to replace<br />
 <i>with</i> the replaceing string<br />
 <i>n</i> the number of the fitting string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true on success</dl>
<p> References ecore_strbuf_replace(). </p>
<p> Referenced by ecore_strbuf_replace().</p>
<h3>EAPI int ecore_strbuf_replace_all (Ecore_Strbuf * buf, const char * str, const char * with)</h3>
<p>Replace all strings with an other string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the Ecore_Strbuf to work with<br />
 <i>str</i> the string to replace<br />
 <i>with</i> the replaceing string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>how often the string was replaced</dl>
<p> References ecore_strbuf_replace_all(). </p>
<p> Referenced by ecore_strbuf_replace_all().</p>
<h3>EAPI const char* ecore_strbuf_string_get (Ecore_Strbuf * buf)</h3>
<p>Retrieve a pointer to the contents of a string buffer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>buf</i> the buffer</dl>
<p> This pointer must not be modified, and will no longer be valid if the Ecore_Strbuf is modified. </p>
<p> References ecore_strbuf_string_get(). </p>
<p> Referenced by ecore_strbuf_string_get().</p>
<h3>EAPI int ecore_string_init (void)</h3>
<p>Initialize the ecore string internal structure. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Zero on failure, non-zero on successful initialization.</dl>
<p> References ecore_hash_free_value_cb_set(), ecore_hash_new(), ecore_str_compare(), ecore_str_hash(), and ecore_string_init(). </p>
<p> Referenced by ecore_string_init().</p>
<h3>EAPI void* ecore_tree_closest_larger_get (Ecore_Tree * tree, const void * key)</h3>
<p>Find the closest value greater than or equal to the key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> The tree to search.<br />
 <i>key</i> The key to search for in <i>tree</i>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL if no valid nodes, otherwise the node greater than or equal to the key</dl>
<p> References ecore_tree_closest_larger_get(). </p>
<p> Referenced by ecore_tree_closest_larger_get().</p>
<h3>EAPI void* ecore_tree_closest_smaller_get (Ecore_Tree * tree, const void * key)</h3>
<p>Find the closest value &lt;= key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> the tree to search<br />
 <i>key</i> the key to search for in tree</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns NULL if no valid nodes, otherwise the node &lt;= key</dl>
<p> References ecore_tree_closest_smaller_get(). </p>
<p> Referenced by ecore_tree_closest_smaller_get().</p>
<h3>EAPI int ecore_tree_destroy (Ecore_Tree * tree)</h3>
<p>Free the tree and it&#8217;s stored data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to destroy</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE if tree destroyed successfully, FALSE if not.</dl>
<p> References ecore_tree_destroy(), and ecore_tree_node_remove(). </p>
<p> Referenced by ecore_tree_destroy().</p>
<h3>EAPI int ecore_tree_empty_is (Ecore_Tree * tree)</h3>
<p>Test to see if the tree has any nodes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to check for nodes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE if no nodes exist, FALSE otherwise</dl>
<p> References ecore_tree_empty_is(). </p>
<p> Referenced by ecore_tree_empty_is().</p>
<h3>EAPI int ecore_tree_for_each_node (Ecore_Tree * tree, Ecore_For_Each for_each_func, void * user_data)</h3>
<p>Execute the function for each node in the tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to traverse<br />
 <i>for_each_func,:</i> the function to execute for each node<br />
 <i>user_data,:</i> data passed to each for_each_func call</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on success, FALSE on failure.</dl>
<p> References ecore_tree_for_each_node(). </p>
<p> Referenced by ecore_tree_for_each_node().</p>
<h3>EAPI int ecore_tree_for_each_node_value (Ecore_Tree * tree, Ecore_For_Each for_each_func, void * user_data)</h3>
<p>Execute function for each value in the tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to traverse<br />
 <i>for_each_func,:</i> the function to execute for each value in the tree<br />
 <i>user_data,:</i> data passed to each for_each_func call</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on success, FALSE on failure.</dl>
<p> References ecore_tree_for_each_node_value(). </p>
<p> Referenced by ecore_tree_for_each_node_value().</p>
<h3>EAPI void* ecore_tree_get (Ecore_Tree * tree, const void * key)</h3>
<p>Return the value corresponding to key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to search<br />
 <i>key,:</i> the key to search for in <i>tree</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the value corresponding to the key if found, otherwise NULL.</dl>
<p> References ecore_tree_get(). </p>
<p> Referenced by ecore_tree_get().</p>
<h3>EAPI Ecore_Tree_Node* ecore_tree_get_node (Ecore_Tree * tree, const void * key)</h3>
<p>Return the node corresponding to key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree,:</i> the tree to search<br />
 <i>key,:</i> the key to search for in the tree</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns the node corresponding to the key if found, otherwise NULL.</dl>
<p> References ecore_tree_get_node(). </p>
<p> Referenced by ecore_tree_get_node().</p>
<h3>EAPI int ecore_tree_init (Ecore_Tree * new_tree, Ecore_Compare_Cb compare_func)</h3>
<p>Initialize a tree structure to some sane initial values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>new_tree,:</i> the new tree structure to be initialized<br />
 <i>compare_func,:</i> the function used to compare node keys</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns TRUE on successful initialization, FALSE on an error</dl>
<p> References ecore_direct_compare(), and ecore_tree_init(). </p>
<p> Referenced by ecore_tree_init(), and ecore_tree_new().</p>
<h3>EAPI Ecore_Tree* ecore_tree_new (Ecore_Compare_Cb compare_func)</h3>
<p>Allocate a new tree structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>compare_func,:</i> function used to compare the two values</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns NULL if the operation fails, otherwise the new tree</dl>
<p> References ecore_tree_init(), and ecore_tree_new(). </p>
<p> Referenced by ecore_tree_new().</p>
<h3>EAPI int ecore_tree_node_add (Ecore_Tree * tree, Ecore_Tree_Node * node)</h3>
<p>Place a node in the tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> The tree to add <i>node</i>.<br />
 <i>node</i> The node to add to <i>tree</i>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on a successful add, FALSE otherwise.</dl>
<p> References ecore_tree_node_add(). </p>
<p> Referenced by ecore_tree_node_add(), and ecore_tree_set().</p>
<h3>EAPI int ecore_tree_node_remove (Ecore_Tree * tree, Ecore_Tree_Node * node)</h3>
<p>Remove the node from the tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> The tree to remove <i>node</i> from.<br />
 <i>node</i> The node to remove from <i>tree</i>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on a successful remove, FALSE otherwise.</dl>
<p> References ecore_tree_node_remove(). </p>
<p> Referenced by ecore_tree_destroy(), ecore_tree_node_remove(), and ecore_tree_remove().</p>
<h3>EAPI int ecore_tree_remove (Ecore_Tree * tree, const void * key)</h3>
<p>Remove the key from the tree. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> The tree to remove <i>key</i>.<br />
 <i>key</i> The key to remove from <i>tree</i>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE on a successful remove, FALSE otherwise.</dl>
<p> References ecore_tree_node_remove(), and ecore_tree_remove(). </p>
<p> Referenced by ecore_tree_remove().</p>
<h3>EAPI int ecore_tree_set (Ecore_Tree * tree, void * key, void * value)</h3>
<p>Set the value associated with key to <i>value</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tree</i> The tree that contains the key/value pair.<br />
 <i>key</i> The key to identify which node to set a value.<br />
 <i>value</i> Value to set the found node.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TRUE if successful, FALSE if not.</dl>
<p> References ecore_tree_node_add(), and ecore_tree_set(). </p>
<p> Referenced by ecore_tree_set().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
