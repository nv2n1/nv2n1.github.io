---
title: "memcached_decrement_with_initial(3)"
name: "memcached_decrement_with_initial"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_decrement_with_initial/"
description: "memcached_decrement_with_initial – Incrementing and Decrementing Values"
---

<h2>NAME</h2>
<p> memcached_decrement_with_initial &#8211; Incrementing and Decrementing Values</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_increment(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint32_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_decrement(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint32_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_increment_with_initial(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint64_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>initial</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_decrement_with_initial(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint64_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>initial</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_increment_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint32_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_decrement_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint32_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_increment_with_initial_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint64_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>initial</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_decrement_with_initial_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, uint64_t<i>&nbsp;<wbr>offset</i>, uint64_t<i>&nbsp;<wbr>initial</i>, time_t<i>&nbsp;<wbr>expiration</i>, uint64_t<i>&nbsp;<wbr>*value</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> servers have the ability to increment and decrement keys (overflow and underflow are not detected). This gives you the ability to use memcached to generate shared sequences of values. </p>
<p> memcached_increment takes a key and keylength and increments the value by the offset passed to it. The value is then returned via the uint32_t value pointer you pass to it. </p>
<p> memcached_decrement takes a key and keylength and decrements the value by the offset passed to it. The value is then returned via the uint32_t value pointer you pass to it. </p>
<p> memcached_increment_with_initial takes a key and keylength and increments the value by the offset passed to it. If the object specified by key does not exist, one of two things may happen: If the expiration value is MEMCACHED_EXPIRATION_NOT_ADD, the operation will fail. For all other expiration values, the operation will succeed by seeding the value for that key with a initial value to expire with the provided expiration time. The flags will be set to zero.The value is then returned via the uint32_t value pointer you pass to it. </p>
<p> memcached_decrement_with_initial takes a key and keylength and decrements the value by the offset passed to it. If the object specified by key does not exist, one of two things may happen: If the expiration value is MEMCACHED_EXPIRATION_NOT_ADD, the operation will fail. For all other expiration values, the operation will succeed by seeding the value for that key with a initial value to expire with the provided expiration time. The flags will be set to zero.The value is then returned via the uint32_t value pointer you pass to it. </p>
<p> <i>memcached_increment_by_key()</i>, <i>memcached_decrement_by_key()</i>, <i>memcached_increment_with_initial_by_key()</i>, and <i>memcached_decrement_with_initial_by_key()</i> are master key equivalents of the above.</p>
<h2>RETURN</h2>
<p> A value of type <code>memcached_return_t</code> is returned. On success that value will be <code>MEMCACHED_SUCCESS</code>. Use memcached_strerror to translate this value to a printable string.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
