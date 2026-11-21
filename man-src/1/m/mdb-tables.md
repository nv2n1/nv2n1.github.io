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
<pre><code>
mdb - tables[-S][-1 | -d delimiter] database
</code></pre>
<p> <code>mdb-tables</code> is a utility program distributed with MDB Tools. </p>
<p> It produces a list of tables contained within an MDB <i>database</i> in a format suitable for use in shell scripts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-S</code></dt>
<dd> Show system tables. System tables are generally those beginning with &#8216;MSys&#8217;</dd>
<dt><code>-1</code></dt>
<dd> specifies that the tables should be listed 1 per line.</dd>
<dt><code>-d</code> <i>delimiter</i></dt>
<dd> specifies an alternative <i>delimiter</i>. If no <i>delimiter</i> is specified, table names will be delimited by a tab character, or by newline if the <code>-1</code> option was specified.</dd></dl>
<h2>NOTES</h2>
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
<h2>HISTORY</h2>
<p> <code>mdb-tables</code> first appeared in MDB Tools 0.3.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-tables</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<dl>
<dt><code>Access allows for tables to have spaces embeded in the table name.</code></dt>
<dd> You must specify a <i>delimiter</i> (<code>-d</code>) if you intend on piping the output of <code>mdb-tables</code> to a program such as awk or cut. </dd>
</dl>
