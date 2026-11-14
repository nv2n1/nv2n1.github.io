---
title: "mongoc_find_and_modify_opts_set_fields(3)"
name: "mongoc_find_and_modify_opts_set_fields"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_set_fields/"
description: "mongoc_find_and_modify_opts_set_fields() – Adds fields argument to the builder."
---

<p>mongoc_find_and_modify_opts_set_fields() &#8211; Adds fields argument to the builder.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_find_and_modify_opts_set_fields (mongoc_find_and_modify_opts_t *opts,
 const bson_t *fields);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_find_and_modify_opts_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>fields</code></p>
<dd>A subset of fields to return. Choose which fields to include by appending <code>{fieldname: 1}</code> for each fieldname, or excluding it with <code>{fieldname: 0}</code> \&amp;.</dl>
<h2>Description</h2>
<p>Adds fields argument to the builder. </p>
<h2>Returns</h2>
<p>Returns true if it successfully added the option to the builder. </p>
<h2>Setting Fields</h2>
<pre>void fam_fields(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t fields = BSON_INITIALIZER;
 bson_t *update;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find Zlatan Ibrahimovic */
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 /* Return his goal tally */
 BSON_APPEND_INT32 (&amp;fields, &quot;goals&quot;, 1);
 /* Bump his goal tally */
 update = BCON_NEW (&quot;$inc&quot;, &quot;{&quot;,
 &quot;goals&quot;, BCON_INT32 (1),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 mongoc_find_and_modify_opts_set_fields (opts, &amp;fields);
 /* Return the new tally */
 mongoc_find_and_modify_opts_set_flags (opts, MONGOC_FIND_AND_MODIFY_RETURN_NEW);
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
 bson_destroy (&amp;fields);
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
 &quot;goals&quot;: 343
 },
 &quot;ok&quot;: 1
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
