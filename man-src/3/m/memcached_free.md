---
title: "memcached_free(3)"
name: "memcached_free"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_free/"
description: "memcached_free – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_free &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_st</code></p>
<dd>
<dt><i>memcached_st</i>* memcached_create(<i>memcached_st</i><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>void memcached_free(</code><i>memcached_st</i><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><i>memcached_st</i>* memcached_clone(<i>memcached_st</i><i>&nbsp;<wbr>*destination</i>, <i>memcached_st</i><i>&nbsp;<wbr>*source</i>)</p>
<dd>
<dt><code>void memcached_servers_reset(</code><i>memcached_st</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i>memcached_create()</i> is used to create a <i>memcached_st</i> structure that will then be used by other <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) functions to communicate with the server. You should either pass a statically declared <i>memcached_st</i> to <i>memcached_create()</i> or a NULL. If a NULL passed in then a structure is allocated for you. </p>
<p> Please note, when you write new application use <code>memcached()</code> over <i>memcached_create()</i>. </p>
<p> <i>memcached_clone()</i> is similar to <i>memcached_create()</i> but it copies the defaults and list of servers from the source <i>memcached_st</i>. If you pass a null as the argument for the source to clone, it is the same as a call to <i>memcached_create()</i>. If the destination argument is NULL a <i>memcached_st</i> will be allocated for you. </p>
<p> <i>memcached_servers_reset()</i> allows you to zero out the list of servers that the <i>memcached_st</i> has. </p>
<p> To clean up memory associated with a <i>memcached_st</i> structure you should pass it to <i>memcached_free()</i> when you are finished using it. <i>memcached_free()</i> is the only way to make sure all memory is deallocated when you finish using the structure. </p>
<p> You may wish to avoid using <a href="/docs/linux/man/3-memcached_create/">memcached_create</a>(3) or <a href="/docs/linux/man/3-memcached_clone/">memcached_clone</a>(3) with a stack based allocation. The most common issues related to ABI safety involve heap allocated structures.</p>
<h2>RETURN</h2>
<p> <i>memcached_create()</i> returns a pointer to the <i>memcached_st</i> that was created (or initialized). On an allocation failure, it returns NULL. </p>
<p> <i>memcached_clone()</i> returns a pointer to the <i>memcached_st</i> that was created (or initialized). On an allocation failure, it returns NULL.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
