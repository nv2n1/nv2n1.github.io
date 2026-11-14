---
title: "memcached_last_error_message(3)"
name: "memcached_last_error_message"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_last_error_message/"
description: "memcached_last_error_message – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_last_error_message &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>const char *memcached_last_error_message(memcached_st</code><i>&nbsp;<wbr>*</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_last_error_message()</i> is used to return the last error message that the server responded too. If this error came from a specific server, its hostname and port will be provided in the error message.</p>
<h2>RETURN</h2>
<p> memcached_last_error_message returns a const char* which does not need to be de-allocated. If no error has occurred then it will return NULL.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
