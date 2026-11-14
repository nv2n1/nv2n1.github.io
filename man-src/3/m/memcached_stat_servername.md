---
title: "memcached_stat_servername(3)"
name: "memcached_stat_servername"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_stat_servername/"
description: "memcached_stat_servername – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_stat_servername &#8211; libmemcached Documentation </p>
<p> Get memcached statistics</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_stat_st</code></p>
<dd>
<dt><code>memcached_return_t (*memcached_stat_fn)(memcached_server_instance_st</code><i>&nbsp;<wbr>server</i>, const char<i>&nbsp;<wbr>*key</i>, size_t<i>&nbsp;<wbr>key_length</i>, const char<i>&nbsp;<wbr>*value</i>, size_t<i>&nbsp;<wbr>value_length</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<dt><i>memcached_stat_st</i> *memcached_stat(memcached_st<i>&nbsp;<wbr>*ptr</i>, char<i>&nbsp;<wbr>*args</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_stat_servername(</code><i>memcached_stat_st</i><i>&nbsp;<wbr>*stat</i>, char<i>&nbsp;<wbr>*args</i>, const char<i>&nbsp;<wbr>*hostname</i>, in_port_t<i>&nbsp;<wbr>port</i>)</p>
<dd>
<dt><code>char * memcached_stat_get_value(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_stat_st</i><i>&nbsp;<wbr>*stat</i>, const char<i>&nbsp;<wbr>*key</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>char ** memcached_stat_get_keys(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_stat_st</i><i>&nbsp;<wbr>*stat</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_stat_execute(memcached_st</code><i>&nbsp;<wbr>*memc</i>, const char<i>&nbsp;<wbr>*args</i>, <i>memcached_stat_fn</i><i>&nbsp;<wbr>func</i>, void<i>&nbsp;<wbr>*context</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) has the ability to query a memcached server (or collection of servers) for their current state. Queries to find state return a <i>memcached_stat_st</i> structure. You are responsible for freeing this structure. While it is possible to access the structure directly it is not advisable. <i>memcached_stat_get_value()</i> has been provided to query the structure. </p>
<p> <i>memcached_stat_execute()</i> uses the servers found in <i>memcached_stat_st</i> and executes a &quot;stat&quot; command on each server. args is an optional argument that can be passed in to modify the behavior of &quot;stats&quot;. You will need to supply a callback function that will be supplied each pair of values returned by the memcached server. </p>
<p> <i>memcached_stat()</i> fetches an array of <i>memcached_stat_st</i> structures containing the state of all available memcached servers. The return value must be freed by the calling application. If called with the <code>MEMCACHED_BEHAVIOR_USE_UDP</code> behavior set, a NULL value is returned and the error parameter is set to <code>MEMCACHED_NOT_SUPPORTED</code>. </p>
<p> <i>memcached_stat_servername()</i> can be used standalone without a <code>memcached_st</code> to obtain the state of a particular server. &quot;args&quot; is used to define a particular state object (a list of these are not provided for by either the <i>memcached_stat_get_keys()</i> call nor are they defined in the memcached protocol). You must specify the hostname and port of the server you want to obtain information on. </p>
<p> <i>memcached_stat_get_value()</i> returns the value of a particular state key. You specify the key you wish to obtain. The key must be null terminated. </p>
<p> <i>memcached_stat_get_keys()</i> returns a list of keys that the server has state objects on. You are responsible for freeing this list. </p>
<p> A command line tool, <a href="/docs/linux/man/1-memstat/">memstat</a>(1), is provided so that you do not have to write an application to do this.</p>
<h2>RETURN</h2>
<p> Varies, see particular functions. </p>
<p> Any method returning a <i>memcached_stat_st</i> expects you to free the memory allocated for it.</p>
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
