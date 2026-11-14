---
title: "libmemcachedutil(3)"
name: "libmemcachedutil"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmemcachedutil/"
description: "libmemcachedutil – libmemcached Documentation"
---

<h2>NAME</h2>
<p> libmemcachedutil &#8211; libmemcached Documentation </p>
<p> Utility library for libmemcached</p>
<h2>SYNOPSIS</h2>
<pre><code>
cc[flag...] file... - lmemcachedutil
#include &lt;libmemcached/memcached_util.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>libmemcachedutil</code> is a small and thread-safe client library that provides extra functionality built on top of <code>libmemcached</code>.</p>
<h2>THREADS</h2>
<p> Do not try to access an instance of <code>memcached_st</code> from multiple threads at the same time. If you want to access memcached from multiple threads you should either clone the <code>memcached_st</code>, or use the memcached pool implementation. see <code>memcached_pool_create()</code>.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_pool_create/">memcached_pool_create</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_pool_destroy/">memcached_pool_destroy</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_pool_pop/">memcached_pool_pop</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_pool_push/">memcached_pool_push</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
