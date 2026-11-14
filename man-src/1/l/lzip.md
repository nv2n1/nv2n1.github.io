---
title: "lzip(1)"
name: "lzip"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzip/"
description: "lzip – reduces the size of files"
---

<h2>NAME</h2>
<p> lzip &#8211; reduces the size of files</p>
<h2>SYNOPSIS</h2>
<p> <code>lzip</code> [<i>,options/</i>] [<i>,files/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Lzip &#8211; LZMA lossless data compressor.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-a</code>, <code>&#8211;trailing-error</code></p>
<dd> exit with error status if trailing data</p>
<dt><code>-b</code>, <code>&#8211;member-size=</code>&lt;bytes&gt;</p>
<dd> set member size limit in bytes</p>
<dt><code>-c</code>, <code>&#8211;stdout</code></p>
<dd> write to standard output, keep input files</p>
<dt><code>-d</code>, <code>&#8211;decompress</code></p>
<dd> decompress</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> overwrite existing output files</p>
<dt><code>-F</code>, <code>&#8211;recompress</code></p>
<dd> force re-compression of compressed files</p>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> keep (don&#8217;t delete) input files</p>
<dt><code>-m</code>, <code>&#8211;match-length=</code>&lt;bytes&gt;</p>
<dd> set match length limit in bytes [36]</p>
<dt><code>-o</code>, <code>&#8211;output=</code>&lt;file&gt;</p>
<dd> if reading standard input, write to &lt;file&gt;</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress all messages</p>
<dt><code>-s</code>, <code>&#8211;dictionary-size=</code>&lt;bytes&gt;</p>
<dd> set dictionary size limit in bytes [8 MiB]</p>
<dt><code>-S</code>, <code>&#8211;volume-size=</code>&lt;bytes&gt;</p>
<dd> set volume size limit in bytes</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd> test compressed file integrity</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose (a 2nd <code>-v</code> gives more)</p>
<dt><code>-0</code> .. <code>-9</code></p>
<dd> set compression level [default 6]</p>
<dt><code>&#8211;fast</code></p>
<dd> alias for <code>-0</code></p>
<dt><code>&#8211;best</code></p>
<dd> alias for <code>-9</code></dl>
<p> If no file names are given, or if a file is &#8216;-&#8216;, lzip compresses or decompresses from standard input to standard output. Numbers may be followed by a multiplier: k = kB = 10^3 = 1000, Ki = KiB = 2^10 = 1024, M = 10^6, Mi = 2^20, G = 10^9, Gi = 2^30, etc&#8230; Dictionary sizes 12 to 29 are interpreted as powers of two, meaning 2^12 to 2^29 bytes. </p>
<p> The bidimensional parameter space of LZMA can&#8217;t be mapped to a linear scale optimal for all files. If your files are large, very repetitive, etc, you may need to use the <code>&#8211;dictionary-size</code> and <code>&#8211;match-length</code> options directly to achieve optimal performance. </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (eg, bug) which caused lzip to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to lzip-bug [at] nongnu.org<br />
 Lzip home page: <a rel="nofollow" href="http://www.nongnu.org/lzip/lzip.html">http://www.nongnu.org/lzip/lzip.html</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>lzip</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>lzip</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info lzip</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
