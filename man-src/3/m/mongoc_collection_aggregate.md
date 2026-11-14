---
title: "mongoc_collection_aggregate(3)"
name: "mongoc_collection_aggregate"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_aggregate/"
description: "mongoc_collection_aggregate() – This function shall execute an aggregation query on the underlying ‘collection’. The bson ‘pipeline’ is not validated, simply passed along as appropriate to the serv..."
---

<p>mongoc_collection_aggregate() &#8211; This function shall execute an aggregation query on the underlying &#8216;collection&#8217;. The bson &#8216;pipeline&#8217; is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation.</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_collection_aggregate (mongoc_collection_t *collection,
 mongoc_query_flags_t flags,
 const bson_t *pipeline,
 const bson_t *options,
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
<dt><code>pipeline</code></p>
<dd>A <code>bson_t</code> containing the pipeline array.</dl>
<dl COMPACT>
<dt><code>options</code></p>
<dd>A <code>bson_t</code> containing options for the pipeline, or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall execute an aggregation query on the underlying &#8216;collection&#8217;. The bson &#8216;pipeline&#8217; is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation. </p>
<p> In the case of older server versions, &lt; v2.5, the returned cursor is a synthetic iterator over the result set. This provides a limitation insofar as returned documents can be no larger than 16MB. When connecting to newer servers this limitation doesn&#8217;t exist. The specific test is for wire_version &gt; 0. </p>
<p> For more information on building MongoDB pipelines, see <code>MongoDB Aggregation Command</code> on the MongoDB website. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>The <code>pipeline</code> parameter should contain a field named <code>pipeline</code> containing a BSON array of pipeline stages.</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>The <code>mongoc_read_concern_t</code> specified on the <code>mongoc_collection_t</code> will be used, if any.</dl>
<h2>Returns</h2>
<p>This function returns a newly allocated <code>mongoc_cursor_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> when no longer in use. <code>NULL</code> may be returned if parameters are invalid. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dl>
<h2>Example</h2>
<pre>#include &lt;bcon.h&gt;
#include &lt;mongoc.h&gt;
static mongoc_cursor_t *
pipeline_query (mongoc_collection_t *collection)
{
 mongoc_cursor_t *cursor;
 bson_t *pipeline;
 pipeline = BCON_NEW (&quot;pipeline&quot;, &quot;[&quot;,
 &quot;{&quot;, &quot;$match&quot;, &quot;{&quot;, &quot;foo&quot;, BCON_UTF8 (&quot;A&quot;), &quot;}&quot;, &quot;}&quot;,
 &quot;{&quot;, &quot;$match&quot;, &quot;{&quot;, &quot;bar&quot;, BCON_BOOL (false), &quot;}&quot;, &quot;}&quot;,
 &quot;]&quot;);
 cursor = mongoc_collection_aggregate (collection,
 MONGOC_QUERY_NONE,
 pipeline,
 NULL,
 NULL);
 bson_destroy (pipeline);
 return cursor;
}</pre>
<h2>Other Parameters</h2>
<p>Pass any parameters to the <code>aggregate</code> command, besides <code>pipeline</code> , as fields in <code>options</code> : </p>
<pre>pipeline = BCON_NEW (&quot;pipeline&quot;, &quot;[&quot;,
 &quot;{&quot;, &quot;$out&quot;, BCON_UTF8 (&quot;collection2&quot;), &quot;}&quot;,
 &quot;]&quot;);
options = BCON_NEW (&quot;bypassDocumentValidation&quot;, BCON_BOOL (true));
cursor = mongoc_collection_aggregate (collection1,
 MONGOC_QUERY_NONE,
 pipeline,
 options,
 NULL);</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
