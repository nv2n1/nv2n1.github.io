---
title: "whisper-resize(1)"
name: "whisper-resize"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whisper-resize/"
description: "whisper-resize – resize a whisper database"
---

<h2>NAME</h2>
<p> whisper-resize &#8211; resize a whisper database</p>
<h2>SYNOPSYS</h2>
<pre>
whisper-resize path secondsPerPoint:pointsToStore [secondsPerPoint:pointsToStore]*
</pre>
<h2>DESCRIPTION</h2>
<p> This command resizes a whisper fixed-size database. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;force</code></dt>
<dd> Force a destructive change to an existing database.</dd>
<dt><code>&#8211;newfile</code></dt>
<dd> Create a new database file without removing the existing one.</dd>
<dt><code>&#8211;xFilesFactor</code></dt>
<dd> The fraction of data points in a propagation interval that must have known values for a propagation to occur.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show the embedded help.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Elliot Murphy &lt;elliot [at] ubuntu.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
