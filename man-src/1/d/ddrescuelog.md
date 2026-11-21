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
<p> <code>ddrescuelog</code> [<i>,options/</i>] <i>,mapfile/</i></p>
<p> GNU ddrescuelog &#8211; Tool for ddrescue mapfiles. Manipulates ddrescue mapfiles, shows their contents, converts them to/from other formats, compares them, and tests rescue status. </p>
<p> NOTE: In versions of ddrescue prior to 1.20 the mapfile was called &#8216;logfile&#8217;. The format is the same; only the name has changed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-a</code>, <code>&#8211;change-types=</code>&lt;ot&gt;,&lt;nt&gt;</dt>
<dd> change the block types of mapfile</dd>
<dt><code>-A</code>, <code>&#8211;annotate-mapfile</code></dt>
<dd> add comments with human-readable pos/sizes</dd>
<dt><code>-b</code>, <code>&#8211;block-size=</code>&lt;bytes&gt;</dt>
<dd> block size in bytes [default 512]</dd>
<dt><code>-B</code>, <code>&#8211;binary-prefixes</code></dt>
<dd> show binary multipliers in numbers [SI]</dd>
<dt><code>-c</code>, <code>&#8211;create-mapfile[=</code>&lt;tt&gt;]</dt>
<dd> create mapfile from list of blocks [+-]</dd>
<dt><code>-C</code>, <code>&#8211;complete-mapfile[=</code>&lt;t&gt;]</dt>
<dd> complete mapfile adding blocks of type t [?]</dd>
<dt><code>-d</code>, <code>&#8211;delete-if-done</code></dt>
<dd> delete the mapfile if rescue is finished</dd>
<dt><code>-D</code>, <code>&#8211;done-status</code></dt>
<dd> return 0 if rescue is finished</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> overwrite existing output files</dd>
<dt><code>-i</code>, <code>&#8211;input-position=</code>&lt;bytes&gt;</dt>
<dd> starting position of rescue domain [0]</dd>
<dt><code>-l</code>, <code>&#8211;list-blocks=</code>&lt;types&gt;</dt>
<dd> print block numbers of given types (?*/-+)</dd>
<dt><code>-L</code>, <code>&#8211;loose-domain</code></dt>
<dd> accept an incomplete domain mapfile</dd>
<dt><code>-m</code>, <code>&#8211;domain-mapfile=</code>&lt;file&gt;</dt>
<dd> restrict domain to finished blocks in file</dd>
<dt><code>-n</code>, <code>&#8211;invert-mapfile</code></dt>
<dd> invert block types (finished &lt;&#8211;&gt; others)</dd>
<dt><code>-o</code>, <code>&#8211;output-position=</code>&lt;bytes&gt;</dt>
<dd> starting position in output file [ipos]</dd>
<dt><code>-p</code>, <code>&#8211;compare-mapfile=</code>&lt;file&gt;</dt>
<dd> compare block types in domain of both files</dd>
<dt><code>-P</code>, <code>&#8211;compare-as-domain=</code>&lt;file&gt;</dt>
<dd> like <code>-p</code> but compare finished blocks only</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress all messages</dd>
<dt><code>-s</code>, <code>&#8211;size=</code>&lt;bytes&gt;</dt>
<dd> maximum size of rescue domain to be processed</dd>
<dt><code>-t</code>, <code>&#8211;show-status</code></dt>
<dd> show a summary of mapfile contents</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose (a 2nd <code>-v</code> gives more)</dd>
<dt><code>-x</code>, <code>&#8211;xor-mapfile=</code>&lt;file&gt;</dt>
<dd> XOR the finished blocks in file with mapfile</dd>
<dt><code>-y</code>, <code>&#8211;and-mapfile=</code>&lt;file&gt;</dt>
<dd> AND the finished blocks in file with mapfile</dd>
<dt><code>-z</code>, <code>&#8211;or-mapfile=</code>&lt;file&gt;</dt>
<dd> OR the finished blocks in file with mapfile</dd></dl>
<p> Use &#8216;-&#8216; to read a mapfile from standard input or to write the mapfile created by &#8216;&#8211;create-mapfile&#8217; to standard output. Numbers may be in decimal, hexadecimal or octal, and may be followed by a multiplier: s = sectors, k = 1000, Ki = 1024, M = 10^6, Mi = 2^20, etc&#8230; </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (eg, bug) which caused ddrescuelog to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ddrescue [at] gnu.org<br />
 Ddrescue home page: <a rel="nofollow" href="http://www.gnu.org/software/ddrescue/ddrescue.html">http://www.gnu.org/software/ddrescue/ddrescue.html</a><br />
 General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2017 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
