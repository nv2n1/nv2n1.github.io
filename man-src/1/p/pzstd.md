---

title: "pzstd(1)"
name: "pzstd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pzstd/"
description: "PZSTD – parallelised Zstandard compression, al la pigz"
---

<p> PZSTD &#8211; parallelised Zstandard compression, al la pigz </p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> pzstd [args] [FILE(s)]</dd></dl>
<h3>Parallel ZSTD options:</h3>
<dl>
<dt><code>-p</code>, <code>&#8211;processes</code></dt>
<dd> # : number of threads to use for (de)compression (default:&lt;numcpus&gt;)</dd></dl>
<h3>ZSTD options:</h3>
<dl>
<dt>-#</dt>
<dd> : # compression level (1-19, default:&lt;numcpus&gt;)</dd>
<dt><code>-d</code>, <code>&#8211;decompress</code></dt>
<dd> : decompression</dd>
<dt><code>-o</code></dt>
<dd> file : result stored into `file` (only if 1 input file)</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> : overwrite output without prompting, (de)compress links</dd>
<dt><code>&#8211;rm</code></dt>
<dd> : remove source file(s) after successful (de)compression</dd>
<dt><code>-k</code>, <code>&#8211;keep</code></dt>
<dd> : preserve source file(s) (default)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> : display help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> : display version number and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> : verbose mode; specify multiple times to increase log level (default:2)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> : suppress warnings; specify twice to suppress errors too</dd>
<dt><code>-c</code>, <code>&#8211;stdout</code></dt>
<dd> : force write to standard output, even if it is the console</dd>
<dt><code>-r</code></dt>
<dd> : operate recursively on directories</dd>
<dt><code>&#8211;ultra</code></dt>
<dd> : enable levels beyond 19, up to 22 (requires more memory)</dd>
<dt><code>-C</code>, <code>&#8211;check</code></dt>
<dd> : integrity check (default)</dd>
<dt><code>&#8211;no-check</code></dt>
<dd> : no integrity check</dd>
<dt><code>-t</code>, <code>&#8211;test</code></dt>
<dd> : test compressed file integrity</dd>
<dt><code>&#8212;</code></dt>
<dd> : all arguments after &quot;&#8211;&quot; are treated as files </dd>
</dl>
