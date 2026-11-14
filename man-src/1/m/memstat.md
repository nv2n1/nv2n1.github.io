---
title: "memstat(1)"
name: "memstat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memstat/"
description: "memstat – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memstat &#8211; libmemcached Documentation </p>
<p> memstat &#8211; Display the operating status of a single or group of memcached servers</p>
<h2>SYNOPSIS</h2>
<p> memstat [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>memstat</code> dumps the state of <a href="/docs/linux/man/1-memcached/">memcached</a>(1) servers. It displays all data to stdout.</p>
<h2>OPTIONS</h2>
<p> You can specify servers via the option:</p>
<dl>
<dt><code>&#8211;servers</code></p>
<dd>
<p> or via the environment variable:</p>
<dt><code>&#8216;MEMCACHED_SERVERS, &#8211;args&#8217;</code></p>
<dd>
<p> which can be used to specify the &quot;argument&quot; sent to the stats command (ie slab, size, items, etc..). </p>
<p> For a full list of operations run the tool with:</p>
<dt><code>&#8211;help</code></p>
<dd>
<dt><code>&#8211;analyze</code></p>
<dd></dl>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
