---
title: "bson_init_from_json(3)"
name: "bson_init_from_json"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_init_from_json/"
description: "bson_init_from_json() – The bson_init_from_json() function will initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set and fa..."
---

<h2>NAME</h2>
<p> bson_init_from_json() &#8211; The bson_init_from_json() function will initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set and false returned.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_init_from_json(bson_t *bson,
                         const char *data,
                         ssize_t len,
                         bson_error_t *error);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>data</code></p>
<dd> A UTF-8 encoded string containing valid JSON.</dl>
<dl>
<dt><code>len</code></p>
<dd> The length of <code>data</code> in bytes excluding a trailing <code>
