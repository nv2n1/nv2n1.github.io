---
title: "mongoc_find_and_modify_opts_set_flags(3)"
name: "mongoc_find_and_modify_opts_set_flags"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_set_flags/"
description: "mongoc_find_and_modify_opts_set_flags() – Adds one or more flags to the builder."
---

<p>mongoc_find_and_modify_opts_set_flags() &#8211; Adds one or more flags to the builder.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_find_and_modify_opts_set_flags (mongoc_find_and_modify_opts_t *opts,
 const mongoc_find_and_modify_flags_t flags);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_find_and_modify_opts_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>\&amp;.</dl>
<h2>Description</h2>
<p>Adds one or more flags to the builder. </p>
<dl COMPACT>
<dt><code>MONGOC_FIND_AND_MODIFY_NONE</code></p>
<dd>Default. Doesn&#8217;t add anything to the builder.</dl>
<dl COMPACT>
<dt><code>MONGOC_FIND_AND_MODIFY_REMOVE</code></p>
<dd>Will instruct find_and_modify to remove the matching document.</dl>
<dl COMPACT>
<dt><code>MONGOC_FIND_AND_MODIFY_UPSERT</code></p>
<dd>Update the matching document or, if no document matches, insert the document.</dl>
<dl COMPACT>
<dt><code>MONGOC_FIND_AND_MODIFY_RETURN_NEW</code></p>
<dd>Return the resulting document.</dl>
<h2>Returns</h2>
<p>Returns true if it successfully added the option to the builder. </p>
<h2>Setting Flags</h2>
<pre>void fam_flags(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bson_t *update;
 bool success;
 /* Find Zlatan Ibrahimovic, the striker */
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;profession&quot;, &quot;Football player&quot;);
 BSON_APPEND_INT32 (&amp;query, &quot;age&quot;, 34);
 BSON_APPEND_INT32 (&amp;query, &quot;goals&quot;, (16+35+23+57+16+14+28+84)+(1+6+62));
 /* Add his football position */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;,
 &quot;position&quot;, BCON_UTF8 (&quot;striker&quot;),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 /* Create the document if it didn't exist, and return the updated document */
 mongoc_find_and_modify_opts_set_flags (opts, MONGOC_FIND_AND_MODIFY_UPSERT|MONGOC_FIND_AND_MODIFY_RETURN_NEW);
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
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<p>Outputs: </p>
<pre>{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: false,
 &quot;n&quot;: 1,
 &quot;upserted&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 }
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 34,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 342,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;
 },
 &quot;ok&quot;: 1
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
