---
title: "bson_append_document_begin(3)"
name: "bson_append_document_begin"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_document_begin/"
description: "bson_append_document_begin() – The bson_append_document_begin() function shall begin appending a sub-document to bson. Use child to add fields to the sub-document. When completed, call bson_append_..."
---

<h2>NAME</h2>
<p> bson_append_document_begin() &#8211; The bson_append_document_begin() function shall begin appending a sub-document to bson. Use child to add fields to the sub-document. When completed, call bson_append_document_end() to complete the element.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_document_begin(bson_t *bson,
                                const char *key,
                                int key_length,
                                bson_t *child);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>child</code></p>
<dd> An uninitialized <code>bson_t</code> to be initialized as the sub-document.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_document_begin/">bson_append_document_begin</a>(3)</code> function shall begin appending a sub-document to <code>bson</code> \&amp;. Use <code>child</code> to add fields to the sub-document. When completed, call <code><a href="/docs/linux/man/3-bson_append_document_end/">bson_append_document_end</a>(3)</code> to complete the element. </p>
<p> <code>child</code> </p>
<p> <code>MUST</code> be an uninitialized <code>bson_t</code> to avoid leaking memory. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
