---
title: "memcached_delete(3)"
name: "memcached_delete"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_delete/"
description: "memcached_delete – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_delete &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_delete(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, time_t<i>&nbsp;<wbr>expiration</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_delete_by_key(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*group_key</i>, size_t<i>&nbsp;<wbr>group_key_length</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, time_t<i>&nbsp;<wbr>expiration</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_delete()</i> is used to delete a particular key. <i>memcached_delete_by_key()</i> works the same, but it takes a master key to find the given value. </p>
<p> Expiration works by placing the item into a delete queue, which means that it won&#8217;t be possible to retrieve it by the &quot;get&quot; command. The &quot;add&quot; and &quot;replace&quot; commands with this key will also fail (the &quot;set&quot; command will succeed, however). After the time passes, the item is finally deleted from server memory. </p>
<p> Please note the the Danga memcached server removed tests for expiration in the 1.4 version.</p>
<h2>RETURN</h2>
<p> A value of type <code>memcached_return_t</code> is returned On success that value will be <code>MEMCACHED_SUCCESS</code>. Use <code>memcached_strerror()</code> to translate this value to a printable string. </p>
<p> If you are using the non-blocking mode of the library, success only means that the message was queued for delivery.</p>
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
