---
title: "memcached_pool_destroy(3)"
name: "memcached_pool_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_pool_destroy/"
description: "memcached_pool_destroy – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_pool_destroy &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached_pool.h&gt;</p>
<dl>
<dt><code>memcached_pool_st</code></p>
<dd>
<dt><i>memcached_pool_st</i>* memcached_pool(const char<i>&nbsp;<wbr>*option_string</i>, size_t<i>&nbsp;<wbr>option_string_length</i>)</p>
<dd>
<dt><i>memcached_pool_st</i>* memcached_pool_create(memcached_st*<i>&nbsp;<wbr>mmc</i>, int<i>&nbsp;<wbr>initial</i>, int<i>&nbsp;<wbr>max</i>)</p>
<dd>
<p> Deprecated since version 0.46: Use <i>memcached_pool()</i></p>
<dt><code>memcached_st* memcached_pool_destroy(</code><i>memcached_pool_st</i>*<i>&nbsp;<wbr>pool</i>)</p>
<dd>
<dt><code>memcached_st* memcached_pool_pop(</code><i>memcached_pool_st</i>*<i>&nbsp;<wbr>pool</i>, bool<i>&nbsp;<wbr>block</i>, memcached_return_t<i>&nbsp;<wbr>*rc</i>)</p>
<dd>
<p> Deprecated since version 0.53: Use <i>memcached_pool_fetch()</i></p>
<dt><code>memcached_st* memcached_pool_fetch(</code><i>memcached_pool_st</i>*, struct timespec*<i>&nbsp;<wbr>relative_time</i>, memcached_return_t*<i>&nbsp;<wbr>rc</i>)</p>
<dd>
<p> New in version 0.53: Synonym for memcached_pool_pop</p>
<dt><code>memcached_return_t memcached_pool_push(</code><i>memcached_pool_st</i>*<i>&nbsp;<wbr>pool</i>, memcached_st<i>&nbsp;<wbr>*mmc</i>)</p>
<dd>
<p> Deprecated since version 0.53: Use <i>memcached_pool_push()</i></p>
<dt><code>memcached_return_t memcached_pool_release(</code><i>memcached_pool_st</i>*<i>&nbsp;<wbr>pool</i>, memcached_st*<i>&nbsp;<wbr>mmc</i>)</p>
<dd>
<p> New in version 0.53: Synonym for memcached_pool_push.</p>
<dt><code>memcached_return_t memcached_pool_behavior_set(</code><i>memcached_pool_st</i><i>&nbsp;<wbr>*pool</i>, memcached_behavior_t<i>&nbsp;<wbr>flag</i>, uint64_t<i>&nbsp;<wbr>data</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_pool_behavior_get(</code><i>memcached_pool_st</i><i>&nbsp;<wbr>*pool</i>, memcached_behavior_t<i>&nbsp;<wbr>flag</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<p> Compile and link with -lmemcachedutil -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_pool()</i> is used to create a connection pool of objects you may use to remove the overhead of using memcached_clone for short lived <code>memcached_st</code> objects. Please see <code>libmemcached_configuration</code> for details on the format of the configuration string. </p>
<p> <i>memcached_pool_destroy()</i> is used to destroy the connection pool created with <i>memcached_pool_create()</i> and release all allocated resources. It will return the pointer to the <code>memcached_st</code> structure passed as an argument to <i>memcached_pool_create()</i>, and returns the ownership of the pointer to the caller when created with <i>memcached_pool_create()</i>, otherwise NULL is returned.. </p>
<p> <i>memcached_pool_fetch()</i> is used to fetch a connection structure from the connection pool. The relative_time argument specifies if the function should block and wait for a connection structure to be available if we try to exceed the maximum size. You need to specify time in relative time. </p>
<p> <i>memcached_pool_release()</i> is used to return a connection structure back to the pool. </p>
<p> <i>memcached_pool_behavior_get()</i> and <i>memcached_pool_behavior_set()</i> is used to get/set behavior flags on all connections in the pool. </p>
<p> Both <i>memcached_pool_release()</i> and <i>memcached_pool_fetch()</i> are thread safe.</p>
<h2>RETURN</h2>
<p> <i>memcached_pool_destroy()</i> returns the pointer (and ownership) to the <code>memcached_st</code> structure used to create the pool. If connections are in use it returns NULL. </p>
<p> <i>memcached_pool_pop()</i> returns a pointer to a <code>memcached_st</code> structure from the pool (or NULL if an allocation cannot be satisfied). </p>
<p> <i>memcached_pool_release()</i> returns <code>MEMCACHED_SUCCESS</code> upon success. </p>
<p> <i>memcached_pool_behavior_get()</i> and <i>memcached_pool_behavior_get()</i> returns <code>MEMCACHED_SUCCESS</code> upon success. </p>
<p> If any methods returns MEMCACHED_IN_PROGRESS then a lock on the pool could not be obtained. If any of the parameters passed to any of these functions is invalid, MEMCACHED_INVALID_ARGUMENTS will be returned. </p>
<p> memcached_pool_fetch may return MEMCACHED_TIMEOUT if a timeout occurs while waiting for a free memcached_st. MEMCACHED_NOTFOUND if no memcached_st was available.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Brian Aker, &lt;<i>brian [at] tangent.org</i>&gt; </p>
<p> Trond Norbye, &lt;<i>trond.norbye [at] gmail.com</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i> <i><a href="/docs/linux/man/3-libmemcached_configuration/">libmemcached_configuration</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
