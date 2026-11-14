---
title: "memcached_dump(3)"
name: "memcached_dump"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_dump/"
description: "memcached_dump – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_dump &#8211; libmemcached Documentation </p>
<p> Get a list of keys found on memcached servers</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_dump(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_dump_fn</i><i>&nbsp;<wbr>*function</i>, void<i>&nbsp;<wbr>*context</i>, uint32_t<i>&nbsp;<wbr>number_of_callbacks</i>)</p>
<dd>
<dt><code>memcached_return_t (*memcached_dump_fn)(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_dump()</i> is used to get a list of keys found in <a href="/docs/linux/man/1-memcached/">memcached</a>(1) servers. Because <a href="/docs/linux/man/1-memcached/">memcached</a>(1) does not guarentee to dump all keys you can not assume you have fetched all keys from the server. The function takes an array of callbacks that it will use to execute on keys as they are found. </p>
<p> Currently the binary protocol is not testsed.</p>
<h2>RETURN</h2>
<p> A value of type <code>memcached_return_t</code> is returned On success that value will be <code>MEMCACHED_SUCCESS</code>. Use <code>memcached_strerror()</code> to translate this value to a printable string.</p>
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
