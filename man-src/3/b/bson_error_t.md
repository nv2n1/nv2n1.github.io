---
title: "bson_error_t(3)"
name: "bson_error_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_error_t/"
description: "bson_error_t – BSON Error Encapsulation"
---

<h2>NAME</h2>
<p> bson_error_t &#8211; BSON Error Encapsulation</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct
{
    uint32_t domain;
    uint32_t code;
    char message[504];
} bson_error_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_error_t</code> structure is used to encapsulate information about an error. Think of it as the information stored in an exception without stack trace information. It includes information about the module and error code of the error along with a human printable message. </p>
<p> The <code>error.domain</code> field contains the logical domain within a library that created the error. This might be the JSON subsystem or <code>bson_reader_t</code> for example. </p>
<p> The <code>error.code</code> field contains the domain specific error code. </p>
<p> The <code>error.message</code> field contains a human printable error message. </p>
<h2>EXAMPLE</h2>
<pre><code>
bson_reader_t *reader;
bson_error_t error;
reader = bson_reader_new_from_file("dump.bson", &amp;error);
if (!reader) {
    fprintf(stderr, "ERROR: %d.%d: %s
",
            error.domain, error.code, error.message);
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
