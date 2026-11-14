---
title: "advzip(1)"
name: "advzip"
section: "1"
letter: "a"
url: "/docs/linux/man/1-advzip/"
description: "advzip – AdvanceCOMP ZIP Compression Utility"
---

<h2>NAME</h2>
<p> advzip &#8211; AdvanceCOMP ZIP Compression Utility</p>
<h2>SYNOPSIS</h2>
<p> advzip [-a, &#8211;add] [-x, &#8211;extract] [-l, &#8211;list] </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-z, &#8211;recompress] [-t, &#8211;test] [-0, &#8211;shrink-store]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-1, &#8211;shrink-fast] [-2, &#8211;shrink-normal] [-3, &#8211;shrink-extra]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-4, &#8211;shrink-insane] [-i, &#8211;iter N]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-k, &#8211;keep-file-time] [-p, &#8211;pedantic] [-q, &#8211;quiet]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-h, &#8211;help] [-V, &#8211;version] ARCHIVES&#8230; [FILES&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The main purpose of this utility is to recompress and test the zip archives to get the smallest possible size. </p>
<p> For recompression the 7-Zip (<a rel="nofollow" href="http://www.7-zip.com">www.7-zip.com</a>) Deflate implementation is used. This implementation generally gives 5-10% more compression than the zLib Deflate implementation. </p>
<p> For experimental purpose also the 7-Zip LZMA algorithm is available with the -N option. In this case, the generated zips WILL NOT BE USABLE by any other program. To make them usable you need to recompress them without the -N option. Generally this algorithm gives 10-20% more compression than the 7-Zip Deflate implementation.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;add ARCHIVE FILES&#8230;</code></p>
<dd> Create the specified archive with the specified files. You must specify only one archive.</p>
<dt><code>-x, &#8211;extract ARCHIVE</code></p>
<dd> Extract all the files on the specified archive. You must specify only one archive.</p>
<dt><code>-l, &#8211;list ARCHIVES&#8230;</code></p>
<dd> List the content of the specified archives.</p>
<dt><code>-z, &#8211;recompress ARCHIVES&#8230;</code></p>
<dd> Recompress the specified archives. If the -1, -2, -3, -4 options are specified, it&#8217;s used the smallest file choice from: the previous compressed data, the new compression and the uncompressed format. If the -0 option is specified the archive is always rewritten without any compression.</p>
<dt><code>-t, &#8211;test ARCHIVES&#8230;</code></p>
<dd> Test the specified archives. The tests may be extended with the -p option.</p>
<dt><code>-k, &#8211;keep-file-time</code></p>
<dd> When recompressing with -z keep the .zip file time.</p>
<dt><code>-p, &#8211;pedantic</code></p>
<dd> Be pedantic on the zip tests. If this flag is enabled some more extensive tests on the zip integrity are done. These tests are generally not done by other zip utilities.</p>
<dt><code>-0, &#8211;shrink-store</code></p>
<dd> Disable the compression. The file is only stored and not compressed. This option is very useful to expand the archives of .png and .mp3 files. These files are already compressed, trying to compress them another time is really a waste of time and resource.</p>
<dt><code>-1, &#8211;shrink-fast</code></p>
<dd> Set the compression level to &quot;fast&quot; using the zlib compressor.</p>
<dt><code>-2, &#8211;shrink-normal</code></p>
<dd> Set the compression level to &quot;normal&quot; using the 7z compressor. This is the default level of compression.</p>
<dt><code>-3, &#8211;shrink-extra</code></p>
<dd> Set the compression level to &quot;extra&quot; using the 7z compressor. You can define the compressor iterations with the -i, &#8211;iter option.</p>
<dt><code>-4, &#8211;shrink-insane</code></p>
<dd> Set the compression level to &quot;insane&quot; using the zopfli compressor. You can define the compressor iterations with the -i, &#8211;iter option.</p>
<dt><code>-i, &#8211;iter N</code></p>
<dd> Define an additional numer of iterations for the 7z and zopfli compressors for modes -3 and -4. More iterations usually give a better compression, but may require a lot more time. Try for example with 10, 15, 20, and so on.</dl>
<h2>COPYRIGHT</h2>
<p> This file is Copyright (C) 2002 Andrea Mazzoleni, Filipe Estima</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-advpng/">advpng</a>(1), <a href="/docs/linux/man/1-advmng/">advmng</a>(1), <a href="/docs/linux/man/1-advdef/">advdef</a>(1) </p>
<h2>Index</h2>
