---
title: "advdef(1)"
name: "advdef"
section: "1"
letter: "a"
url: "/docs/linux/man/1-advdef/"
description: "advdef – AdvanceCOMP Deflate Compression Utility"
---

<h2>NAME</h2>
<p> advdef &#8211; AdvanceCOMP Deflate Compression Utility</p>
<h2>SYNOPSIS</h2>
<p> advdef [-z, &#8211;recompress] [-0, &#8211;shrink-store] </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-1, &#8211;shrink-fast] [-2, &#8211;shrink-normal] [-3, &#8211;shrink-extra]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-4, &#8211;shrink-insane] [-i, &#8211;iter N]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-f, &#8211;force] [-q, &#8211;quiet]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-h, &#8211;help] [-V, &#8211;version] FILES&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The main purpose of this utility is to recompress the data present in the .png, .mng, .gz, .tgz and .svgz files. </p>
<p> The internal structure of the files isn&#8217;t changed. Only the compressed data is modified.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z, &#8211;recompress FILES&#8230;</code></p>
<dd> Recompress the specified files. If the -1, -2, -3, -4 options are specified it&#8217;s used the smallest file choice from the previous compressed data and the new compression. If the -0 option is specified the file is always rewritten without any compression.</p>
<dt><code>-0, &#8211;shrink-store</code></p>
<dd> Disable the compression. The file is only stored and not compressed. The file is always rewritten also if it&#8217;s bigger.</p>
<dt><code>-1, &#8211;shrink-fast</code></p>
<dd> Set the compression level to &quot;fast&quot; using the zlib compressor.</p>
<dt><code>-2, &#8211;shrink-normal</code></p>
<dd> Set the compression level to &quot;normal&quot; using the 7z compressor. This is the default level of compression.</p>
<dt><code>-3, &#8211;shrink-extra</code></p>
<dd> Set the compression level to &quot;extra&quot; using the 7z compressor. You can define the compressor iterations with the -i, &#8211;iter option.</p>
<dt><code>-4, &#8211;shrink-insane</code></p>
<dd> Set the compression level to &quot;insane&quot; using the zopfli compressor. You can define the compressor iterations with the -i, &#8211;iter option.</p>
<dt><code>-i, &#8211;iter N</code></p>
<dd> Define an additional numer of iterations for the 7z and zopfli compressors for modes -3 and -4. More iterations usually give a better compression, but may require a lot more time. Try for example with 10, 15, 20, and so on.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force the use of the new file also if it&#8217;s bigger.</dl>
<h2>LIMITATIONS</h2>
<p> The advdef program cannot be used to recompress huge files because it needs to allocate memory for both the complete compressed and uncompressed data.</p>
<h2>COPYRIGHT</h2>
<p> This file is Copyright (C) 2003, 2004 Andrea Mazzoleni</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-advpng/">advpng</a>(1), <a href="/docs/linux/man/1-advmng/">advmng</a>(1), <a href="/docs/linux/man/1-advzip/">advzip</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1), <a href="/docs/linux/man/1-bzip2/">bzip2</a>(1) </p>
<h2>Index</h2>
