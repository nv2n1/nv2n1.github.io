---
title: "bson_append_timestamp(3)"
name: "bson_append_timestamp"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_timestamp/"
description: "bson_append_timestamp() – This function is not similar in functionality to bson_append_date_time(). Timestamp elements are different in that they include only second precision and an increment field."
---

<h2>NAME</h2>
<p> bson_append_timestamp() &#8211; This function is not similar in functionality to bson_append_date_time(). Timestamp elements are different in that they include only second precision and an increment field.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_timestamp(bson_t *bson,
                           const char *key,
                           int key_length,
                           uint32_t timestamp,
                           uint32_t increment);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> An ASCII C string containing the name of the field.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> in bytes, or -1 to determine the length with <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>timestamp</code></p>
<dd> A uint32_t.</dl>
<dl>
<dt><code>increment</code></p>
<dd> A uint32_t.</dl>
<h2>DESCRIPTION</h2>
<p> This function is not similar in functionality to <code><a href="/docs/linux/man/3-bson_append_date_time/">bson_append_date_time</a>(3)</code> \&amp;. Timestamp elements are different in that they include only second precision and an increment field. </p>
<p> They are primarily used for intra-MongoDB server communication. </p>
<p> The <code><a href="/docs/linux/man/3-bson_append_timestamp/">bson_append_timestamp</a>(3)</code> function shall append a new element of type BSON_TYPE_TIMESTAMP. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
