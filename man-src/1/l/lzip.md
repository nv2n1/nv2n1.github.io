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
<p> <code>lzip</code> [<i>,options/</i>] [<i>,files/</i>]</p>
<p> Lzip &#8211; LZMA lossless data compressor.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-a</code>, <code>&#8211;trailing-error</code></dt>
<dd> exit with error status if trailing data</dd>
<dt><code>-b</code>, <code>&#8211;member-size=</code>&lt;bytes&gt;</dt>
<dd> set member size limit in bytes</dd>
<dt><code>-c</code>, <code>&#8211;stdout</code></dt>
<dd> write to standard output, keep input files</dd>
<dt><code>-d</code>, <code>&#8211;decompress</code></dt>
<dd> decompress</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> overwrite existing output files</dd>
<dt><code>-F</code>, <code>&#8211;recompress</code></dt>
<dd> force re-compression of compressed files</dd>
<dt><code>-k</code>, <code>&#8211;keep</code></dt>
<dd> keep (don&#8217;t delete) input files</dd>
<dt><code>-m</code>, <code>&#8211;match-length=</code>&lt;bytes&gt;</dt>
<dd> set match length limit in bytes [36]</dd>
<dt><code>-o</code>, <code>&#8211;output=</code>&lt;file&gt;</dt>
<dd> if reading standard input, write to &lt;file&gt;</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress all messages</dd>
<dt><code>-s</code>, <code>&#8211;dictionary-size=</code>&lt;bytes&gt;</dt>
<dd> set dictionary size limit in bytes [8 MiB]</dd>
<dt><code>-S</code>, <code>&#8211;volume-size=</code>&lt;bytes&gt;</dt>
<dd> set volume size limit in bytes</dd>
<dt><code>-t</code>, <code>&#8211;test</code></dt>
<dd> test compressed file integrity</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose (a 2nd <code>-v</code> gives more)</dd>
<dt><code>-0</code> .. <code>-9</code></dt>
<dd> set compression level [default 6]</dd>
<dt><code>&#8211;fast</code></dt>
<dd> alias for <code>-0</code></dd>
<dt><code>&#8211;best</code></dt>
<dd> alias for <code>-9</code></dd></dl>
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
</dt><dd> <code>info lzip</code></dd></dl>
<p> should give you access to the complete manual. </p>
