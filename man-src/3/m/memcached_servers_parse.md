---
title: "memcached_servers_parse(3)"
name: "memcached_servers_parse"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_servers_parse/"
description: "memcached_servers_parse – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_servers_parse &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_server_instance_st</code></p>
<dd>
<dt><code>memcached_server_list_st</code></p>
<dd>
<dt><code>memcached_server_st</code></p>
<dd>
<dt><code>const </code><i>memcached_server_instance_st</i> memcached_server_list(memcached_st<i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>void memcached_server_list_free(</code><i>memcached_server_list_st</i><i>&nbsp;<wbr>list</i>)</p>
<dd>
<dt><i>memcached_server_list_st</i> memcached_server_list_append(<i>memcached_server_list_st</i><i>&nbsp;<wbr>list</i>, const char<i>&nbsp;<wbr>*hostname</i>, in_port_t<i>&nbsp;<wbr>port</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<dt><code>uint32_t memcached_server_list_count(</code><i>memcached_server_list_st</i><i>&nbsp;<wbr>list</i>)</p>
<dd>
<dt><code>const char *memcached_server_error(</code><i>memcached_server_instance_st</i><i>&nbsp;<wbr>instance</i>)</p>
<dd>
<dt><code>void memcached_server_error_reset(</code><i>memcached_server_instance_st</i><i>&nbsp;<wbr>list</i>)</p>
<dd>
<p> Deprecated since version 0.39.</p>
<dt><code>void memcached_servers_parse()</code></p>
<dd>
<p> Deprecated since version 0.39. </p>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) operates on a list of hosts which are stored in <i>memcached_server_st</i> structures. You should not modify these structures directly. Functions are provided to modify these structures (and more can be added, just ask!). </p>
<p> <i>memcached_server_list()</i> is used to provide an array of all defined hosts. This was incorrectly documented as &quot;requiring free&quot; up till version 0.39. </p>
<p> <i>memcached_server_list_free()</i> deallocates all memory associated with the array of <i>memcached_server_st</i> that you passed to it. </p>
<p> <i>memcached_server_list_append()</i> adds a server to the end of a <i>memcached_server_st</i> array. On error null will be returned and the <code>memcached_return_t</code> pointer you passed into the function will be set with the appropriate error. If the value of port is zero, it is set to the default port of a memcached server. </p>
<p> DEPRECATED <i>memcached_servers_parse()</i>, please see <code>memcached()</code> </p>
<p> <i>memcached_server_error()</i> can be used to look at the text of the last error message sent by the server to to the client. </p>
<p> Before version 0.39 theses functions used a memcache_server_st *. In 0.39 memcached_server_st * was aliased to <i>memcached_server_list_st</i>. This was done for a style reason to help clean up some concepts in the code.</p>
<h2>RETURN</h2>
<p> Varies, see particular functions.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
