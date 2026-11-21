---

title: "mdb-header(1)"
name: "mdb-header"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-header/"
description: "mdb-header – Write header file from an MDB database"
---

<p> <code>mdb-header </code>&#8211; Write header file from an MDB database</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mdb-header</code> [<i>database</i>]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-header</code> is a utility program distributed with MDB Tools. </p>
<p> It will dump the names and types of the tables and columns in an MDB <i>database</i> in a C header format. </p>
<p> It will create three files &#8211; types.h and dumptypes.[ch]</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></dt>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</dd>
<dt><code>MDBICONV</code></dt>
<dd> Defines the output charset. Default is UTF-8. mdbtools must have been compiled with iconv.</dd>
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
<h2>EXIT STATUS</h2>
<p> <code>mdb-header</code> exits with error code 1 if there was anunsupported type.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-header</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<p> Only a few types are currently supported. </p>
