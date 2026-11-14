---
title: "mdb-prop(1)"
name: "mdb-prop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-prop/"
description: "mdb-prop – Get properties list from MDB database"
---

<h2>NAME</h2>
<p> <code>mdb-prop </code>&#8211; Get properties list from MDB database</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mdb-prop</code> <i>database</i> <i>name</i> [<i>propcol</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-prop</code> is a utility program distributed with MDB Tools. </p>
<p> Print a properties list from an MDB <i>database</i>. </p>
<p> <i>name</i> is the <i>name</i> of the table, querry, or other object. </p>
<p> <i>propcol</i> is the <i>name</i> of the system table MSysObjects&#8217; column containing properties. It defaults to LvProp.</p>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-prop</code> utility was written by Brian Bruns. </p>
<h2>Index</h2>
