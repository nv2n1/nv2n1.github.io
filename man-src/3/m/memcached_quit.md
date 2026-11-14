---
title: "memcached_quit(3)"
name: "memcached_quit"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_quit/"
description: "memcached_quit – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_quit &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>void memcached_quit(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_quit()</i> will disconnect you from all currently connected servers. It will also reset the state of the connection (ie, any <code>memcached_fetch()</code> you are in the middle of will be terminated). This function is called automatically when you call <code>memcached_free()</code> on the <code>memcached_st</code> structure. </p>
<p> You do not need to call this on your own. All operations to change server hashes and parameters will handle connections to the server for you. This function is provided mainly so that you can timeout your connections or reset connections during the middle of a <code>memcached_fetch()</code>.</p>
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
