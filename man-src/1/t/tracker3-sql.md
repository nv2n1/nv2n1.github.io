---
title: "tracker3-sql(1)"
name: "tracker3-sql"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-sql/"
description: "tracker3-sql – Use SQL to query the Tracker databases."
---

<h2 class="name">NAME</h2>
<p> tracker3-sql &#8211; Use SQL to query the Tracker databases. </p>
<h2>SYNOPSIS</h2>
<pre>
tracker3 sql -q &lt;sql&gt; | -f &lt;file&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> This command allows probing of the current database. When using commands like <code>tracker3 sparql</code>, the SPARQL used is translated into SQL before being run on the database. This allows direct use of the database using SQL avoiding the SPARQL engine entirely. </p>
<p> The caller can run a query two ways, either by providing a <i>file</i> with the query or by providing a string with the <i>sql</i> query. </p>
<p> The <i>file</i> argument can be either a local path or a URI. It also does not have to be an absolute path.</p>
<h2>OPTIONS</h2>
<p> <code>-f, &#8211;file=&lt;</code><i>file</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Use a <i>file</i> with SPARQL content to query. Don&#8217;t forget to end all queries with a semicolon (;) and also to use quotes around table names. The quotes are important because most tables are named after ontology classes like &quot;nfo:Document&quot; and queries will fail without the quotes.</dl>
<p> <code>-q, &#8211;query=&lt;</code><i>sql</i><code>&gt;</code></p>
<dl>
<dt>
<dd> Use a <i>sql</i> string to query the database with.</dl>
<h2>EXAMPLES</h2>
<p> Show first 10 &quot;nfo:Document&quot; entries where the TOC is not NULL</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ tracker3 sql -q 'SELECT * FROM &quot;nfo:Document&quot; WHERE &quot;nfo:tableOfContents&quot; NOT NULL LIMIT 10;'
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<p> <code><a rel="nofollow" href="http://en.wikipedia.org/wiki/SQL">http://en.wikipedia.org/wiki/SQL</a></code> </p>
<h2>Index</h2>
