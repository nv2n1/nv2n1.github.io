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
<h2>SYNOPSIS</h2>
<pre><code>
mdb - schema[options] database[backend]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mdb-schema</code> is a utility program distributed with MDB Tools. </p>
<p> It produces DDL (data definition language) output for the given <i>database</i>. This can be passed to another <i>database</i> to create a replica of the original access table format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-T</code> &lt;table&gt;, <code>&#8211;table</code> &lt;table&gt;</p>
<dd> Single table option. Create schema for this table only. Default is to export all tables.</p>
<dt><code>-N</code> namespace</p>
<dd> Prefix identifiers with namespace.</p>
<dt><code>&#8211;drop-table</code></p>
<dd> Issue DROP TABLE statement.</p>
<dt><code>&#8211;no-drop-table</code></p>
<dd> Don&#8217;t issue DROP TABLE statement. This is the default.</p>
<dt><code>&#8211;not-null</code></p>
<dd> Issue NOT NULL constraints. This is the default.</p>
<dt><code>&#8211;no-not-null</code></p>
<dd> Don&#8217;t issue NOT NULL constraints.</p>
<dt><code>&#8211;default-values</code></p>
<dd> Issue DEFAULT values.</p>
<dt><code>&#8211;no-default-values</code></p>
<dd> Don&#8217;t issue DEFAULT values. This is the default.</p>
<dt><code>&#8211;not-empty</code></p>
<dd> Issue CHECK &lt;&gt; &#8221; constraints.</p>
<dt><code>&#8211;no-not-empty</code></p>
<dd> Don&#8217;t issue CHECK &lt;&gt; &#8221; constraints. This is the default.</p>
<dt><code>&#8211;indexes</code></p>
<dd> Export INDEXes. This is the default.</p>
<dt><code>&#8211;no-indexes</code></p>
<dd> Don&#8217;t export INDEXes.</p>
<dt><code>&#8211;relations</code></p>
<dd> Export foreign keys constraints. This is the default.</p>
<dt><code>&#8211;no-relations</code></p>
<dd> Don&#8217;t export foreign keys constraints.</p>
<dt><i>backend</i></p>
<dd> Specifies target DDL dialect. Supported values are access, sybase, oracle, postgres, mysql and sqlite. If not specified the generated DDL will be in access format.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MDB_JET3_CHARSET</code></p>
<dd> Defines the charset of the input JET3 (access 97) file. Default is CP1252. See <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1).</p>
<dt><code>MDBICONV</code></p>
<dd> Defines the output charset to use for the SQL file. Default is UTF-8. mdbtools must have been compiled with iconv.</p>
<dt><code>MDBOPTS</code></p>
<dd> semi-column separated list of <i>options</i>:</p>
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
<dd> debug_all is a shortcut for all debug_* <i>options</i></dl>
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
<h2>Index</h2>
