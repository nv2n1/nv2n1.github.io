---
title: "bson_t(3)"
name: "bson_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_t/"
description: "bson_t – BSON Document Abstraction"
---

<h2>NAME</h2>
<p> bson_t &#8211; BSON Document Abstraction</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
BSON_ALIGNED_BEGIN(128)
typedef struct
{
    uint32_t flags;       /* Internal flags for the bson_t. */
    uint32_t len;         /* Length of BSON data. */
    uint8_t padding[120]; /* Padding for stack allocation. */
} bson_t
    BSON_ALIGNED_END(128);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_t</code> structure represents a BSON document. This structure manages the underlying BSON encoded buffer. For mutable documents, it can append new data to the document. </p>
<h2>PERFORMANCE NOTES</h2>
<p> The <code>bson_t</code> structure attepts to use an inline allocation within the structure to speed up performance of small documents. When this internal buffer has been exhausted, a heap allocated buffer will be dynamically allocated. Therefore, it is essential to call <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> on allocated documents. </p>
<h2>EXAMPLE</h2>
<pre><code>
static void
create_on_heap(void)
{
    bson_t *b = bson_new();
    BSON_APPEND_INT32(b, "foo", 123);
    BSON_APPEND_UTF8(b, "bar", "foo");
    BSON_APPEND_DOUBLE(b, "baz", 1.23f);
    bson_destroy(b);
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
