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
<p> This command retrieves records from a whisper fixed-size database. </p>
<p> The options are described below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;from</code></dt>
<dd> Unix epoch time of the beginning of your requested interval (default: 24 hours ago).</dd>
<dt><code>&#8211;until</code></dt>
<dd> Unix epoch time of the end of your requested interval (default: now).</dd>
<dt><code>&#8211;json</code></dt>
<dd> Output results in JSON form.</dd>
<dt><code>&#8211;pretty</code></dt>
<dd> Show human-readable timestamps instead of unix times.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show the embedded help.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Elliot Murphy &lt;elliot [at] ubuntu.com&gt;, for the Debian project (but may be used by others). </p>
