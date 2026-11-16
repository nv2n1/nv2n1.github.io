---
title: "mdb-parsecsv(1)"
name: "mdb-parsecsv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-parsecsv/"
description: "mdb-parsecsv – Convert CSV table dump into C file."
---

<h2>NAME</h2>
<p> <code>mdb-parsecsv </code>&#8211; Convert CSV table dump into C file.</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mdb-parsecsv</code> <i>file</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-parsecsv</code> is a utility program distributed with MDB Tools. </p>
<p> <code>mdb-parsecsv</code> takes a CSV <i>file</i> representing a database table, and converts it into a C array.</p>
<h2>NOTES</h2>
<p> If the first argument does not exist as a <i>file</i>, <code>mdb-parsecsv</code> will look for the same filename with &#8216;.txt&#8217; appended. </p>
<p> The <i>file</i> extension is stripped, and the output written to the base name plus a &#8216;.c&#8217; extension.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></dt>
<dd> Defines the charset of the input JET3 (access 97) <i>file</i>. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</dd>
<dt><code>MDBICONV</code></dt>
<dd> Defines the output charset to use for the SQL <i>file</i>. Default is UTF-8. mdbtools must have been compiled with iconv.</dd>
<dt><code>MDBOPTS</code></dt>
<dd> semi-column separated list of options:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> use_index</dd>
<dt>&bull;</dt>
<dd> no_memo</dd>
<dt>&bull;</dt>
<dd> debug_like</dd>
<dt>&bull;</dt>
<dd> debug_write</dd>
<dt>&bull;</dt>
<dd> debug_usage</dd>
<dt>&bull;</dt>
<dd> debug_ole</dd>
<dt>&bull;</dt>
<dd> debug_row</dd>
<dt>&bull;</dt>
<dd> debug_props</dd>
<dt>&bull;</dt>
<dd> debug_all is a shortcut for all debug_* options</dd></dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-parsecsv</code> utility was written by Brian Bruns. </p>
<h2>Index</h2>
