---
title: "bson_type_t(3)"
name: "bson_type_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_type_t/"
description: "bson_type_t – BSON Type Enumeration"
---

<h2>NAME</h2>
<p> bson_type_t &#8211; BSON Type Enumeration</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef enum {
    BSON_TYPE_EOD = 0x00,
    BSON_TYPE_DOUBLE = 0x01,
    BSON_TYPE_UTF8 = 0x02,
    BSON_TYPE_DOCUMENT = 0x03,
    BSON_TYPE_ARRAY = 0x04,
    BSON_TYPE_BINARY = 0x05,
    BSON_TYPE_UNDEFINED = 0x06,
    BSON_TYPE_OID = 0x07,
    BSON_TYPE_BOOL = 0x08,
    BSON_TYPE_DATE_TIME = 0x09,
    BSON_TYPE_NULL = 0x0A,
    BSON_TYPE_REGEX = 0x0B,
    BSON_TYPE_DBPOINTER = 0x0C,
    BSON_TYPE_CODE = 0x0D,
    BSON_TYPE_SYMBOL = 0x0E,
    BSON_TYPE_CODEWSCOPE = 0x0F,
    BSON_TYPE_INT32 = 0x10,
    BSON_TYPE_TIMESTAMP = 0x11,
    BSON_TYPE_INT64 = 0x12,
    BSON_TYPE_MAXKEY = 0x7F,
    BSON_TYPE_MINKEY = 0xFF,
} bson_type_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_type_t</code> enumeration contains all of the types from the <code>BSON Specification</code> \&amp;. It can be used to determine the type of a field at runtime. </p>
<h2>EXAMPLE</h2>
<pre><code>
bson_iter_t iter;
if (bson_iter_init_find(&amp;iter, doc, "foo") &amp;&amp;
    (BSON_TYPE_INT32 == bson_iter_type(&amp;iter))) {
    printf("'foo' is an int32.
");
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
