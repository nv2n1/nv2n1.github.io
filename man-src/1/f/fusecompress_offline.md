---
title: "fusecompress_offline(1)"
name: "fusecompress_offline"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusecompress_offline/"
description: "fusecompress_offline – decompress or compress data without need to mount the compressed virtual filesystem"
---

<h2>NAME</h2>
<p> fusecompress_offline &#8211; decompress or compress data without need to mount the compressed virtual filesystem</p>
<h2>SYNOPSIS</h2>
<p> <code>fusecompress_offline</code> [-h] [-v] [-o OPTIONS] path</p>
<h2>DESCRIPTION</h2>
<p> If compression method is set the data will be compressed by required compression method. Files already compressed by a different compression method are recompressed to the required compression method. Files already compressed by the required compression method are left untouched. If compression method is not set (using -o fc_c) then file(s) are decompressed. </p>
<p> Path may be directory or file. Directories are processed recursively. </p>
<p> This allows you to, among other things, &quot;compress&quot; an existing folder (ex:) $ fusecompress_offline -o fc_c:lzma formerly_uncompressed_folder </p>
<p> and to &quot;decompress&quot; an existing compressed folder (ex:) </p>
<p> $ fusecompress_offline compressed_folder </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints help.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints version.</p>
<dt><code>-o, &#8211;options</code></p>
<dd>
<p> <code>fc_c:arg</code> set compression method (lzo/bzip2/zlib/lzma) (default:zlib) </p>
<p> <code>fc_b:arg</code> set size of the blocks in kilobytes (default:100) </p>
<p> <code>fc_d</code> run in debug mode </p>
<p> <code>fc_ma:arg1;arg2</code> files with passed mime types to be always not compressed </p>
<p> <code>fc_mr:arg1;arg2</code> files with passed mime types to be always compressed </p>
<p> Lzo is the fastest, bzip2 has high compression ratio, but it is the slowest, zlib is somewhere between them in terms of speed and compression ratio and lzma has highest compression ratio, it&#8217;s compression speed is better than bzip2 and decompression is fast. </p>
<p> Block size influences compression ratio. Bigger block size allows better compression ratio, but random access to data will be slower and memory requirements will be bigger. </p>
</dl>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Please refer to the &quot;COPYING&quot; file distributed with fusecompress for complete details.</p>
<h2>AUTHORS</h2>
<p> fusecompress_offline was written by Milan Svoboda &lt;milan.svoboda [at] centrum.cz&gt;.</p>
<h2>SEE ALSO</h2>
<p> fusecompress </p>
<h2>Index</h2>
