---
title: "mdb-sql(1)"
name: "mdb-sql"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-sql/"
description: "mdb-sql – SQL interface to MDB Tools"
---

<h2>NAME</h2>
<p> <code>mdb-sql </code>&#8211; SQL interface to MDB Tools</p>
<h2>SYNOPSIS</h2>
<pre><code>
mdb - sql[-HFp][-d delimiter][-i file][-o file][database]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-sql</code> is a utility program distributed with MDB Tools. </p>
<p> <code>mdb-sql</code> allows querying of an MDB <i>database</i> using a limited SQL subset language.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code></p>
<dd> Supress header row.</p>
<dt><code>-F</code></p>
<dd> Supress footer row.</p>
<dt><code>-p</code></p>
<dd> Turn off pretty printing. By default results are printed in an ascii table format which looks nice but is not conducive to manipulating the output with unix tools. This option prints output plainly in a tab separated format.</p>
<dt><code>-d</code></p>
<dd> Specify an alternative column <i>delimiter</i>. If no <i>delimiter</i> is specified, columns will be delimited by a tab character if pretty printing (<code>-p</code>) is turned off. If pretty printing is enabled this option is meaningless.</p>
<dt><code>-i</code></p>
<dd> Specify an input <i>file</i>. This option allows an input <i>file</i> containing the SQL to be passed to <code>mdb-sql</code>. See Notes.</p>
<dt><code>-o</code></p>
<dd> Specify an output <i>file</i>. This option allows the name of an output <i>file</i> to be used instead of stdout.</dl>
<h2>COMMANDS</h2>
<p> <code>mdb-sql</code> in interactive mode takes some special commands.</p>
<dl>
<dt><code>connect to &lt;</code><i>database</i>&gt;</p>
<dd> If no <i>database</i> was specified on the command line this command is necessary before any querys are issued. It also allows the switching of databases once in the tool.</p>
<dt><code>disconnect</code></p>
<dd> Will disconnect from the current <i>database</i>.</p>
<dt><code>go</code></p>
<dd> Each batch is sent to the parser using the &#8216;go&#8217; command.</dl>
<p> reset A batch can be cleared using the &#8216;reset&#8217; command.</p>
<dl>
<dt><code>list tables</code></p>
<dd> The list tables command will display a list of available tables in this <i>database</i>, similar to the mdb-tables utility on the command line.</p>
<dt><code>describe table &lt;table&gt;</code></p>
<dd> Will display the column information for the specified table.</p>
<dt><code>quit</code></p>
<dd> Will exit the tool.</dl>
<h2>SQL LANGUAGE</h2>
<p> The currently implemented SQL subset is quite small, supporting only single table queries, no aggregates, and limited support for WHERE clauses. Here is a brief synopsis of the supported language.</p>
<dl>
<dt><code>select:</code></p>
<dd> SELECT [* | &lt;column list&gt;] FROM &lt;table&gt; WHERE &lt;where clause&gt;</p>
<dt><code>column list:</code></p>
<dd> &lt;column&gt; [, &lt;column list&gt;]</p>
<dt><code>where clause:</code></p>
<dd> &lt;column&gt; &lt;operator&gt; &lt;literal&gt; [AND &lt;where clause&gt;]</p>
<dt><code>operator:</code></p>
<dd> =, =&gt;, =&lt;, &lt;&gt;, like, &lt;, &gt;</p>
<dt><code>literal:</code></p>
<dd> integers, floating point numbers, or string literal in single quotes</dl>
<h2>NOTES</h2>
<p> When passing a <i>file</i> (<code>-i</code>) or piping output to <code>mdb-sql</code> the final &#8216;go&#8217; is optional. This allow constructs like </p>
<p> echo &quot;Select * from Table1&quot; | <code>mdb-sql</code> mydb.mdb </p>
<p> to work correctly. </p>
<p> The <code>-i</code> command can be passed the string &#8216;stdin&#8217; to test entering text as if using a pipe.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></p>
<dd> Defines the charset of the input JET3 (access 97) <i>file</i>. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</p>
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
<p> <code>mdb-sql</code> first appeared in MDB Tools 0.3.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1) <code><a href="/docs/linux/man/1-isql/">isql</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-sql</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<p> The supported SQL syntax is a very limited subset and deficient in several ways. </p>
<h2>Index</h2>
