---

title: "du(1)"
name: "du"
section: "1"
letter: "d"
url: "/docs/linux/man/1-du/"
description: "du – estimate file space usage"
---

<p> <code>du</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;<br />
 <code>du</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;files0-from=F/</i></p>
<p> Summarize disk usage of the set of FILEs, recursively for directories. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-0</code>, <code>&#8211;null</code></dt>
<dd> end each output line with NUL, not newline</dd>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> write counts for all files, not just directories</dd>
<dt><code>&#8211;apparent-size</code></dt>
<dd> print apparent sizes, rather than disk usage; although the apparent size is usually smaller, it may be larger due to holes in (&#8216;sparse&#8217;) files, internal fragmentation, indirect blocks, and the like</dd>
<dt><code>-B</code>, <code>&#8211;block-size</code>=<i>,SIZE/</i></dt>
<dd> scale sizes by SIZE before printing them; e.g., &#8216;-BM&#8217; prints sizes in units of 1,048,576 bytes; see SIZE format below</dd>
<dt><code>-b</code>, <code>&#8211;bytes</code></dt>
<dd> equivalent to &#8216;&#8211;apparent-size <code>&#8211;block-size</code>=<i>,1/</i>&#8216;</dd>
<dt><code>-c</code>, <code>&#8211;total</code></dt>
<dd> produce a grand total</dd>
<dt><code>-D</code>, <code>&#8211;dereference-args</code></dt>
<dd> dereference only symlinks that are listed on the command line</dd>
<dt><code>-d</code>, <code>&#8211;max-depth</code>=<i>,N/</i></dt>
<dd> print the total for a directory (or file, with <code>&#8211;all</code>) only if it is N or fewer levels below the command line argument; <code>&#8211;max-depth</code>=<i>,0/</i> is the same as <code>&#8211;summarize</code></dd>
<dt><code>&#8211;files0-from</code>=<i>,F/</i></dt>
<dd> summarize disk usage of the NUL-terminated file names specified in file F; if F is -, then read names from standard input</dd>
<dt><code>-H</code></dt>
<dd> equivalent to <code>&#8211;dereference-args</code> (<code>-D</code>)</dd>
<dt><code>-h</code>, <code>&#8211;human-readable</code></dt>
<dd> print sizes in human readable format (e.g., 1K 234M 2G)</dd>
<dt><code>&#8211;inodes</code></dt>
<dd> list inode usage information instead of block usage</dd>
<dt><code>-k</code></dt>
<dd> like <code>&#8211;block-size</code>=<i>,1K/</i></dd>
<dt><code>-L</code>, <code>&#8211;dereference</code></dt>
<dd> dereference all symbolic links</dd>
<dt><code>-l</code>, <code>&#8211;count-links</code></dt>
<dd> count sizes many times if hard linked</dd>
<dt><code>-m</code></dt>
<dd> like <code>&#8211;block-size</code>=<i>,1M/</i></dd>
<dt><code>-P</code>, <code>&#8211;no-dereference</code></dt>
<dd> don&#8217;t follow any symbolic links (this is the default)</dd>
<dt><code>-S</code>, <code>&#8211;separate-dirs</code></dt>
<dd> for directories do not include size of subdirectories</dd>
<dt><code>&#8211;si</code></dt>
<dd> like <code>-h</code>, but use powers of 1000 not 1024</dd>
<dt><code>-s</code>, <code>&#8211;summarize</code></dt>
<dd> display only a total for each argument</dd>
<dt><code>-t</code>, <code>&#8211;threshold</code>=<i>,SIZE/</i></dt>
<dd> exclude entries smaller than SIZE if positive, or entries greater than SIZE if negative</dd>
<dt><code>&#8211;time</code></dt>
<dd> show time of the last modification of any file in the directory, or any of its subdirectories</dd>
<dt><code>&#8211;time</code>=<i>,WORD/</i></dt>
<dd> show time as WORD instead of modification time: atime, access, use, ctime or status</dd>
<dt><code>&#8211;time-style</code>=<i>,STYLE/</i></dt>
<dd> show times using STYLE, which can be: full-iso, long-iso, iso, or +FORMAT; FORMAT is interpreted like in &#8216;date&#8217;</dd>
<dt><code>-X</code>, <code>&#8211;exclude-from</code>=<i>,FILE/</i></dt>
<dd> exclude files that match any pattern in FILE</dd>
<dt><code>&#8211;exclude</code>=<i>,PATTERN/</i></dt>
<dd> exclude files that match PATTERN</dd>
<dt><code>-x</code>, <code>&#8211;one-file-system</code></dt>
<dd> skip directories on different file systems</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> Display values are in units of the first available SIZE from <code>&#8211;block-size</code>, and the DU_BLOCK_SIZE, BLOCK_SIZE and BLOCKSIZE environment variables. Otherwise, units default to 1024 bytes (or 512 if POSIXLY_CORRECT is set). </p>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,&#8230; (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on.</p>
<h2>PATTERNS</h2>
<p> PATTERN is a shell pattern (not a regular expression). The pattern <code>?</code> matches any one character, whereas <code>*</code> matches any string (composed of zero, one or multiple characters). For example, <code>*.o</code> will match any files whose names end in <code>.o</code>. Therefore, the command</p>
<dl>
<dt>
</dt><dd> <code>du &#8211;exclude=&#8217;*.o&#8217;</code></dd></dl>
<p> will skip all files and subdirectories ending in <code>.o</code> (including the file <code>.o</code> itself).</p>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund, David MacKenzie, Paul Eggert, and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/du">https://www.gnu.org/software/coreutils/du</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) du invocation&#8217; </p>
