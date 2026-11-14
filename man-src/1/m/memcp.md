---
title: "memcp(1)"
name: "memcp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memcp/"
description: "memcp – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcp &#8211; libmemcached Documentation </p>
<p> Copies files to a collection of memcached servers</p>
<h2>SYNOPSIS</h2>
<p> memcp [options] [file] [server]</p>
<h2>DESCRIPTION</h2>
<p> <code>memcp</code> copies one or more files into <a href="/docs/linux/man/1-memcached/">memcached</a>(1) servers. It is similar to the standard UNIX <a href="/docs/linux/man/1-cp/">cp</a>(1) command. </p>
<p> The key names will be the names of the files, without any directory path.</p>
<h2>OPTIONS</h2>
<p> You can specify servers via the option:</p>
<dl>
<dt><code>&#8211;servers</code></p>
<dd>
<p> or via the environment variable:</p>
<dt><code>`MEMCACHED_SERVERS`</code></p>
<dd>
<p> If you do not specify either these, the final value in the command line list is the name of a server(s). </p>
<p> For a full list of operations run the tool with the option:</p>
<dt><code>&#8211;help</code></p>
<dd></dl>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Brian Aker, &lt;<i>brian [at] tangent.org</i>&gt; </p>
<p> Mark Atwood, &lt;<i>mark [at] fallenpegasus.com</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
