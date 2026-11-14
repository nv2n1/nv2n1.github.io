---
title: "mongoc_bulk_operation_execute(3)"
name: "mongoc_bulk_operation_execute"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_execute/"
description: "mongoc_bulk_operation_execute() – None"
---

<p>mongoc_bulk_operation_execute() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
uint32_t
mongoc_bulk_operation_execute (mongoc_bulk_operation_t *bulk,
                               bson_t                  *reply,
                               bson_error_t            *error);
</pre>
<p> This function executes all operations queued into the bulk operation. If <code>ordered</code> was specified to <code><a href="/docs/linux/man/3-mongoc_collection_create_bulk_operation/">mongoc_collection_create_bulk_operation</a>(3)</code> , then forward progress will be stopped upon the first error. </p>
<p> It is only valid to call <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> once. The <code>mongoc_bulk_operation_t</code> must be destroyed afterwards. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> <code>reply</code> is always initialized, even upon failure. Callers <code>must</code> call <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> to release this potential allocation.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd> An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p> Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p> A non-zero <code>hint</code> of the peer node on success, otherwise <code>0</code> and <code>error</code> is set. </p>
<p> The <code>reply</code> document counts operations and collects error information. See <code>Bulk Write Operations</code> for examples. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
