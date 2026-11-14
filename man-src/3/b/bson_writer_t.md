---
title: "bson_writer_t(3)"
name: "bson_writer_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_writer_t/"
description: "bson_writer_t – Bulk BSON serialization Abstraction"
---

<h2>NAME</h2>
<p> bson_writer_t &#8211; Bulk BSON serialization Abstraction</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct _bson_writer_t bson_writer_t;
bson_writer_t *bson_writer_new(uint8_t **buf,
                               size_t *buflen,
                               size_t offset,
                               bson_realloc_func realloc_func,
                               void *realloc_func_ctx);
void bson_writer_destroy(bson_writer_t *writer);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_writer_t</code> API provides an abstraction for serializing many BSON documents to a single memory region. The memory region may be dynamically allocated and re-allocated as more memory is demanded. This can be useful when building network packets from a high-level language. For example, you can serialize a Python Dictionary directly to a single buffer destined for a TCP packet. </p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;bson.h&gt;
int main(int argc, char *argv[])
{
    bson_writer_t *writer;
    uint8_t *buf = NULL;
    size_t buflen = 0;
    bson_t *doc;
    writer = bson_writer_new(&amp;buf, &amp;buflen, 0, bson_realloc_ctx, NULL);
    for (i = 0; i &lt; 1000; i++) {
        bson_writer_begin(writer, &amp;doc);
        BSON_APPEND_INT32(&amp;doc, "i", i);
        bson_writer_end(writer);
    }
    bson_writer_destroy(writer);
    bson_free(buf);
    return 0;
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
