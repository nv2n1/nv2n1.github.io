---
title: "whisper-create(1)"
name: "whisper-create"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whisper-create/"
description: "whisper-create – create a whisper database"
---

<h2>NAME</h2>
<p> whisper-create &#8211; create a whisper database</p>
<h2>SYNOPSYS</h2>
<pre>
whisper-create path secondsPerPoint:pointsToStore [secondsPerPoint:pointsToStore]*
</pre>
<h2>DESCRIPTION</h2>
<p> This command creates a new whisper fixed-size database. For each database you specify one or more pairs of numbers describing how data points should be archived in this database. The first part of the pair is the precision, the second part of the pair is how many data points should be stored. You cannot configure two archives with the same precision inside a single database. Higher precision archives must evenly divide all lower precision archives&#8217; precision. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;overwrite</code></p>
<dd> Overwrite an existing database.</p>
<dt><code>&#8211;xFilesFactor</code></p>
<dd> The fraction of data points in a propagation interval that must have known values for a propagation to occur.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Elliot Murphy &lt;elliot [at] ubuntu.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
