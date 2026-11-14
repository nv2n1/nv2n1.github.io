---
title: "mongoc_bulk_operation_replace_one(3)"
name: "mongoc_bulk_operation_replace_one"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_replace_one/"
description: "mongoc_bulk_operation_replace_one() – None"
---

<p>mongoc_bulk_operation_replace_one() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
void
mongoc_bulk_operation_replace_one (mongoc_bulk_operation_t *bulk,
                                   const bson_t            *selector,
                                   const bson_t            *document,
                                   bool                     upsert);
</pre>
<p> Replace a single document as part of a bulk operation. This only queues the operation. To execute it, call <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>selector</code></p>
<dd> A <code>bson_t</code> containing the selector to query.</dl>
<dl COMPACT>
<dt><code>document</code></p>
<dd> A <code>bson_t</code> containing the replacement document.</dl>
<dl COMPACT>
<dt><code>upsert</code></p>
<dd> <code>true</code> if this should be an <code>upsert</code> \&amp;.</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> <code>document</code> may not contain fields with keys containing <code>.</code> or <code>$</code> \&amp;.</dl>
<h2>Errors</h2>
<p> Errors are propagated via <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
