---

title: "lziprecover(1)"
name: "lziprecover"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lziprecover/"
description: "lziprecover – recovers data from damaged lzip files"
---

<h2>NAME</h2>
<p> lziprecover &#8211; recovers data from damaged lzip files</p>
<p> <code>lziprecover</code> [<i>,options/</i>] [<i>,files/</i>]</p>
<p> Lziprecover &#8211; Data recovery tool and decompressor for the lzip format. </p>
<p> Lziprecover can repair perfectly most files with small errors (up to one single-byte error per member), without the need of any extra redundance at all. Losing an entire archive just because of a corrupt byte near the beginning is a thing of the past. </p>
<p> Lziprecover can also produce a correct file by merging the good parts of two or more damaged copies, extract data from damaged files, decompress files and test integrity of files. </p>
<p> Lziprecover is not a replacement for regular backups, but a last line of defense for the case where the backups are also damaged.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-a</code>, <code>&#8211;trailing-error</code></dt>
<dd> exit with error status if trailing data</dd>
<dt><code>-A</code>, <code>&#8211;alone-to-lz</code></dt>
<dd> convert lzma-alone files to lzip format</dd>
<dt><code>-c</code>, <code>&#8211;stdout</code></dt>
<dd> write to standard output, keep input files</dd>
<dt><code>-d</code>, <code>&#8211;decompress</code></dt>
<dd> decompress</dd>
<dt><code>-D</code>, <code>&#8211;range-decompress=</code>&lt;range&gt;</dt>
<dd> decompress a range of bytes (N-M) to stdout</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> overwrite existing output files</dd>
<dt><code>-i</code>, <code>&#8211;ignore-errors</code></dt>
<dd> make &#8216;&#8211;range-decompress&#8217; ignore data errors</dd>
<dt><code>-k</code>, <code>&#8211;keep</code></dt>
<dd> keep (don&#8217;t delete) input files</dd>
<dt><code>-l</code>, <code>&#8211;list</code></dt>
<dd> print total file sizes and ratios</dd>
<dt><code>-m</code>, <code>&#8211;merge</code></dt>
<dd> correct errors in file using several copies</dd>
<dt><code>-o</code>, <code>&#8211;output=</code>&lt;file&gt;</dt>
<dd> place the output into &lt;file&gt;</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress all messages</dd>
<dt><code>-R</code>, <code>&#8211;repair</code></dt>
<dd> try to repair a small error in file</dd>
<dt><code>-s</code>, <code>&#8211;split</code></dt>
<dd> split multimember file in single-member files</dd>
<dt><code>-t</code>, <code>&#8211;test</code></dt>
<dd> test compressed file integrity</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose (a 2nd <code>-v</code> gives more)</dd></dl>
<p> If no file names are given, or if a file is &#8216;-&#8216;, lziprecover decompresses from standard input to standard output. Numbers may be followed by a multiplier: k = kB = 10^3 = 1000, Ki = KiB = 2^10 = 1024, M = 10^6, Mi = 2^20, G = 10^9, Gi = 2^30, etc&#8230; </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (eg, bug) which caused lziprecover to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to lzip-bug [at] nongnu.org<br />
 Lziprecover home page: <a rel="nofollow" href="http://www.nongnu.org/lzip/lziprecover.html">http://www.nongnu.org/lzip/lziprecover.html</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>lziprecover</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>lziprecover</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info lziprecover</code></dd></dl>
<p> should give you access to the complete manual. </p>
