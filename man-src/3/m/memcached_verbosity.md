---
title: "memcached_verbosity(3)"
name: "memcached_verbosity"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_verbosity/"
description: "memcached_verbosity – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_verbosity &#8211; libmemcached Documentation </p>
<p> Modifiy verbosity of servers</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_return_t memcached_verbosity(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, uint32_t<i>&nbsp;<wbr>verbosity</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_verbosity()</i> modifies the &quot;verbosity&quot; of the <a href="/docs/linux/man/1-memcached/">memcached</a>(1) servers referenced in the <code>memcached_st</code> parameter.</p>
<h2>RETURN</h2>
<p> A value of type <code>memcached_return_t</code> is returned. </p>
<p> On success that value will be <code>MEMCACHED_SUCCESS</code>. </p>
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
