---

title: "mdb-schema(1)"
name: "mdb-schema"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb-schema/"
description: "mdb-schema – Generate schema creation DDL"
---

<h2>NAME</h2>
<p> <code>mdb-schema </code>&#8211; Generate schema creation DDL</p>
<pre><code>
mdb - schema[options] database[backend]
</code></pre>
<p> <code>mdb-schema</code> is a utility program distributed with MDB Tools. </p>
<p> It produces DDL (data definition language) output for the given <i>database</i>. This can be passed to another <i>database</i> to create a replica of the original access table format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-T</code> &lt;table&gt;, <code>&#8211;table</code> &lt;table&gt;</dt>
<dd> Single table option. Create schema for this table only. Default is to export all tables.</dd>
<dt><code>-N</code> namespace</dt>
<dd> Prefix identifiers with namespace.</dd>
<dt><code>&#8211;drop-table</code></dt>
<dd> Issue DROP TABLE statement.</dd>
<dt><code>&#8211;no-drop-table</code></dt>
<dd> Don&#8217;t issue DROP TABLE statement. This is the default.</dd>
<dt><code>&#8211;not-null</code></dt>
<dd> Issue NOT NULL constraints. This is the default.</dd>
<dt><code>&#8211;no-not-null</code></dt>
<dd> Don&#8217;t issue NOT NULL constraints.</dd>
<dt><code>&#8211;default-values</code></dt>
<dd> Issue DEFAULT values.</dd>
<dt><code>&#8211;no-default-values</code></dt>
<dd> Don&#8217;t issue DEFAULT values. This is the default.</dd>
<dt><code>&#8211;not-empty</code></dt>
<dd> Issue CHECK &lt;&gt; &#8221; constraints.</dd>
<dt><code>&#8211;no-not-empty</code></dt>
<dd> Don&#8217;t issue CHECK &lt;&gt; &#8221; constraints. This is the default.</dd>
<dt><code>&#8211;indexes</code></dt>
<dd> Export INDEXes. This is the default.</dd>
<dt><code>&#8211;no-indexes</code></dt>
<dd> Don&#8217;t export INDEXes.</dd>
<dt><code>&#8211;relations</code></dt>
<dd> Export foreign keys constraints. This is the default.</dd>
<dt><code>&#8211;no-relations</code></dt>
<dd> Don&#8217;t export foreign keys constraints.</dd>
<dt><i>backend</i></dt>
<dd> Specifies target DDL dialect. Supported values are access, sybase, oracle, postgres, mysql and sqlite. If not specified the generated DDL will be in access format.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></dt>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</dd>
<dt><code>MDBICONV</code></dt>
<dd> Defines the output charset to use for the SQL file. Default is UTF-8. mdbtools must have been compiled with iconv.</dd>
<dt><code>MDBOPTS</code></dt>
<dd> semi-column separated list of <i>options</i>:</dd>
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
<dd> debug_all is a shortcut for all debug_* <i>options</i></dd></dl>
</dl>
</dl>
<h2>NOTES</h2>
<h2>HISTORY</h2>
<p> <code>mdb-schema</code> first appeared in MDB Tools 0.1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gmdb2/">gmdb2</a></code>(1) <code><a href="/docs/linux/man/1-mdb-export/">mdb-export</a></code>(1) <code><a href="/docs/linux/man/1-mdb-hexdump/">mdb-hexdump</a></code>(1) <code><a href="/docs/linux/man/1-mdb-prop/">mdb-prop</a></code>(1) <code><a href="/docs/linux/man/1-mdb-sql/">mdb-sql</a></code>(1) <code><a href="/docs/linux/man/1-mdb-ver/">mdb-ver</a></code>(1) <code><a href="/docs/linux/man/1-mdb-array/">mdb-array</a></code>(1) <code><a href="/docs/linux/man/1-mdb-header/">mdb-header</a></code>(1) <code><a href="/docs/linux/man/1-mdb-parsecsv/">mdb-parsecsv</a></code>(1) <code><a href="/docs/linux/man/1-mdb-tables/">mdb-tables</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> The <code>mdb-schema</code> utility was written by Brian Bruns and others.</p>
<h2>BUGS</h2>
<p> Relationships and other features may not be supported by all databases. Access datatypes are mapped to their closest counterparts in the target <i>backend</i>. This may not always yield an exact fit. </p>
