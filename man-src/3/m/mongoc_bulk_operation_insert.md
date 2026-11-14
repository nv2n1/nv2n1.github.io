---
title: "mongoc_bulk_operation_insert(3)"
name: "mongoc_bulk_operation_insert"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_insert/"
description: "mongoc_bulk_operation_insert() – None"
---

<p>mongoc_bulk_operation_insert() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
void
mongoc_bulk_operation_insert (mongoc_bulk_operation_t *bulk,
                              const bson_t            *document);
</pre>
<p> Queue an insert of a single document into a bulk operation. The insert is not performed until <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> is called. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>document</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>Errors</h2>
<p> Errors are propagated via <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
