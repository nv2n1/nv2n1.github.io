---
title: "mongoc_bulk_operation_t(3)"
name: "mongoc_bulk_operation_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_t/"
description: "mongoc_bulk_operation_t – Bulk Write Operations"
---

<p>mongoc_bulk_operation_t &#8211; Bulk Write Operations</p>
<h2>Synopsis</h2>
<pre>
typedef struct _mongoc_bulk_operation_t mongoc_bulk_operation_t;
</pre>
<p> The opaque type <code>mongoc_bulk_operation_t</code> provides an abstraction for submitting multiple write operations as a single batch. </p>
<p> After adding all of the write operations to the <code>mongoc_bulk_operation_t</code> , call <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> to execute the operation. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> It is only valid to call <code><a href="/docs/linux/man/3-mongoc_bulk_operation_execute/">mongoc_bulk_operation_execute</a>(3)</code> once. The <code>mongoc_bulk_operation_t</code> must be destroyed afterwards.</dl>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
