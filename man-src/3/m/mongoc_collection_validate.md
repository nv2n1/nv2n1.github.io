---
title: "mongoc_collection_validate(3)"
name: "mongoc_collection_validate"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_validate/"
description: "mongoc_collection_validate() – This function is a helper function to execute the validate MongoDB command."
---

<p>mongoc_collection_validate() &#8211; This function is a helper function to execute the validate MongoDB command.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_validate (mongoc_collection_t *collection,
 const bson_t *options,
 bson_t *reply,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>options</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function is a helper function to execute the <code>validate</code> MongoDB command. </p>
<p> Currently, the only supported options are <code>full</code> , which is a boolean and <code>scandata</code> , also a boolean. </p>
<p> See the MongoDB documentation for more information on this command. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<p> <code>reply</code> is always initialized and must be destroyed with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
