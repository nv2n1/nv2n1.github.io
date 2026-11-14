---
title: "glite-lb-bkindex(8)"
name: "glite-lb-bkindex"
section: "8"
letter: "g"
url: "/docs/linux/man/8-glite-lb-bkindex/"
description: "glite-lb-bkindex – dump or rebuild bookkeeping server indices"
---

<p>glite-lb-bkindex &#8211; dump or rebuild bookkeeping server indices</p>
<h2>Synopsis</h2>
<p><code>glite-lb-bkindex</code> [<code>-mrv</code>] [<i>FILE</i>]<br />
 <code>glite-lb-bkindex</code> [<code>-dmv</code>] </p>
<h2>Description</h2>
<p>The bookkeeping server <code>glite-lb-bkserverd</code> uses database indices to support various types of user queries efficiently. <code>glite-lb-bkindex </code> is a tool for dumping and manipulating the indices. Both single- and multiple-column indices are supported. Due to performance reasons (reindexing may take rather long time) the default invocation performs only &quot;dry run&quot; &#8211; the input is checked and intended actions reported but not really performed. The option -r has to be specified to do the real work. <code>glite-lb-bkindex</code> should not be run while there is a running <code>glite-lb-bkserverd</code> on top of the same database. By default the L&amp;B server indexes data according to JobId only. Because the querying capabilities of L&amp;B release 2 were considerably extended, the server refuses to process a query which would not utilize any index. This prevent overloading the underlying database engine. Consequently, even a trivial query &#8216;give me all my jobs&#8217; results in an error in the default setup because under certain conditions processing such query may require handling gigabytes of data. The server administrator can create and modify the set of indices and control the set of supported queries. The description of columns to be indexed is given to <code>glite-lb-bkindex</code> utility via <i>FILE</i> that follows this syntax (subset of ClassAd syntax):</p>
<dl>
<dd><i>FILE</i> ::= <code>[&nbsp;<wbr>JobIndices&nbsp;<wbr>=&nbsp;<wbr>{&nbsp;<wbr></code><i>index-description&nbsp;<wbr></i>[<code>,&nbsp;<wbr></code><i>index-description</i>]* <code>} ]</code><br />
 <i>index-description</i> ::= <i>column-description </i>| list-of-columns<br />
 <i>list-of-columns </i> ::= <code>{&nbsp;<wbr></code><i>column-description&nbsp;<wbr></i>+&nbsp;<wbr><code>}</code><br />
 <i>column-description </i> ::= <code>[&nbsp;<wbr></code><i>column-type</i><code>;&nbsp;<wbr></code><i>column-name</i><code>;&nbsp;<wbr></code><i>prefix-len&nbsp;<wbr></i>?&nbsp;<wbr>]<br />
 <i>column-type </i> ::= <code>type = user </code>| type = system | type = time<br />
 <i>column-name </i> ::= <code>name = </code><i>actual_column_name</i><br />
 <i>prefix-len </i> ::= <code>prefixlen&nbsp;<wbr>=&nbsp;<wbr></code><i>integer</i>  The only top-level attribute <code>JobIndices</code> is a list (possibly empty) of index descriptions. Each index description is either a single column or a list of columns (where the order is important). The column is described by mandatory attributes <code>type </code> and <code>name</code>, and an optional attribute <code>prefixlen</code>. Possible values of type are <code>system</code> (L&amp;B internal attributes) <code>time</code> (&quot;state entered&quot; timestamps), and <code>user</code> (user tags). Currently supported system column names are <i>owner</i>, destination and location. and valid timestamps are the job states, i.e. <i>submitted, waiting, ready, scheduled, running, done, cleared, cancelled, aborted</i>. Names of user tags are arbitrary as long as their length is less than 60 characters and they contain only ASCII printable characters excluding backtick (`). The <code>prefixlen</code> value may be used to restrict indexing of columns, which may grow rather long, to a fixed size. This becomes necessary with compound indices as MySQL limits the total size of index to 250 bytes only. In the following example the index file contains two indices, the first one on a single system attribute &#8212; &lt;job owner&gt;, the second one composed from system attribute (job) &lt;destination&gt; and user tag called &lt;experiment number&gt;:</p>
<dl>
<dd>[<br />
 &nbsp;<wbr>&nbsp;<wbr>JobIndices = {<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ type = &quot;system&quot;; name = &quot;owner&quot; ],<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ type = &quot;system&quot;; name = &quot;destination&quot;;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prefixlen = 100 ],<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ type = &quot;user&quot;; name = &quot;experiment number&quot;;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prefixlen = 100 ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}<br />
 &nbsp;<wbr>&nbsp;<wbr>}<br />
 ] </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, &#8211;dump</p>
<dd>Print current setup on <i>stdout</i>. </p>
<dt><code>-m</code><i> STRING</i>, &#8211;mysql <i>STRING</i></p>
<dd><i>STRING</i> is the database connect string in the form </p>
<p> USER_NAME/PASSWORD [at] DB_HOSTNAME:DB_NAME </p>
<p> It defaults to lbserver/@localhost:lbserver20 (common with <code>glite-lb-bkserverd</code>). </p>
<dt><code>-r, &#8211;really</code></p>
<dd>Really perform reindexing. </p>
<dt><code>-R, &#8211;remove</code></p>
<dd>Remove all indexes from server. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase verbosity. </p>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-glite-lb-purge/">glite-lb-purge</a></code>(1), <a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a>(8) </p>
<h2>Author</h2>
<p>EU EGEE, JRA1.</p>
