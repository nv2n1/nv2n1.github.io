---
title: "memcached_destroy_sasl_auth_data(3)"
name: "memcached_destroy_sasl_auth_data"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_destroy_sasl_auth_data/"
description: "memcached_destroy_sasl_auth_data – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_destroy_sasl_auth_data &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached_pool.h&gt;</p>
<dl>
<dt><code>void memcached_set_sasl_callbacks(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const sasl_callback_t<i>&nbsp;<wbr>*callbacks</i>)</p>
<dd>
<dt><code>const sasl_callback_t *memcached_get_sasl_callbacks(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_set_sasl_auth_data(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, const char<i>&nbsp;<wbr>*username</i>, const char<i>&nbsp;<wbr>*password</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_destroy_sasl_auth_data(memcached_st</code><i>&nbsp;<wbr>*ptr</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3) allows you to plug in your own callbacks function used by libsasl to perform SASL authentication. </p>
<p> Please note that SASL requires the memcached binary protocol, and you have to specify the callbacks before you connect to the server. </p>
<p> <i>memcached_set_sasl_auth_data()</i> is a helper function defining the basic functionality for you, but it will store the username and password in memory. If you choose to use this method you have to call <i>memcached_destroy_sasl_auth_data</i> before calling <code>memcached_free</code> to avoid a memory leak. You should NOT call <i>memcached_destroy_sasl_auth_data</i> if you specify your own callback function with <i>memcached_set_sasl_callbacks()</i>.</p>
<h2>RETURN</h2>
<p> <i>memcached_get_sasl_callbacks()</i> returns the callbacks currently used by this memcached handle. <i>memcached_set_sasl_auth_data()</i> returns <code>MEMCACHED_SUCCESS</code> upon success.</p>
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
