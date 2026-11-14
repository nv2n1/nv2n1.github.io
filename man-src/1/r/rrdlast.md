---
title: "rrdlast(1)"
name: "rrdlast"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdlast/"
description: "rrdlast – Return the date of the last data sample in an RRD"
---

<h2 class="name">NAME</h2>
<p> rrdlast &#8211; Return the date of the last data sample in an RRD </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>last</code> <i>filename</i> [<code>&#8211;daemon</code>&nbsp;<wbr><i>address</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>last</code> function returns the <font SIZE="-1">UNIX</font> timestamp of the most recent update of the <font SIZE="-1">RRD</font>.</p>
<dl>
<dt><i>filename</i></p>
<dd> The name of the <font SIZE="-1"><code>RRD</code></font> that contains the data.</p>
<dt><code>&#8211;daemon</code> <i>address</i></p>
<dd> Address of the rrdcached daemon. If specified, a <tt>&quot;flush&quot;</tt> command is sent to the server before reading the <font SIZE="-1">RRD</font> files. This allows <code>rrdtool</code> to return fresh data even if the daemon is configured to cache values for a long time. For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre>
 rrdtool last --daemon unix:/var/run/rrdcached.sock /var/lib/rrd/foo.rrd
</pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool last&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>AUTHOR</h2>
<p> Russ Wright &lt;rwwright [at] home.com&gt; </p>
<h2>Index</h2>
