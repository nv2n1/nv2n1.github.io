---
title: "mongoc_collection_stats(3)"
name: "mongoc_collection_stats"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_stats/"
description: "mongoc_collection_stats() – This function is a helper to retrieve statistics about the collection."
---

<p>mongoc_collection_stats() &#8211; This function is a helper to retrieve statistics about the collection.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_stats (mongoc_collection_t *collection,
 const bson_t *options,
 bson_t *reply,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>options</code></p>
<dd>An optional <code>bson_t</code> containing extra options to pass to the <code>collStats</code> command.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>An optional location for a <code>bson_t</code> to store the result.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function is a helper to retrieve statistics about the collection. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful </p>
<p> <code>reply</code> is always initialized to simplfiy memory handling. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
