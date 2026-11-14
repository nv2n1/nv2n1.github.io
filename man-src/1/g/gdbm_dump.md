---
title: "gdbm_dump(1)"
name: "gdbm_dump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbm_dump/"
description: "gdbm_dump – dump a GDBM database to a file"
---

<h2>NAME</h2>
<p> gdbm_dump &#8211; dump a GDBM database to a file</p>
<h2>SYNOPSIS</h2>
<p> <code>gdbm_dump</code> [<code>-H </code><i>FMT</i>] [<code>&#8211;format</code>=<i>FMT</i>] <i>DB_FILE</i> [<i>FILE</i>] </p>
<p> <code>gdbm_dump</code> [<code>-Vh</code>] [<code>&#8211;help</code>] [<code>&#8211;usage</code>] [<code>&#8211;version</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>gdbm_dump</code> utility creates a dump of the specified <code><a href="/docs/linux/man/3-gdbm/">gdbm</a></code>(3) database file. The name for the output dump file is supplied by the second argument (<i>FILE</i>). If not specified, the output goes to the standard error. </p>
<p> The created dump can be given as argument to the <code><a href="/docs/linux/man/1-gdbm_load/">gdbm_load</a></code>(1) utility in order to re-create an exact copy of the <i>DB_FILE</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code>, <code>&#8211;format</code>=<i>FMT</i></p>
<dd> Select dump format. The value <code>binary</code> (or <code>0</code>) instructs <code>gdbm_dump</code> to produce a binary dump, compatible with earlier <code>gdbm</code> versions (up to version 1.9). The value <code>ascii</code> (or <code>1</code>) instructs it to create an ASCII dump (this is the default). The latter is preferred because, apart from the actual data, it also contains meta-information which will allow <code><a href="/docs/linux/man/1-gdbm_load/">gdbm_load</a></code>(1) to recreate an exact copy of the file.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a short usage summary.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a list of available options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdbm_load/">gdbm_load</a></code>(1), <code><a href="/docs/linux/man/1-gdbmtool/">gdbmtool</a></code>(1), <code><a href="/docs/linux/man/3-gdbm/">gdbm</a></code>(3). </p>
<p> For a detailed description of <code>gdbm_dump</code> and other <code>gdbm</code> utilities, refer to the <code>GDBM Manual</code> available in Texinfo format. To access it, run: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>info gdbm</code> </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-gdbm [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
