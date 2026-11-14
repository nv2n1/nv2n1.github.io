---
title: "pzstd(1)"
name: "pzstd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pzstd/"
description: "PZSTD – parallelised Zstandard compression, al la pigz"
---

<h2 class="name">NAME</h2>
<p> PZSTD &#8211; parallelised Zstandard compression, al la pigz </p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> pzstd [args] [FILE(s)]</dl>
<h3>Parallel ZSTD options:</h3>
<dl>
<dt><code>-p</code>, <code>&#8211;processes</code></p>
<dd> # : number of threads to use for (de)compression (default:&lt;numcpus&gt;)</dl>
<h3>ZSTD options:</h3>
<dl>
<dt>-#</p>
<dd> : # compression level (1-19, default:&lt;numcpus&gt;)</p>
<dt><code>-d</code>, <code>&#8211;decompress</code></p>
<dd> : decompression</p>
<dt><code>-o</code></p>
<dd> file : result stored into `file` (only if 1 input file)</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> : overwrite output without prompting, (de)compress links</p>
<dt><code>&#8211;rm</code></p>
<dd> : remove source file(s) after successful (de)compression</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> : preserve source file(s) (default)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> : display help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> : display version number and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> : verbose mode; specify multiple times to increase log level (default:2)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> : suppress warnings; specify twice to suppress errors too</p>
<dt><code>-c</code>, <code>&#8211;stdout</code></p>
<dd> : force write to standard output, even if it is the console</p>
<dt><code>-r</code></p>
<dd> : operate recursively on directories</p>
<dt><code>&#8211;ultra</code></p>
<dd> : enable levels beyond 19, up to 22 (requires more memory)</p>
<dt><code>-C</code>, <code>&#8211;check</code></p>
<dd> : integrity check (default)</p>
<dt><code>&#8211;no-check</code></p>
<dd> : no integrity check</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> : test compressed file integrity</p>
<dt><code>&#8212;</code></p>
<dd> : all arguments after &quot;&#8211;&quot; are treated as files </p>
</dl>
<h2>Index</h2>
