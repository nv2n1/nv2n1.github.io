---
title: "mongoc_bulk_operation_delete_one(3)"
name: "mongoc_bulk_operation_delete_one"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_delete_one/"
description: "mongoc_bulk_operation_delete_one() – None"
---

<p>mongoc_bulk_operation_delete_one() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
void
mongoc_bulk_operation_delete_one (mongoc_bulk_operation_t *bulk,
                                  const bson_t            *selector);
</pre>
<p> This function queues a delete operation as part of <code>bulk</code> that will delete a single document matching <code>selector</code> \&amp;. To delete a multiple documents, see <code><a href="/docs/linux/man/3-mongoc_bulk_operation_delete/">mongoc_bulk_operation_delete</a>(3)</code> \&amp;. </p>
<h2>Deprecated</h2>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> This function is deprecated and should not be used in new code.</dl>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_bulk_operation_remove_one/">mongoc_bulk_operation_remove_one</a>(3)</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>selector</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>Errors</h2>
<p> Errors are propagated via <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
