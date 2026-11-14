---
title: "mongoc_bulk_operation_get_write_concern(3)"
name: "mongoc_bulk_operation_get_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_get_write_concern/"
description: "mongoc_bulk_operation_get_write_concern() – Fetches the write concern to be used for bulk."
---

<p>mongoc_bulk_operation_get_write_concern() &#8211; Fetches the write concern to be used for bulk.</p>
<h2>Synopsis</h2>
<pre>
const mongoc_write_concern_t *
mongoc_bulk_operation_get_write_concern (const mongoc_bulk_operation_t *bulk);
</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<h2>Description</h2>
<p> Fetches the write concern to be used for <code>bulk</code> \&amp;. </p>
<h2>Returns</h2>
<p> A <code>mongoc_write_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
