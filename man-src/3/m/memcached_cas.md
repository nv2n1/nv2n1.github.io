---
title: "memcached_cas(3)"
name: "memcached_cas"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_cas/"
description: "memcached_cas – Working with data on the server in an atomic fashion"
---

<h2>NAME</h2>
<p> memcached_cas &#8211; Working with data on the server in an atomic fashion</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_cas(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>, uint64_t<i>&nbsp;<wbr>cas</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_cas_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint32_t<i>&nbsp;<wbr>flags</i>, uint64_t<i>&nbsp;<wbr>cas</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_cas()</i> overwrites data in the server as long as the &quot;cas&quot; value is still the same in the server. You can get the cas value of a result by calling <code>memcached_result_cas()</code> on a <a href="/docs/linux/man/3-memcached_result_st/">memcached_result_st</a>(3) structure. At the point that this note was written cas is still buggy in memached. Turning on tests for it in <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) is optional. Please see <code>memcached_set()</code> for information on how to do this. </p>
<p> <i>memcached_cas_by_key()</i> method behaves in a similar method as the non key methods. The difference is that it uses the group_key parameter to map objects to particular servers. </p>
<p> <i>memcached_cas()</i> is testsed with the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> behavior enabled. However, when using these operations with this behavior on, there are limits to the size of the payload being sent to the server. The reason for these limits is that the Memcached Server does not allow multi-datagram requests and the current server implementation sets a datagram size to 1400 bytes. Due to protocol overhead, the actual limit of the user supplied data is less than 1400 bytes and depends on the protocol in use as, well as the operation being executed. When running with the binary protocol, <code>MEMCACHED_BEHAVIOR_BINARY_PROTOCOL</code>, the size of the key,value, flags and expiry combined may not exceed 1368 bytes. When running with the ASCII protocol, the exact limit fluctuates depending on which function is being executed and whether the function is a cas operation or not. For non-cas ASCII set operations, there are at least 1335 bytes available to split among the key, key_prefix, and value; for cas ASCII operations there are at least 1318 bytes available to split among the key, key_prefix and value. If the total size of the command, including overhead, exceeds 1400 bytes, a <code>MEMCACHED_WRITE_FAILURE</code> will be returned.</p>
<h2>RETURN</h2>
<p> All methods return a value of type <code>memcached_return_t</code>. On success the value will be <code>MEMCACHED_SUCCESS</code>. Use <code>memcached_strerror()</code> to translate this value to a printable string.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemached/">libmemached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_set/">memcached_set</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_append/">memcached_append</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_add/">memcached_add</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_prepend/">memcached_prepend</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_replace/">memcached_replace</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
