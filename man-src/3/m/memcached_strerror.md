---
title: "memcached_strerror(3)"
name: "memcached_strerror"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_strerror/"
description: "memcached_strerror – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_strerror &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>const char * memcached_strerror(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, memcached_return_t<i>&nbsp;<wbr>rc</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_strerror()</i> takes a <code>memcached_return_t</code> value and returns a string describing the error. </p>
<p> This string must not be modified by the application. </p>
<p> <code>memcached_return_t</code> values are returned from nearly all <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) functions. </p>
<p> <code>memcached_return_t</code> values are of an enum type so that you can set up responses with switch/case and know that you are capturing all possible return values.</p>
<h2>RETURN</h2>
<p> <i>memcached_strerror()</i> returns a string describing a <code>memcached_return_t</code> value.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
