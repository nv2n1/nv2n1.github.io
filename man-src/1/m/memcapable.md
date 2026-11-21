---
title: "memcapable(1)"
name: "memcapable"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memcapable/"
description: "memcapable – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcapable &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> memcapable [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>memcapable</code> connects to the specified memcached server and tries to determine its capabilities by running the various commands and verifying the response.</p>
<h2>LIMITATIONS</h2>
<p> The current version of memcapable will only verify the binary protocol.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h hostname</code></dt>
<dd>
<p> Specify the hostname to connect to. The default is <i>localhost</i></p>
</dd><dt><code>-p port</code></dt>
<dd>
<p> Specify the port number to connect to. The default is <i>11211</i></p>
</dd><dt><code>-c</code></dt>
<dd>
<p> Generate a coredump when it detects an error from the server.</p>
</dd><dt><code>-v</code></dt>
<dd>
<p> Print out the comparison when it detects an error from the server.</p>
</dd><dt><code>-t n</code></dt>
<dd>
<p> Set the timeout from an IO operation to/from the server to <i>n</i> seconds.</dd></dl>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Trond Norbye, &lt;<i>trond.norbye [at] gmail.com</i>&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
