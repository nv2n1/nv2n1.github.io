---
title: "mongoc_collection_count_with_opts(3)"
name: "mongoc_collection_count_with_opts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_count_with_opts/"
description: "mongoc_collection_count_with_opts() – This function shall execute a count query on the underlying ‘collection’. The bson ‘query’ is not validated, simply passed along as appropriate to the server. ..."
---

<p>mongoc_collection_count_with_opts() &#8211; This function shall execute a count query on the underlying &#8216;collection&#8217;. The bson &#8216;query&#8217; is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation.</p>
<h2>Synopsis</h2>
<pre>int64_t
mongoc_collection_count_with_opts (mongoc_collection_t *collection,
 mongoc_query_flags_t flags,
 const bson_t *query,
 int64_t skip,
 int64_t limit,
 const bson_t *opts,
 const mongoc_read_prefs_t *read_prefs,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A <code>mongoc_query_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> containing the query.</dl>
<dl COMPACT>
<dt><code>skip</code></p>
<dd>A int64_t, zero to ignore.</dl>
<dl COMPACT>
<dt><code>limit</code></p>
<dd>A int64_t, zero to ignore.</dl>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>bson_t</code> , <code>NULL</code> to ignore.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall execute a count query on the underlying &#8216;collection&#8217;. The bson &#8216;query&#8217; is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation. </p>
<p> In addition to the standard functionality available from mongoc_collection_count, this function allows the user to add arbitrary extra keys to the count. This pass through enables features such as hinting for counts. </p>
<p> For more information, see the <code>query reference</code> at the MongoDB website. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>The <code>mongoc_read_concern_t</code> specified on the <code>mongoc_collection_t</code> will be used, if any.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>-1 on failure, otherwise the number of documents counted. </p>
<h2>Example</h2>
<pre>#include &lt;mongoc.h&gt;
#include &lt;bcon.h&gt;
#include &lt;stdio.h&gt;
static void
print_query_count (mongoc_collection_t *collection,
 bson_t *query)
{
 bson_error_t error;
 int64_t count;
 bson_t opts;
 bson_init(&amp;opts);
 BSON_APPEND_UTF8(&amp;opts, &quot;hint&quot;, &quot;_id_&quot;);
 count = mongoc_collection_count_with_opts (collection, MONGOC_QUERY_NONE, query, 0, 0, &amp;opts, NULL, &amp;error);
 bson_destroy(&amp;opts);
 if (count &lt; 0) {
 fprintf (stderr, &quot;Count failed: %s
&quot;, error.message);
 } else {
 printf (&quot;%&quot;PRId64&quot; documents counted.
&quot;, count);
 }
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
