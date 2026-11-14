---
title: "libmemcached(3)"
name: "libmemcached"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmemcached/"
description: "libmemcached – Introducing the C Client Library for memcached"
---

<h2>NAME</h2>
<p> libmemcached &#8211; Introducing the C Client Library for memcached</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt; </p>
<p> Compile and link with -lmemcached </p>
<p> <center> &#8212;-<br />
 </center> </p>
<p> libMemcached is an open source C/C++ client library and tools for the memcached server (<i><a rel="nofollow" href="http://memcached.org/">http://memcached.org/</a></i>). It has been designed to be light on memory usage, thread safe, and provide full access to server side methods. </p>
<p> libMemcached was designed to provide the greatest number of options to use Memcached. Some of the features provided:</p>
<dl>
<dt>1.</p>
<dd> Asynchronous and Synchronous Transport Support.</p>
<dt>2.</p>
<dd> Consistent Hashing and Distribution.</p>
<dt>3.</p>
<dd> Tunable Hashing algorithm to match keys.</p>
<dt>4.</p>
<dd> Access to large object support.</p>
<dt>5.</p>
<dd> Local replication.</p>
<dt>6.</p>
<dd> A complete reference guide and documentation to the API.</p>
<dt>7.</p>
<dd> Tools to Manage your Memcached networks.</dl>
<h2>DESCRIPTION</h2>
<p> &quot;Memcached is a high-performance, distributed memory object caching system, generic in nature, but intended for use in speeding up dynamic web applications by alleviating database load.&quot; <i><a rel="nofollow" href="http://memcached.org/">http://memcached.org/</a></i> </p>
<p> <code>libmemcached</code> is a small, thread-safe client library for the memcached protocol. The code has all been written to allow for both web and embedded usage. It handles the work behind routing individual keys to specific servers specified by the developer (and values are matched based on server order as supplied by the user). It implements a modular and consistent method of object distribution. </p>
<p> There are multiple implemented routing and hashing methods. See the <code>memcached_behavior_set()</code> manpage for more information. </p>
<p> All operations are performed against a <code>memcached_st</code> structure. These structures can either be dynamically allocated or statically allocated and then initialized by <code>memcached_create()</code>. Functions have been written in order to encapsulate the <code>memcached_st</code>. It is not recommended that you operate directly against the structure. </p>
<p> Nearly all functions return a <code>memcached_return_t</code> value. This value can be translated to a printable string with <code>memcached_strerror</code>. </p>
<p> Objects are stored on servers by hashing keys. The hash value maps the key to a particular server. All clients understand how this hashing works, so it is possibly to reliably both push data to a server and retrieve data from a server. </p>
<p> Group keys can be optionally used to group sets of objects with servers. </p>
<p> Namespaces are supported, and can be used to partition caches so that multiple applications can use the same memcached servers. </p>
<p> <code>memcached_st</code> structures are thread-safe, but each thread must contain its own structure (that is, if you want to share these among threads you must provide your own locking). No global variables are used in this library. </p>
<p> If you are working with GNU autotools you will want to add the following to your COPYING to properly include libmemcached in your application. </p>
<p> PKG_CHECK_MODULES(DEPS, libmemcached &gt;= 0.8.0) AC_SUBST(DEPS_CFLAGS) AC_SUBST(DEPS_LIBS) </p>
<p> Some features of the library must be enabled through <code>memcached_behavior_set()</code>. </p>
<p> Hope you enjoy it!</p>
<h2>CONSTANTS</h2>
<p> A number of constants have been provided for in the library.</p>
<dl>
<dt><code>MEMCACHED_DEFAULT_PORT</code></p>
<dd> The default port used by <a href="/docs/linux/man/3-memcached/">memcached</a>(3).</p>
<dt><code>MEMCACHED_MAX_KEY</code></p>
<dd> Default maximum size of a key (which includes the null pointer). Master keys have no limit, this only applies to keys used for storage.</p>
<dt><code>MEMCACHED_MAX_KEY</code></p>
<dd> Default size of key (which includes the null pointer).</p>
<dt><code>MEMCACHED_STRIDE</code></p>
<dd> This is the &quot;stride&quot; used in the consistent hash used between replicas.</p>
<dt><code>MEMCACHED_MAX_HOST_LENGTH</code></p>
<dd> Maximum allowed size of the hostname.</p>
<dt><code>LIBMEMCACHED_VERSION_STRING</code></p>
<dd> String value of libmemcached version such as &quot;1.23.4&quot;</p>
<dt><code>LIBMEMCACHED_VERSION_HEX</code></p>
<dd> Hex value of the version number. &quot;0x00048000&quot; This can be used for comparing versions based on number.</p>
<dt><code>MEMCACHED_PREFIX_KEY_MAX_SIZE</code></p>
<dd> Maximum length allowed for namespacing of a key.</dl>
<h2>THREADS AND PROCESSES</h2>
<p> When using threads or forked processes it is important to keep one instance of <code>memcached_st</code> per process or thread. Without creating your own locking structures you can not share a single <code>memcached_st</code>. However, you can call <code>memcached_quit()</code> on a <code>memcached_st</code> and then use the resulting cloned structure.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached_examples/">libmemcached_examples</a>(3)</i> <i><a href="/docs/linux/man/1-libmemcached/">libmemcached</a>(1)</i> <i><a href="/docs/linux/man/1-memcat/">memcat</a>(1)</i> <i><a href="/docs/linux/man/1-memcp/">memcp</a>(1)</i> <i><a href="/docs/linux/man/1-memflush/">memflush</a>(1)</i> <i><a href="/docs/linux/man/1-memrm/">memrm</a>(1)</i> <i><a href="/docs/linux/man/1-memslap/">memslap</a>(1)</i> <i><a href="/docs/linux/man/1-memstat/">memstat</a>(1)</i> <i><a href="/docs/linux/man/3-memcached_fetch/">memcached_fetch</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_replace/">memcached_replace</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_list_free/">memcached_server_list_free</a>(3)</i> <i><a href="/docs/linux/man/3-libmemcached_examples/">libmemcached_examples</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_clone/">memcached_clone</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_free/">memcached_free</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_add/">memcached_server_add</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_push/">memcached_server_push</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_add/">memcached_add</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_get/">memcached_get</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_count/">memcached_server_count</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_create/">memcached_create</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_increment/">memcached_increment</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_list/">memcached_server_list</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_set/">memcached_set</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_decrement/">memcached_decrement</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_mget/">memcached_mget</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_list_append/">memcached_server_list_append</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_delete/">memcached_delete</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_quit/">memcached_quit</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_list_count/">memcached_server_list_count</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_verbosity/">memcached_verbosity</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_server_add_unix_socket/">memcached_server_add_unix_socket</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_create/">memcached_result_create</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_free/">memcached_result_free</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_key_value/">memcached_result_key_value</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_key_length/">memcached_result_key_length</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_value/">memcached_result_value</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_length/">memcached_result_length</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_flags/">memcached_result_flags</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_cas/">memcached_result_cas</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_st/">memcached_result_st</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_append/">memcached_append</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_prepend/">memcached_prepend</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_fetch_result/">memcached_fetch_result</a>(3)</i> <i><a href="/docs/linux/man/1-memerror/">memerror</a>(1)</i> <i><a href="/docs/linux/man/3-memcached_get_by_key/">memcached_get_by_key</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_mget_by_key/">memcached_mget_by_key</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_delete_by_key/">memcached_delete_by_key</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_fetch_execute/">memcached_fetch_execute</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_callback_get/">memcached_callback_get</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_callback_set/">memcached_callback_set</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_version/">memcached_version</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_lib_version/">memcached_lib_version</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_result_set_value/">memcached_result_set_value</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_dump/">memcached_dump</a>(3)</i> <i><a href="/docs/linux/man/1-memdump/">memdump</a>(1)</i> <i><a href="/docs/linux/man/3-memcached_set_memory_allocators/">memcached_set_memory_allocators</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_get_memory_allocators/">memcached_get_memory_allocators</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_get_user_data/">memcached_get_user_data</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_set_user_data/">memcached_set_user_data</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
