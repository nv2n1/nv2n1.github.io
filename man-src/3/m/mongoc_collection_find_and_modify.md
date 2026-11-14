---
title: "mongoc_collection_find_and_modify(3)"
name: "mongoc_collection_find_and_modify"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_find_and_modify/"
description: "mongoc_collection_find_and_modify() – Update and return an object."
---

<p>mongoc_collection_find_and_modify() &#8211; Update and return an object.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_find_and_modify (mongoc_collection_t *collection,
 const bson_t *query,
 const bson_t *sort,
 const bson_t *update,
 const bson_t *fields,
 bool _remove,
 bool upsert,
 bool _new,
 bson_t *reply,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> containing the query to locate target document(s).</dl>
<dl COMPACT>
<dt><code>sort</code></p>
<dd>A <code>bson_t</code> containing the sort order for <code>query</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>update</code></p>
<dd>A <code>bson_t</code> containing an update spec.</dl>
<dl COMPACT>
<dt><code>fields</code></p>
<dd>An optional <code>bson_t</code> containing the fields to return or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>_remove</code></p>
<dd>If the matching documents should be removed.</dl>
<dl COMPACT>
<dt><code>upsert</code></p>
<dd>If an upsert should be performed.</dl>
<dl COMPACT>
<dt><code>_new</code></p>
<dd>If the new version of the document should be returned.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>An optional location for a <code>bson_t</code> that will be initialized with the result or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>Update and return an object. </p>
<p> This is a thin wrapper around the <code>findAndModify</code> command. Either <code>update</code> or <code>_remove</code> arguments are required. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>As of MongoDB 3.2 and mongoc 1.3.0, the <code>mongoc_write_concern_t</code> specified on the <code>mongoc_collection_t</code> will be used, if any.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns either the document before or after modification based on the <code>_new</code> parameter. </p>
<h2>Example</h2>
<pre>#include &lt;bcon.h&gt;
#include &lt;mongoc.h&gt;
#include &lt;stdio.h&gt;
int
main (int argc,
 char *argv[])
{
 mongoc_collection_t *collection;
 mongoc_client_t *client;
 bson_error_t error;
 bson_t *query;
 bson_t *update;
 bson_t reply;
 char *str;
 mongoc_init ();
 client = mongoc_client_new (&quot;mongodb://127.0.0.1:27017/&quot;);
 collection = mongoc_client_get_collection (client, &quot;test&quot;, &quot;test&quot;);
 /*
 * Build our query, {&quot;cmpxchg&quot;: 1}
 */
 query = BCON_NEW (&quot;cmpxchg&quot;, BCON_INT32 (1));
 /*
 * Build our update. {&quot;$set&quot;: {&quot;cmpxchg&quot;: 2}}
 */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;, &quot;cmpxchg&quot;, BCON_INT32 (2), &quot;}&quot;);
 /*
 * Submit the findAndModify.
 */
 if (!mongoc_collection_find_and_modify (collection, query, NULL, update, NULL, false, false, true, &amp;reply, &amp;error)) {
 fprintf (stderr, &quot;find_and_modify() failure: %s
&quot;, error.message);
 return 1;
 }
 /*
 * Print the result as JSON.
 */
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 /*
 * Cleanup.
 */
 bson_destroy (query);
 bson_destroy (update);
 bson_destroy (&amp;reply);
 mongoc_collection_destroy (collection);
 mongoc_client_destroy (client);
 mongoc_cleanup ();
 return 0;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
