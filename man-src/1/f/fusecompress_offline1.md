---
title: "fusecompress_offline1(1)"
name: "fusecompress_offline1"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusecompress_offline1/"
description: "fusecompress_offline – decompress or compress data without need to mount the compressed virtual filesystem"
---

<h2>NAME</h2>
<p> fusecompress_offline &#8211; decompress or compress data without need to mount the compressed virtual filesystem</p>
<h2>SYNOPSIS</h2>
<p> <code>fusecompress_offline</code> [-h] [-v] [-c TYPE] [-b SIZE] targetDir</p>
<h2>DESCRIPTION</h2>
<p> fusecompress_offline decompress or compress data without need to mount the compressed virtual filesystem. It works like the tar or zip programs. </p>
<p> If -c is set the data will be compressed by required compression method. Files already compressed by a different compression method are recompressed to required compression method. Files already compressed by the required compression method are left untouched. </p>
<p> targetDir may be a single file or a directory. In the latter case the directory will be processed recursively and all found files are processed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Prints help.</p>
<dt><code>-v</code></p>
<dd> Prints version.</p>
<dt><code>-c [lzo|bz2|gz|none]</code></p>
<dd> Sets the default compression method. Lzo, bz2 and gz are supported at this time. Lzo is the fastest, bz2 has the highest compression ratio, but it is the slowest and the gz is somewhere between them in terms of speed and compression ratio. The none compression method is there for testing only as it doesn&#8217;t compress data, it copies the data without any modification (fusecompress&#8217; header is added). </p>
<p> If this option is not set, fusecompress_offline decompress the data.</p>
<dt><code>-b SIZE</code></p>
<dd> Sets the block size. The vaule is in kilobytes. Bigger block size allows better compression ratio, but random access to data will be slower and memory requirements will be bigger. </p>
<p> If this option is not set, the block size is set to 100KiB.</p>
<dt><code>-f EXT1,EXT2,EXT3,&#8230;</code></p>
<dd> Files with listed extensions will be always compressed. Usable when you want to compress files like *.avi, *.pdf, etc&#8230;</dl>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Please refer to the &quot;COPYING&quot; file distributed with fusecompress for complete details.</p>
<h2>AUTHORS</h2>
<p> fusecompress_offline was written by Milan Svoboda &lt;milan.svoboda [at] centrum.cz&gt;.</p>
<h2>SEE ALSO</h2>
<p> fusecompress </p>
<h2>Index</h2>
