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
<pre><code>
mdb - sql[-HFp][-d delimiter][-i file][-o file][database]
</code></pre>
<p> <code>mdb-sql</code> is a utility program distributed with MDB Tools. </p>
<p> <code>mdb-sql</code> allows querying of an MDB <i>database</i> using a limited SQL subset language.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-H</code></dt>
<dd> Supress header row.</dd>
<dt><code>-F</code></dt>
<dd> Supress footer row.</dd>
<dt><code>-p</code></dt>
<dd> Turn off pretty printing. By default results are printed in an ascii table format which looks nice but is not conducive to manipulating the output with unix tools. This option prints output plainly in a tab separated format.</dd>
<dt><code>-d</code></dt>
<dd> Specify an alternative column <i>delimiter</i>. If no <i>delimiter</i> is specified, columns will be delimited by a tab character if pretty printing (<code>-p</code>) is turned off. If pretty printing is enabled this option is meaningless.</dd>
<dt><code>-i</code></dt>
<dd> Specify an input <i>file</i>. This option allows an input <i>file</i> containing the SQL to be passed to <code>mdb-sql</code>. See Notes.</dd>
<dt><code>-o</code></dt>
<dd> Specify an output <i>file</i>. This option allows the name of an output <i>file</i> to be used instead of stdout.</dd></dl>
<h2>COMMANDS</h2>
<p> <code>mdb-sql</code> in interactive mode takes some special commands.</p>
<dl>
<dt><code>connect to &lt;</code><i>database</i>&gt;</dt>
<dd> If no <i>database</i> was specified on the command line this command is necessary before any querys are issued. It also allows the switching of databases once in the tool.</dd>
<dt><code>disconnect</code></dt>
<dd> Will disconnect from the current <i>database</i>.</dd>
<dt><code>go</code></dt>
<dd> Each batch is sent to the parser using the &#8216;go&#8217; command.</dd></dl>
<p> reset A batch can be cleared using the &#8216;reset&#8217; command.</p>
<dl>
<dt><code>list tables</code></dt>
<dd> The list tables command will display a list of available tables in this <i>database</i>, similar to the mdb-tables utility on the command line.</dd>
<dt><code>describe table &lt;table&gt;</code></dt>
<dd> Will display the column information for the specified table.</dd>
<dt><code>quit</code></dt>
<dd> Will exit the tool.</dd></dl>
<h2>SQL LANGUAGE</h2>
<p> The currently implemented SQL subset is quite small, supporting only single table queries, no aggregates, and limited support for WHERE clauses. Here is a brief synopsis of the supported language.</p>
<dl>
<dt><code>select:</code></dt>
<dd> SELECT [* | &lt;column list&gt;] FROM &lt;table&gt; WHERE &lt;where clause&gt;</dd>
<dt><code>column list:</code></dt>
<dd> &lt;column&gt; [, &lt;column list&gt;]</dd>
<dt><code>where clause:</code></dt>
<dd> &lt;column&gt; &lt;operator&gt; &lt;literal&gt; [AND &lt;where clause&gt;]</dd>
<dt><code>operator:</code></dt>
<dd> =, =&gt;, =&lt;, &lt;&gt;, like, &lt;, &gt;</dd>
<dt><code>literal:</code></dt>
<dd> integers, floating point numbers, or string literal in single quotes</dd></dl>
<h2>NOTES</h2>
<p> When passing a <i>file</i> (<code>-i</code>) or piping output to <code>mdb-sql</code> the final &#8216;go&#8217; is optional. This allow constructs like </p>
<p> echo &quot;Select * from Table1&quot; | <code>mdb-sql</code> mydb.mdb </p>
<p> to work correctly. </p>
<p> The <code>-i</code> command can be passed the string &#8216;stdin&#8217; to test entering text as if using a pipe.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></dt>
<dd> Defines the charset of the input JET3 (access 97) <i>file</i>. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</dd>
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
<p> <code>mdb-sql</code> first appeared in MDB Tools 0.3.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-schema/">mdb-schema</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1) <code><a href="/docs/linux/man/1-isql/">isql</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-sql</code> utility was written by Brian Bruns.</p>
<h2>BUGS</h2>
<p> The supported SQL syntax is a very limited subset and deficient in several ways. </p>
