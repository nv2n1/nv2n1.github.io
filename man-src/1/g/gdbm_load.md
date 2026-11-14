---
title: "gdbm_load(1)"
name: "gdbm_load"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbm_load/"
description: "gdbm_load – re-create a GDBM database from a dump file."
---

<h2>NAME</h2>
<p> gdbm_load &#8211; re-create a GDBM database from a dump file.</p>
<h2>SYNOPSIS</h2>
<p> <code>gdbm_load</code> [<code>-Mnr</code>] [<code>-b</code> <i>NUM</i>] [<code>-c</code> <i>NUM]<br />
&nbsp;<wbr>[</i><code>-m</code>&nbsp;<wbr><i>MODE</i>]&nbsp;<wbr>[<code>-u</code>&nbsp;<wbr><i>NAME</i>|<i>UID</i>[:<i>NAME</i>|<i>GID</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;block-size</code>=<i>NUM</i>]&nbsp;<wbr>[<code>&#8211;cache-size</code>=<i>NUM</i>]&nbsp;<wbr>[<code>&#8211;mmap</code>=<i>NUM</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;mode</code>=<i>MODE</i>]&nbsp;<wbr>[<code>&#8211;no-meta</code>]&nbsp;<wbr>[<code>&#8211;replace</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;user</code>=<i>NAME</i>|<i>UID</i>[:<i>NAME</i>|<i>GID</i>]]&nbsp;<wbr><i>FILE</i>&nbsp;<wbr>[<i>DB_FILE</i>] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
<p> <code>gdbm_load</code> [<code>-Vh</code>] [<code>&#8211;help</code>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>]</p>
<h2>DESCRIPTION</h2>
<p> Create a <code>gdbm</code> database file <i>DB_FILE</i> from the dump file <i>FILE</i>. If the <i>FILE</i> argument is not supplied, output the created database to the standard error. </p>
<p> If the input file is in ASCII dump format, the mode and ownership of the created database are restored from the information in the dump. This can be overridden using the command line options (see below).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;block-size</code>=<i>NUM</i></p>
<dd> Sets block size.</p>
<dt><code>-c</code>, <code>&#8211;cache-size</code>=<i>NUM</i></p>
<dd> Sets cache size.</p>
<dt><code>-M</code>, <code>&#8211;mmap</code></p>
<dd> Use memory mapping.</p>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>MODE</i></p>
<dd> Set database file mode (octal number).</p>
<dt><code>-n</code>, <code>&#8211;no-meta</code></p>
<dd> Do not attempt to restore database meta-data (mode and ownership).</p>
<dt><code>-r</code>, <code>&#8211;replace</code></p>
<dd> If the database exists, replace records in it.</p>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>NAME</i>|<i>UID</i>[:<i>NAME</i>|<i>GID</i>]</p>
<dd> Set file ownership.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a short usage summary.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a list of available options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdbm_dump/">gdbm_dump</a></code>(1), <code><a href="/docs/linux/man/1-gdbmtool/">gdbmtool</a></code>(1), <code><a href="/docs/linux/man/3-gdbm/">gdbm</a></code>(3). </p>
<p> For a detailed description of <code>gdbm_load</code> and other <code>gdbm</code> utilities, refer to the <code>GDBM Manual</code> available in Texinfo format. To access it, run: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>info gdbm</code> </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gdbm [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
