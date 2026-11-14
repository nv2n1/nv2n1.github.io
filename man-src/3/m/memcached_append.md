---
title: "memcached_append(3)"
name: "memcached_append"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_append/"
description: "memcached_append – Appending to or Prepending to data on the server"
---

<h2>NAME</h2>
<p> memcached_append &#8211; Appending to or Prepending to data on the server </p>
<p> Appending or Prepending to data on the server</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_prepend(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_append(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_prepend_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_append_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_prepend()</i> and memcached_append are used to modify information on a server. All methods take a key, and its length to store the object. Keys are currently limited to 250 characters when using either a version of memcached which is 1.4 or below, or when using the text protocol. You must supply both a value and a length. Optionally you may test an expiration time for the object and a 16 byte value (it is meant to be used as a bitmap). &quot;flags&quot; is a 4byte space that is stored alongside of the main value. Many sub libraries make use of this field, so in most cases users should avoid making use of it. </p>
<p> <i>memcached_prepend()</i> places a segment of data before the last piece of data stored. Currently expiration and key are not used in the server. </p>
<p> <i>memcached_append()</i> places a segment of data at the end of the last piece of data stored. Currently expiration and key are not used in the server. </p>
<p> <i>memcached_prepend_by_key()</i> and <i>memcached_append_by_key()</i> methods both behave in a similar method as the non key methods. The difference is that they use their group_key parameter to map objects to particular servers. </p>
<p> If you are looking for performance, <code>memcached_set()</code> with non-blocking IO is the fastest way to store data on the server. </p>
<p> All of the above functions are testsed with the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> behavior enabled. However, when using these operations with this behavior on, there are limits to the size of the payload being sent to the server. The reason for these limits is that the Memcached Server does not allow multi-datagram requests and the current server implementation sets a datagram size to 1400 bytes. Due to protocol overhead, the actual limit of the user supplied data is less than 1400 bytes and depends on the protocol in use as, well as the operation being executed. When running with the binary protocol, <code>MEMCACHED_BEHAVIOR_BINARY_PROTOCOL</code>, the size of the key,value, flags and expiry combined may not exceed 1368 bytes. When running with the ASCII protocol, the exact limit fluctuates depending on which function is being executed and whether the function is a cas operation or not. For non-cas ASCII set operations, there are at least 1335 bytes available to split among the key, key_prefix, and value; for cas ASCII operations there are at least 1318 bytes available to split among the key, key_prefix and value. If the total size of the command, including overhead, exceeds 1400 bytes, a <code>MEMCACHED_WRITE_FAILURE</code> will be returned.</p>
<h2>RETURN</h2>
<p> All methods return a value of type <code>memcached_return_t</code>. On success the value will be <code>MEMCACHED_SUCCESS</code>. Use <code>memcached_strerror()</code> to translate this value to a printable string.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemached/">libmemached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_set/">memcached_set</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_add/">memcached_add</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_cas/">memcached_cas</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_replace/">memcached_replace</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
