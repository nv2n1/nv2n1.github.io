---
title: "memcached_server_cursor(3)"
name: "memcached_server_cursor"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_server_cursor/"
description: "memcached_server_cursor – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_server_cursor &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_server_fn</code></p>
<dd>
<dt><code>uint32_t memcached_server_count(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_server_add(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*hostname</i>, in_port_t<i>&nbsp;<wbr>port</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_server_add_udp(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*hostname</i>, in_port_t<i>&nbsp;<wbr>port</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_server_add_unix_socket(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*socket</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_server_push(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const memcached_server_st<i>&nbsp;<wbr>*list</i>)</p>
<dd>
<dt><code>memcached_server_instance_st memcached_server_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>memcached_server_instance_st memcached_server_get_last_disconnect(const memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_server_cursor(const memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const <i>memcached_server_fn</i><i>&nbsp;<wbr>*callback</i>, void<i>&nbsp;<wbr>*context</i>, uint32_t<i>&nbsp;<wbr>number_of_callbacks</i>)</p>
<dd>
<p> compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <code>libmemcached</code> performs operations on a list of hosts. The order of these hosts determine routing to keys. Functions are provided to add keys to memcached_st structures. To manipulate lists of servers see <a href="/docs/linux/man/3-memcached_server_st/">memcached_server_st</a>(3). </p>
<p> <i>memcached_server_count()</i> provides you a count of the current number of servers being used by a <code>memcached_st</code> structure.</p>
<dl>
<dt><i>memcached_server_add()</i> pushes a single TCP server into the <code>memcached_st</code> structure. This server will be placed at the end. Duplicate servers</p>
<dd> are allowed, so duplication is not checked. Executing this function with the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> behavior set will result in a <code>MEMCACHED_INVALID_HOST_PROTOCOL</code>. </p>
<p> <i>memcached_server_add_udp()</i> pushes a single UDP server into the <code>memcached_st</code> structure. This server will be placed at the end. Duplicate servers are allowed, so duplication is not checked. Executing this function with out setting the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> behavior will result in a <code>MEMCACHED_INVALID_HOST_PROTOCOL</code>. </p>
<p> <i>memcached_server_add_unix_socket()</i> pushes a single UNIX socket into the <code>memcached_st</code> structure. This UNIX socket will be placed at the end. Duplicate servers are allowed, so duplication is not checked. The length of the filename must be one character less than <code>MEMCACHED_MAX_HOST_LENGTH</code>. </p>
<p> <i>memcached_server_push()</i> pushes an array of <code>memcached_server_st</code> into the <code>memcached_st</code> structure. These servers will be placed at the end. Duplicate servers are allowed, so duplication is not checked. A copy is made of structure so the list provided (and any operations on the list) are not saved. </p>
<p> <i>memcached_server_by_key()</i> allows you to provide a key and retrieve the server which would be used for assignment. </p>
<p> <i>memcached_server_get_last_disconnect()</i> returns a pointer to the last server for which there was a connection problem. It does not mean this particular server is currently dead but if the library is reporting a server is, the returned server is a very good candidate. </p>
<p> <i>memcached_server_cursor()</i> takes a memcached_st and loops through the list of hosts currently in the cursor calling the list of callback functions provided. You can optionally pass in a value via context which will be provided to each callback function. An error return from any callback will terminate the loop. <i>memcached_server_cursor()</i> is passed the original caller <code>memcached_st</code> in its current state.</dl>
<h2>RETURN</h2>
<p> Varies, see particular functions.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
