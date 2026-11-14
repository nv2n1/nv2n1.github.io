---
title: "memcached_set_user_data(3)"
name: "memcached_set_user_data"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_set_user_data/"
description: "memcached_set_user_data – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_set_user_data &#8211; libmemcached Documentation </p>
<p> Manage user specific data</p>
<h2>LIBRARY</h2>
<p> C Client Library for memcached (libmemcached, -lmemcached)</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>void *memcached_get_user_data(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>void *memcached_set_user_data(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, void<i>&nbsp;<wbr>*data</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) allows you to store a pointer to a user specific data inside the memcached_st structure. </p>
<p> <i>memcached_set_user_data()</i> is used to set the user specific data in the <code>memcached_st</code> structure. </p>
<p> <i>memcached_get_user_data()</i> is used to retrieve the user specific data in the <code>memcached_st</code> structure.</p>
<h2>RETURN</h2>
<p> <i>memcached_set_user_data()</i> returns the previous value of the user specific data. </p>
<p> <i>memcached_get_user_data()</i> returns the current value uf the user specific data.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
