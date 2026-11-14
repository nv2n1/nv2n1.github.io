---
title: "whisper-fill(1)"
name: "whisper-fill"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whisper-fill/"
description: "whisper-fill – copy missing metrics from src into dst"
---

<h2>NAME</h2>
<p> whisper-fill &#8211; copy missing metrics from src into dst</p>
<h2>SYNOPSYS</h2>
<pre>
whisper-fill src_path dst_path
</pre>
<h2>DESCRIPTION</h2>
<p> Copies data from src in dst, if missing. Unlike whisper-merge, don&#8217;t overwrite data that&#8217;s already present in the target file, but instead, only add the missing data (e.g. where the gaps in the target file are). Because no values are overwritten, no data or precision gets lost. Also, unlike whisper-merge, try to take the highest-precision archive to provide the data, instead of the one with the largest retention. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the embedded help.</dl>
<h2>AUTHOR</h2>
<p> <code>whisper</code> is a fixed size database, created by Chris Davis. </p>
<p> This manual page was written by Piotr Popieluch &lt;piotr1212 [at] gmail.com&gt;, for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
