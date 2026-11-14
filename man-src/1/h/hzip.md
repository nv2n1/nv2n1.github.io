---
title: "hzip(1)"
name: "hzip"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hzip/"
description: "hunzip – compress and encrypt dictionary files"
---

<h2 class="name">NAME</h2>
<p> hunzip &#8211; compress and encrypt dictionary files </p>
<h2>SYNOPSIS</h2>
<p> hzip [-h] [-P password] [file(s)]</p>
<h2>DESCRIPTION</h2>
<p> <i>hunzip</i> is a small utility for text file compression and encryption, especially for sorted dictionaries. &quot;hunspell filename&quot; creates the compressed file &quot;filename.hz&quot; without removing the original file. </p>
<p> The compression algorithm uses 16-bit Huffman encoding and line-oriented prefix-suffix compression. It has good compression ratio for huge sorted word lists.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display short help description.</p>
<dt><code>-P</p>
<dd> Encrypted compression by an arbitrary length password.</dl>
<p> </code></p>
<h2>SEE ALSO</h2>
<p> <code>hzip (1), <a href="/docs/linux/man/1-hunspell/">hunspell</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> László Németh. </p>
<h2>Index</h2>
