---
title: "bson_new_from_json(3)"
name: "bson_new_from_json"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_new_from_json/"
description: "bson_new_from_json() – The bson_new_from_json() function allocates and initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set..."
---

<h2>NAME</h2>
<p> bson_new_from_json() &#8211; The bson_new_from_json() function allocates and initialize a new bson_t by parsing the JSON found in data. Only a single JSON object may exist in data or an error will be set and NULL returned.</p>
<h2>SYNOPSIS</h2>
<pre>
bson_t *
bson_new_from_json (const uint8_t *data,
                    ssize_t        len,
                    bson_error_t  *error);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>data</code></p>
<dd> A UTF-8 encoded string containing valid JSON.</dl>
<dl>
<dt><code>len</code></p>
<dd> The length of <code>data</code> in bytes excluding a trailing <code>
