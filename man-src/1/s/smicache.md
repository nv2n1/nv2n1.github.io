---
title: "smicache(1)"
name: "smicache"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smicache/"
description: "smicache – caching method for use with libsmi"
---

<h2>NAME</h2>
<p> smicache &#8211; caching method for use with libsmi</p>
<h2>SYNOPSIS</h2>
<p> <code>smicache</code> [ <code>-Vh</code> ] [ <code>-d </code><i>dir</i> ] [ <code>-p </code><i>prefix</i> ] [ <i>mib</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>smicache</code> program can be used by libsmi to fetch MIB modules that cannot be found in regular local MIB directories.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Show the smicache version and exit.</p>
<dt><code>-h</code></p>
<dd> Show a help text and exit.</p>
<dt><code>-d </code><i>dir</i></p>
<dd> Write fetched module file(s) to directory <i>dir</i>.</p>
<dt><code>-p </code><i>prefix</i></p>
<dd> Use the URL prefix <i>prefix</i> for fetching modules.</p>
<dt><i>mib</i></p>
<dd> The MIB module to be fetched.</dl>
<p> Note that <code>smicache</code> is just a very simple script that builds on the wget program to retrieve files from URLs. It does not handle the file attributes of retrieved modules in any special way, so that you have to care about permissions in multi-user environments.</p>
<h2>EXAMPLE</h2>
<p> <code>Smicache</code> can be used by putting the following line into the global configuration file: </p>
<pre>
  cache /usr/local/share/mibs/cache \
    /usr/local/bin/smicache \
    -d /usr/local/share/mibs/cache \
    -p <a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/smicache/">http://www.ibr.cs.tu-bs.de/projects/libsmi/smicache/</a>
</pre>
<p> You might want to chmod 1777 /usr/local/share/mibs/cache.</p>
<h2>SEE ALSO</h2>
<p> The <code><a href="/docs/linux/man/3-libsmi/">libsmi</a></code>(3) project is documented at <code><a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/">http://www.ibr.cs.tu-bs.de/projects/libsmi/</a></code>. </p>
<p> <code><a href="/docs/linux/man/1-smilint/">smilint</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> (C) 2001-2004 Frank Strauss, TU Braunschweig, Germany &lt;strauss [at] ibr.cs.tu-bs.de&gt; </p>
<h2>Index</h2>
