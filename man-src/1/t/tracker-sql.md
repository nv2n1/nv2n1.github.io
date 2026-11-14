---
title: "tracker-sql(1)"
name: "tracker-sql"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-sql/"
description: "tracker-sql – Use SQL to query the Tracker databases."
---

<h2 class="name">NAME</h2>
<p> tracker-sql &#8211; Use SQL to query the Tracker databases.</p>
<h2>SYNOPSIS</h2>
<pre>
<code>tracker sql</code> -q &lt;<i>sql</i>&gt; | -f &lt;<i>file</i>&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> This command allows probing of the current database. When using commands like <code>tracker sparql</code>, the SPARQL used is translated into SQL before being run on the database. This allows direct use of the database using SQL avoiding the SPARQL engine entirely. </p>
<p> The caller can run a query two ways, either by providing a <i>file</i> with the query or by providing a string with the <i>sql</i> query. </p>
<p> The <i>file</i> argument can be either a local path or a URI. It also does not have to be an absolute path. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;file</code>=&lt;<i>file</i>&gt;</p>
<dd> Use a <i>file</i> with SPARQL content to query. Don&#8217;t forget to end all queries with a semicolon (;) and also to use quotes around table names. The quotes are important because most tables are named after ontology classes like &quot;nfo:Document&quot; and queries will fail without the quotes.</p>
<dt><code>-q, &#8211;query</code>=&lt;<i>sql</i>&gt;</p>
<dd> Use a <i>sql</i> string to query the database with. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Show first 10 &quot;nfo:Document&quot; entries where the TOC is not NULL:</p>
<dd>
<pre>
$ tracker sql -q 'SELECT * FROM &quot;nfo:Document&quot; WHERE &quot;nfo:tableOfContents&quot; NOT NULL LIMIT 10;'
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-sparql/">tracker-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1).</p>
<dl>
<dt><code><a rel="nofollow" href="http://en.wikipedia.org/wiki/SQL">http://en.wikipedia.org/wiki/SQL</a></code></p>
<dd>
</dl>
<h2>Index</h2>
