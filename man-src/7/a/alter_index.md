---
title: "alter_index(7)"
name: "alter_index"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_index/"
description: "ALTER INDEX – change the definition of an index"
---

<p>ALTER INDEX &#8211; change the definition of an index </p>
<h2>Synopsis</h2>
<pre>ALTER INDEX <i>name</i> RENAME TO <i>new_name</i>
ALTER INDEX <i>name</i> SET TABLESPACE <i>tablespace_name</i>
ALTER INDEX <i>name</i> SET ( <i>storage_parameter</i> = <i>value</i> [, ... ] )
ALTER INDEX <i>name</i> RESET ( <i>storage_parameter</i> [, ... ] )</pre>
<h2>Description</h2>
<p><code>ALTER INDEX</code> changes the definition of an existing index. There are several subforms:</p>
<dl>
<dt><code>RENAME</code></p>
<dd>The RENAME form changes the name of the index. There is no effect on the stored data.</p>
<dt><code>SET TABLESPACE</code></p>
<dd>This form changes the index&#8217;s tablespace to the specified tablespace and moves the data file(s) associated with the index to the new tablespace. See also CREATE TABLESPACE [<code><a href="/docs/linux/man/7-create_tablespace/">create_tablespace</a></code>(7)].</p>
<dt><code>SET ( </code><i>storage_parameter</i><code> = </code><i>value</i><code> [, &#8230; ] )</code></p>
<dd>This form changes one or more index-method-specific storage parameters for the index. See CREATE INDEX [<code><a href="/docs/linux/man/7-create_index/">create_index</a></code>(7)] for details on the available parameters. Note that the index contents will not be modified immediately by this command; depending on the parameter you might need to rebuild the index with REINDEX [<code><a href="/docs/linux/man/7-reindex/">reindex</a></code>(7)] to get the desired effects.</p>
<dt><code>RESET ( </code><i>storage_parameter</i><code> [, &#8230; ] )</code></p>
<dd>This form resets one or more index-method-specific storage parameters to their defaults. As with SET, a REINDEX might be needed to update the index entirely.</dl>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (possibly schema-qualified) of an existing index to alter.</p>
<dt><i>new_name</i></p>
<dd>The new name for the index.</p>
<dt><i>tablespace_name</i></p>
<dd>The tablespace to which the index will be moved.</p>
<dt><i>storage_parameter</i></p>
<dd>The name of an index-method-specific storage parameter.</p>
<dt><i>value</i></p>
<dd>The new value for an index-method-specific storage parameter. This might be a number or a word depending on the parameter.</dl>
<h2>Notes</h2>
<p>These operations are also possible using ALTER TABLE [<code><a href="/docs/linux/man/7-alter_table/">alter_table</a></code>(7)]. <code>ALTER INDEX</code> is in fact just an alias for the forms of <code>ALTER TABLE</code> that apply to indexes. </p>
<p> There was formerly an <code>ALTER INDEX OWNER</code> variant, but this is now ignored (with a warning). An index cannot have an owner different from its table&#8217;s owner. Changing the table&#8217;s owner automatically changes the index as well. </p>
<p> Changing any part of a system catalog index is not permitted.</p>
<h2>Examples</h2>
<p>To rename an existing index: </p>
<pre>ALTER INDEX distributors RENAME TO suppliers;</pre>
<p>To move an index to a different tablespace: </p>
<pre>ALTER INDEX distributors SET TABLESPACE fasttablespace;</pre>
<p>To change an index&#8217;s fill factor (assuming that the index method supports it): </p>
<pre><code>ALTER INDEX distributors SET (fillfactor = 75);
REINDEX INDEX distributors;</code></pre>
<h2>Compatibility</h2>
<p><code>ALTER INDEX</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE INDEX [<code><a href="/docs/linux/man/7-create_index/">create_index</a></code>(7)], REINDEX [<code><a href="/docs/linux/man/7-reindex/">reindex</a></code>(7)] </p>
