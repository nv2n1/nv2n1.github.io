---
title: "mongoc_collection_create_bulk_operation(3)"
name: "mongoc_collection_create_bulk_operation"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_create_bulk_operation/"
description: "mongoc_collection_create_bulk_operation() – This function shall begin a new bulk operation. After creating this you may call various functions such as mongoc_bulk_operation_update(), mongoc_bulk_op..."
---

<p>mongoc_collection_create_bulk_operation() &#8211; This function shall begin a new bulk operation. After creating this you may call various functions such as mongoc_bulk_operation_update(), mongoc_bulk_operation_insert() and others.</p>
<h2>Synopsis</h2>
<pre>mongoc_bulk_operation_t *
mongoc_collection_create_bulk_operation (
 mongoc_collection_t *collection,
 bool ordered,
 const mongoc_write_concern_t *write_concern)
 BSON_GNUC_WARN_UNUSED_RESULT;</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>ordered</code></p>
<dd>If the operations must be performed in order.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>An optional <code>mongoc_write_concern_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall begin a new bulk operation. After creating this you may call various functions such as <code><a href="/docs/linux/man/3-mongoc_bulk_operation_update/">mongoc_bulk_operation_update</a>(3)</code> , <code><a href="/docs/linux/man/3-mongoc_bulk_operation_insert/">mongoc_bulk_operation_insert</a>(3)</code> and others. </p>
<p> After calling <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> the commands will be executed in as large as batches as reasonable by the client. </p>
<p> If <code>ordered</code> is true, then processing will stop at the first error. </p>
<p> If <code>ordered</code> is not true, then the bulk operation will attempt to continue processing even after the first failure. </p>
<p> <code>write_concern</code> contains the write concern for all operations in the bulk operation. If <code>NULL</code> , the collection&#8217;s write concern is used. The global default is acknowledged writes: MONGOC_WRITE_CONCERN_W_DEFAULT. </p>
<h2>Errors</h2>
<p>Errors are propagated when executing the bulk operation. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_bulk_operation_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_bulk_operation_destroy/">mongoc_bulk_operation_destroy</a>(3)</code> when no longer in use. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
