---
title: "memcached_generate_hash_value(3)"
name: "memcached_generate_hash_value"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_generate_hash_value/"
description: "memcached_generate_hash_value – Generating hash values directly"
---

<h2>NAME</h2>
<p> memcached_generate_hash_value &#8211; Generating hash values directly </p>
<p> Hash a key value</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_hash_t</code></p>
<dd>
<dt><code>uint32_t memcached_generate_hash_value(const char</code><i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, <i>memcached_hash_t</i><i>&nbsp;<wbr>hash_algorithm</i>)</p>
<dd>
<dt><code>uint32_t memcached_generate_hash(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>)</p>
<dd>
<dt><code>MEMCACHED_HASH_DEFAULT</code></p>
<dd>
<dt><code>MEMCACHED_HASH_MD5</code></p>
<dd>
<dt><code>MEMCACHED_HASH_CRC</code></p>
<dd>
<dt><code>MEMCACHED_HASH_FNV1_64</code></p>
<dd>
<dt><code>MEMCACHED_HASH_FNV1A_64</code></p>
<dd>
<dt><code>MEMCACHED_HASH_FNV1_32</code></p>
<dd>
<dt><code>MEMCACHED_HASH_FNV1A_32</code></p>
<dd>
<dt><code>MEMCACHED_HASH_JENKINS</code></p>
<dd>
<dt><code>MEMCACHED_HASH_MURMUR</code></p>
<dd>
<dt><code>MEMCACHED_HASH_HSIEH</code></p>
<dd>
<dt><code>MEMCACHED_HASH_MURMUR3</code></p>
<dd>
<p> Compile and link with -lmemcachedutil -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_generate_hash_value()</i> allows you to hash a key using one of the hash functions defined in the library. This method is provided for the convenience of higher-level language bindings and is not necessary for normal memcache operations. </p>
<p> The allowed hash algorithm constants are listed in the manpage for <code>memcached_behavior_set()</code>. </p>
<p> <i>memcached_generate_hash()</i> takes a <code>memcached_st</code> struture and produces the hash value that would have been generated based on the defaults of <code>memcached_st</code>. </p>
<p> As of version 0.36 all hash methods have been placed into the library <a href="/docs/linux/man/3-libhashkit/">libhashkit</a>(3) which is linked with <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3). For more information please see its documentation.</p>
<h2>RETURN</h2>
<p> A 32-bit integer which is the result of hashing the given key. For 64-bit hash algorithms, only the least-significant 32 bits are returned.</p>
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
