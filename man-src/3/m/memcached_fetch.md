---
title: "memcached_fetch(3)"
name: "memcached_fetch"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_fetch/"
description: "memcached_fetch – Retrieving data from the server"
---

<h2>NAME</h2>
<p> memcached_fetch &#8211; Retrieving data from the server</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>char *memcached_fetch(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>*key_length</i>, size_t<i>&nbsp;<wbr>*value_length</i>, uint32_t<i>&nbsp;<wbr>*flags</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd> Deprecated since version 0.50: Use <code>memcached_fetch_result()</code> instead. </p>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_fetch()</i> is used to fetch an individual value from the server. <code>memcached_mget()</code> must always be called before using this method. You must pass in a key and its length to fetch the object. You must supply three pointer variables which will give you the state of the returned object. A <code>uint32_t</code> pointer to contain whatever flags you stored with the value, a <code>size_t</code> pointer which will be filled with size of of the object, and a <code>memcached_return_t</code> pointer to hold any error. The object will be returned upon success and NULL will be returned on failure. <code>MEMCACHED_END</code> is returned by the *error value when all objects that have been found are returned. The final value upon <code>MEMCACHED_END</code> is null. </p>
<p> Values returned by <i>memcached_fetch()</i> must be freed by the caller. </p>
<p> All of the above functions are not tested when the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> has been set. Executing any of these functions with this behavior on will result in <code>MEMCACHED_NOT_SUPPORTED</code> being returned, or for those functions which do not return a <code>memcached_return_t</code>, the error function parameter will be set to <code>MEMCACHED_NOT_SUPPORTED</code>.</p>
<h2>RETURN</h2>
<p> <i>memcached_fetch()</i> sets error to to <code>MEMCACHED_END</code> upon successful conclusion. <code>MEMCACHED_NOTFOUND</code> will be return if no keys at all were found. </p>
<p> <code>MEMCACHED_KEY_TOO_BIG</code> is set to error whenever <i>memcached_fetch()</i> was used and the key was set larger then <code>MEMCACHED_MAX_KEY</code>, which was the largest key allowed for the original memcached ascii server.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_fetch_result/">memcached_fetch_result</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
