---
title: "globus_thread_key(3)"
name: "globus_thread_key"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_thread_key/"
description: "Thread-Specific Storage –"
---

<h2 class="name">NAME</h2>
<p> Thread-Specific Storage &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_thread_key_create</code> (<code>globus_thread_key_t</code> *key, <code>globus_thread_key_destructor_func_t</code> destructor)<br />
 <i>Create a key for thread-specific storage. </i><br />
 int <code>globus_thread_key_delete</code> (<code>globus_thread_key_t</code> key)<br />
 <i>Delete a thread-local storage key. </i><br />
 void * <code>globus_thread_getspecific</code> (<code>globus_thread_key_t</code> key)<br />
 <i>Get a thread-specific data value. </i><br />
 int <code>globus_thread_setspecific</code> (<code>globus_thread_key_t</code> key, void *value)<br />
 <i>Set a thread-specific data value. </i></p>
<h2>Detailed Description</h2>
<p> The <code>globus_thread_key_t</code> data type acts as a key to thread-specific storage. For each key created by <code>globus_thread_key_create()</code>, each thread may store and retrieve its own value.</p>
<h2>Function Documentation</h2>
<h3>void* globus_thread_getspecific (<code>globus_thread_key_t</code>key)</h3>
<p> Get a thread-specific data value. The <code>globus_thread_getspecific()</code> function returns the value associated with the thread-specific data key passed as its first parameter. This function returns NULL if the value has not been set by the current thread. The return value is undefined if the key is not valid. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Thread-specific data key to look up.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The value passed to a previous call to <code>globus_thread_setspecific()</code> in the current thread for this key.</dl>
<h3>int globus_thread_key_create (<code>globus_thread_key_t</code> *key, <code>globus_thread_key_destructor_func_t</code>destructor)</h3>
<p> Create a key for thread-specific storage. The <code>globus_thread_key_create()</code> function creates a new key for thread-specific data. The new key will be available for all threads to store a distinct value. If the function pointer <i>destructor</i> is non-NULL, then that function will be invoked when a thread exits that has a non-NULL value associated with the key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Pointer to be set to the new key.<br />
 <i>destructor</i> Pointer to a function to call when a thread exits to free the key&#8217;s value.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, globus_thread_create_key() will create a new key to thread-local storage and return GLOBUS_SUCCESS. If an error occurs, then the value of <i>key</i> is undefined and globus_thread_create_key() returns an implementation-specific non-zero error value.</dl>
<h3>int globus_thread_key_delete (<code>globus_thread_key_t</code>key)</h3>
<p> Delete a thread-local storage key. The <code>globus_thread_key_delete()</code> function deletes the key used for a thread-local storage association. The destructor function for this key will no longer be called after this function returns. The behavior of subsequent calls to <code>globus_thread_getspecific()</code> or <code>globus_thread_setspecific()</code> with this key will be undefined. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Key to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_key_delete()</code> will delete a thread-local storage key and return GLOBUS_SUCCESS. If an error occurs, then the value of <i>key</i> is undefined and globus_thread_create_key() returns an implementation-specific non-zero error value.</dl>
<h3>int globus_thread_setspecific (<code>globus_thread_key_t</code>key, void *value)</h3>
<p> Set a thread-specific data value. The <code>globus_thread_setspecific()</code> function associates a thread-specific value with a data key. If the key had a previous value set in the current thread, it is replaced, but the destructor function is not called for the old value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>key</i> Thread-specific data key to store.<br />
 <i>value</i> A pointer to data to store as the thread-specific data for this thread.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_setspecific()</code> stores value in the thread-specific data for the specified key and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_setspecific()</code> returns an implementation-specific non-zero error code and does not modify the key&#8217;s value for this thread.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
