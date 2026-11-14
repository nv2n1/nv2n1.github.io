---
title: "qbmap-h(3)"
name: "qbmap-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbmap-h/"
description: "qbmap.h –"
---

<p>qbmap.h &#8211; </p>
<p> This provides a map interface to a Patricia trie, hashtable or skiplist.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;

#include &lt;unistd.h&gt;</code></pre>
<h3>Macros</h3>
<pre><code>#define QB_MAP_NOTIFY_DELETED   1



#define QB_MAP_NOTIFY_REPLACED   2



#define QB_MAP_NOTIFY_INSERTED   4



#define QB_MAP_NOTIFY_RECURSIVE   8



#define QB_MAP_NOTIFY_FREE   16



Typedefs</code></pre>
<p> typedef struct qb_map <code>qb_map_t</code><br />
 <i>This is an opaque data type representing an instance of a map. </i><br />
 typedef struct qb_map_iter <code>qb_map_iter_t</code><br />
 <i>This is an opaque data type representing an iterator instance. </i><br />
 typedef void(* <code>qb_map_notify_fn</code> )(uint32_t event, char *key, void *old_value, void *value, void *user_data) </p>
<p> typedef int32_t(* <code>qb_map_transverse_fn</code> )(const char *key, void *value, void *user_data)</p>
<h3>Functions</h3>
<p><code>qb_map_t</code> * <code>qb_hashtable_create</code> (size_t max_size)<br />
 <i>Create an unsorted map based on a hashtable. </i><br />
 <code>qb_map_t</code> * <code>qb_skiplist_create</code> (void)<br />
 <i>Create a sorted map using a skiplist. </i><br />
 <code>qb_map_t</code> * <code>qb_trie_create</code> (void)<br />
 <i>Create a sorted map using a Patricia trie or &#8216;Radix tree&#8217;. </i><br />
 void <code>qb_trie_dump</code> (<code>qb_map_t</code> *m)<br />
 <i>print out the nodes in the trie </i><br />
 int32_t <code>qb_map_notify_add</code> (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code> fn, int32_t events, void *user_data)<br />
 <i>Add a notifier to the map. </i><br />
 int32_t <code>qb_map_notify_del</code> (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code> fn, int32_t events)<br />
 <i>Delete a notifier from the map. </i><br />
 int32_t <code>qb_map_notify_del_2</code> (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code> fn, int32_t events, void *user_data)<br />
 <i>Delete a notifier from the map (including the userdata). </i><br />
 void <code>qb_map_put</code> (<code>qb_map_t</code> *map, const char *key, const void *value)<br />
 <i>Inserts a new key and value into a qb_map_t. </i><br />
 void * <code>qb_map_get</code> (<code>qb_map_t</code> *map, const char *key)<br />
 <i>Gets the value corresponding to the given key. </i><br />
 int32_t <code>qb_map_rm</code> (<code>qb_map_t</code> *map, const char *key)<br />
 <i>Removes a key/value pair from a map. </i><br />
 size_t <code>qb_map_count_get</code> (<code>qb_map_t</code> *map)<br />
 <i>Get the number of items in the map. </i><br />
 void <code>qb_map_foreach</code> (<code>qb_map_t</code> *map, <code>qb_map_transverse_fn</code> func, void *user_data)<br />
 <i>Calls the given function for each of the key/value pairs in the map. </i><br />
 <code>qb_map_iter_t</code> * <code>qb_map_iter_create</code> (<code>qb_map_t</code> *map)<br />
 <i>Create an iterator. </i><br />
 <code>qb_map_iter_t</code> * <code>qb_map_pref_iter_create</code> (<code>qb_map_t</code> *map, const char *prefix)<br />
 <i>Create a prefix iterator. </i><br />
 const char * <code>qb_map_iter_next</code> (<code>qb_map_iter_t</code> *i, void **value)<br />
 <i>Get the next item. </i><br />
 void <code>qb_map_iter_free</code> (<code>qb_map_iter_t</code> *i)<br />
 <i>free the iterator </i><br />
 void <code>qb_map_destroy</code> (<code>qb_map_t</code> *map)<br />
 <i>Destroy the map, removes all the items from the map. </i></p>
<h2>Detailed Description</h2>
<p>This provides a map interface to a Patricia trie, hashtable or skiplist. </p>
<p> <code>Ordering</code></p>
<dl>
<dd>The hashtable is NOT ordered, but ptrie and skiplist are.</dl>
<p> <code>Iterating</code></p>
<dl>
<dd>Below is a simple example of how to iterate over a map. </p>
<pre>* const char *p;
* void *data;
* qb_map_iter_t *it = qb_map_iter_create(m);
* for (p = qb_map_iter_next(it, &amp;data); p; p = qb_map_iter_next(it, &amp;data)) {
* printf(&quot;%s &gt; %s, p, (char*) data);
* }
* qb_map_iter_free(it);
* </pre>
</dl>
<p> Deletion of items within the iterator is supported. But note do not free the item memory in the iterator. If you need to free the data items then register for a notifier and free the memory there. This is required as the items are reference counted. </p>
<pre>* qb_map_notify_add(m, NULL, my_map_free_handler,
* QB_MAP_NOTIFY_FREE, NULL);
* </pre>
<p><code>Notifications</code></p>
<dl>
<dd>These allow you to get callbacks when values are inserted/removed or replaced.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>hashtable only supports deletion and replacement notificatins. There is also a special global callback for freeing deleted and replaced values (QB_MAP_NOTIFY_FREE).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_map_notify_add()</code> <code>qb_map_notify_del_2()</code></dl>
<p> <code>Prefix matching</code></p>
<dl>
<dd>The ptrie supports prefixes in the iterator:</dl>
<pre>* it = qb_map_pref_iter_create(m, &quot;aa&quot;);
* while ((p = qb_map_iter_next(it, &amp;data)) != NULL) {
* printf(&quot;%s &gt; %s, p, (char*)data);
* }
* qb_map_iter_free(it);
* </pre>
<p>The ptrie also supports prefixes in notifications: (remember to pass QB_MAP_NOTIFY_RECURSIVE into the notify_add. </p>
<pre>* qb_map_notify_add(m, &quot;root&quot;, my_map_notification,
* (QB_MAP_NOTIFY_INSERTED|
* QB_MAP_NOTIFY_DELETED|
* QB_MAP_NOTIFY_REPLACED|
* QB_MAP_NOTIFY_RECURSIVE),
* NULL);
*
* </pre>
<p>&nbsp;<wbr></p>
<h2>Macro Definition Documentation</h2>
<h3>#define QB_MAP_NOTIFY_DELETED 1</h3>
<h3>#define QB_MAP_NOTIFY_FREE 16</h3>
<h3>#define QB_MAP_NOTIFY_INSERTED 4</h3>
<h3>#define QB_MAP_NOTIFY_RECURSIVE 8</h3>
<h3>#define QB_MAP_NOTIFY_REPLACED 2</h3>
<h2>Typedef Documentation</h2>
<h3>typedef struct qb_map_iter <code>qb_map_iter_t</code></h3>
<p>This is an opaque data type representing an iterator instance.</p>
<h3>typedef void(* qb_map_notify_fn)(uint32_t event, char *key, void *old_value, void *value, void *user_data)</h3>
<h3>typedef struct qb_map <code>qb_map_t</code></h3>
<p>This is an opaque data type representing an instance of a map.</p>
<h3>typedef int32_t(* qb_map_transverse_fn)(const char *key, void *value, void *user_data)</h3>
<h2>Function Documentation</h2>
<h3><code>qb_map_t</code>* qb_hashtable_create (size_tmax_size)</h3>
<p>Create an unsorted map based on a hashtable. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>max_size</i> maximum size of the hashtable</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the map instance</dl>
<h3>size_t qb_map_count_get (<code>qb_map_t</code> *map)</h3>
<p>Get the number of items in the map.</p>
<h3>void qb_map_destroy (<code>qb_map_t</code> *map)</h3>
<p>Destroy the map, removes all the items from the map.</p>
<h3>void qb_map_foreach (<code>qb_map_t</code> *map, <code>qb_map_transverse_fn</code>func, void *user_data)</h3>
<p>Calls the given function for each of the key/value pairs in the map. The function is passed the key and value of each pair, and the given data parameter. The map is traversed in sorted order.</p>
<h3>void* qb_map_get (<code>qb_map_t</code> *map, const char *key)</h3>
<p>Gets the value corresponding to the given key. </p>
<p> <code>Return values:</code></p>
<dl>
<dd><i>NULL</i> (if the key does not exist)<br />
 <i>a</i> pointer to the value</dl>
<h3><code>qb_map_iter_t</code>* qb_map_iter_create (<code>qb_map_t</code> *map)</h3>
<p>Create an iterator.</p>
<h3>void qb_map_iter_free (<code>qb_map_iter_t</code> *i)</h3>
<p>free the iterator </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>i</i> the iterator</dl>
<h3>const char* qb_map_iter_next (<code>qb_map_iter_t</code> *i, void **value)</h3>
<p>Get the next item. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>i</i> the iterator<br />
 <i>value</i> (out) the next item&#8217;s value</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>the</i> next key<br />
 <i>NULL</i> &#8211; the end of the iteration</dl>
<h3>int32_t qb_map_notify_add (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code>fn, int32_tevents, void *user_data)</h3>
<p>Add a notifier to the map. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>m</i> the map instance<br />
 <i>key</i> the key (or prefix) to attach the notification to.<br />
 <i>fn</i> the callback<br />
 <i>events</i> the type of events to register for.<br />
 <i>user_data</i> a pointer to be passed into the callback</dl>
<p> <code>Note:</code></p>
<dl>
<dd>QB_MAP_NOTIFY_INSERTED is only valid on tries. </p>
<p> you can use key prefixes with trie maps.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>0</i> success<br />
 <i>-errno</i> failure</dl>
<h3>int32_t qb_map_notify_del (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code>fn, int32_tevents)</h3>
<p>Delete a notifier from the map. </p>
<p> <code>Note:</code></p>
<dl>
<dd>the key,fn and events must match those you added.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>m</i> the map instance<br />
 <i>key</i> the key (or prefix) to attach the notification to.<br />
 <i>fn</i> the callback<br />
 <i>events</i> the type of events to register for.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>0</i> success<br />
 <i>-errno</i> failure</dl>
<h3>int32_t qb_map_notify_del_2 (<code>qb_map_t</code> *m, const char *key, <code>qb_map_notify_fn</code>fn, int32_tevents, void *user_data)</h3>
<p>Delete a notifier from the map (including the userdata). </p>
<p> <code>Note:</code></p>
<dl>
<dd>the key, fn, events and userdata must match those you added.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>m</i> the map instance<br />
 <i>key</i> the key (or prefix) to attach the notification to.<br />
 <i>fn</i> the callback<br />
 <i>events</i> the type of events to register for.<br />
 <i>user_data</i> a pointer to be passed into the callback</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>0</i> success<br />
 <i>-errno</i> failure</dl>
<h3><code>qb_map_iter_t</code>* qb_map_pref_iter_create (<code>qb_map_t</code> *map, const char *prefix)</h3>
<p>Create a prefix iterator. This will iterate over all items with the given prefix. </p>
<p> <code>Note:</code></p>
<dl>
<dd>this is only supported by the trie.</dl>
<h3>void qb_map_put (<code>qb_map_t</code> *map, const char *key, const void *value)</h3>
<p>Inserts a new key and value into a qb_map_t. If the key already exists in the qb_map_t, it gets replaced by the new key.</p>
<h3>int32_t qb_map_rm (<code>qb_map_t</code> *map, const char *key)</h3>
<p>Removes a key/value pair from a map.</p>
<h3><code>qb_map_t</code>* qb_skiplist_create (void)</h3>
<p>Create a sorted map using a skiplist. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>the map instance</dl>
<h3><code>qb_map_t</code>* qb_trie_create (void)</h3>
<p>Create a sorted map using a Patricia trie or &#8216;Radix tree&#8217;.</p>
<h3>void qb_trie_dump (<code>qb_map_t</code> *m)</h3>
<p>print out the nodes in the trie (for debug purposes)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
