---
title: "mongoc_find_and_modify_opts_set_sort(3)"
name: "mongoc_find_and_modify_opts_set_sort"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_set_sort/"
description: "mongoc_find_and_modify_opts_set_sort() – Adds sort argument to the builder."
---

<p>mongoc_find_and_modify_opts_set_sort() &#8211; Adds sort argument to the builder.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_find_and_modify_opts_set_sort (mongoc_find_and_modify_opts_t *opts,
 const bson_t *sort);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_find_and_modify_opts_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>sort</code></p>
<dd>Determines which document the operation modifies if the query selects multiple documents. findAndModify modifies the first document in the sort order specified by this argument.</dl>
<h2>Description</h2>
<p>Adds sort argument to the builder. </p>
<h2>Returns</h2>
<p>Returns true if it successfully added the option to the builder. </p>
<h2>Setting Sort</h2>
<pre>void fam_sort(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t *update;
 bson_t sort = BSON_INITIALIZER;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find all users with the lastname Ibrahimovic */
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 /* Sort by age (descending) */
 BSON_APPEND_INT32 (&amp;sort, &quot;age&quot;, -1);
 /* Bump his goal tally */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;,
 &quot;oldest&quot;, BCON_BOOL (true),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 mongoc_find_and_modify_opts_set_sort (opts, &amp;sort);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;sort);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<p>Outputs: </p>
<pre>{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: true,
 &quot;n&quot;: 1
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 35,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 343,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;,
 &quot;author&quot;: true
 },
 &quot;ok&quot;: 1
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
