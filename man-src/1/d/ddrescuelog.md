---
title: "ddrescuelog(1)"
name: "ddrescuelog"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddrescuelog/"
description: "ddrescuelog – tool for ddrescue mapfiles"
---

<h2>NAME</h2>
<p> ddrescuelog &#8211; tool for ddrescue mapfiles</p>
<h2>SYNOPSIS</h2>
<p> <code>ddrescuelog</code> [<i>,options/</i>] <i>,mapfile/</i></p>
<h2>DESCRIPTION</h2>
<p> GNU ddrescuelog &#8211; Tool for ddrescue mapfiles. Manipulates ddrescue mapfiles, shows their contents, converts them to/from other formats, compares them, and tests rescue status. </p>
<p> NOTE: In versions of ddrescue prior to 1.20 the mapfile was called &#8216;logfile&#8217;. The format is the same; only the name has changed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-a</code>, <code>&#8211;change-types=</code>&lt;ot&gt;,&lt;nt&gt;</p>
<dd> change the block types of mapfile</p>
<dt><code>-A</code>, <code>&#8211;annotate-mapfile</code></p>
<dd> add comments with human-readable pos/sizes</p>
<dt><code>-b</code>, <code>&#8211;block-size=</code>&lt;bytes&gt;</p>
<dd> block size in bytes [default 512]</p>
<dt><code>-B</code>, <code>&#8211;binary-prefixes</code></p>
<dd> show binary multipliers in numbers [SI]</p>
<dt><code>-c</code>, <code>&#8211;create-mapfile[=</code>&lt;tt&gt;]</p>
<dd> create mapfile from list of blocks [+-]</p>
<dt><code>-C</code>, <code>&#8211;complete-mapfile[=</code>&lt;t&gt;]</p>
<dd> complete mapfile adding blocks of type t [?]</p>
<dt><code>-d</code>, <code>&#8211;delete-if-done</code></p>
<dd> delete the mapfile if rescue is finished</p>
<dt><code>-D</code>, <code>&#8211;done-status</code></p>
<dd> return 0 if rescue is finished</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> overwrite existing output files</p>
<dt><code>-i</code>, <code>&#8211;input-position=</code>&lt;bytes&gt;</p>
<dd> starting position of rescue domain [0]</p>
<dt><code>-l</code>, <code>&#8211;list-blocks=</code>&lt;types&gt;</p>
<dd> print block numbers of given types (?*/-+)</p>
<dt><code>-L</code>, <code>&#8211;loose-domain</code></p>
<dd> accept an incomplete domain mapfile</p>
<dt><code>-m</code>, <code>&#8211;domain-mapfile=</code>&lt;file&gt;</p>
<dd> restrict domain to finished blocks in file</p>
<dt><code>-n</code>, <code>&#8211;invert-mapfile</code></p>
<dd> invert block types (finished &lt;&#8211;&gt; others)</p>
<dt><code>-o</code>, <code>&#8211;output-position=</code>&lt;bytes&gt;</p>
<dd> starting position in output file [ipos]</p>
<dt><code>-p</code>, <code>&#8211;compare-mapfile=</code>&lt;file&gt;</p>
<dd> compare block types in domain of both files</p>
<dt><code>-P</code>, <code>&#8211;compare-as-domain=</code>&lt;file&gt;</p>
<dd> like <code>-p</code> but compare finished blocks only</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress all messages</p>
<dt><code>-s</code>, <code>&#8211;size=</code>&lt;bytes&gt;</p>
<dd> maximum size of rescue domain to be processed</p>
<dt><code>-t</code>, <code>&#8211;show-status</code></p>
<dd> show a summary of mapfile contents</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose (a 2nd <code>-v</code> gives more)</p>
<dt><code>-x</code>, <code>&#8211;xor-mapfile=</code>&lt;file&gt;</p>
<dd> XOR the finished blocks in file with mapfile</p>
<dt><code>-y</code>, <code>&#8211;and-mapfile=</code>&lt;file&gt;</p>
<dd> AND the finished blocks in file with mapfile</p>
<dt><code>-z</code>, <code>&#8211;or-mapfile=</code>&lt;file&gt;</p>
<dd> OR the finished blocks in file with mapfile</dl>
<p> Use &#8216;-&#8216; to read a mapfile from standard input or to write the mapfile created by &#8216;&#8211;create-mapfile&#8217; to standard output. Numbers may be in decimal, hexadecimal or octal, and may be followed by a multiplier: s = sectors, k = 1000, Ki = 1024, M = 10^6, Mi = 2^20, etc&#8230; </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (eg, bug) which caused ddrescuelog to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ddrescue [at] gnu.org<br />
 Ddrescue home page: <a rel="nofollow" href="http://www.gnu.org/software/ddrescue/ddrescue.html">http://www.gnu.org/software/ddrescue/ddrescue.html</a><br />
 General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2017 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
