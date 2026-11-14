---
title: "mongoc_bulk_operation_set_bypass_document_validation(3)"
name: "mongoc_bulk_operation_set_bypass_document_validation"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_bulk_operation_set_bypass_document_validation/"
description: "mongoc_bulk_operation_set_bypass_document_validation() – Will bypass document validation for all operations part of this bulk."
---

<p>mongoc_bulk_operation_set_bypass_document_validation() &#8211; Will bypass document validation for all operations part of this bulk.</p>
<h2>Synopsis</h2>
<pre>
void
mongoc_bulk_operation_set_bypass_document_validation (mongoc_bulk_operation_t   *bulk,
                                                      bool                       bypass);
</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>bulk</code></p>
<dd> A <code>mongoc_bulk_operation_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>bypass</code></p>
<dd> A boolean.</dl>
<h2>Description</h2>
<p> Will bypass document validation for all operations part of this <code>bulk</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
