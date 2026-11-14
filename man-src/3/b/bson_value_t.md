---
title: "bson_value_t(3)"
name: "bson_value_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_value_t/"
description: "bson_value_t – BSON Boxed Container Type"
---

<h2>NAME</h2>
<p> bson_value_t &#8211; BSON Boxed Container Type</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct _bson_value_t {
    bson_type_t value_type;
    union {
        bson_oid_t v_oid;
        int64_t v_int64;
        int32_t v_int32;
        int8_t v_int8;
        double v_double;
        bool v_bool;
        int64_t v_datetime;
        struct {
            uint32_t timestamp;
            uint32_t increment;
        } v_timestamp;
        struct {
            uint32_t len;
            char *str;
        } v_utf8;
        struct {
            uint32_t data_len;
            uint8_t *data;
        } v_doc;
        struct {
            uint32_t data_len;
            uint8_t *data;
            bson_subtype_t subtype;
        } v_binary;
        struct {
            char *regex;
            char *options;
        } v_regex;
        struct {
            char *collection;
            uint32_t collection_len;
            bson_oid_t oid;
        } v_dbpointer;
        struct {
            uint32_t code_len;
            char *code;
        } v_code;
        struct {
            uint32_t code_len;
            char *code;
            uint32_t scope_len;
            uint8_t *scope_data;
        } v_codewscope;
        struct {
            uint32_t len;
            char *symbol;
        } v_symbol;
    } value;
} bson_value_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_value_t</code> structure is a boxed type for encapsulating a runtime determined type. </p>
<h2>EXAMPLE</h2>
<pre><code>
const bson_value_t *value;
value = bson_iter_value(&amp;iter);
if (value.type == BSON_TYPE_INT32) {
    printf("%d
", value.value.v_int32);
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
