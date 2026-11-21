---
title: "bson_append_binary(3)"
name: "bson_append_binary"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_binary/"
description: "bson_append_binary() – The bson_append_binary() function shall append a new element to bson containing the binary data provided."
---

<h2>NAME</h2>
<p> bson_append_binary() &#8211; The bson_append_binary() function shall append a new element to bson containing the binary data provided.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_binary(bson_t *bson,
                        const char *key,
                        int key_length,
                        bson_subtype_t subtype,
                        const uint8_t *binary,
                        uint32_t length);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></dt>
<dd> A <code>bson_t</code> \&amp;.</dd></dl>
<dl>
<dt><code>key</code></dt>
<dd> The key name.</dd></dl>
<dl>
<dt><code>key_length</code></dt>
<dd> The length of <code>key</code> in bytes or -1 to use strlen().</dd></dl>
<dl>
<dt><code>subtype</code></dt>
<dd> A bson_subtype_t indicationg the binary subtype.</dd></dl>
<dl>
<dt><code>binary</code></dt>
<dd> A buffer to embed as binary data.</dd></dl>
<dl>
<dt><code>length</code></dt>
<dd> The length of <code>buffer</code> in bytes.</dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_binary/">bson_append_binary</a>(3)</code> function shall append a new element to <code>bson</code> containing the binary data provided. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
