---
title: "bson_append_array_begin(3)"
name: "bson_append_array_begin"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_append_array_begin/"
description: "bson_append_array_begin() – The bson_append_array_begin() function shall begin appending an array field to bson. This allows for incrementally building a sub-array. Doing so will generally yield be..."
---

<h2>NAME</h2>
<p> bson_append_array_begin() &#8211; The bson_append_array_begin() function shall begin appending an array field to bson. This allows for incrementally building a sub-array. Doing so will generally yield better performance as you will serialize to a single buffer. When done building the sub-array, the caller MUST call bson_append_array_end().</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_append_array_begin(bson_t *bson,
                             const char *key,
                             int key_length,
                             bson_t *child);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> A string containing the name for the key.</dl>
<dl>
<dt><code>key_length</code></p>
<dd> The length of <code>key</code> or -1 to call <code><a href="/docs/linux/man/3-strlen/">strlen</a>(3)</code> \&amp;.</dl>
<dl>
<dt><code>child</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_append_array_begin/">bson_append_array_begin</a>(3)</code> function shall begin appending an array field to <code>bson</code> \&amp;. This allows for incrementally building a sub-array. Doing so will generally yield better performance as you will serialize to a single buffer. When done building the sub-array, the caller <code>MUST</code> call <code><a href="/docs/linux/man/3-bson_append_array_end/">bson_append_array_end</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> true if the operation was applied successfully, otherwise false and <code>bson</code> should be discarded. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
