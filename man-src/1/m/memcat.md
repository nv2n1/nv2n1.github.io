---
title: "memcat(1)"
name: "memcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memcat/"
description: "memcat – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcat &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> memcat [options] key </p>
<p> Copy a set of keys to stdout</p>
<h2>DESCRIPTION</h2>
<p> <code>memcat</code> outputs to stdout the value a single or multiple set of keys stored in a <a href="/docs/linux/man/1-memcached/">memcached</a>(1) server. If any key is not found an error is returned. </p>
<p> It is similar to the standard UNIX <a href="/docs/linux/man/1-cat/">cat</a>(1) utility.</p>
<h2>OPTIONS</h2>
<p> You can specify servers via the option:</p>
<dl>
<dt><code>&#8211;servers</code></p>
<dd>
<p> or via the environment variable:</p>
<dt><code>`MEMCACHED_SERVERS`</code></p>
<dd>
<p> For a full list of operations run the tool with the option:</p>
<dt><code>&#8211;help</code></p>
<dd></dl>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Brian Aker, &lt;<i>brian [at] tangent.org</i>&gt; </p>
<p> Mark Atwood &lt;<i>mark [at] fallenpegasus.com</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
