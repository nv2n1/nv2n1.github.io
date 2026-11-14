---
title: "memcached_exist_by_key(3)"
name: "memcached_exist_by_key"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_exist_by_key/"
description: "memcached_exist_by_key – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_exist_by_key &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_exist(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>*key_length</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_exist_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>*group_key_length</i>, char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>*key_length</i>)</p>
<dd> New in version 0.53. </p>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_exist()</i> can be used to check to see if a key exists. No value is returned if the key exists, or does not exist, on the server.</p>
<h2>RETURN</h2>
<p> <i>memcached_exist()</i> sets error to to <code>MEMCACHED_SUCCESS</code> upon finding that the key exists. <code>MEMCACHED_NOTFOUND</code> will be return if the key is not found.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
