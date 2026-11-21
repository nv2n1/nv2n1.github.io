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
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> display help</dd>
<dt><code>-d</code> <code>&#8211;decompress</code></dt>
<dd> force decompression</dd>
<dt><code>-z</code> <code>&#8211;compress</code></dt>
<dd> dorce compression</dd>
<dt><code>-L</code> <code>&#8211;license</code></dt>
<dd> display software license</dd>
<dt><code>-V</code> <code>&#8211;version</code></dt>
<dd> display version</dd>
<dt><code>-c</code> <code>&#8211;stdout</code></dt>
<dd> decompress to standard output</dd>
<dt><code>-f</code> <code>&#8211;force</code></dt>
<dd> force</dd>
<dt><code>-k</code> <code>&#8211;keep</code></dt>
<dd> keep input files</dd>
<dt><code>-s</code> <code>&#8211;sort</code></dt>
<dd> sort and remove duplicates before compressing</dd>
<dt><code>-S</code> <code>&#8211;nocwl</code></dt>
<dd> do not rename .wl suffix to .cwl (use .wl.pz instead)</dd>
<dt><code>-q</code> <code>&#8211;quiet</code></dt>
<dd> suppress all warnings</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Brian Nelson &lt;pyro [at] debian.org&gt; based on the output of help2man. Aspell is Copyright &#169; 2002 Kevin Atkinson. </p>
