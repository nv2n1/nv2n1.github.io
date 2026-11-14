---
title: "bson_append_document_end(3)"
name: "bson_append_document_end"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_document_end/"
description: "bson_append_document_end() – The bson_append_document_end() function shall complete the appending of a document with bson_append_document_begin(). child is invalid after calling this function."
---

<h2>NAME</h2>
<p> bson_append_document_end() &#8211; The bson_append_document_end() function shall complete the appending of a document with bson_append_document_begin(). child is invalid after calling this function.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_append_document_end (bson_t *bson,
                          bson_t *child);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>child</code></p>
<dd> The child <code>bson_t</code> initialized in a call to <code><a href="/docs/linux/man/3-bson_append_document_begin/">bson_append_document_begin</a>(3)</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_document_end/">bson_append_document_end</a>(3)</code> function shall complete the appending of a document with <code><a href="/docs/linux/man/3-bson_append_document_begin/">bson_append_document_begin</a>(3)</code> \&amp;. <code>child</code> is invalid after calling this function. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
