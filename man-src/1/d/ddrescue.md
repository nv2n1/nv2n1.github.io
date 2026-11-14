---
title: "ddrescue(1)"
name: "ddrescue"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddrescue/"
description: "ddrescue – data recovery tool"
---

<h2>NAME</h2>
<p> ddrescue &#8211; data recovery tool</p>
<h2>SYNOPSIS</h2>
<p> <code>ddrescue</code> [<i>,options/</i>] <i>,infile outfile /</i>[<i>,mapfile/</i>]</p>
<h2>DESCRIPTION</h2>
<p> GNU ddrescue &#8211; Data recovery tool. Copies data from one file or block device to another, trying to rescue the good parts first in case of read errors. </p>
<p> Always use a mapfile unless you know you won&#8217;t need it. Without a mapfile, ddrescue can&#8217;t resume a rescue, only reinitiate it. NOTE: In versions of ddrescue prior to 1.20 the mapfile was called &#8216;logfile&#8217;. The format is the same; only the name has changed. </p>
<p> If you reboot, check the device names before restarting ddrescue. Don&#8217;t use options &#8216;-F&#8217; or &#8216;-G&#8217; without reading the manual first.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-a</code>, <code>&#8211;min-read-rate=</code>&lt;bytes&gt;</p>
<dd> minimum read rate of good areas in bytes/s</p>
<dt><code>-A</code>, <code>&#8211;try-again</code></p>
<dd> mark non-trimmed, non-scraped as non-tried</p>
<dt><code>-b</code>, <code>&#8211;sector-size=</code>&lt;bytes&gt;</p>
<dd> sector size of input device [default 512]</p>
<dt><code>-B</code>, <code>&#8211;binary-prefixes</code></p>
<dd> show binary multipliers in numbers [SI]</p>
<dt><code>-c</code>, <code>&#8211;cluster-size=</code>&lt;sectors&gt;</p>
<dd> sectors to copy at a time [128]</p>
<dt><code>-C</code>, <code>&#8211;complete-only</code></p>
<dd> don&#8217;t read new data beyond mapfile limits</p>
<dt><code>-d</code>, <code>&#8211;idirect</code></p>
<dd> use direct disc access for input file</p>
<dt><code>-D</code>, <code>&#8211;odirect</code></p>
<dd> use direct disc access for output file</p>
<dt><code>-e</code>, <code>&#8211;max-bad-areas</code>=<i>,[/</i>+]&lt;n&gt;</p>
<dd> maximum number of [new] bad areas allowed</p>
<dt><code>-E</code>, <code>&#8211;max-error-rate=</code>&lt;bytes&gt;</p>
<dd> maximum allowed rate of read errors per second</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> overwrite output device or partition</p>
<dt><code>-F</code>, <code>&#8211;fill-mode=</code>&lt;types&gt;</p>
<dd> fill blocks of given types with data (?*/-+l)</p>
<dt><code>-G</code>, <code>&#8211;generate-mode</code></p>
<dd> generate approximate mapfile from partial copy</p>
<dt><code>-H</code>, <code>&#8211;test-mode=</code>&lt;file&gt;</p>
<dd> set map of good/bad blocks from given mapfile</p>
<dt><code>-i</code>, <code>&#8211;input-position=</code>&lt;bytes&gt;</p>
<dd> starting position of domain in input file [0]</p>
<dt><code>-I</code>, <code>&#8211;verify-input-size</code></p>
<dd> verify input file size with size in mapfile</p>
<dt><code>-J</code>, <code>&#8211;verify-on-error</code></p>
<dd> reread latest good sector after every error</p>
<dt><code>-K</code>, <code>&#8211;skip-size</code>=<i>,[/</i>&lt;i&gt;][,&lt;max&gt;]</p>
<dd> initial,maximum size to skip on read error</p>
<dt><code>-L</code>, <code>&#8211;loose-domain</code></p>
<dd> accept an incomplete domain mapfile</p>
<dt><code>-m</code>, <code>&#8211;domain-mapfile=</code>&lt;file&gt;</p>
<dd> restrict domain to finished blocks in &lt;file&gt;</p>
<dt><code>-M</code>, <code>&#8211;retrim</code></p>
<dd> mark all failed blocks as non-trimmed</p>
<dt><code>-n</code>, <code>&#8211;no-scrape</code></p>
<dd> skip the scraping phase</p>
<dt><code>-N</code>, <code>&#8211;no-trim</code></p>
<dd> skip the trimming phase</p>
<dt><code>-o</code>, <code>&#8211;output-position=</code>&lt;bytes&gt;</p>
<dd> starting position in output file [ipos]</p>
<dt><code>-O</code>, <code>&#8211;reopen-on-error</code></p>
<dd> reopen input file after every read error</p>
<dt><code>-p</code>, <code>&#8211;preallocate</code></p>
<dd> preallocate space on disc for output file</p>
<dt><code>-P</code>, <code>&#8211;data-preview[=</code>&lt;lines&gt;]</p>
<dd> show some lines of the latest data read [3]</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress all messages</p>
<dt><code>-r</code>, <code>&#8211;retry-passes=</code>&lt;n&gt;</p>
<dd> exit after &lt;n&gt; retry passes (<code>-1</code>=<i>,infinity/</i>) [0]</p>
<dt><code>-R</code>, <code>&#8211;reverse</code></p>
<dd> reverse the direction of all passes</p>
<dt><code>-s</code>, <code>&#8211;size=</code>&lt;bytes&gt;</p>
<dd> maximum size of input data to be copied</p>
<dt><code>-S</code>, <code>&#8211;sparse</code></p>
<dd> use sparse writes for output file</p>
<dt><code>-t</code>, <code>&#8211;truncate</code></p>
<dd> truncate output file to zero size</p>
<dt><code>-T</code>, <code>&#8211;timeout=</code>&lt;interval&gt;</p>
<dd> maximum time since last successful read</p>
<dt><code>-u</code>, <code>&#8211;unidirectional</code></p>
<dd> run all passes in the same direction</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose (a 2nd <code>-v</code> gives more)</p>
<dt><code>-w</code>, <code>&#8211;ignore-write-errors</code></p>
<dd> make fill mode ignore write errors</p>
<dt><code>-x</code>, <code>&#8211;extend-outfile=</code>&lt;bytes&gt;</p>
<dd> extend outfile size to be at least this long</p>
<dt><code>-X</code>, <code>&#8211;max-read-errors=</code>&lt;n&gt;</p>
<dd> maximum number of read errors allowed</p>
<dt><code>-y</code>, <code>&#8211;synchronous</code></p>
<dd> use synchronous writes for output file</p>
<dt><code>-Z</code>, <code>&#8211;max-read-rate=</code>&lt;bytes&gt;</p>
<dd> maximum read rate in bytes/s</p>
<dt><code>&#8211;ask</code></p>
<dd> ask for confirmation before starting the copy</p>
<dt><code>&#8211;cpass=</code>&lt;n&gt;[,&lt;n&gt;]</p>
<dd> select what copying pass(es) to run</p>
<dt><code>&#8211;delay-slow=</code>&lt;interval&gt;</p>
<dd> initial delay before checking slow reads [30]</p>
<dt><code>&#8211;log-events=</code>&lt;file&gt;</p>
<dd> log significant events in &lt;file&gt;</p>
<dt><code>&#8211;log-rates=</code>&lt;file&gt;</p>
<dd> log rates and error sizes in &lt;file&gt;</p>
<dt><code>&#8211;log-reads=</code>&lt;file&gt;</p>
<dd> log all read operations in &lt;file&gt;</p>
<dt><code>&#8211;mapfile-interval</code>=<i>,[i][/</i>,i]</p>
<dd> save/sync mapfile at given interval [auto]</p>
<dt><code>&#8211;max-slow-reads=</code>&lt;n&gt;</p>
<dd> maximum number of slow reads allowed</p>
<dt><code>&#8211;pause-on-error=</code>&lt;interval&gt;</p>
<dd> time to wait after each read error [0]</p>
<dt><code>&#8211;pause-on-pass=</code>&lt;interval&gt;</p>
<dd> time to wait between passes [0]</p>
<dt><code>&#8211;reset-slow</code></p>
<dd> reset slow reads if rate rises above min</dl>
<p> Numbers may be in decimal, hexadecimal or octal, and may be followed by a multiplier: s = sectors, k = 1000, Ki = 1024, M = 10^6, Mi = 2^20, etc&#8230; Time intervals have the format 1[.5][smhd] or 1/2[smhd]. </p>
<p> Exit status: 0 for a normal exit, 1 for environmental problems (file not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or invalid input file, 3 for an internal consistency error (eg, bug) which caused ddrescue to panic.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ddrescue [at] gnu.org<br />
 Ddrescue home page: <a rel="nofollow" href="http://www.gnu.org/software/ddrescue/ddrescue.html">http://www.gnu.org/software/ddrescue/ddrescue.html</a><br />
 General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2017 Antonio Diaz Diaz. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>ddrescue</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>ddrescue</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info ddrescue</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
