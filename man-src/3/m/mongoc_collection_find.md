---
title: "mongoc_collection_find(3)"
name: "mongoc_collection_find"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_find/"
description: "mongoc_collection_find() – This function shall execute a query on the underlying collection."
---

<p>mongoc_collection_find() &#8211; This function shall execute a query on the underlying collection.</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_collection_find (mongoc_collection_t *collection,
 mongoc_query_flags_t flags,
 uint32_t skip,
 uint32_t limit,
 uint32_t batch_size,
 const bson_t *query,
 const bson_t *fields,
 const mongoc_read_prefs_t *read_prefs)
 BSON_GNUC_WARN_UNUSED_RESULT;</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A <code>mongoc_query_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>skip</code></p>
<dd>A uint32_t of number of documents to skip or 0.</dl>
<dl COMPACT>
<dt><code>limit</code></p>
<dd>A uint32_t of max number of documents to return or 0.</dl>
<dl COMPACT>
<dt><code>batch_size</code></p>
<dd>A uint32_t containing batch size of document result sets or 0 for default. Default is 100.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> containing the query and options to execute.</dl>
<dl COMPACT>
<dt><code>fields</code></p>
<dd>A <code>bson_t</code> containing fields to return or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> or <code>NULL</code> for default read preferences.</dl>
<h2>Description</h2>
<p>This function shall execute a query on the underlying <code>collection</code> \&amp;. </p>
<p> If no options are necessary, <code>query</code> can simply contain a query such as <code>{a:1}</code> \&amp;. If you would like to specify options such as a sort order, the query must be placed inside of <code>{$query: {}}</code> as specified by the server documentation. See the example below for how to properly specify additional options to <code>query</code> \&amp;. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_cursor_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> when no longer in use. If invalid parameters are supplied, <code>NULL</code> may be returned. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dl>
<h2>Example</h2>
<pre>#include &lt;mongoc.h&gt;
#include &lt;stdio.h&gt;
static void
print_all_documents (mongoc_collection_t *collection)
{
 mongoc_cursor_t *cursor;
 bson_error_t error;
 const bson_t *doc;
 char *str;
 bson_t *query;
 query = BCON_NEW (&quot;$query&quot;, &quot;{&quot;, &quot;foo&quot;, BCON_INT32 (1), &quot;}&quot;,
 &quot;$orderby&quot;, &quot;{&quot;, &quot;bar&quot;, BCON_INT32 (-1), &quot;}&quot;);
 cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);
 while (mongoc_cursor_more (cursor) &amp;&amp; mongoc_cursor_next (cursor, &amp;doc)) {
 str = bson_as_json (doc, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 }
 if (mongoc_cursor_error (cursor, &amp;error)) {
 fprintf (stderr, &quot;An error occurred: %s
&quot;, error.message);
 }
 mongoc_cursor_destroy (cursor);
 bson_destroy (query);
}</pre>
<h2>The Find Command</h2>
<p>Queries have historically been sent as OP_QUERY wire protocol messages, but beginning in MongoDB 3.2 queries use <code>the find command</code> instead. </p>
<p> The driver automatically converts queries to the new &quot;find&quot; command syntax if needed, so this change is typically invisible to C Driver users. However, an application written exclusively for MongoDB 3.2 and later can choose to use the new syntax directly instead of relying on the driver to convert from the old syntax: </p>
<pre>/* MongoDB 3.2+ &quot;find&quot; command syntax */
query = BCON_NEW (&quot;filter&quot;, &quot;{&quot;, &quot;foo&quot;, BCON_INT32 (1), &quot;}&quot;,
 &quot;sort&quot;: &quot;{&quot;, &quot;bar&quot;, BCON_INT32 (-1), &quot;}&quot;);
cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);</pre>
<p>The &quot;find&quot; command takes different options from the traditional OP_QUERY message. </p>
<dl COMPACT>
<dt><code>Query</code></p>
<dd><code>$query</code> <code>filter</code></dl>
<dl COMPACT>
<dt><code>Sort</code></p>
<dd><code>$orderby</code> <code>sort</code></dl>
<dl COMPACT>
<dt><code>Show record location</code></p>
<dd><code>$showDiskLoc</code> <code>showRecordId</code></dl>
<dl COMPACT>
<dt><code>Other $-options</code></p>
<dd><code>$&lt;option name&gt;</code> <code>&lt;option name&gt;</code></dl>
<p> Most applications should use the OP_QUERY syntax, with &quot;$query&quot;, &quot;$orderby&quot;, and so on, and rely on the driver to convert to the new syntax if needed. There are two caveats: querying documents by a key named &quot;filter&quot;, and using new &quot;find&quot; command options that OP_QUERY does not support. </p>
<h2>See Also</h2>
<p><code>The find command</code> in the MongoDB Manual. </p>
<h2>Finding A Document By A Key Named Filter</h2>
<p>To find a document like <code>{ _id: 1, filter: value }</code> , this query works in MongoDB before 3.2: </p>
<pre>/* Fails with MongoDB 3.2+ */
query = BCON_NEW (&quot;filter&quot;, BCON_UTF8 (&quot;value&quot;));
cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);</pre>
<p>Beginning in MongoDB 3.2, the &quot;filter&quot; option has special meaning, and it is no longer assumed to be a field in a document you are querying for. To execute this query on any MongoDB version, wrap it in &quot;$query&quot;: </p>
<pre>/* Works in all MongoDB versions */
query = BCON_NEW (&quot;$query&quot;, &quot;{&quot;, &quot;filter&quot;, BCON_UTF8 (&quot;value&quot;), &quot;}&quot;);
cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);</pre>
<p>This code works for any MongoDB version. The driver sends it as-is to a MongoDB server older than 3.2, and before sending to MongoDB 3.2 or later converts it to the following: </p>
<p> <code>{ filter: { filter: value } }</code> </p>
<h2>Options Specific To The Find Command</h2>
<p>The &quot;find&quot; command has new options like &quot;singleBatch&quot; not supported by OP_QUERY. Applications should use the new &quot;find&quot; syntax directly to take advantage of them: </p>
<pre>/* MongoDB 3.2+ &quot;find&quot; command syntax */
query = BCON_NEW (&quot;filter&quot;, &quot;{&quot;, &quot;foo&quot;, BCON_INT32 (1), &quot;}&quot;,
 &quot;sort&quot;: &quot;{&quot;, &quot;bar&quot;, BCON_INT32 (-1), &quot;}&quot;,
 &quot;singleBatch&quot;, BCON_BOOL (true));
cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);</pre>
<h2>The Explain Command</h2>
<p>With MongoDB before 3.2, a query with option <code>$explain: true</code> returns information about the query plan, instead of the query results. Beginning in MongoDB 3.2, there is a separate &quot;explain&quot; command. The driver will not convert &quot;$explain&quot; queries to &quot;explain&quot; commands, you must call the &quot;explain&quot; command explicitly: </p>
<pre>/* MongoDB 3.2+, &quot;explain&quot; command syntax */
command = BCON_NEW (&quot;explain&quot;, &quot;{&quot;,
 &quot;find&quot;, BCON_UTF8 (&quot;collection_name&quot;),
 &quot;filter&quot;, &quot;{&quot;,
 &quot;foo&quot;, BCON_INT32 (1), &quot;}&quot;,
 &quot;}&quot;, &quot;}&quot;);
cursor = mongoc_collection_find (collection, MONGOC_QUERY_NONE, 0, 0, 0, query, NULL, NULL);</pre>
<h2>See Also</h2>
<p><code>The explain command</code> in the MongoDB Manual. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
