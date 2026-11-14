---
title: "precat(1)"
name: "precat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-precat/"
description: "prezip, preunzip, precat – prefix delta compressor for Aspell"
---

<h2 class="name">NAME</h2>
<p> prezip, preunzip, precat &#8211; prefix delta compressor for Aspell </p>
<h2>SYNOPSIS</h2>
<p> precat [-dzhLV] [-cfksSq] [file &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>prezip</code> is a a prefix delta compressor. It is <i>not</i> a general purpose compressor and should only be used on sorted word lists or other similar text files. It will likely <i>increase</i> the size of binary data. </p>
<p> If invoked as <code>prezip,</code> the default action is to compress. If invoked as <code>preunzip,</code> the default action is to decompress. If invoked as <code>precat,</code> the default action is to decompress to stdout. </p>
<p> If no file names are given then <code>prezip</code> will compress or decompress from the standard input to the standard output. Short flags can be combined so that &quot;-c <code>-s</code>&quot; is the same as &quot;-cs&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display help</p>
<dt><code>-d</code> <code>&#8211;decompress</code></p>
<dd> force decompression</p>
<dt><code>-z</code> <code>&#8211;compress</code></p>
<dd> dorce compression</p>
<dt><code>-L</code> <code>&#8211;license</code></p>
<dd> display software license</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-c</code> <code>&#8211;stdout</code></p>
<dd> decompress to standard output</p>
<dt><code>-f</code> <code>&#8211;force</code></p>
<dd> force</p>
<dt><code>-k</code> <code>&#8211;keep</code></p>
<dd> keep input files</p>
<dt><code>-s</code> <code>&#8211;sort</code></p>
<dd> sort and remove duplicates before compressing</p>
<dt><code>-S</code> <code>&#8211;nocwl</code></p>
<dd> do not rename .wl suffix to .cwl (use .wl.pz instead)</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> suppress all warnings</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Brian Nelson &lt;pyro [at] debian.org&gt; based on the output of help2man. Aspell is Copyright &#169; 2002 Kevin Atkinson. </p>
<h2>Index</h2>
