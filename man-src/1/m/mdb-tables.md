---
title: "mdb-tables(1)"
name: "mdb-tables"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-tables/"
description: "mdb-tables – Get listing of tables in an MDB database"
---

<h2>NAME</h2>
<p> <code>mdb-tables </code>&#8211; Get listing of tables in an MDB database</p>
<h2>SYNOPSIS</h2>
<pre><code>
mdb - tables[-S][-1 | -d delimiter] database
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-tables</code> is a utility program distributed with MDB Tools. </p>
<p> It produces a list of tables contained within an MDB <i>database</i> in a format suitable for use in shell scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-S</code></p>
<dd> Show system tables. System tables are generally those beginning with &#8216;MSys&#8217;</p>
<dt><code>-1</code></p>
<dd> specifies that the tables should be listed 1 per line.</p>
<dt><code>-d</code> <i>delimiter</i></p>
<dd> specifies an alternative <i>delimiter</i>. If no <i>delimiter</i> is specified, table names will be delimited by a tab character, or by newline if the <code>-1</code> option was specified.</dl>
<h2>NOTES</h2>
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
<p> <code>mdb-tables</code> first appeared in MDB Tools 0.3.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-tables</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<dl>
<dt><code>Access allows for tables to have spaces embeded in the table name.</code></p>
<dd> You must specify a <i>delimiter</i> (<code>-d</code>) if you intend on piping the output of <code>mdb-tables</code> to a program such as awk or cut. </p>
</dl>
<h2>Index</h2>
