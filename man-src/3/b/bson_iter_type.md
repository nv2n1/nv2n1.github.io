---
title: "bson_iter_type(3)"
name: "bson_iter_type"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_type/"
description: "bson_iter_type() – The bson_iter_type() function shall return the type of the observed element in a bson document."
---

<h2>NAME</h2>
<p> bson_iter_type() &#8211; The bson_iter_type() function shall return the type of the observed element in a bson document.</p>
<h2>SYNOPSIS</h2>
<pre><code>
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
bson_type_t
bson_iter_type(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> function shall return the type of the observed element in a bson document. </p>
<h2>RETURNS</h2>
<p> A <code>bson_type_t</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
