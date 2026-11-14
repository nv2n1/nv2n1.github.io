---
title: "memcached_version(3)"
name: "memcached_version"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_version/"
description: "memcached_version – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_version &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>const char * memcached_lib_version(void)</code></p>
<dd>
<dt><code>memcached_return_t memcached_version(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_lib_version()</i> is used to return a simple version string representing the libmemcached version (client library version, not server version) </p>
<p> <i>memcached_version()</i> is used to set the major, minor, and micro versions of each memcached server being used by the memcached_st connection structure. It returns the memcached server return code.</p>
<h2>RETURN</h2>
<p> <i>memcached_lib_version()</i> returns a string with the version of the libmemcached driver. </p>
<p> A value of <code>memcached_return_t</code> is returned from :c:func:&#8217;memcached_version&#8217; </p>
<p> On success that value will be <code>MEMCACHED_SUCCESS</code>. </p>
<p> If called with the <code>MEMCACHED_BEHAVIOR_USE_UDP()</code> behavior set, the value <code>MEMCACHED_NOT_SUPPORTED</code> will be returned. </p>
<p> Use <code>memcached_strerror()</code> to translate this value to a printable string.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
