---
title: "rrd2whisper(1)"
name: "rrd2whisper"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrd2whisper/"
description: "rrd2whisper – convert an RRD database to a whisper database"
---

<h2>NAME</h2>
<p> rrd2whisper &#8211; convert an RRD database to a whisper database</p>
<h2>SYNOPSYS</h2>
<pre>
wrrd2whisper rrd_path
</pre>
<h2>DESCRIPTION</h2>
<p> This command converts an RRD database to a whisper fixed-size database. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;xFilesFactor</code></p>
<dd> The fraction of data points in a propagation interval that must have known values for a propagation to occur.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Elliot Murphy &lt;elliot [at] ubuntu.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
