---
title: "memcached_analyze(3)"
name: "memcached_analyze"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_analyze/"
description: "memcached_analyze – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_analyze &#8211; libmemcached Documentation </p>
<p> Analyze server information</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_analysis_st</code></p>
<dd>
<dt><i>memcached_analysis_st</i> * memcached_analyze(memcached_st<i>&nbsp;<wbr>*ptr</i>, memcached_stat_st<i>&nbsp;<wbr>*stat</i>, memcached_return_t<i>&nbsp;<wbr>*error</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <code>libmemcached</code> has the ability to query a memcached server (or collection of servers) for their current state. Queries to find state return a <i>memcached_analysis_st</i> structure. You are responsible for freeing this structure. </p>
<p> <i>memcached_analyze()</i> analyzes useful information based on the provided servers and sets the result to the <i>memcached_analysis_st</i> structure. The return value must be freed by the calling application. </p>
<p> A command line tool, <code>memstat</code> with the option <i>memstat &#8211;analyze</i>, is provided so that you do not have to write an application to use this method.</p>
<h2>RETURN</h2>
<p> A pointer to the allocated <i>memcached_analysis_st</i> structure on success and a NULL pointer on failure. You may inspect the error detail by checking the <code>memcached_return_t</code> value. </p>
<p> Any method returning a <i>memcached_analysis_st</i> expects you to free the memory allocated for it.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
