---
title: "memcached_callback_get(3)"
name: "memcached_callback_get"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_callback_get/"
description: "memcached_callback_get – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_callback_get &#8211; libmemcached Documentation </p>
<p> Get and set a callback</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_callback_t</code></p>
<dd>
<dt><code>memcached_return_t memcached_callback_set(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_callback_t</i><i>&nbsp;<wbr>flag</i>, const void<i>&nbsp;<wbr>*data</i>)</p>
<dd>
<dt><code>void * memcached_callback_get(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_callback_t</i><i>&nbsp;<wbr>flag</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) can have callbacks set key execution points. These either provide function calls at points in the code, or return pointers to structures for particular usages. </p>
<p> <i>memcached_callback_get()</i> takes a callback flag and returns the structure or function set by <i>memcached_callback_set()</i>. </p>
<p> <i>memcached_callback_set()</i> changes the function/structure assigned by a callback flag. No connections are reset. </p>
<p> You can use <i>MEMCACHED_CALLBACK_USER_DATA</i> to provide custom context if required for any of the callbacks.</p>
<dl>
<dt><code>MEMCACHED_CALLBACK_CLEANUP_FUNCTION</code></p>
<dd>
<p> When <code>memcached_delete()</code> is called this function will be excuted. At the point of its execution all connections are closed.</p>
<dt><code>MEMCACHED_CALLBACK_CLONE_FUNCTION</code></p>
<dd>
<p> When <code>memcached_delete()</code> is called this function will be excuted. At the point of its execution all connections are closed.</p>
<dt><code>MEMCACHED_CALLBACK_PREFIX_KEY</code></p>
<dd> See <i>MEMCACHED_CALLBACK_NAMESPACE</i></p>
<dt><code>MEMCACHED_CALLBACK_NAMESPACE</code></p>
<dd>
<p> You can set a value which will be used to create a domain for your keys. The value specified here will be prefixed to each of your keys. The value can not be greater then <code>MEMCACHED_PREFIX_KEY_MAX_SIZE</code> &#8211; 1 and will reduce <code>MEMCACHED_MAX_KEY</code> by the value of your key. </p>
<p> The prefix key is only applied to the primary key, not the master key. <code>MEMCACHED_FAILURE</code> will be returned if no key is set. In the case of a key which is too long, <code>MEMCACHED_BAD_KEY_PROVIDED</code> will be returned. </p>
<p> If you set a value with the value being NULL then the prefix key is disabled.</p>
<dt><code>MEMCACHED_CALLBACK_USER_DATA</code></p>
<dd>
<p> This allows you to store a pointer to a specifc piece of data. This can be retrieved from inside of <code>memcached_fetch_execute()</code>. Cloning a <code>memcached_st</code> will copy the pointer to the clone.</p>
<dt><code>MEMCACHED_CALLBACK_MALLOC_FUNCTION</code></p>
<dd>
<p> Deprecated since version &lt;0.32: Use <code>memcached_set_memory_allocators</code> instead.</p>
<dt><code>MEMCACHED_CALLBACK_REALLOC_FUNCTION</code></p>
<dd>
<p> Deprecated since version &lt;0.32: Use <code>memcached_set_memory_allocators</code> instead.</p>
<dt><code>MEMCACHED_CALLBACK_FREE_FUNCTION</code></p>
<dd>
<p> Deprecated since version &lt;0.32: Use <code>memcached_set_memory_allocators</code> instead.</p>
<dt><code>MEMCACHED_CALLBACK_GET_FAILURE</code></p>
<dd>
<p> This function implements the read through cache behavior. On failure of retrieval this callback will be called. </p>
<p> You are responsible for populating the result object provided. This result object will then be stored in the server and returned to the calling process. </p>
<p> You must clone the <code>memcached_st</code> in order to make use of it. The value will be stored only if you return <code>MEMCACHED_SUCCESS</code> or <code>MEMCACHED_BUFFERED</code>. Returning <code>MEMCACHED_BUFFERED</code> will cause the object to be buffered and not sent immediatly (if this is the default behavior based on your connection setup this will happen automatically). </p>
<p> The prototype for this is:</p>
<dt><code>memcached_return_t (*memcached_trigger_key)(memcached_st *ptr, char *key, size_t key_length, memcached_result_st *result);</code></p>
<dd>
<dt><code>MEMCACHED_CALLBACK_DELETE_TRIGGER</code></p>
<dd>
<p> This function implements a trigger upon successful deletion of a key. The memcached_st structure will need to be cloned in order to make use of it. </p>
<p> The prototype for this is:</p>
<dt><code>typedef memcached_return_t (*memcached_trigger_delete_key)(memcached_st *ptr, char *key, size_t key_length);</code></p>
<dd></dl>
<h2>RETURN</h2>
<p> <i>memcached_callback_get()</i> return the function or structure that was provided. Upon error, nothing is set, null is returned, and the <code>memcached_return_t</code> argument is set to <code>MEMCACHED_FAILURE</code>. </p>
<p> <i>memcached_callback_set()</i> returns <code>MEMCACHED_SUCCESS</code> upon successful setting, otherwise <code>MEMCACHED_FAILURE</code> on error.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Brian Aker, &lt;<i>brian [at] tangent.org</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
