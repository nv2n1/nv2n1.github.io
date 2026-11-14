---
title: "memcached_set_memory_allocators(3)"
name: "memcached_set_memory_allocators"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_set_memory_allocators/"
description: "memcached_set_memory_allocators – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_set_memory_allocators &#8211; libmemcached Documentation </p>
<p> Manage memory allocator functions</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_set_memory_allocators(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_malloc_fn</i><i>&nbsp;<wbr>mem_malloc</i>, <i>memcached_free_fn</i><i>&nbsp;<wbr>mem_free</i>, <i>memcached_realloc_fn</i><i>&nbsp;<wbr>mem_realloc</i>, <i>memcached_calloc_fn</i><i>&nbsp;<wbr>mem_calloc</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<dt><code>void memcached_get_memory_allocators(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_malloc_fn</i><i>&nbsp;<wbr>*mem_malloc</i>, <i>memcached_free_fn</i><i>&nbsp;<wbr>*mem_free</i>, <i>memcached_realloc_fn</i><i>&nbsp;<wbr>*mem_realloc</i>, <i>memcached_calloc_fn</i><i>&nbsp;<wbr>*mem_calloc</i>)</p>
<dd>
<dt><code>void * memcached_get_memory_allocators_context(const memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>void * (*memcached_malloc_fn)(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const size_t<i>&nbsp;<wbr>size</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<dt><code>void * (*memcached_realloc_fn)(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, void<i>&nbsp;<wbr>*mem</i>, const size_t<i>&nbsp;<wbr>size</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<dt><code>void (*memcached_free_fn)(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, void<i>&nbsp;<wbr>*mem</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<dt><code>void * (*memcached_calloc_fn)(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, size_t<i>&nbsp;<wbr>nelem</i>, const size_t<i>&nbsp;<wbr>elsize</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) allows you to specify your own memory allocators, optimized for your application. This enables libmemcached to be used inside of applications that have their own malloc implementation. </p>
<p> <i>memcached_set_memory_allocators()</i> is used to set the memory allocators used by the memcached instance specified by ptr. Please note that you cannot override only one of the memory allocators, you have to specify a complete new set if you want to override one of them. All of the memory allocation functions should behave as specified in the C99 standard. Specify NULL as all functions to reset them to the default values. </p>
<p> <i>memcached_get_memory_allocators()</i> is used to get the currently used memory allocators by a mamcached handle. </p>
<p> <i>memcached_get_memory_allocators_context()</i> returns the void * that was passed in during the call to <i>memcached_set_memory_allocators()</i>. </p>
<p> The first argument to the memory allocator functions is a pointer to a memcached structure, the is passed as const and you will need to clone it in order to make use of any operation which would modify it.</p>
<h2>NOTES</h2>
<p> In version 0.38 all functions were modified to have a context void pointer passed to them. This was so that customer allocators could have their own space for memory.</p>
<h2>RETURN</h2>
<p> <i>memcached_set_memory_allocators()</i> return <code>MEMCACHED_SUCCESS</code> upon success, and <code>MEMCACHED_FAILURE</code> if you don&#8217;t pass a complete set of function pointers.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
