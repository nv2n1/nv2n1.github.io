---
title: "mongoc_bulk_operation_update(3)"
name: "mongoc_bulk_operation_update"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_update/"
description: "mongoc_bulk_operation_update() – None"
---

<p>mongoc_bulk_operation_update() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
void
mongoc_bulk_operation_update (mongoc_bulk_operation_t *bulk,
                              const bson_t            *selector,
                              const bson_t            *document,
                              bool                     upsert);
</pre>
<p> This function queues an update as part of a bulk operation. This does not execute the operation. To execute the entirety of the bulk operation call <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> <code>document</code> MUST only contain fields whose key starts with <code>$</code> \&amp;. See the update document specification for more details.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>selector</code></p>
<dd> A <code>bson_t</code> containing the selector to query.</dl>
<dl COMPACT>
<dt><code>document</code></p>
<dd> A <code>bson_t</code> containing the update document.</dl>
<dl COMPACT>
<dt><code>upsert</code></p>
<dd> <code>true</code> if an <code>upsert</code> should be performed.</dl>
<h2>Errors</h2>
<p> Errors are propagated via <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-mongoc_bulk_operation_update_one/">mongoc_bulk_operation_update_one</a>(3)</code> </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
