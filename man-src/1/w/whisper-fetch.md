---
title: "whisper-fetch(1)"
name: "whisper-fetch"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whisper-fetch/"
description: "whisper-fetch – extract records from a whisper database"
---

<h2>NAME</h2>
<p> whisper-fetch &#8211; extract records from a whisper database</p>
<h2>SYNOPSYS</h2>
<pre>
whisper-fetch [options] path
</pre>
<h2>DESCRIPTION</h2>
<p> This command retrieves records from a whisper fixed-size database. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;from</code></p>
<dd> Unix epoch time of the beginning of your requested interval (default: 24 hours ago).</p>
<dt><code>&#8211;until</code></p>
<dd> Unix epoch time of the end of your requested interval (default: now).</p>
<dt><code>&#8211;json</code></p>
<dd> Output results in JSON form.</p>
<dt><code>&#8211;pretty</code></p>
<dd> Show human-readable timestamps instead of unix times.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Elliot Murphy &lt;elliot [at] ubuntu.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
