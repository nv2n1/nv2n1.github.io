---
title: "bson_iter_document(3)"
name: "bson_iter_document"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_document/"
description: "bson_iter_document() – The bson_iter_document() function shall retrieve the raw buffer of a sub-document from iter. iter MUST be on an element that is of type BSON_TYPE_DOCUMENT. This can be verifi..."
---

<h2>NAME</h2>
<p> bson_iter_document() &#8211; The bson_iter_document() function shall retrieve the raw buffer of a sub-document from iter. iter MUST be on an element that is of type BSON_TYPE_DOCUMENT. This can be verified with bson_iter_type() or the BSON_ITER_HOLDS_DOCUMENT() macro.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_DOCUMENT(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_DOCUMENT)
void bson_iter_document(const bson_iter_t *iter,
                        uint32_t *document_len,
                        const uint8_t **document);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>document_len</code></p>
<dd> A location for the length of the document in bytes.</dl>
<dl>
<dt><code>document</code></p>
<dd> A location for the document buffer.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_document/">bson_iter_document</a>(3)</code> function shall retrieve the raw buffer of a sub-document from <code>iter</code> \&amp;. <code>iter</code> </p>
<p> <code>MUST</code> be on an element that is of type BSON_TYPE_DOCUMENT. This can be verified with <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> or the <code><a href="/docs/linux/man/3-bson_iter_holds_document/">BSON_ITER_HOLDS_DOCUMENT</a>(3)</code> macro. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
