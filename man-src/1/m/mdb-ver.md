---
title: "mdb-ver(1)"
name: "mdb-ver"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-ver/"
description: "mdb-ver – Return the format of a given MDB database."
---

<h2>NAME</h2>
<p> <code>mdb-ver </code>&#8211; Return the format of a given MDB database.</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mdb-ver</code> <i>database</i>
<code>mdb-ver</code> <code>-M</code>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-ver</code> is a utility program distributed with MDB Tools. </p>
<p> It will return a single line of output with &#8216;JET3&#8217; for those files produced in Access 97 format, &#8216;JET4&#8217; for those produced by Access 2000, XP and 2003, &#8216;ACE12&#8217; for those produced by Access 2007, or &#8216;ACE14&#8217; for those produced by Access 2010.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-M</code></p>
<dd> Prints the version of MDB Tools itself instead of the MDB file.</dl>
<h2>NOTES</h2>
<p> Access changed its format between Jet 3 used in Access 97 and Jet 4 used for Access 2000 and XP. The nature of the changes included moving the page size from 2K to 4K and added support for unicode. MDB Tools actively supports both formats. Newer version are very much like Jet4.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></p>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</p>
<dt><code>MDBICONV</code></p>
<dd> Defines the output charset. Default is UTF-8. mdbtools must have been compiled with iconv.</p>
<dt><code>MDBOPTS</code></p>
<dd> semi-column separated list of options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> use_index</p>
<dt>&bull;</p>
<dd> no_memo</p>
<dt>&bull;</p>
<dd> debug_like</p>
<dt>&bull;</p>
<dd> debug_write</p>
<dt>&bull;</p>
<dd> debug_usage</p>
<dt>&bull;</p>
<dd> debug_ole</p>
<dt>&bull;</p>
<dd> debug_row</p>
<dt>&bull;</p>
<dd> debug_props</p>
<dt>&bull;</p>
<dd> debug_all is a shortcut for all debug_* options</dl>
</dl>
</dl>
<h2>HISTORY</h2>
<p> <code>mdb-ver</code> first appeared in MDB Tools 0.4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-ver</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<p> <code>mdb-ver</code> does minimal checking on the validity of a file. It is possbile for it to misidentify a non-MDB file. </p>
<p> <code>mdb-ver</code> does not recognize Access 2.0 (Jet 2). </p>
<h2>Index</h2>
