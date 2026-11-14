---
title: "memcached_fetch_result(3)"
name: "memcached_fetch_result"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_fetch_result/"
description: "memcached_fetch_result – Retrieving data from the server"
---

<h2>NAME</h2>
<p> memcached_fetch_result &#8211; Retrieving data from the server</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_result_st * memcached_fetch_result(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, memcached_result_st<i>&nbsp;<wbr>*result</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>char * memcached_get(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, size_t<i>&nbsp;<wbr>*value_length</i>, uint32_t<i>&nbsp;<wbr>*flags</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_mget(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char * const<i>&nbsp;<wbr>*keys</i>, const size_t<i>&nbsp;<wbr>*key_length</i>, size_t<i>&nbsp;<wbr>number_of_keys</i>)</p>
<dd>
<dt><code>char * memcached_get_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, size_t<i>&nbsp;<wbr>*value_length</i>, uint32_t<i>&nbsp;<wbr>*flags</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_mget_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char * const<i>&nbsp;<wbr>*keys</i>, const size_t<i>&nbsp;<wbr>*key_length</i>, size_t<i>&nbsp;<wbr>number_of_keys</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_fetch_execute(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_execute_fn</i><i>&nbsp;<wbr>*callback</i>, void<i>&nbsp;<wbr>*context</i>, uint32_t<i>&nbsp;<wbr>number_of_callbacks</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_mget_execute(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char * const<i>&nbsp;<wbr>*keys</i>, const size_t<i>&nbsp;<wbr>*key_length</i>, size_t<i>&nbsp;<wbr>number_of_keys</i>, <i>memcached_execute_fn</i><i>&nbsp;<wbr>*callback</i>, void<i>&nbsp;<wbr>*context</i>, uint32_t<i>&nbsp;<wbr>number_of_callbacks</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_mget_execute_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char * const<i>&nbsp;<wbr>*keys</i>, const size_t<i>&nbsp;<wbr>*key_length</i>, size_t<i>&nbsp;<wbr>number_of_keys</i>, <i>memcached_execute_fn</i><i>&nbsp;<wbr>*callback</i>, void<i>&nbsp;<wbr>*context</i>, uint32_t<i>&nbsp;<wbr>number_of_callbacks</i>)</p>
<dd>
<dt><code>memcached_return_t (*memcached_execute_fn)(const memcached_st</code><i>&nbsp;<wbr>*ptr</i>, memcached_result_st<i>&nbsp;<wbr>*result</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_get()</i> is used to fetch an individual value from the server. You must pass in a key and its length to fetch the object. You must supply three pointer variables which will give you the state of the returned object. A <code>uint32_t</code> pointer to contain whatever flags you stored with the value, a <code>size_t</code> pointer which will be filled with size of of the object, and a <code>memcached_return_t</code> pointer to hold any error. The object will be returned upon success and NULL will be returned on failure. Any object returned by <i>memcached_get()</i> must be released by the caller application. </p>
<p> <i>memcached_mget()</i> is used to select multiple keys at once. For multiple key operations it is always faster to use this function. This function always works asynchronously. </p>
<p> To retrieve data after a successful execution of <i>memcached_mget()</i>, you will need to call <i>memcached_fetch_result()</i>. You should continue to call this function until it returns a NULL (i.e. no more values). If you need to quit in the middle of a <i>memcached_mget()</i> call, you can execute a <code>memcached_quit()</code>, those this is not required. </p>
<p> <i>memcached_fetch_result()</i> is used to fetch an individual value from the server. <i>memcached_mget()</i> must always be called before using this method. You must pass in a key and its length to fetch the object. You must supply three pointer variables which will give you the state of the returned object. A <code>uint32_t</code> pointer to contain whatever flags you stored with the value, a <code>size_t</code> pointer which will be filled with size of of the object, and a <code>memcached_return_t</code> pointer to hold any error. The object will be returned upon success and NULL will be returned on failure. <code>MEMCACHED_END</code> is returned by the *error value when all objects that have been found are returned. The final value upon <code>MEMCACHED_END</code> is null. </p>
<p> <i>memcached_fetch_result()</i> is used to return a <code>memcached_result_st</code> structure from a memcached server. The result object is forward compatible with changes to the server. For more information please refer to the <code>memcached_result_st</code> help. This function will dynamically allocate a result structure for you if you do not pass one to the function. </p>
<p> <i>memcached_fetch_execute()</i> is a callback function for result sets. Instead of returning the results to you for processing, it passes each of the result sets to the list of functions you provide. It passes to the function a <code>memcached_st</code> that can be cloned for use in the called function (it can not be used directly). It also passes a result set which does not need to be freed. Finally it passes a &quot;context&quot;. This is just a pointer to a memory reference you supply the calling function. Currently only one value is being passed to each function call. In the future there will be an option to allow this to be an array. </p>
<p> <i>memcached_mget_execute()</i> and <i>memcached_mget_execute_by_key()</i> is similar to <i>memcached_mget()</i>, but it may trigger the supplied callbacks with result sets while sending out the queries. If you try to perform a really large multiget with <i>memcached_mget()</i> you may encounter a deadlock in the OS kernel (it will fail to write data to the socket because the input buffer is full). <i>memcached_mget_execute()</i> solves this problem by processing some of the results before continuing sending out requests. Please note that this function is only available in the binary protocol. </p>
<p> <i>memcached_get_by_key()</i> and <i>memcached_mget_by_key()</i> behave in a similar nature as <i>memcached_get()</i> and <i>memcached_mget()</i>. The difference is that they take a master key that is used for determining which server an object was stored if key partitioning was used for storage. </p>
<p> All of the above functions are not tested when the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> has been set. Executing any of these functions with this behavior on will result in <code>MEMCACHED_NOT_SUPPORTED</code> being returned, or for those functions which do not return a <code>memcached_return_t</code>, the error function parameter will be set to <code>MEMCACHED_NOT_SUPPORTED</code>.</p>
<h2>RETURN</h2>
<p> All objects retrieved via <i>memcached_get()</i> or <i>memcached_get_by_key()</i> must be freed with <i><a href="/docs/linux/man/3-free/">free</a>(3)</i>. </p>
<p> <i>memcached_get()</i> will return NULL on error. You must look at the value of error to determine what the actual error was. </p>
<p> <i>memcached_fetch_execute()</i> return <code>MEMCACHED_SUCCESS</code> if all keys were successful. <code>MEMCACHED_NOTFOUND</code> will be return if no keys at all were found. </p>
<p> <i>memcached_fetch_result()</i> sets error to <code>MEMCACHED_END</code> upon successful conclusion. <code>MEMCACHED_NOTFOUND</code> will be return if no keys at all were found.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
