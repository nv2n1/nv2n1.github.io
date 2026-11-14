---
title: "mdb-export(1)"
name: "mdb-export"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-export/"
description: "mdb-export – Export data in an MDB database table to CSV format."
---

<h2>NAME</h2>
<p> <code>mdb-export </code>&#8211; Export data in an MDB database table to CSV format.</p>
<h2>SYNOPSIS</h2>
<pre><code>
mdb - export[-H][-d delimiter][-R row_delim][[-Q] | [-q quote[-X escape]]][-I backend][-D format][-N namespace][-b strip | raw | octal] database table
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-export</code> is a utility program distributed with MDB Tools. </p>
<p> It produces a CSV (comma separated value) output for the given <i>table</i>. Such output is suitable for importation into databases or spreadsheets.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code></p>
<dd> Supress header row</p>
<dt><code>-Q</code></p>
<dd> Don&#8217;t wrap text-like fields (text, memo, date) in quotes. If not specified text fiels will be surrounded by &quot; (double <i>quote</i>) characters.</p>
<dt><code>-d</code></p>
<dd> Specify an alternative column <i>delimiter</i> If no <i>delimiter</i> is specified, <i>table</i> names will be delimited by a , (comma) character.</p>
<dt><code>-R</code></p>
<dd> Specify a row <i>delimiter</i></p>
<dt><code>-I</code> <i>backend</i></p>
<dd> INSERT statements (instead of CSV). You must specify which SQL <i>backend</i> dialect to use. Allowed values are: access, sybase, oracle, postgres, mysql and sqlite.</p>
<dt><code>-D</code></p>
<dd> Set the date <i>format</i> (see <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for details)</p>
<dt><code>-q</code></p>
<dd> Use to wrap text-like fields. Default is &quot;.</p>
<dt><code>-X</code></p>
<dd> Use to <i>escape</i> quoted characters within a field. Default is doubling.</p>
<dt><code>-N</code> <i>namespace</i></p>
<dd> Prefix identifiers with <i>namespace</i>.</p>
<dt><code>-b</code> strip|raw|octal</p>
<dd> Binary export mode: strip binaries, export as-is, or output style octal data.</dl>
<h2>NOTES</h2>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></p>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</p>
<dt><code>MDBICONV</code></p>
<dd> Defines the output charset to use for the SQL file. Default is UTF-8. mdbtools must have been compiled with iconv.</p>
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
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>HISTORY</h2>
<p> <code>mdb-export</code> first appeared in MDB Tools 0.1.</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-export</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<p> Memo fields are allowed to contain a newline characters, the current program does nothing about this. </p>
<h2>Index</h2>
