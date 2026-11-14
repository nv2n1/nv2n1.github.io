---
title: "evas_object_data_group(3)"
name: "evas_object_data_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_data_group/"
description: "Object Data Functions – Functions that retrieve and set data associated attached to an evas object."
---

<p>Object Data Functions &#8211; Functions that retrieve and set data associated attached to an evas object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_data_set</code> (<code>Evas_Object</code> *obj, const char *key, const void *data)<br />
 <i>Set an attached data pointer to an object with a given string key. </i><br />
 EAPI void * <code>evas_object_data_get</code> (const <code>Evas_Object</code> *obj, const char *key)<br />
 <i>Return an attached data pointer by its given string key. </i><br />
 EAPI void * <code>evas_object_data_del</code> (<code>Evas_Object</code> *obj, const char *key)<br />
 <i>Delete at attached data pointer from an object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve and set data associated attached to an evas object.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* evas_object_data_del (<code>Evas_Object</code> * obj, const char * key)</h3>
<p>Delete at attached data pointer from an object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to delete the data pointer from<br />
 <i>key</i> The string key the data was stored under</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The original data pointer stored at key on obj</dl>
<p> This will remove thee stored data pointer from obj stored under key, and return the original pointer stored under key, if any, nor NULL if nothing was stored under that key. </p>
<p> Example: </p>
<pre> int *my_data;
 extern Evas_Object *obj;
 my_data = evas_object_data_del(obj, 'name_of_my_data');</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, evas_list_remove_list(), and _Evas_List::next. </p>
<p> Referenced by evas_object_data_set().</p>
<h3>EAPI void* evas_object_data_get (const <code>Evas_Object</code> * obj, const char * key)</h3>
<p>Return an attached data pointer by its given string key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to which the data was attached<br />
 <i>key</i> The string key the data was stored under</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer stored, or NULL if none was stored</dl>
<p> This function will return the data pointer attached to the object obj stored using the string key key. If the object is valid and data was stored under the given key, the pointer that was stored will be reuturned. If this is not the case, NULL will be returned, signifying an invalid object or non-existent key. It is possible a NULL pointer was stored given that key, but this situation is non-sensical and thus can be considered an error as well. NULL pointers are never stored as this is the return value if an error occurs. </p>
<p> Example: </p>
<pre> int *my_data;
 extern Evas_Object *obj;
 my_data = evas_object_data_get(obj, 'name_of_my_data');
 if (my_data) printf('Data stored was %p, my_data);
 else printf('No data was stored on the object);</pre>
<p>&nbsp;<wbr> </p>
<p> References _Evas_List::data, and _Evas_List::next.</p>
<h3>EAPI void evas_object_data_set (<code>Evas_Object</code> * obj, const char * key, const void * data)</h3>
<p>Set an attached data pointer to an object with a given string key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The object to attach the data pointer to<br />
 <i>key</i> The string key for the data to access it<br />
 <i>data</i> The ponter to the data to be attached</dl>
<p> This attaches the pointer data to the object obj given the string key. This pointer will stay &#8216;hooked&#8217; to the object until a new pointer with the same string key is attached with <code>evas_object_data_set()</code> or it is deleted with <code>evas_object_data_del()</code>. On deletion of the object obj, the pointers will not be accessible from the object anymore. </p>
<p> You can find the pointer attached under a string key using <code>evas_object_data_get()</code>. It is the job of the calling application to free any data pointed to by data when it is no longer required. </p>
<p> If data is NULL, the old value stored at key will be removed but no new value will be stored. This is synonymous with calling <code>evas_object_data_del()</code> with obj and key. </p>
<p> Example: </p>
<pre> int *my_data;
 extern Evas_Object *obj;
 my_data = malloc(500);
 evas_object_data_set(obj, 'name_of_data', my_data);
 printf('The data that was attached was %p, evas_object_data_get(obj, 'name_of_data'));</pre>
<p>&nbsp;<wbr> </p>
<p> References evas_list_prepend(), and evas_object_data_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
