---
title: "rrdflushcached(1)"
name: "rrdflushcached"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdflushcached/"
description: "rrdflushcached – Flush the values for a spcific RRD file from memory."
---

<h2 class="name">NAME</h2>
<p> rrdflushcached &#8211; Flush the values for a spcific RRD file from memory. </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>flushcached</code> [<code>&#8211;daemon</code>&nbsp;<wbr><i>address</i>] <i>filename</i> [<i>filename</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flushcached</code> function connects to rrdcached, the <font SIZE="-1">RRD</font> caching daemon, and issues a &#8220;flush&#8221; command for the given files. The daemon will put the files to the head of the update queue so they are written &#8220;soon&#8221;. The status will be returned only after the files&#8217; pending updates have been written to disk.</p>
<dl>
<dt><i>filename</i></p>
<dd> The name(s) of the <font SIZE="-1"><code>RRD</code></font> file(s) that are to be written to disk.</p>
<dt><code>&#8211;daemon</code> <i>address</i></p>
<dd> Address of the rrdcached daemon. If not specified, the <font SIZE="-1">RRDCACHED_ADDRESS</font> environment variable must be set (see below). For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre>
 rrdtool flush --daemon unix:/var/run/rrdcached.sock /var/lib/rrd/foo.rrd
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool flushcached&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>AUTHOR</h2>
<p> Florian Forster &lt;octo at verplant.org&gt; </p>
<h2>Index</h2>
