---
title: "memcached_flush_buffers(3)"
name: "memcached_flush_buffers"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_flush_buffers/"
description: "memcached_flush_buffers – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_flush_buffers &#8211; libmemcached Documentation </p>
<p> Flush and senf buffered commands</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_flush_buffers(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_flush_buffers()</i> is used in conjunction with <code>MEMCACHED_BEHAVIOR_BUFFER_REQUESTS</code> (see <a href="/docs/linux/man/3-memcached_behavior/">memcached_behavior</a>(3)) to flush all buffers by sending the buffered commands to the server for processing.</p>
<h2>RETURN</h2>
<p> A value of type <code>memcached_return_t</code> is returned On success that value will be <code>MEMCACHED_SUCCESS</code>. Use <code>memcached_strerror()</code> to translate this value to a printable string.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Brian Aker, &lt;<i>brian [at] tangent.org</i>&gt; </p>
<p> Trond Norbye, &lt;<i>trond.norbye [at] gmail.com</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
